# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:21:44 2020

@author: takic
"""

# first string
firstString = "ABcdefgh"    # orjinal
secondString = "hgfedcbs"   # tranlate
thirdString = "Bxwq"            # remove orjinal char

orj_metin = "abcdef"
print("Original string:", orj_metin)

translation = orj_metin.maketrans(firstString, secondString, thirdString)
print(type(translation))
print(translation)
# translate string
print("Translated string:", orj_metin.translate(translation))