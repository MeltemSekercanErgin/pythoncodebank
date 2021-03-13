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
from statsmodels.tsa.seasonal import STL

def veribirlestir():
    try:
        df = pd.read_csv("TarihselVeriler_main.csv")
        df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
        df.dropna(inplace=True)
        
        SonTarih = df["Tarih"].max()
        
        
        dfy = pd.read_csv("TarihselVeriler.csv")
        dfy["Tarih"] = pd.to_datetime(dfy["Tarih"], format="%d.%m.%Y")
        dfy.dropna(inplace=True)
        
        dfy = dfy[dfy["Tarih"]>SonTarih]
        
        
        if len(dfy)>0:
            dfy["sil"] = dfy['Fon Adı'].apply(lambda x : ("ÖZEL FON" in x) or ("SERBEST" in x))
            dfy.drop(dfy[dfy['sil']].index, inplace = True) 
            dfy.drop('sil', axis=1, inplace=True)
            
            df = pd.concat([df, dfy], ignore_index = True)
            
            df.to_csv("TarihselVeriler_main.csv", index=False)
    
    except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
        
    
    
def veriYukle():
    try:
    
        df = pd.read_csv("TarihselVeriler_main.csv")
        df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
        df.dropna(inplace=True)
        return df
    
    except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
            
def fonAnaliz(fon_kod, df, Baslangic, Bitis, HO1 = 30, HO2 = 50, HO3 = 200):
    
    try:
        
        tmpdf = df[df["Fon Kodu"] == fon_kod ]  
        tmpdf["Tarih"] = pd.to_datetime(tmpdf["Tarih"], format="%d.%m.%Y")
        tmpdf.sort_values("Tarih", inplace=True)
        
        
        tmpdf["Fiyat"]= tmpdf["Fiyat"].apply(lambda x: str(x).replace(",","."))
        tmpdf["Fiyat"] = pd.to_numeric(tmpdf["Fiyat"], downcast="float")
        
        
        tmpdf["ho30"] = tmpdf["Fiyat"].rolling(window =HO1).mean()
        tmpdf["ho50"] = tmpdf["Fiyat"].rolling(window =HO2).mean()
        tmpdf["ho200"] = tmpdf["Fiyat"].rolling(window =HO3).mean()
        
        tmpdf["SELLs"] =  tmpdf["Fiyat"]<tmpdf["ho30"] 
        tmpdf["BUYs"] = tmpdf["Fiyat"]>tmpdf["ho200"] 
        
        tmpdf["BUY"] =  (tmpdf["BUYs"] == True)  & (tmpdf["BUYs"].rolling(window =2).min() == False)
        tmpdf["SELL"] =  (tmpdf["SELLs"] == True)  & (tmpdf["SELLs"].rolling(window =2).min() == False)
        
        
        tmpdf["BUY"] = tmpdf["BUY"].astype(int)
        tmpdf["SELL"] = tmpdf["SELL"].astype(int)
        
    
       
    
        condition1 = tmpdf['Tarih'] >= Baslangic 
        condition2 = tmpdf['Tarih'] <= Bitis 
        tmpdf = tmpdf.loc[condition1]
        tmpdf = tmpdf.loc[condition2]
        
        return tmpdf
    
    except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
            
def fonGrafik(fon_kod, df):
    try:
        tmpdf = df.copy()
        
        tmpdf["BUY"]=  tmpdf["Fiyat"] * tmpdf["BUY"]
        tmpdf["SELL"]=  tmpdf["Fiyat"] * tmpdf["SELL"]
        tmpdf["BUY"].replace(0, np.nan, inplace=True)
        tmpdf["SELL"].replace(0, np.nan, inplace=True)
        
        tmpdf = pd.melt(tmpdf, id_vars=['Tarih', 'BUY','SELL'], value_vars=['Fiyat', 'ho30', 'ho50', 'ho200'])
        
        fig, ax = plt.subplots()
        
        sns.lineplot(ax = ax, x ="Tarih", y = "BUY",  data=tmpdf, marker="^", color="green")  
        sns.lineplot(ax = ax, x ="Tarih", y = "SELL",  data=tmpdf, marker="v", color="red")  
        
        sns.lineplot(ax = ax,  x ="Tarih", y = "value", hue="variable", data=tmpdf, linewidth=.80)   # 'AES')
        plt.xticks(rotation='vertical')
        
        #today = date.today()
        #plt.savefig('./plots/'+ fon_kod + today.strftime("%Y%m%d") + '.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
        
        return fig
    
    except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)

def fonTrend(fon_kod, df):
    
    try:
    
        tmpdf = df.copy()
        
        tmpdf["Tarih"] = pd.to_datetime(tmpdf["Tarih"], format="%Y.%m.%d")
        tmpdf.sort_values("Tarih", inplace=True)
        
        tmpdf = tmpdf[["Tarih", "Fiyat"]]
        
        tmpdf["Fiyat"]= tmpdf["Fiyat"].apply(lambda x: str(x).replace(",","."))
        tmpdf["Fiyat"] = pd.to_numeric(tmpdf["Fiyat"], downcast="float")
            
        tmpdf.set_index('Tarih', inplace=True)
        
        
        res = STL(tmpdf, period=30, ).fit()
        plt.xticks(rotation='vertical')
        
        fig1 = res.plot()
        
        
        
        return fig1
    
    except BaseException as e:
            
            print("Bir Hata Oluştu : ", e)
   