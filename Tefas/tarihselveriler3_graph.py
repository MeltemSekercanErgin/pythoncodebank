# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

df = pd.read_csv("TarihselVeriler_gd.csv")



for i in df["FON KODU"].unique():
   
    df[df["FON KODU"] == i ].plot(x="TARİH", y= "g_degisim", sort_columns="TARİH", title=i)
    df[df["FON KODU"] == i ].plot(x="TARİH", y= "FİYAT", sort_columns="TARİH", title=i)

