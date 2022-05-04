import matplotlib.pyplot as plt
import re
import os
import time
from colorama import Fore,Back,Style
from bs4 import BeautifulSoup

class bcolors:
    OK = '\033[92m' 
    WA = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m'

print("Aşağıdan İstediğiniz Emeliyati Sece Bilersiniz : ")
print(" ")
print(f"{bcolors.OK}[1] 2D Line Graf")
print(f"{bcolors.OK}[2] Pie Graf")
print(f"{bcolors.OK}[Q] Çıx")
n = input("-> ")

def normal():
    name = input(f"{bcolors.FAIL}Grafınızın Adı : ")
    xg =  input(f"{bcolors.FAIL}X'ın adı : ")
    yg =  input(f"{bcolors.FAIL}Y'ın adı : ")
    xn =  int(input(f"{bcolors.FAIL}X'ın içinde neçe dene eleman olacak : "))
    yn =  int(input(f"{bcolors.FAIL}Y'ın içinde neçe dene eleman olucak : "))
    x = []
    y = []
    print("X Datasi : ")
    for i in range(0, xn):
        j = int(input())
        x.append(j)
    print("Y Datasi : ")
    for i in range(0,yn):
        j = int(input())
        y.append(j)
    plt.plot(x, y)
    plt.xlabel(xg)
    plt.ylabel(yg)
    plt.title(name)
    plt.show()

def pie():
    name = input(f"{bcolors.FAIL}Grafınızın Adı : ")
    x = []
    xn =  int(input(f"{bcolors.FAIL}X'ın içinde neçe dene eleman olacak : "))

    print("X Datasi : ")
    for i in range(0, xn):
        j = int(input())
        x.append(j)
    print(f"{bcolors.OK}Pie chart graph datasi alindi...")
    time.sleep(1)
    print(f"{bcolors.OK}İndi ise grafik görünüm datasini girin (0 birleşik 1 ise ayrı demekdir. Ve ek bilgi : Grafik Görünüm datasi X datasi ile eyni sayida olmalidir.) : ")
    e=[]
    print(f"{bcolors.OK}E Datasi : ")
    for i in range(0,xn):
        j = int(input())
        e.append(j)
    plt.pie(x, explode = e)
    plt.title(name)
    plt.show()

if n == '1':
    normal()
elif n == '2':
    pie()
elif n == 'Q' or n == 'q':
    print(f"{bcolors.FAIL}AST yi istifade elediğiniz için teşekkür ederiz...")
    print(f"{bcolors.FAIL}Programdan çıxılır...")
