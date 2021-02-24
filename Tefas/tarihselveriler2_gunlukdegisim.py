# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

df = pd.read_csv("TarihselVeriler.csv")



df['TARİH'] = pd.to_datetime(df['TARİH'], format="%Y-%m-%d")


df["fark"] = 0

for index, row in df.iterrows():
    Tarih = df[df["TARİH"] < row["TARİH"] ]["TARİH"].max()
    Fiyat = df[(df["TARİH"] == Tarih) & (df["FON KODU"]==row["FON KODU"]) ]["FİYAT"].mean()
    deger = row["FİYAT"] - Fiyat
    
    df.loc[index, "fark"] = deger 
    print(deger)
    
"""
for index, row in df.iterrows():
    row["fark"] = df[(df["TARİH"] == row["TARİH"] -  pd.to_timedelta(1, unit='d')) & (df["FON KODU"]==row["FON KODU"]) ]["FİYAT"]
    
    if row["fark"].mean() == 0 :
        row["fark"] = df[(df["TARİH"] == row["TARİH"] -  pd.to_timedelta(3, unit='d')) & (df["FON KODU"]==row["FON KODU"]) ]["FİYAT"]
        print("değer yok")
    
    
    if row["fark"].mean() == 0 :
        df.loc[index, "fark"] = 0
        print("hiç değer yok")
    else:
        deger = row["FİYAT"] - row["fark"].mean()
        print(index,"     ", deger)
        df.loc[index, "fark"] = deger        
"""
       
df["g_degisim"] = df["fark"]/df["FİYAT"]



df.to_csv("TarihselVeriler_gd.csv", index=False)
