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
        ---__\   \   ___________   /|_\  __---      |	version: 1.0			            |
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
		hunt(str(argv[1]),"/"+str(argv[2]))
		hunt(str(argv[1])+"/"+hunt.goodir,"/"+str(argv[2]))

	else:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+ 'usage: python3 DirHunter.py "url" "wordlist"')

def hunt(urls,wordlist):
	url=urls
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
					print(bcolors.OK+"[+] "+bcolors.RESET+"Aiming : "+url+"/"+dir+"   "+str(rq.status_code)+": dir shot ︻デ═一") 
					goodir=dir
				elif rq.status_code == 403:
					print("Aiming : "+url+"/"+dir,end="\r")
					time.sleep(0.05)
					print("Aiming : "+url+"/"+dir_len*" ",end="\r")
					print("\n")
					print(bcolors.WARNING+"[-] "+bcolors.RESET+"Aiming : "+url+"/"+dir+"   "+str(rq.status_code)+": restricted area !") 
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
		print(e)




if __name__ == '__main__':
	main()
