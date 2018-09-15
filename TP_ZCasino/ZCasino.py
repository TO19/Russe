#####################
# TP_ZCasino V 1.0.0
# ZCasino.py
# main
# FOURRAGEAT Baptiste
#####################

#-------langue-------

# ** Français **

#-----------encodage-----------

# -*-coding:Utf-8 -*

#-----------------modules------------------

import style
import os
from time import sleep
from time import asctime
from random import randrange
from sys import argv
from math import ceil

#-----------------------fonctions----------------------------

# ref : module style.py

# ref (5)
logsfile = '/home/anto/desktop/Roulette_Ageat/Python-OpenClassRooms/TP_ZCasino/logsfile.txt'
def logs(arg1, arg2, arg3):
    target = open(logsfile, 'a')
    target.write(str(asctime()))
    target.write("\n")
    target.write(f"\t{arg1}{arg2}{arg3}\n\n")
    target.close()

# dictionnaire de fonctions
ref = {}
ref[1] = style.head
ref[2] = style.roulette_annimation
ref[3] = style.str_annimation1
ref[4] = style.str_annimation2
ref[5] = logs

#---------------------------------intro--------------------------------------

os.system('clear') # on nettoie le prompt
os.system('tput civis -- invisible') # on rend invisible le curseur du prompt

cred = 00 # initialisation des cédits
titre = "roulette" # (modifiable) la décoration est gérée par la fonction head ref (1)

ref[1](cred, titre) # ref (1)

target = open(logsfile, 'w')

pseudo = input("Veuillez choisir un nom de joueur : ")

target.write("\n----------------------------------------\n")
target.write(f"Historique de la partie de : {pseudo}\n")
target.write("logon : ")
target.write(str(asctime()))
target.write("\n----------------------------------------\n\n")
target.close()

cred = 50

ref[1](cred, titre) # ref (1)
ref[4](cred, titre, f"Bonjour {pseudo}, vous allez jouer à la roulette...", 0.1) # ref (4)
sleep(0.5) # pause en secondes
ref[3](cred, titre, "\nVous disposez de", "$\n" , "$\n", cred, var = True) # ref (3)
sleep(0.5) # pause en secondes
input("Appuyez sur ENTREE pour continuer... ") # on demande une confirmation pour continuer

ref[5]('début de partie : ', cred, '$')

#-------------------------------------------boucle de jeu------------------------------------------------

# on initialise la variable comme une chaine de caracteres vide car on l'utilise dans les conditions
# de la boucle de jeu. Elle deffinit si on relance la boucle de jeu ou non
ctn = str()

