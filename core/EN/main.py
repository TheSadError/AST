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

print("Please Select Operation : ")
print(" ")
print(f"{bcolors.OK}[1] 2D Line Graf")
print(f"{bcolors.OK}[2] Pie Graph")
print(f"{bcolors.OK}[Q] Quit")
n = input("-> ")

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

def pie():
    name = input(f"{bcolors.FAIL}Name of graph : ")
    x = []
    xn =  int(input(f"{bcolors.FAIL}How many elements will be in X data: "))

    print("X Datasi : ")
    for i in range(0, xn):
        j = int(input())
        x.append(j)
    print(f"{bcolors.OK}Getting Inputted Data...")
    time.sleep(1)
    print(f"{bcolors.OK}Now, enter the chart view data (0 means combined, 1 separate. And additional information: Chart View data must be the same number as X data.) : ")
    e=[]
    print(f"{bcolors.OK}E Data : ")
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
    print(f"{bcolors.FAIL}Thanks you for using ATS...")
    print(f"{bcolors.FAIL}Quitting...")
