import os
from PIL import Image

Size : int = 128,128
PathFol : str

#Commences le script
def start():
    print("[Script] Quel est le chemin du dossier que vous souhaitez? (exemple: 'C:/Users/')")
    PathFol = str(input("Ecrivez le chemin de votre dossier: "))
    print ("[Script] le chemin actuel du dossier est: " + PathFol)
    rezise(PathFol)
    
#Obtiens les images qui sont dans le fichier où se trouve le script
def GetFile(path1):
    try: 
        FilesInFolder = os.listdir(path1)
    except os.error:
        print ("[Script] Erreur la recherche du dossier, veuillez recommencer!")
        print ("------------------------------------------------------------------")
        return start()
    Files = []
    
    for a in FilesInFolder:
        if a.endswith((".png",".jpg")):
            Files.append(a)
    if len(Files) > 0:
        print (("[Script] les images trouvées sont: ") + str(Files))
    else:
        print ("[Script] Dossier non trouvé")
    return Files

#Redimensionnes les images obtenus avec la func GetFile()
def rezise(path1):
    pictures = GetFile(path1)
    if len(pictures) > 0 :
        FolderThumbnails = '\\thumbnails\\'
        try:
            os.mkdir(path1 + FolderThumbnails)
        except os.error:
            print ("[Script] Dossier déjà existant!")
        else:
            print ("[Script] dossier Créé!")
        print ("--------------------------------------------------------")
        for pic in pictures:
            picResize = Image.open(path1 +'\\' + str(pic))
            picResize.thumbnail(size=Size)
            picResize.save( path1 + FolderThumbnails + pic.split(".")[0] +"-thumbnail" + ".png","png")
            print ("[Script] Vignettes crées et placer dans le dosier Thumbnails")
            print ("--------------------------------------------------------")
            restart()
    else:
        print("[Script] Erreur! Dossier ou image non trouvé!")
        print ("--------------------------------------------------------")
        restart()

#Rejoues le script ou non
def restart():
    Choice = str(input("Voulez-vous réessayer? [y/n]"))
    if Choice == ("y" or "Y"):
        print ("--------------------------------------------------------")
        return start()
    elif Choice == ("n" or "N"):
        return exit()
    else:
        return restart()

# ---------------------------------------- #
start()



