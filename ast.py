import re
import os
import time
from colorama import Fore,Back,Style
import socket
from bs4 import BeautifulSoup
class bcolors:
    OK = '\033[92m' 
    WA = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m'
print(f"{bcolors.OK} AST yә Hoşgәldiniz! (Azәrbaycan İstatistika Teşkilatı) Aşağıda dilinizi seçә bilәrsiniz : ")
print(f"{bcolors.OK} AST ye Hoşgeldiniz! (Azerbaycan İstatistika Teşkilatı) Aşağıda dilinizi seçe bilirsiniz : ")
print(f"{bcolors.OK} Welcome to AST! (Azerbaijan Statistics Team) You can select your language below         : ")
print(" ")

print(f"{bcolors.OK} Azәrbaycanca : AZ")
print(f"{bcolors.OK} Türkçe       : TR")
print(f"{bcolors.OK} English      : EN")
n = input(f"{bcolors.FAIL} > ")

if n=="AZ":
    print("Azәrbaycanca dili seçildi...")
    print("Program Başlatılır...")
    time.sleep(2)
    os.system("python3 ./core/AZ/main.py")
if n=="TR":
    print("Türkçe dili seçildi...")
    print("Program başlatılıyor...")
    time.sleep(2)
    os.system("python3 ./core/TR/main.py")
if n=="EN":
    print("Language selected english...")
    print("Aplication starting...")
    time.sleep(2)
    os.system("python3 ./core/EN/main.py")