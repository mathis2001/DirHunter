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
		Start=time.time()	#d??marrage du chrono ?? t=0s
		hunt(str(argv[1]),"/"+str(argv[2]))	#On utilise la fonction hunt sur les arguments donn??s
		count=hunt.count	#On initialise un compteur

		if not hunt.path:	#Si on ne trouve pas de r??p??rtoire 
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"no dir found.")	#message d'erreur
		elif hunt.path[0] == "": 	#Si le premier ??l??ment de la liste est vide
			hunt.path.pop(0)	#On le supprime
		for dir in hunt.path:	#Pour tout les r??p??rtoires trouv??s lors du premier passage
			hunt.count=hunt.count-1		#On enleve 1 au compteur
			hunt(str(argv[1])+"/"+dir,"/"+str(argv[2]))	#On refait un  deuxi??me passage dans le nouveau r??p??rtoire trouv??

		End=time.time()		#On stop le chronom??tre
		Time=End-Start		#On fait le calcul du temps de traitement du script
		print("\n")
		print(bcolors.OK+"[+] "+bcolors.RESET+"Hunting time: ", Time, "sec")	#On affiche le temps de recherche
		print(bcolors.OK+"[+] "+bcolors.RESET+"End time: ", time.ctime())	#On affiche la date ?? laquelle le script c'est termin??
		print(bcolors.OK+"[+] "+bcolors.RESET+"Your day's catch: ", count+hunt.count)	#On affiche le nombre de r??p??rtoires trouv??s
	else:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+ 'usage: python3 DirHunter.py "url" "wordlist"')

def hunt(urls,wordlist):	#D??finition de la fonction hunt avec les arguments urls et wordlist
	hunt.path=[]	#On initialise hunt.path en tant que liste
	url=urls
	hunt.count=0	#On d??marre le compteur ?? 0
	try:
		if os.path.exists(os.getcwd()+wordlist):	#Si le dictionnaire de mots existe
			file=open(os.getcwd()+wordlist,"r")	#On l'ouvre
			for i in file:	#et pour chaque mot se trouvant dedans
				dir=i.splitlines()	#On fait une liste de toutes les lignes du fichier
				dir=''.join(dir)	#et on les rejoint
				rq=requests.get(url+"/"+dir)	#On envoie la requ??te ?? l'url suivie d'un / et du mot de la liste
				dir_len=len(dir)	#initialise une variable qui contient la longueur du mot de la liste

				if rq.status_code == 200:	#Si la r??quete renvoie un code 200
					print("Aiming : "+url+"/"+dir,end="\r")		#On affiche l'url de la cible vis??e et on revient au d??but de la ligne du terminal
					time.sleep(0.05)	#On marque un temps de pause
					print("Aiming : "+url+"/"+dir_len*" ",end="\r") 	#Puis affiche l'url en remplacant la cible par des espace pour la supprimer et reviens au d??but de la ligne
					print("\n")
					print(bcolors.OK+"[+] "+bcolors.RESET+"Aiming : "+url+"/"+dir+"   "+bcolors.OK+str(rq.status_code)+bcolors.RESET+": dir shot ????????????")
					#Enfin on affiche tout avec le code re??u et la confirmation du r??sultat ??crit
					hunt.goodir=dir		#On cr??e une variable contenant le r??pertoire trouv??
					hunt.count=hunt.count+1		#On incr??mente le compteur de 1
					hunt.path.append(hunt.goodir)	#On ajoute le r??p??rtoire trouv?? dans la liste hunt.path

				elif rq.status_code == 403:	#Si la r??quete renvoie un code 403
					print("Aiming : "+url+"/"+dir,end="\r")		#On affiche l'url de la cible vis??e et on revient au d??but de la ligne du terminal
					time.sleep(0.05)	#On marque un temps de pause
					print("Aiming : "+url+"/"+dir_len*" ",end="\r")		#Puis affiche l'url en remplacant la cible par des espace pour la supprimer et reviens au d??but de la ligne
					print("\n")
					print(bcolors.WARNING+"[-] "+bcolors.RESET+"Aiming : "+url+"/"+dir+"   "+bcolors.WARNING+str(rq.status_code)+bcolors.RESET+": restricted area !") 
					#Enfin on affiche tout avec le code re??u et la signification du code
				else:	#Si la r??quete renvoie un autre code on affiche juste l'url cibl?? sans message de confirmation
					print("Aiming :"+url+"/"+dir,end="\r")
					time.sleep(0.05)
					print("Aiming :"+url+"/"+dir_len*" ",end="\r") 

			file.close()	#On ferme le dictionnaire
			print("\n")
			print(bcolors.OK+"[+] "+bcolors.RESET+"Hunt finished.")		#On informe de la fin du script

		else: #Si le chemin d'acc??s au dictionnaire n'est pas bon, on affiche un message d'erreur
			print(bcolors.FAIL+"[!] "+bcolors.RESET+wordlist+" don't exist in this directory")

	except KeyboardInterrupt:	#En cas d'interruption clavier
		print("\n")
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"Hunting has been abandoned") 	#On affiche l'abandon du script

	except Exception as e:		#Si une autre erreur arrive
		print(bcolors.FAIL+"[!] "+bcolors.RESET+e)	#On affiche le message d'erreur g??n??r??


if __name__ == '__main__':
	main()	#Lancement du script
