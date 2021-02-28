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


df = pd.read_csv("TarihselVerilerTC.csv")
df['Tarih'] = pd.to_datetime(df['Tarih'], format="%d.%m.%Y")
df.dropna(inplace=True)

condition3 = df['Tarih'] >= '01.01.2020'
df = df.loc[condition3]




# 'HYF' YENİ PARAPİYASASI FONU İLK AYI TAKİP EDİLECEK


for i in df["Fon Kodu"].unique():
    
    tmpdf = df[df["Fon Kodu"] == i ]  #'GUH'] # i ] #
    #tmpdf["ho5"] = tmpdf["FİYAT"].ewm(span =10).mean()
    tmpdf['Tarih'] = pd.to_datetime(tmpdf['Tarih'], format="%d.%m.%Y")
    tmpdf.sort_values("Tarih", inplace=True)
    
    
    """
        tmpdf["ho14"] = tmpdf["Fiyat"].ewm(span =30).mean()
        tmpdf["ho21"] = tmpdf["Fiyat"].ewm(span =50).mean()
        tmpdf["ho30"] = tmpdf["Fiyat"].ewm(span =200).mean()
    """

    tmpdf["ho30"] = tmpdf["Fiyat"].rolling(window =30).mean()
    tmpdf["ho50"] = tmpdf["Fiyat"].rolling(window =50).mean()
    tmpdf["ho200"] = tmpdf["Fiyat"].rolling(window =200).mean()
    
    tmpdf = pd.melt(tmpdf, id_vars=['Tarih'], value_vars=['Fiyat', 'ho30', 'ho50', 'ho200'])


    
    sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf, linewidth=.80).set_title(i)   # 'AES')
    plt.savefig('./plots/'+i+'_2020_Ocak.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
    plt.show()
    
    condition4 = tmpdf['Tarih'] >= '12.01.2020'
    tmpdf2 = tmpdf.loc[condition4]

    sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf2, linewidth=.80).set_title(i)   # 'AES')
    plt.savefig('./plots/'+i+'_2020_Aralik.png')
    plt.show()

    
   