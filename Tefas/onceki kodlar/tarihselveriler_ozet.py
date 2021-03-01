# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

df = pd.read_csv("TarihselVeriler_gd.csv")

df.dropna(inplace=True)

ozetdf = pd.DataFrame()

for i in df["FON KODU"].unique():
    tmpdf = df[df["FON KODU"] == i ]
    
    df2 = tmpdf[["FİYAT","g_degisim"]].describe()
    df2["FON ADI"] = i
    
    ozetdf = pd.concat([ozetdf, df2])
  
print(ozetdf)

ozetdf.to_csv("TarihselVeriler_describe.csv")