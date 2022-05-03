# 1. Explanation Of Normal 2d Line Graph Code :

**First you need to import some libraries below : **
```py
import matplotlib.pyplot as plt
import re
import os
import time
from colorama import Fore,Back,Style
import socket
from bs4 import BeautifulSoup
```

**And Color Class :**
**Its for make sentences colorfull.**
```py
class bcolors:
    OK = '\033[92m' 
    WA = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m'
```

**Menu Code for select operation number : **
```py
print("Please Select Operation : ")
print(" ")
print(f"{bcolors.OK}[1] 2D Line Graf")
print(f"{bcolors.OK}[Q] Quit")
n = input("-> ")
```

**Function To plot normal 2d line graph with matplotlib library : **
```py
def normal():
    name = input(f"{bcolors.FAIL}Name Of Graph : ")
    xg =  input(f"{bcolors.FAIL}Name of X : ")
    yg =  input(f"{bcolors.FAIL}Name of Y : ")
    xn =  int(input(f"{bcolors.FAIL}How many elements will be inside X : "))
    yn =  int(input(f"{bcolors.FAIL}How many elements will be inside Y : "))
    x = []
    y = []
    print("X Elements : ")
    for i in range(0, xn):
        j = int(input())
        x.append(j)
    print("Y Elements : ")
    for i in range(0,yn):
        j = int(input())
        y.append(j)
    plt.plot(x, y)
    plt.xlabel(xg)
    plt.ylabel(yg)
    plt.title(name)
    plt.show()
```

**And last one for run selected operation :**
```py

if n == '1':
    normal()
elif n == 'Q' or n == 'q':
    print(f"{bcolors.FAIL}Thanks you for using ATS...")
    print(f"{bcolors.FAIL}Quitting...")
```
