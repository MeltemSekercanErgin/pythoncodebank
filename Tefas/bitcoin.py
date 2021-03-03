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




df = pd.read_csv("Bitcoin.csv")


df["Tarih"] = pd.to_datetime(df["Tarih"], format="%d.%m.%Y")
df["Şimdi"] = df["Şimdi"].apply(lambda x: x.replace(".",""))
df["Şimdi"] = df["Şimdi"].apply(lambda x: x.replace(",","."))


df["Şimdi"] = df["Şimdi"].astype(float)

df.dropna(inplace=True)

tmpdf = df.copy()
tmpdf.sort_values("Tarih", inplace=True)

tmpdf["ho10"] = tmpdf["Şimdi"].rolling(window =10).mean()
tmpdf["ho20"] = tmpdf["Şimdi"].rolling(window =20).mean()
tmpdf["ho30"] = tmpdf["Şimdi"].rolling(window =30).mean()

tmpdf["SELLs"] =  tmpdf["Şimdi"]<tmpdf["ho10"] 
tmpdf["BUYs"] = tmpdf["Şimdi"]>tmpdf["ho30"] 

tmpdf["BUY"] =  (tmpdf["BUYs"] == True)  & (tmpdf["BUYs"].rolling(window =2).min() == False)
tmpdf["SELL"] =  (tmpdf["SELLs"] == True)  & (tmpdf["SELLs"].rolling(window =2).min() == False)


tmpdf["BUY"] = tmpdf["BUY"].astype(int)
tmpdf["SELL"] = tmpdf["SELL"].astype(int)

tmpdf["BUY"]=  tmpdf["Şimdi"] * tmpdf["BUY"]
tmpdf["SELL"]=  tmpdf["Şimdi"] * tmpdf["SELL"]
tmpdf["BUY"].replace(0, np.nan, inplace=True)
tmpdf["SELL"].replace(0, np.nan, inplace=True)
   

#tmpdf = pd.melt(tmpdf, id_vars=['Tarih'], value_vars=['Fiyat', 'ho30', 'ho50', 'ho200', 'BUY','SELL'])
tmpdf = pd.melt(tmpdf, id_vars=['Tarih', 'BUY','SELL'], value_vars=['Şimdi', 'ho10', 'ho20', 'ho30'])

sns.lineplot(x ="Tarih", y = "BUY",  data=tmpdf, marker="^", color="green")  
sns.lineplot(x ="Tarih", y = "SELL",  data=tmpdf, marker="v", color="red")  

sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf, linewidth=.80).set_title("bitcoin")   # 'AES')
plt.xticks(rotation='vertical')

today = date.today()
plt.savefig('./plots/bitcoin'+ today.strftime("%Y%m%d") + '.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...

plt.show()
