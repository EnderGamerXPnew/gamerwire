#gamewire by EnderGamerXP
import os
os.putenv


if(os.system("call check.bat")=="config"):
    print("voici le dossier de configuration\n")
    os.system("start wire")
    print("le fichier inout contient les lien des dossier entree est sortie separer par un retour chario\n")
    print("le dossier pools contien les images des structures de remplacement\n")
    print("le fichier equi est le filtre de remplacement des structures les struture sont connecter par un espace et separer aussi par un retour chario marquer sur une ligne in ou out definira la cible de communication\n\n")
    print("appuyer sur entree pour quiter")
    os.system("pause>nul")
else:
    bin=False
    inout=open("wire/inout.txt")
    for i in inout:
        if(bin==False):
            IN=i
            bin=True
        else:
            OUT=i
            break
    bin=False
    inout.close()
    equi=open("wire/equi.txt")
    for i in equi:
        buff=""
        odr=""
        scan=""
        for j in i:
            if (j!=" " and j!="\n"):
                buff=buff+j
            else:
                if(odr!=""):
                    if(scan!=""):
                        print("execution de l'instruction...")
                        os.environ['odr']=odr
                        os.environ['in']=IN
                        os.environ['out']=OUT
                        os.environ['buff']=buff
                        os.environ['scan']=scan
                        os.system("call pompe.bat")
                    else:
                        scan=buff
                        print("analyse du fichier "+buff)
                        buff=""
                if(buff=="in"):
                    print("ordre=entre")
                    odr="in"
                    buff=""
                if(buff=="out"):
                    print("ordre=sortie")
                    odr="out"
                    buff=""
    equi.close()
    print("fin du programme")
