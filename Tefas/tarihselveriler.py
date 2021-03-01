# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:51:31 2021

@author: SS
"""
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from datetime import date


ChBaslangic = '01.01.2020' # AY GÜN YIL ALIYOR

df = pd.read_csv("TarihselVeriler_main.csv")
df["Tarih"] = pd.to_datetime(df["Tarih"], format="%d.%m.%Y")
df.dropna(inplace=True)



for i in df["Fon Kodu"].unique():
    
    tmpdf = df[df["Fon Kodu"] == i ]  
    tmpdf["Tarih"] = pd.to_datetime(tmpdf["Tarih"], format="%d.%m.%Y")
    tmpdf.sort_values("Tarih", inplace=True)

    tmpdf["ho30"] = tmpdf["Fiyat"].rolling(window =30).mean()
    tmpdf["ho50"] = tmpdf["Fiyat"].rolling(window =50).mean()
    tmpdf["ho200"] = tmpdf["Fiyat"].rolling(window =200).mean()
    
    tmpdf["SELLs"] =  tmpdf["Fiyat"]<tmpdf["ho30"] 
    tmpdf["BUYs"] = tmpdf["Fiyat"]>tmpdf["ho200"] 
    
    tmpdf["BUY"] =  (tmpdf["BUYs"] == True)  & (tmpdf["BUYs"].rolling(window =2).min() == False)
    tmpdf["SELL"] =  (tmpdf["SELLs"] == True)  & (tmpdf["SELLs"].rolling(window =2).min() == False)
    
    
    tmpdf["BUY"] = tmpdf["BUY"].astype(int)
    tmpdf["SELL"] = tmpdf["SELL"].astype(int)
    
    tmpdf["BUY"]=  tmpdf["Fiyat"] * tmpdf["BUY"]
    tmpdf["SELL"]=  tmpdf["Fiyat"] * tmpdf["SELL"]
    tmpdf["BUY"].replace(0, np.nan, inplace=True)
    tmpdf["SELL"].replace(0, np.nan, inplace=True)
   
    
    
    condition = tmpdf['Tarih'] >= ChBaslangic
    tmpdf = tmpdf.loc[condition]

    #tmpdf = pd.melt(tmpdf, id_vars=['Tarih'], value_vars=['Fiyat', 'ho30', 'ho50', 'ho200', 'BUY','SELL'])
    tmpdf = pd.melt(tmpdf, id_vars=['Tarih', 'BUY','SELL'], value_vars=['Fiyat', 'ho30', 'ho50', 'ho200'])
    
    sns.lineplot(x ="Tarih", y = "BUY",  data=tmpdf, marker="^", color="green")  
    sns.lineplot(x ="Tarih", y = "SELL",  data=tmpdf, marker="v", color="red")  
    
    sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf, linewidth=.80).set_title(i)   # 'AES')
    plt.xticks(rotation='vertical')
    
    today = date.today()
    plt.savefig('./plots/'+i+ today.strftime("%Y%m%d") + '.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
    
    plt.show()
    
 
   