# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:13:32 2021

@author: SS
"""
from statsmodels.tsa.seasonal import STL
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("TarihselVeriler_main.csv")

df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
df.sort_values("Tarih", inplace=True)

df = df[df["Fon Kodu"] == "AAL" ]  
df = df[["Tarih", "Fiyat"]]

df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
    
df.set_index('Tarih', inplace=True)

print(df)
res = STL(df, period=30, ).fit()
res.plot()
plt.show()
