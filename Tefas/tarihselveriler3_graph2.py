# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_csv("TarihselVeriler_gd.csv")

df.dropna(inplace=True)


for i in df["FON KODU"].unique():
    tmpdf = df[df["FON KODU"] == i ]
    tmpdf = pd.melt(tmpdf, id_vars=['TARİH'], value_vars=['FİYAT', 'g_degisim'])
    
    sns.lineplot(x ="TARİH", y = "value", hue="variable", data=tmpdf)
   
    plt.show()
   
    