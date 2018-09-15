#####################
# TP_ZCasino V 1.0.0
# style.py
# module
# FOURRAGEAT Baptiste
#####################

#-------langue-------

# ** Français **

#-----------encodage-----------

# -*-coding:Utf-8 -*

#-----------------modules------------------

import os
from time import sleep

#-----------------------fonctions----------------------------

# ref (1)
def head (cred, titre):
    os.system ('clear')
    deco = ""
    for i in titre:
        i = "-"
        deco = deco + i
    print (f"Crédits : {cred}$\n\n" + titre.upper().center(70))
    print (deco.center(70) + "\n\n")

# ref (2)
def roulette_annimation (cred, titre, str, max):
    i = 0
    y = 0
    while (y != max) and (i != 400):
        head (cred, titre)
        print (f"{str}{y}")
        sleep (0.005)
        if y == (max - 1):
            y = 0
        else:
            y += 1
        i += 1

# ref (3)
def str_annimation1 (cred, titre, str1, str2, str3, nbr, var):
    i = 0
    while i != 5:
        head (cred, titre)
        sleep (0.4)
        if var is True:
            print (f"{str1} {nbr} {str2}")
        else:
            print (f"{str1} {nbr} {str3}")
        sleep (0.4)
        i += 1

# ref (4)
def str_annimation2 (cred, titre, chaine, speed):
    str = ""
    for i in chaine:
        head (cred, titre)
        str = str + i
        print (str)
        sleep (speed)

#---------------------fin du module---------------------
