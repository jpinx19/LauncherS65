import sys
import wget
import os
import requests
from bs4 import BeautifulSoup


VersionDL = "1.0.17"

url3 = "https://jpinx.000webhostapp.com/"
page3 = requests.get(url3)
soup3 = BeautifulSoup(page3.content, 'html.parser')
lienSCP3 = soup3.find_all("p",class_="LatestVersion")
for lien13 in lienSCP3:
    S3 = lien13.string

if(S3 == VersionDL):
    print()
    print("A jour !")
    print()
else:
    print()
    print("Une mise a jour est disponible!")
    print("Version actuelle : ",VersionDL)
    print("Version disponible : ",S3)
    print()
url = "https://raw.githubusercontent.com/jpinx19/LauncherS65/main/update/"
urlLS65 = url + "LS65.exe"
urlS65L = url + "S65L.exe"
urlconfigo = url + "configurercompte.o"
urlmain = url +"main.o"
urlmainS65 = url  + "mainS65L.o"
urlmc = url +"minecraft.py"
urlmoc1 = url +"moc_predefs.h"
urlmoc2 = url + "moc_widget.cpp"
urlmoc3 = url + "moc_widget.h"
urlwidget = url + "widget.o"
urlupdate = url + "update.py"
try:
    
    os.remove("LS65.exe")
    os.remove("S65L.exe")
    os.remove("configurercompte.o")
    os.remove("main.o")
    os.remove("mainS65L.o")
    os.remove("minecraft.py")
    os.remove("moc_predefs.h")
    os.remove("moc_widget.cpp")
    os.remove("moc_widget.h")
    os.remove("widget.o")
except:
    print("code 100")
    
try:
    wget.download(urlLS65)
    wget.download(urlS65L)
    wget.download(urlconfigo)
    wget.download(urlmain)
    wget.download(urlmainS65)
    wget.download(urlmc)
    wget.download(urlmoc1)
    wget.download(urlmoc2)
    wget.download(urlmoc3)
    wget.download(urlwidget)
    wget.download(urlupdate)
except:
    print("Mise a jour / telechargement impossible")

try:
    os.remove("update.py")
except:
    print("code 200")
