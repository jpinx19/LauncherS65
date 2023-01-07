# This Python file uses the following encoding: utf-8
import sys
import time
import wget
import subprocess
import minecraft_launcher_lib
import os.path
import requests
from bs4 import BeautifulSoup


version = sys.argv[1]
avecforge = sys.argv[2]
pseudo = sys.argv[3]
maxG = sys.argv[4]
RinstallF = sys.argv[5]
LatestPseudo = sys.argv[6]
optifine = sys.argv[7]
optimise = sys.argv[8] #1 = avec mods et reinstaller Mc 0 = nn
speSS65 = sys.argv[9]
memoiremini = "-Xms3g"
memoiremax = "-Xmx"

memoiremax = memoiremax + maxG + "g"
print()
print("               ******** Affichage de la configuration de lancement ********")
print("Pseudo actuel : ",pseudo)
print("Version du launcher : ",VersionDL)
print("Ram allouee : ",memoiremini," minimum et ",memoiremax," Maximum")
print("Version de Minecraft : ",version)
print("Optimisation du lancement de Minecraft (1=oui/0=non) : ",optimise)
print("Lancement de Minecraft avec forge (1=oui/0=non)   :",avecforge)
print("(RE)installation de forge (1=oui/0=non) :",RinstallF)
print("The version of Minecraft installed : ",version)
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
minecraft_directory += "/launcherSite65/"
dirlocal = minecraft_directory
minecraft_directory += version
#enregistrement prerelease
dirconfig = dirlocal + "config.txt"
dirconfigr = dirlocal + "config.txt"
configr = open(dirconfigr,"r")

texte = configr.readline()
nbrelease = 0
for car in texte:
    nbrelease = nbrelease + 1

i=1
newpre =False
print(nbrelease)
while(i<nbrelease):
    
    fichier = open((dirlocal + "prerelease" + str(i)+".txt"),"r")
    line = fichier.readline()
    line = fichier.readline()
    line.lstrip("Version : ")
    line2 = fichier.readline()
    line2.lstrip("Username : ")
    line3 = fichier.readline()
    line3.lstrip("Avec forge : ")
    line4 = fichier.readline()
    line4.lstrip("RAMM : ")
    if(line == version and line2 == pseudo and line3 == avecforge and line4 == maxG):
        newpre = False
    else:
        newpre =True
    i = i +1

config = open(dirconfig,"a+")
if(newpre):
    config.write("1")
else:
    pass
    #rien car pas de nouvelle prerelease

print("Accedez aux fichiers de jeux et de configuration du Launcher ici : ",dirlocal)
print("Minecrafts sera installé dans ce repertoire : ",minecraft_directory)
print()


def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max



callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

dirfichier = dirlocal + "latestPseudo.txt"
if(LatestPseudo=="1"):
    print("Chargement de l'ancien pseudo")
    fichier = open(dirfichier,"r")
    pseudo = fichier.read(20)
    if(pseudo != ""):
        print("Modification du pseudo : ",pseudo)
    else:
        print("Aucun ancien pseudo detecte. Pseudo : ",pseudo)
    
else:
    print()

#prerelease
if(newpre):
    direct = dirlocal + "prerelease"
    direct += str(nbrelease)
    direct += ".txt"
    essayer = open(direct,"w")
    PRERELEASE = "Prerelease" + str(nbrelease)
    essayer.write(PRERELEASE)
    essayer.write("\n")
    VERSION = "Version : "+version
    essayer.write(VERSION)
    essayer.write("\n")
    USERNAME = "Username : "+pseudo
    essayer.write(USERNAME)
    essayer.write("\n")
    AVECFORGE = "Avec forge : "+avecforge
    essayer.write(AVECFORGE)
    essayer.write("\n")
    RAM = "RAMM : "+maxG
    essayer.write(RAM)
else:
    pass
    #rien car pas de nouvelle prerelease
time.sleep(1)


