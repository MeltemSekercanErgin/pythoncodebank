# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""


import pandas as pd
  
    
    
df = pd.read_csv("TarihselVeriler.csv")

df.rename(columns={'TARİH' : 'Tarih', 'FON KODU' : 'Fon Kodu', 'FON ADI' : 'Fon Adı', 'FİYAT' : 'Fiyat'}, inplace = True)
print(df.columns)

df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y-%m-%d")
df.dropna(inplace=True)

df["nxFiyat"] = 0



    
    
""" BEGIN - Tahmin için eklendi"""
df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
    

tmpdf = pd.DataFrame()

for fon in df["Fon Kodu"].unique():
    
    fdf = df[df["Fon Kodu"] == fon ] 
    
    fdf["ho_short"] = fdf["Fiyat"].rolling(window =30).mean()
    fdf["ho_middle"] = fdf["Fiyat"].rolling(window =50).mean()
    fdf["ho_long"] = fdf["Fiyat"].rolling(window =200).mean()
    
    tmpdf = pd.concat([tmpdf, fdf], ignore_index = True)
    
    print(fon)

df = tmpdf.copy()
df["nxFiyat"] = 0 
for index, row in df.iterrows():
    
    if row["nxFiyat"]==0:
    
        Tarih = df[df["Tarih"] > row["Tarih"] ]["Tarih"].min()
        
        Fiyat = df[(df["Tarih"] == Tarih) & (df["Fon Kodu"]==row["Fon Kodu"]) ]["Fiyat"].mean()
        
        df.loc[index, "nxFiyat"] = Fiyat
        
        print(row["Fiyat"], "  ", Fiyat)
    
""" END - Tahmin için eklendi"""

df.to_csv("TarihselVeriler_main.csv", index=False)