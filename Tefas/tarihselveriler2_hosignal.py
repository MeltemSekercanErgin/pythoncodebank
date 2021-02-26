# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:51:31 2021

@author: SS
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
"""
df = pd.read_excel("TarihselVeriler5.xlsx")
df2 = pd.read_excel("TarihselVeriler6.xlsx")

df = pd.concat([df,df2])"""


df = pd.read_csv("TarihselVeriler.csv")

df['TARİH'] = pd.to_datetime(df['TARİH'], format="%Y-%m-%d")




df.dropna(inplace=True)


for i in df["FON KODU"].unique():
    
    tmpdf = df[df["FON KODU"] == i ]
    #tmpdf["ho5"] = tmpdf["FİYAT"].ewm(span =10).mean()
    tmpdf["ho14"] = tmpdf["FİYAT"].ewm(span =30).mean()
    tmpdf["ho21"] = tmpdf["FİYAT"].ewm(span =50).mean()
    tmpdf["ho30"] = tmpdf["FİYAT"].ewm(span =200).mean()
    
    
    tmpdf = pd.melt(tmpdf, id_vars=['TARİH'], value_vars=['FİYAT', 'ho14', 'ho21', 'ho30'])
    #tmpdf = pd.melt(tmpdf, id_vars=['TARİH'], value_vars=[ 'ho5', 'ho14', 'ho21', 'ho30'])
    
    sns.lineplot(x ="TARİH", y = "value", hue="variable", data=tmpdf).set_title(i)
       
    plt.show()
    
   