fichier2 = open(dirfichier,"w")
fichier2.write(pseudo)
if(optimise=="1"):
    print("Optimisation...")
    print()
    print("Minecraft ne sera pas installé ni vérifié")
    print()
else:
    minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory, callback=callback)

options = minecraft_launcher_lib.utils.generate_test_options()
options["username"]=pseudo
options["jvmArguments"] = [memoiremini, memoiremax]
options["launcherName"]="Site65 Launcher"
options["launcherVersion"]="1.0.12"
print("Minecraft sera chargé avec ce pseudo : ",options["username"])



if(avecforge =="1"):
    forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
    callback2 = {
            "setStatus": lambda text: print(text)
        }
    #on installe forge mais on supprilme d'abord les mods
    
    directory_mods = minecraft_directory + "/mods/"
    DM = directory_mods
    if(RinstallF == "1"):  #RinstallF == "1" and optimise =="0"
        try:
            minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory, callback=callback2)
        except:
            print("Impossible de telecharger Forge")
    else:
        print("Forge ne sera pas (re)installé")
    #on installle les mods
             
    print("Telechargement des mods dans ce répertoire : ",directory_mods)
        
        
    NPCmod = "https://raw.githubusercontent.com/gamerlucas23456/mods/main/CustomNPCs_1.12.2-(05Jul20).jar"
    CunUtilmod = "https://download.pearltrees.com/s/file/download/282324976/?pearlId=486672134"
    MCglTFmod = "https://download.pearltrees.com/s/file/download/282324975/?pearlId=486672131"
    modularwarfaremode = "https://mediafilez.forgecdn.net/files/4132/725/modularwarfare-2.2.2f.jar"
    Morphmod = "https://download.pearltrees.com/s/file/download/282324973/?pearlId=486672138"
    obfuscatemod = "https://download.pearltrees.com/s/file/download/282324972/?pearlId=486672132"

    url = "https://jpinx.000webhostapp.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lienSCP = soup.find_all("p",class_="SCPLM")
    for lien1 in lienSCP:
        S = lien1.string
    print(S)

    url11 = "https://jpinx.000webhostapp.com/"
    page11 = requests.get(url11)
    soup11 = BeautifulSoup(page11.content, 'html.parser')
    lienSCP11 = soup.find_all("p",class_="ModularVC")
    for lien111 in lienSCP11:
        S11 = lien111.string
    print(S11)
    
    vehiclemod = "https://download.pearltrees.com/s/file/download/282324970/?pearlId=486672137"
    VoiceChat = S11
    WorldEdit = "https://download.pearltrees.com/s/file/download/282324968/?pearlId=486672133"
    #on supprime tous les mods
    if(optimise=="1"):
        print()
        print("Optimisation...")
        print("Les mods ne seront pas mis à jour")
        print("SVP patientez...")
        print()
        arabe = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
        versionn =arabe[1]
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(versionn['id'], minecraft_directory, options)
        subprocess.call(minecraft_command)    
    else:
        try:
            opti = DM +"OptiFine.jar"
            os.remove(opti)
        except:
            print()
            print("Impossible de supprimer OptiFine.jar")
        if(optifine=="1"):
            url6 = "https://jpinx.000webhostapp.com/"
            page6 = requests.get(url6)
            soup6 = BeautifulSoup(page6.content, 'html.parser')
            lienSCP6 = soup.find_all("p",class_="SCPLM")
            for lien16 in lienSCP6:
                S6 = lien16.string
        
            print(S6)
            optiF = directory_mods + "OptiFine.jar"
            print("Telechargement de OptiFIne")
            print()
            try:
                wget.download(S6,optiF)
            except:
                print()
                print("Impossible de telecharger OptiFIne.jar")
        
        else:
            print("OptiFine ne sera pas chargé")
        
        try:
            print("Telechargement/Mise à jour de NPCmod")
            dir1 = directory_mods + "NPCmod.jar"
            wget.download(NPCmod,dir1)
        except:
            print("Impossible de telecharger le mod...")
            #la

        try:
            print()
            dir2 = directory_mods + "CunUtilmod.jar"
            print("Telechargement/Mise à jour de : CunUtilmod")
            wget.download(CunUtilmod,dir2)
        except:
            print("Impossible de telecharger le mod...")
        try:
            print()
            dir3 = directory_mods + "MCglTFmod.jar"
            print("Telechargement/Mise à jour de : MCglTFmod")
            wget.download(MCglTFmod,dir3)
        except:
            print("Impossible de telecharger le mod...")

        try:
            print()
            dir4 = directory_mods + "Morphmod.jar"
            print("Telechargement/Mise à jour de : Morphmod")
            wget.download(Morphmod,dir4)
        except:
            print("Impossible de telecharger le mod...")
            
        try:
            print()
            dir5 = directory_mods + "obfuscatemod.jar"
            print("Telechargement/Mise à jour de : obfuscatemod")
            wget.download(obfuscatemod,dir5)
        except:
            print("Impossible de telecharger le mod...")
    
        try:
            print()
            dir6 = directory_mods + "vehiclemod.jar"
            print("Telechargement/Mise à jour de : vehiclemod")
            wget.download(vehiclemod,dir6)
        except:
            print("Impossible de telecharger le mod...")

        try:    
            print()
            dir7 = directory_mods + "ModularVoiceChatmod.jar"
            print("Telechargement/Mise à jour de : VoiceChatmod")
            wget.download(VoiceChat,dir7)
        except:
            print("Impossible de telecharger le mod...")

        try:
            print()
            dir8 = directory_mods + "WorldEdit.jar"
            print("Telechargement/Mise à jour de : WorldEdit")
            wget.download(WorldEdit,dir8)
        except:
            print("Impossible de telecharger le mod...")

        try:
            print()
            dir9 = directory_mods + "SCPLockdownmod.jar"
            print("Telechargement/Mise à jour de : SCPLockdownmod")
            wget.download(S,dir9)
        except:
            print("Impossible de telecharger le mod...")
        
        try:
            print()
            dir10 = directory_mods + "modularwarfaremod.jar"
            print("Telechargement/Mise à jour de : modularwarfaremod")
            wget.download(modularwarfaremode,dir10)
        except:
            print("Impossible de telecharger le mod...")

            
        try:
            one = DM + "NPCmod (1).jar"
            os.remove(one)
            two = DM + "CunUtilmod (1).jar"
            os.remove(two)
            three = DM + "MCglTFmod (1).jar"
            os.remove(three)
            four = DM + "Morphmod (1).jar"
            os.remove(four)
            five = DM + "obfuscatemod (1).jar"
            os.remove(five)
            six = DM + "vehiclemod (1).jar"
            os.remove(six)
            seven = DM + "VoiceChatmod (1).jar"
            os.remove(seven)
            eight = DM + "WorldEdit (1).jar"
            os.remove(eight)
            nine = DM + "SCPLockdownmod (1).jar"
            os.remove(nine)
        
        
        
        except:
            print("Supression des mods ignorés")
        try:
            ten = DM + "modularwarfaremod (1).jar"
            os.remove(ten)
        except:
            print("Impossible de supprimer modularwarfaremod (1).jar dans le dossier mod")
        

    #et on lance
            if(optimise=="1"):
                pass
            else:
                arabe = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
                try:
                    versionn = arabe[1]
                except:
                    versionn = arabe[0]
                print("Impossible de charger et de detecter Forge (2 causes posssibles , voir README")
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(versionn['id'], minecraft_directory, options)
                subprocess.call(minecraft_command)
            
        
elif(avecforge=="0"):
    
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
    subprocess.call(minecraft_command)

else:

    print("Error:LS65 n'a pas donné l'argument 'avecforge', mettre à jour le LauncherS65peut resoudre ce probleme sinon demander de l'aide au développeur")





