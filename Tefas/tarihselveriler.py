# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

df = pd.read_csv("TarihselVeriler_gd.csv")
tmpdf = df[df["fark"].isnull()]

for index, row in tmpdf.iterrows():
    row["fark"] = df[(df["TARİH"] == row["TARİH"] -  pd.to_timedelta(3, unit='d')) & (df["FON KODU"]==row["FON KODU"]) ]["FİYAT"]
    deger = row["FİYAT"] - row["fark"].mean()
    df.loc[index, "fark"] = deger
    df.loc[index, "g_degisim"] = deger / row["fark"] 
    print(index,"     ", deger)
    



df.to_csv("TarihselVeriler_gd.csv", index=False)