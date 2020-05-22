#!/usr/bin/python3
#coding:utf-8

import os, getopt
import Stegphoto, Steghelp

print("""
 $$$$$$\    $$\                         $$\                           
$$  __$$\   $$ |                        $$ |                          
$$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ 
\$$$$$$\  \_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \$$\ $$  |
 \____$$\   $$ |    $$$$$$$$ |$$ /  $$ |$$ |  $$ |$$ /  $$ | \$$$$  / 
$$\   $$ |  $$ |$$\ $$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ | $$  $$<  
\$$$$$$  |  \$$$$  |\$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$  |$$  /\$$\ 
 \______/    \____/  \_______| \____$$ |\_______/  \______/ \__/  \__|
                              $$\   $$ |                              
                              \$$$$$$  |                              
                               \______/  

[ VERSION BETA : 1.0 || CREATEUR : FAYRED || DATE DE CREATION : 18/05/20 ]

""")
while True:
    try:
        cmd = input(f"Stegbox.py@{os.getlogin()}$> ").split()
        if cmd[0] == "help": Steghelp.Steghelp()
        elif cmd[0] == "exit": exit()
        elif cmd[0] == "clear": os.system("cls") if os.name == "nt" else os.system("clear")
        elif cmd[0] == "stegphoto":
            try:
                lopt, args = getopt.getopt(cmd[1:], "", ["hidden", "restore", "sfile=", "pfile=", "output="])
                if "--hidden" in cmd:
                    for opt, a in lopt:
                        if opt == "--pfile":photo = a
                        elif opt == "--sfile":fichierSecret = a
                        elif opt == "--output": imageEnSortie = a
                    Stegphoto.StegphotoEcriture(photo, fichierSecret, imageEnSortie)
                elif "--restore" in cmd:
                    for opt, a in lopt:
                        if opt == "--pfile":photo = a
                    Stegphoto.StegphotoLecture(photo)
                else:
                    print(" [-] Erreur du aux arguments.")
            except Exception:
                print(" [-] Erreur du aux arguments.")
        else:
            print(" [-] Commande inconnue.")
    except IndexError:
        print(e)
        print(" [-] Veuillez entrer une commande.")