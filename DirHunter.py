import requests 
import os
import sys
from sys import argv 
import time

print('''
          /|
        / /    \  
       | |     ||
        \ \   / /
          \ \/ /                                    ________________________________________________
        \_ | \_/ \                                  [ DirHunter				       -   x]
          \|  |  ||                                 |_______________________________________________|
            |  \_/                                  |						    |
           \_|  |   by Mathis Pais  __       	    |	date: 22/12/2021			    |
        ---__\   \   ___________   /|_\  __---      |	version: 1.3			            |
        \  -  -\   \-           -/   /--   - /      |	description: brute-force tool for           |
          \  \  \                   /    / /        |	websites directories discovery.             |
            \___/       __.__        \___/          |	usage:                                      |
               |          |          |		    |	python3 DirHunter.py "url" "wordlist.txt"   |
               |  ___           ___  |              [_______________________________________________] 
                \ /|\           /|\ /
                 \                 /
                 |\               /|
                  |\      |      /|
                  | \     |     / |
                     \    |    /
                      \___|___/
                       \^   ^/@$
                        \_-_/


''') 

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'

def main():
	if len(argv) == 1 :
		print(bcolors.FAIL+"[!] "+bcolors.RESET+ 'usage: python3 DirHunter.py "url" "wordlist"')
	elif len(argv) == 2:
		if argv[1][len(argv[1])-4:len(argv[1])] == '.txt':
			print(bcolors.FAIL+"[!] "+bcolors.RESET+ 'usage: python3 DirHunter.py "url" "wordlist"')
		else:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+'usage: python3 DirHunter.py "url" "wordlist"')
	elif len(argv) == 3:
		print(bcolors.OK+"[+] "+bcolors.RESET+'ready to hunt the dir !')
		print(bcolors.OK+"[+] "+bcolors.RESET+'searching for deers... Hum, I mean dirs')
		Start=time.time()
		hunt(str(argv[1]),"/"+str(argv[2]))
		count=hunt.count

		if not hunt.path:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"no dir found.")
		elif hunt.path[0] == "":
			hunt.path.pop(0)
		for dir in hunt.path:
			hunt.count=hunt.count-1
			hunt(str(argv[1])+"/"+dir,"/"+str(argv[2]))

		End=time.time()
		Time=End-Start
		print("\n")
		print(bcolors.OK+"[+] "+bcolors.RESET+"Hunting time: ", Time, "sec")
		print(bcolors.OK+"[+] "+bcolors.RESET+"End time: ", time.ctime())
		print(bcolors.OK+"[+] "+bcolors.RESET+"Your day's catch: ", count+hunt.count)
	else:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+ 'usage: python3 DirHunter.py "url" "wordlist"')

def hunt(urls,wordlist):
	hunt.path=[]
	url=urls
	hunt.count=0
	try:
		if os.path.exists(os.getcwd()+wordlist):
			file=open(os.getcwd()+wordlist,"r")
			for i in file:
				dir=i.splitlines()
				dir=''.join(dir)
				rq=requests.get(url+"/"+dir)
				dir_len=len(dir)

				if rq.status_code == 200:
					print("Aiming : "+url+"/"+dir,end="\r")
					time.sleep(0.05)
					print("Aiming : "+url+"/"+dir_len*" ",end="\r") 
					print("\n")
					print(bcolors.OK+"[+] "+bcolors.RESET+"Aiming : "+url+"/"+dir+"   "+bcolors.OK+str(rq.status_code)+bcolors.RESET+": dir shot ︻デ═一") 
					hunt.goodir=dir
					hunt.count=hunt.count+1
					hunt.path.append(hunt.goodir)

				elif rq.status_code == 403:
					print("Aiming : "+url+"/"+dir,end="\r")
					time.sleep(0.05)
					print("Aiming : "+url+"/"+dir_len*" ",end="\r")
					print("\n")
					print(bcolors.WARNING+"[-] "+bcolors.RESET+"Aiming : "+url+"/"+dir+"   "+bcolors.WARNING+str(rq.status_code)+bcolors.RESET+": restricted area !") 
				
				else:
					print("Aiming :"+url+"/"+dir,end="\r")
					time.sleep(0.05)
					print("Aiming :"+url+"/"+dir_len*" ",end="\r") 

			file.close()
			print("\n")
			print(bcolors.OK+"[+] "+bcolors.RESET+"Hunt finished.")

		else:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+wordlist+" don't exist in this directory")	

	except KeyboardInterrupt:
		print("\n")
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"Hunting has been abandoned")

	except Exception as e:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+e)


if __name__ == '__main__':
	main()
