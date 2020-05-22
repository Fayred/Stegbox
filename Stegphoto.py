#coding:utf-8

import os

def StegphotoEcriture(photo, fichier, imageEnSortie):
    if os.path.exists(imageEnSortie): 
        print(f" [-] Nom d'image '{imageEnSortie}' déjà existant.")
    else:
        with open(fichier, "rb") as f:
            lectureBinaireFichier = f.read()
    
        with open(photo, "rb") as f:
            lectureBinairePhoto = f.read()

        with open(imageEnSortie, "ab") as f:
            f.write(lectureBinairePhoto)
            f.write(f"\n{fichier}".encode())
            f.write(("\n"+"STEGPHOTO-FILE".center(30,"-")+"\n").encode()) #délimiteurs du contenu du fichier caché
            f.write(lectureBinaireFichier)
            f.write(b"\n"+"EOF".center(30,"-").encode()+b"\n") #délimiteurs    
            
        print(" [+] Fichier caché.")

def StegphotoLecture(photo):
    with open(photo, "rb") as f:
        l = f.readlines()
        posDebut=l.index(("STEGPHOTO-FILE".center(30,"-")+"\n").encode())+1 #+1 pour le 1er item de la liste concernant le fichier caché
        posFin = l.index(("EOF".center(30,"-")+"\n").encode())

    nomDuFichier = l[posDebut-2].decode().strip() #l[posDebut-2] position du nom de fichier

    if os.path.exists(nomDuFichier):
        print(f" [-] Nom de fichier '{nomDuFichier}' déjà existant.")
    else:
        with open(nomDuFichier, "wb") as f:
            for c in l[posDebut:posFin-1]: #on écrit pas directement la dernière ligne car sinon on va ajouter un \n en trop
                f.write(c)
            f.write(l[posFin-1].strip()) #on enlève le \n en trop 
            print(" [+] Fichier restauré.")

if __name__ == "__main__":
    print("[i'] Module de StegBox.")