# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:20:51 2021

@author: SS
"""
#TARİH SOruNu VAR
#TARİH SOruNu VAR
#TARİH SOruNu VAR
#TARİH SOruNu VAR
#TARİH SOruNu VAR

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("TarihselVeriler_main.csv")
df["Tarih"] = pd.to_datetime(df["Tarih"], format="%d.%m.%Y")
df.dropna(inplace=True)

SonTarih = df["Tarih"].max()

dfy = pd.read_csv("TarihselVeriler.csv")
dfy["Tarih"] = pd.to_datetime(dfy["Tarih"], format="%d.%m.%Y")
dfy.dropna(inplace=True)

dfy = dfy[dfy["Tarih"]>SonTarih]

if len(dfy)>0:
    dfy["sil"] = dfy['Fon Adı'].apply(lambda x : ("ÖZEL FON" in x) or ("SERBEST" in x))
    dfy.drop(dfy[dfy['sil']].index, inplace = True) 
    dfy.drop('sil', axis=1, inplace=True)
    
    df = pd.concat([df, dfy], ignore_index = True)
    
    df.to_csv("TarihselVeriler_main.csv", index=False)
    
    print(len(dfy), " adet kayıt eklendi.")
else:
    print("Veri tabanı güncel")