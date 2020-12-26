# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:41:39 2020
@author: takic


"""
import random
import sys

# il isimlerinde türkçe harf kullanmamaya çalıştım. listeye ek yapılabilir.
citynames = ["ANKARA",
             "BURSA",
             "ANTALYA",
             "SAKARYA",
             "AKSARAY",
             "HATAY",
             "URFA",
             "VAN",
             "KONYA",
             "ERZURUM"]


"""
         |----|
         |    |
         O    |
        /|\   |
        / \   |
             ---
"""
# boşluklar yer kaplamasın diye adetlerini tagladım.
adam = ["\n\n\n\n\n\n",  # boş ekran
        "\n\n\n\n\n(13)---", # toprak
        "(14)|\n(14)|\n(14)|\n(14)|\n(14)|\n(13)---", # direk
        "(10)----|\n(14)|\n(14)|\n(14)|\n(14)|\n(14)|\n(13)---",  # direk ve uzantısı
        "(9)|----|\n(9)|(4)|\n(14)|\n(14)|\n(14)|\n(14)|\n(13)---",  # ip
        "(9)|----|\n(9)|(4)|\n(9)O(4)|\n(14)|\n(14)|\n(14)|\n(13)---", # kafa
        
        "(9)|----|\n(9)|(4)|\n(9)O(4)|\n(9)|(4)|\n(14)|\n(14)|\n(13)---", # gövde
        "(9)|----|\n(9)|(4)|\n(9)O(4)|\n(8)/|(4)|\n(14)|\n(14)|\n(13)---",  # sol kol
        "(9)|----|\n(9)|(4)|\n(9)O(4)|\n(8)/|\(3)|\n(14)|\n(14)|\n(13)---", # sağ kol
        
        "(9)|----|\n(9)|(4)|\n(9)O(4)|\n(8)/|\(3)|\n(8)/(5)|\n(14)|\n(13)---", # sol ayak
        "(9)|----|\n(9)|(4)|\n(9)O(4)|\n(8)/|\(3)|\n(8)/ \(3)|\n(14)|\n(13)---"]  # sağ ayak

# taglı boşlukları adetleri kadar boşlukla replace ediyorum
def replace_space(adamstr):
    adamstr = adamstr.replace("(13)", "             ")
    adamstr = adamstr.replace("(14)", "              ")
    adamstr = adamstr.replace("(10)", "          ")
    adamstr = adamstr.replace("(9)", "         ")
    adamstr = adamstr.replace("(8)", "        ")
    adamstr = adamstr.replace("(5)", "     ")
    adamstr = adamstr.replace("(4)", "    ")
    adamstr = adamstr.replace("(3)", "   ")
    return(adamstr)

def adam_ciz(hak_sayisi):
    adamstr = adam[hak_sayisi]
    adamstr = replace_space(adamstr)
    print("\n--------------------------")
    print(adamstr)
    if hak_sayisi == 0:
        print("You have 10 Health Point")
    elif hak_sayisi == 10:
        print("---------------------------")
        print("Game Over. You died!")
        print("---------------------------\n")
        sys.exit()
    else:
        print(str(10-hak_sayisi), "Health Point Left")
    print("---------------------------\n")
    
def changehiddencitystr(guess):
    global hiddencitystr
    liste = list(hiddencitystr)
    for id, char in enumerate(citystr):
        if char == guess:
            liste[id]=guess
    hiddencitystr = "".join(liste)
    
    
        

user = input("Enter the Player Name : ").upper()
print("\n\n\n")
print("W E L C O M E    ", end=(""))
for char in user:
    print(char + " ", end=(""))

cizgi = 0
citystr = citynames[random.randint(0, len(citynames)-1)]
hiddencitystr = "_"*len(citystr)


while "_" in hiddencitystr:
    adam_ciz(cizgi)
    # print(citystr)   # Test için açık bırak ;)
    print(hiddencitystr)
    guess = input("Enter one letter : ").upper()
    if guess in citystr:
        changehiddencitystr(guess)
    else:
        cizgi += 1

adam_ciz(cizgi)
print("You Win. You are Claver")
