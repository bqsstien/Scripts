#! usr/bin/python3
#--*-- coding: UTF-8 --*-- coding


""" Ce script permet de trier les fichiers d'un répertoire par type d'extension """

import os
import sys
from glob import glob
from shutil import move

print(" ")
print(" ")
print("-" * 60)
print(("-" *20) + " TRIEUR DE FICHIERS " + ("-" * 20))
print("-" * 60 )
print(" ")
print(" ")

#User entre le repertoire de travail
directoryInput = input('Chemin du repertoire à trier -> ')
print(" ")
print(" ")

#Repertoire à trier
if os.path.exists(directoryInput):
    os.chdir(directoryInput)
else:
    print("*** Le Repertoire saisi n'existe pas !")
    sys.exit()
    
print(f'*** REPERTOIRE A TRIER : ', os.getcwd())

#Liste de fichiers possible
fichiersMusiques = [".mp3", ".wav"]
fichiersVideos = [".mp4", ".avi", ".mkv"]
fichiersDocuments = [".docx", ".pdf", ".pptx", ".csv", ".json", ".sql"]
fichiersImages = [".jpg", ".png", ".jpeg", ".svg"]
fichiersArchives = [".zip", ".rar", ".7z", ".hct", ]



#Creer les repertoires
def MakeDirectories(DirectoryName):
    try:
        os.mkdir(DirectoryName)
    except:
        pass

#MakeDirectories("Archives")
#MakeDirectories('Videos')
#MakeDirectories('Images')
#MakeDirectories('Musiques')
#MakeDirectories('Documents')

#Liste les fichiers du repertoire

files = glob(os.path.join(os.getcwd(), "*"))

#tri les fichiers et les classe dans le bon repertoire
for file in files:
    extension = os.path.splitext(file)[1]
    
    if extension in fichiersArchives:
        move(file, 'Archives')
        
    elif extension in fichiersImages:
        move(file, "Images")
        
    elif extension in fichiersDocuments:
        move(file, "Documents")
        
    elif extension in fichiersVideos:
        move(file, "Videos")
        
    elif extension in fichiersMusiques:
        move(file, "Musiques")
        
    else:
        if os.path.isdir(file):
            pass
        else:
            print(f'Impossible de ranger {file}')
        
        