#______________________________________________________________
import webbrowser
from colorama import Style, Back, Fore
import socket
import time
import sys
import uuid
from clear import clear
import os
import requests
import wmi
import platform,socket,re,uuid,json,psutil,logging
import threading
import subprocess
import shutil

class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32
#______________________________________________________________
attemps = 0
hostname = socket.gethostname()
clear()
while attemps < 3:
    password = input(' Terminal──Password :')

    if password == 'root':
        print(' ⭐ Welcome')
        time.sleep(2)
        break
    else:
        print(' Error')        
#______________________________________________________________
clear()
#______________________________________________________________
print(f"                         {Fore.LIGHTGREEN_EX}║ {Fore.WHITE}Update : 1.0 (Beta) {Fore.LIGHTGREEN_EX}║ {Fore.WHITE}Owner : A8Fit {Fore.LIGHTGREEN_EX}║ {Fore.WHITE}iNFO Network {Fore.LIGHTGREEN_EX}║ ")
sys.stdout.write(f"\x1b]2; Copyright © A8Fit'Alruqi | Demo Access@{hostname}\x07")
#______________________________________________________________
def riper():
   int()
print(f'''{Style.BRIGHT}{Fore.GREEN}                                                       
                                          '%$#####%%%##%#####                   
                                         ##%*******++++******###                 
                                        #++##+#+==+#######++++##               
                                       #+++=++#+==#+=====+##+==+#              
                                      #++===+#+===========+#+==+#             
                                     #++====+#+=============+===*#            
                                     #=====+##*=================+%            
                                     #====+*###++++=============+#            
                                    ##*#################*+=======##           
                                   ############################*++=##           
                                  ##################################%           
                                 #######{Style.DIM}{Fore.WHITE} Powerd By : Team-Root{Fore.GREEN} ########          
                          %%#####*++++++======================++++++*++++++*##  
                        %*++++++===================+++++**++++++++==========++#%
                        %#+==+++++++++++++++++++++++++++======================+#
                         ##*+=================================================*%
                          %#*+++=========================================++*# 
                           ####*++++++===========================+++++*##''')
