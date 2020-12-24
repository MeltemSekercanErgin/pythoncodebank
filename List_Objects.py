# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 20:24:13 2020

"""


### LIST Objects :

# Extend:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# List Kopyama bu şekilde yapılmaz...
list1=[1,3]
list2=list1  #Bu tarz bir atamada list1 değiştirilirse list2 de etkilenir.
list1[0]=4
print(list2)