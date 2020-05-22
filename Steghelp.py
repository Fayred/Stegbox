#coding:utf-8

def Steghelp():
    print("""
[Aide] :
    help : affiche la fiche d'aide
    exit : quitte le programme
    clear : efface la console
    stegphoto :
        --hidden : pour cacher un fichier 
         --sfile=<fichier> : chemin vers le fichier à cacher
         --output=<fichier> : nom de l'image en sortie qui contiendra le fichier caché
        --restore : pour retrouver un fichier
        --pfile=<fichier> : chemin vers l'image qui doit contenir le fichier

[Informations] :
    [-] : signifie une erreur/un bug
    [+] : signifie qu'il n'y a eu aucun problème 
    [i'] : informations divers

    """)

if __name__ == "__main__":
    print("[i'] Module de StegBox.")