print("                              ______   ___   _______  _______  ______ ")
print(f"                             |    _ | | {Fore.WHITE}R{Fore.GREEN} | |       ||       ||    _ |")
print(f"                             |   | || | {Fore.WHITE}i{Fore.GREEN} | |    _  ||    ___||   | ||")
print(f"                             |   |_||_| {Fore.WHITE}p{Fore.GREEN} | |   |_| ||   |___ |   |_||")
print(f"                             |    __ || {Fore.WHITE}e{Fore.GREEN} | |    ___||    ___||    __ |")
print(f"                             |   | | || {Fore.WHITE}r{Fore.GREEN} | |   |    |   |___ |   | | |")
print(f"                             |___| |_||___| |___|    |_______||___| |_|")
print(f" {Back.LIGHTBLACK_EX}{Fore.WHITE}#Demo─Mode{Style.DIM}@{hostname}\033[0m\033[0m\033[0m")
riper()
#______________________________________________________________
while True:
 command = input(f"{Fore.GREEN}{Style.BRIGHT} ┌──{hostname}@Terminal{Fore.WHITE}─{Fore.LIGHTGREEN_EX}[{Fore.WHITE}~{Fore.GREEN}]{Fore.GREEN}\n └─{Fore.GREEN}{Fore.LIGHTWHITE_EX}> {Fore.WHITE}")
 if command == "infoWin" or command == "INFOWIN" or command == "InfoWin" or command == "iW" or command == "-i" or command == "infowin":
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ip_address, hostname
    except socket.error as e:
        print(f"{Fore.RED} [Riper]{Fore.WHITE} Failed to Get IP Address And Host {e}")
        ip_address, hostname = infoWin()
    if ip_address and hostname:
      print(f"{Fore.GREEN} [{Fore.WHITE}Riper{Fore.GREEN}]{Fore.WHITE} IP Address: {ip_address}")
      print(f"{Fore.GREEN} [{Fore.WHITE}Riper{Fore.GREEN}]{Fore.WHITE} Hostname: {hostname}")
 elif not command:
    break
 #______________________________________________________________
 elif command == "wifi_history" or command == "Wifi_History" or command == "WIFI_HISTORY" or command == "WH" or command == "-w":
     data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
     profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
     for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
             print ("{:<30}| Password : {:<}".format(i, results[0]))
            except IndexError:
             print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
             print ("{:<30}| Password : {:<}".format(i, f"{Fore.RED}[!] Wifi_ERROR{Fore.WHITE}"))
 #______________________________________________________________
 elif command == "website" or command == "WEBSITE" or command == "WebSite" or command == "Website":
   webbrowser.open('https://salla.sa/rootstory')
 #______________________________________________________________
 elif command == "Close" or command == "CLOSE" or command == "Exit" or command == "exit" or command == "EXIT" or command == "close":
    exit()
 #______________________________________________________________
 elif command == "A8Fit" or command == "A8fit" or command == "a8fit" or command == "A8FIT":
    print(' Ar7b Ei King')
 #______________________________________________________________
 elif command == "ScanPort" or command == "SCANPORT" or command == "scanport" or command == "Scanport" or command == "-s":
   HOST = "localhost"
   PORT = int(input(f' {Fore.GREEN}[Riper]{Fore.WHITE} Port :'))
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   if sock.connect_ex((HOST, PORT)) == 0:
      print(f" {Fore.WHITE}[i] {Fore.GREEN}Port :" + str(PORT) + " is Open")
   else:
      print(f" {Fore.WHITE}[!] {Fore.RED}Port : Closed")
   sock.close()
 elif command == "help" or command == "HELP" or command == "Help" or command == "-h":
    print(f" {Fore.GREEN} [Commands-Help] \n{Fore.WHITE}  If you want to check the port : ScanPort\n  If you want to extract old networks : Wifi_history\n  If you want information about the device name or IP : infoWin\n  Send packets to the target : ping\n  NETSTAT : -n\n  NETSTAT : -t\n  NETSTAT : netstat\n  NETSTAT : -ano")
 elif command == "ping" or command == "Ping" or command == "PING" or command == "-p" or command == "-P":
    print(f'''{Fore.GREEN}    @Ping''')
    url = input(f'  {Fore.WHITE}[{Fore.GREEN}Riper{Fore.WHITE}] URL or IP : ')
    url = os.system(f"  ping  {url}  -t -l 65500 ")
 elif command == "Update" or command == "UPDATE" or command == "update" or command == "Xhash" or command == "-x" or command == "-X":
      print(f"  ╰─>{Fore.WHITE} Version : 1.0d\033[0m")
      update = input (f' {Fore.LIGHTWHITE_EX}[Xhash]{Fore.WHITE} Install Update ? [Y/n] ')
      if update.lower() == 'y' or command == "Y" or command == "Yes":
         os.system('python riper.py --update')
 elif command == "github" or command == "GITHUB" or command == "Github" or command == "git":
    print(f'''
           __________________________________________
          |                                          |
          |{Fore.WHITE}  Riper : 1.0        |{Fore.LIGHTWHITE_EX} Code : 0libdw      |
          |{Fore.WHITE}  Riper : 1.2 (beta) |{Fore.LIGHTWHITE_EX} Code : 15beta      |
          |__________________________________________|''')
 #______________________________________________________________
 elif command == "0libdw":
    print(" You are in the copy (0libdw) ...")
 elif command == "15beta":
    print(" (( Loading ))")
 elif command == "cls" or command == "Clear" or command == "Cls" or command == "CLS" or command == "CLEAR" or command == "clear":
   clear()
   riper()
 elif command == "-t" or command == '-T':
    ip = input(f'  {Fore.WHITE}[{Fore.GREEN}Riper{Fore.WHITE}] IP :')
    ip = os.system(f"tracert {ip}")
 elif command == "-n" or command == '-N':
    os.system('NETSTAT -N')
 elif command == "-ANO" or command == "-ano" or command == "-Ano":
    os.system("NETSTAT -ano")
 elif command == "-o" or command == "-O":
    os.system("NETSTAT -o")
 elif command == "netstat":
    os.system('NETSTAT')
 elif command == "" or command == " ":
    print(' KLZ8')
 elif command == "TIPS" or command == "Tips" or command == "tips" or command == "Command" or command == "Commands":
    print(f"""{Fore.GREEN}
                              ╔═{Fore.WHITE}Tips{Fore.GREEN}══════════════════════════════════════╗
                              ║           {Fore.WHITE}discord.gg/xWXMJ5gmTk{Fore.GREEN}           ║
                              ║───────────────────────────────────────────║
                              ║         -w : Wifi_History                 ║
                              ║         -s : ScanPort                     ║
                              ║         -i : infoWin                      ║
                              ║         -x : Xhash-Update                 ║
                              ║         -p : Ping                         ║
                              ║───────────────────────────────────────────║
                              ║              {Fore.WHITE}Commands Netstat{Fore.GREEN}             ║
                              ║         Netstat : -n                      ║
                              ║         Netstat : -ano                    ║
                              ║         Netstat : -t                      ║
                              ║         Netstat : -o                      ║ 
                              ║                ╔═══════════╗              ║
                              ╚════════════════╣ {Fore.WHITE}Help-Tips{Fore.GREEN} ╠══════════════╝
                                               ╚═══════════╝
                                   """)
 elif command == "neofetch":
   ip_address = socket.gethostbyname(hostname)
   c = wmi.WMI()    
   root = c.Win32_ComputerSystem()[0]
   root = platform.uname()
   total, used, free = shutil.disk_usage("/")
   print(f'''\033[1m          
                                .. 
\033[0;37m                         ....:::^:  {Fore.GREEN}Shell-Team-Root : computer{Fore.WHITE}@{Fore.GREEN}{hostname}  
\033[0;37m          ....  ^^^~~~!!!77777777^  {Fore.WHITE}───────────
\033[0;37m :^^~~~!!!7777! 77777777777777777^  {Fore.GREEN}OS :{Fore.WHITE} {root.system}
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}Windows Name :{Fore.WHITE} {hostname}
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}Network Name :{Fore.WHITE} {platform.node()}
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}Name Computer :{Fore.WHITE} {root.machine}
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}Operating System :{Fore.WHITE} {platform.platform()}
\033[0;37m ~7!!!!!!!!!!!...!!!!!!!!!!!!!!!!^  {Fore.GREEN}HardDisk Size :{Fore.WHITE} GB{(total // (2**30))}
\033[0;37m ~!!!!!!!!!!!!...!!!!!!!!!!!!!!!:   {Fore.GREEN}RAM :{Fore.WHITE} {round(psutil.virtual_memory().total/1000000000, 2)} GB
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}IP :{Fore.WHITE} {ip_address}
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}Shell Update :{Fore.WHITE} 1.0.0 (beta)
\033[0;37m !777777777777! 77777777777777777^  {Fore.GREEN}Shell :{Fore.WHITE} #Team-Root
\033[0;37m ^~!!!!7777777! 77777777777777777^
\033[0;37m   ^~!!7777777! 77777777777777777^  
\033[0;37m       ...:::^^:~~!!!!77777777777^ \033[1m \033[0;32m▒▒▒  \033[0;33m▒▒▒  \033[0;31m▒▒▒  \033[0;34m▒▒▒ \033[0m ▒▒▒ {Fore.WHITE}
\033[0;37m                      ...:::^^^~~:{Style.BRIGHT}\033[0;32m  ███  \033[0;33m███  \033[0;31m███  \033[0;34m███ \033[0m ███''')
 else:
   print(f"  {Fore.GREEN}[{Fore.LIGHTWHITE_EX}!{Fore.GREEN}]{Fore.WHITE} Error Command /Type the command : help")
 #______________________________________________________________
#Xhash Credit BY : A8Fit;Hacker
#Windows Bit : {root.SystemType}
def BETA():
   print(f"""                 #########################
   +----------------------+   #  Xhash> Owner A8fit   #   
   |   ═╗ ╦┬ ┬┌─┐┌─┐┬ ┬   |   #########################   
   |   ╔╩╦╝├─┤├─┤└─┐├─┤   |   #  https://github/a8fit #   
   |   ╩ ╚═┴ ┴┴ ┴└─┘┴ ┴   |   #  Credit : 2023 / beta #
   +----------------------+   #########################   

   """)
   mal = input(' Xhash>')
   if mal == 'help':
      print('Http://a8fit.com/xhash/help')
   elif mal == 'ins': 
      os.system('python riper.py --install')
   elif mal == 'File':
      os.system('dir')
   elif mal == 'cls':
      os.system('cls')
   elif mal == 'Unhash':
      input(' Hash :')
      os.system('python riper.py --unhash')
   elif mal == "Set_Proxy":
      input(' IP Proxy :')
      input(' Port Proxy :')
   elif mal == "Xhash":
      print(f' Name : Xhash\n Version : 1.0 Beta\n Owner By : A8Fit')
   Xhash()
#______________________________________________________________