# lancement de la boucle de jeu
# la boucle vérifie si il y a encore des crédits et si l'on n'a pas souhaité quitter la partie
while (cred > 0) and (ctn.lower() != "n"):

    # ref (1)
    ref[1](cred, titre)

    # on initialise la variable à None pour bien rentrer dans la boucle
    nbr_int = None

    # cette boucle vérifie que les saisies sont correctes et se relance tant que ça n'est pas le cas
    # on demande de saisir un nombre entier positif compris entre 0 et 49 inclus
    while (nbr_int is None) or (nbr_int < 0) or (nbr_int > 49):
        try:
            nbr = input("Choisissez un nombre compris entre 0 et 49 inclus : ")
            nbr_int = int(nbr) # on convertit la chaine de caractere en entier
        except ValueError:
            print("\nSaisie incorecte!\nVeuiller saisir un nombre entier positif.")
        if (nbr_int is None) or (nbr_int < 0) or (nbr_int > 49):
            print("\nSaisie incorecte!")

    # on initialise une variable qui sera vraie si le nombre choisi est pair, faux si il est impair
    # pair = True = noir et impair = False = rouge
    if nbr_int % 2 == 0:
        color_nbr_int = True
        ref[5]('nombre choisi : ', nbr, ' noir')
    else:
        color_nbr_int = False
        ref[5]('nombre choisi : ', nbr, ' rouge')

    # ref (1)
    ref[1](cred, titre)

    # on initialise la variable à None pour bien rentrer dans la boucle
    mise_int = None

    # cette boucle vérifie que les saisies sont correctes et se relance tant que ça n'est pas le cas
    # on demande de saisir un nombre entier positif plus petit ou égale au crédit restant
    while (mise_int is None) or (mise_int > cred) or (mise_int <= 0):
        try:
            mise = input(f"Choisissez le montant de votre mise (solde : {cred}$) : ")
            mise_int = int(mise) # on convertit la chaine de caractere en entier
        except ValueError:
            print("\nSaisie incorecte!\nVeuiller saisir un nombre entier positif.")
        if (mise_int is None) or (mise_int <= 0) or (mise_int > cred):
            print("\nSaisie incorecte!")

    ref[5]('mise choisie : ', mise, '$')

    # on mets à jour le solde de crédits
    cred = cred - mise_int

    # ref (1)
    ref[1](cred, titre)

    # on récapitule au joueur ses données de jeux
    if color_nbr_int is True:
        print(f"\tVous misez {mise_int}$ sur le {nbr_int} noir.")
    else:
        print(f"Vous misez {mise_int}$ sur le {nbr_int} rouge.")

    # on demmande une confirmation pour continuer
    input("\nAppuyez sur ENTREE pour lancer la roulette.")

    # ref (2)
    ref[2](cred, titre, "Rien ne va plus...\t", 50)

    # on fait appel à la fonction randrange qui va stocker dans une variable,
    # un nombre compris entre 0 et 49 inclus, et choisi de façon aléatoire
    roul = randrange(50)
    roul_str = str(roul)

    # on initialise une variable qui sera vraie si roul est paire, faux si elle est impaire
    # pair = noir et impair = rouge
    if roul % 2 == 0:
        color_roul = True
        ref[5]("roulette : ", roul_str, " noir")
    else:
        color_roul = False
        ref[5]("roulette : ", roul_str, " rouge")

    # ref (3)
    params = [cred, titre, "\t\t\tLe", "noir\n", "rouge\n", roul, color_roul]
    ref[3](*params)

    # ref (1)
    ref[1](cred, titre)

    # on indique au joueur le nombre et la couleur de la roulette
    if color_roul is True:
        print(f"\t\t\tLe {roul} noir\n")
    else:
        print(f"\t\t\tLe {roul} rouge\n")

    # ici on compare nos variables, celle choisie par le joueur et celle choisie par l'ordinateur
    # et on agit différement en fonction des résultats
    if nbr_int == roul:
        cred = cred + mise_int * 3
        print(f"Vous gagnez. \n\n\tNouveau solde : {cred}$\n")
    elif color_nbr_int == color_roul:
        cred = ceil(cred + mise_int * 1.5) # ici on arrondi par excès les nombres décimaux
        print(f"Vous gagnez avec la couleur. \n\n\tNouveau solde : {cred}$\n")
    else:
        print(f"Vous perdez. \n\n\tNouveau solde : {cred}$\n")

    ref[5]("nouveau solde : ", cred, "$")

    # on initialise la variable de façon à ce qu'elle soit différente de "n" et de "o" pour rentrer
    # dans la boucle. Lors du premier tour, c'est déjà le cas mais dès le deuxième tour, elle vaudra "o"
    ctn = str()

    # on vérifie que le solde de crédits n'est pas nul
    # si c'est le cas le joueur sort de la boucle sinon, on lui demande si il veut continuer
    if cred == 0:
        print("\nVotre solde est à 0$, vous ne pouvez plus jouer.")
        input("\nAppuyer sur ENTREE pour quitter : ")
    else:
        while(ctn.lower() != "n") and (ctn.lower() != "o"):
            ctn = input("Souhaitez-vous continuer la Roulette (o/n)? : ")
            if (ctn.lower() != "n") and (ctn.lower() != "o"):
                print("\nSaisie incorecte!")

    if (ctn.lower() == "n") or (cred == 0):
        target = open(logsfile, 'a')
        target.write("----------------------------------------\n")
        target.write(f"Historique de la partie de : {pseudo}\n")
        target.write("logout : ")
        target.write(str(asctime()))
        target.write("\n----------------------------------------\n")
        target.close()
    else:
        ref[5]("nouvelle ", "partie", "." )

#------------------------------------------sortie de boucle----------------------------------------------

ref[4](cred, titre, "\n\tMerci d'avoir joué à la roulette...", 0.1) # ref (4)
ref[4](cred, titre, "\n\t...et à bientôt...", 0.1) # ref (4)

sleep(1.0) # pause en secondes
os.system('clear') # on nettoie le prompt
os.system('tput cnorm -- normal') # on rend à nouveau visible le curseur du prompt

#------------------------------------------fin du programme----------------------------------------------
