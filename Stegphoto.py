#coding:utf-8

import os, base64
from cryptography.fernet import Fernet

def StegphotoEcriture(photo, fichier, imageEnSortie, motDePasse):

    if os.path.exists(imageEnSortie): 
        print(f" [-] Nom d'image '{imageEnSortie}' déjà existant.")
    else:        
        with open(fichier, "rb") as f:
            lectureBinaireFichier = f.read()
        
        motDePasse = base64.b64encode((motDePasse*(32//len(motDePasse))+motDePasse[:(32%len(motDePasse))]).encode())
        suiteChiffre = Fernet(motDePasse)
        texteChiffre = suiteChiffre.encrypt(lectureBinaireFichier)
    
        with open(photo, "rb") as f:
            lectureBinairePhoto = f.read()

        with open(imageEnSortie, "ab") as f:
            f.write(lectureBinairePhoto)
            f.write(f"\n{fichier}".encode())
            f.write(("\n"+"STEGPHOTO-FILE".center(30,"-")+"\n").encode())
            f.write(texteChiffre)
            f.write(b"\n"+"EOF".center(30,"-").encode()+b"\n")   
            
        print(" [+] Fichier caché.")

def StegphotoLecture(photo, motDePasse):
    with open(photo, "rb") as f:
        l = f.readlines()
        posDebut = l.index(("STEGPHOTO-FILE".center(30,"-")+"\n").encode())+1
        posFin = l.index(("EOF".center(30,"-")+"\n").encode())-1

    nomDuFichier = l[posDebut-2].decode().strip()

    if os.path.exists(nomDuFichier):
        print(f" [-] Nom de fichier '{nomDuFichier}' déjà existant.")
    else:
        motDePasse = base64.b64encode((motDePasse*(32//len(motDePasse))+motDePasse[:(32%len(motDePasse))]).encode())
        suiteChiffre = Fernet(motDePasse)
        dechiffrement = suiteChiffre.decrypt(l[posDebut].strip())
    
        with open(nomDuFichier, "wb") as f:
            f.write(dechiffrement)

        print(" [+] Fichier restauré.")

if __name__ == "__main__":
    print("[i'] Module de StegBox.")