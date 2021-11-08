import os
from PIL import Image

Size : int = 128,128
PathFol : str

#Commences le script
def start():
    print("[Script] Quel est le chemin du dossier que vous souhaitez? (exemple: 'C:/Users/')")
    PathFol = str(input("Ecrivez le chemin de votre dossier image: "))
    print ("[Script] le chemin actuel du dossier est: " + PathFol)
    rezise(PathFol)

def GetPathFolder(folder):
    Path1 : str = folder
    PathFol2 = str(input("Ecrivez le chemin de votre dossier où se situe votre page HTML: "))
    root = (input("Votre dossier racine: "))
    
    pathsplit = Path1.split(str(root))
    
    try:
        pathfolder = pathsplit[1].split('\\')
    except:
        print ("[Script] Erreur!")
        return GetPathFolder(Path1)
    else:
        pathfolder.pop(0)
        nbsPath = len(PathFol2.split(str(root)))

        Path2 : str = ""
        nbs : int = 0

        while nbs != nbsPath:   
            if nbs == nbsPath - 1:
                Path2 += ".."
            else:
                Path2 += '..\\'
            nbs += 1

        Path2 += str(pathsplit[1])
        print ("[Script] Le chemin vers votre dossier où se situe votre galerie est: " + str(Path2))
        return Path2

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
        print ("------------------------------------------------------------------")
        for pic in pictures:
            namepic = str(pic).split(".")
            picResize = Image.open(path1 +'\\' + str(pic))
            picResize.thumbnail(size=Size)
            picResize.save( path1 + FolderThumbnails + namepic[0] + ".png","png")
        print ("[Script] Vignettes crées et placer dans le dosier Thumbnails")
        print ("------------------------------------------------------------------")
        WriteFile(path1,pictures)
    else:
        print("[Script] Erreur! Dossier ou image non trouvé!")
        print ("------------------------------------------------------------------")
        restart()

#Ecris dans un fichier, les balises pour intégrer les élements
def WriteFile(folder,files):
    path2 = folder
    pictures = files
    path3 = str(GetPathFolder(path2))

    print("[Script] Voulez-vous un fichier texte comprenant les balises?")
    choice = str(input("[y/n]"))
    if choice == ("y" or "Y"):
        try:
            os.path.exists(path2)
        except OSError:
            print ("[Script] Dossier non trouvé! Veuillez réessayer!")
            return WriteFile(path2,pictures)
        else:
            fileText = "GetScriptHTML.txt"

            f = open(str(path2) + "\\" + fileText,"w")
            for i in pictures:
                namepic = str(i).split(".")
                pathFolderImage = str(path3 + "\\" + str(i))
                
                pathFolderThumbnails = path3 + '\\thumbnails\\' + str(namepic[0]) + ".png"
                f.write(("<a href=" + "'" + pathFolderImage + "'" + str(" data-lightbox= ") + "'" + str("illustrations") + "' " + str(" data-title=") + "'" + str(i) + "'" + str("> <img class= ") + "'" + str("illustrations") + "'" + str(" src=") + "'" + pathFolderThumbnails + "'" + str(" alt=") + "'" + str(i) + "'" + str("></a>" + "\n")))
            
            f.close()
            restart()
    elif choice == ("n" or "N"):
        return restart()
    else:
        return WriteFile(folder=path2)

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



