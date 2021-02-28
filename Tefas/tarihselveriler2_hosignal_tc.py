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
# df = df['TARİH'] >= pd.to_datetime('2020-12-20', format="%Y-%m-%d")
condition3 = df['TARİH'] >= '2020-01-20'
df = df.loc[condition3]






for i in df["FON KODU"].unique():
    
    tmpdf = df[df["FON KODU"] == 'AES'] # i ]
    #tmpdf["ho5"] = tmpdf["FİYAT"].ewm(span =10).mean()
    tmpdf['TARİH'] = pd.to_datetime(tmpdf['TARİH'], format="%Y-%m-%d")
    tmpdf.sort_values("TARİH", inplace=True)
    
    
    """tmpdf["ho14"] = tmpdf["FİYAT"].ewm(span =30).mean()
    tmpdf["ho21"] = tmpdf["FİYAT"].ewm(span =50).mean()
    tmpdf["ho30"] = tmpdf["FİYAT"].ewm(span =200).mean()"""
    tmpdf["ho14"] = tmpdf["FİYAT"].rolling(window =30).mean()
    tmpdf["ho21"] = tmpdf["FİYAT"].rolling(window =50).mean()
    tmpdf["ho30"] = tmpdf["FİYAT"].rolling(window =200).mean()
    
    
    tmpdf = pd.melt(tmpdf, id_vars=['TARİH'], value_vars=['FİYAT', 'ho14', 'ho21', 'ho30'])
    #tmpdf = pd.melt(tmpdf, id_vars=['TARİH'], value_vars=[ 'ho5', 'ho14', 'ho21', 'ho30'])
    
    sns.lineplot(x ="TARİH", y = "value", hue="variable", data=tmpdf, linewidth=.80).set_title('AES') #i)
    plt.show()
    break
    
   