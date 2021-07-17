# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:51:31 2021

@author: Meltem ERGİN :)
"""
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from datetime import date
from statsmodels.tsa.seasonal import STL
from PyQt5 import QtWidgets

def hatayakala(function):
    def wrap_function(*args):
        try:
            
            return function(*args)
           
        except BaseException as e:
            
            mesaj = QtWidgets.QMessageBox()
            mesaj.setWindowTitle("Hata Oluştu")
            mesaj.setText(str(e))
            mesaj.setIcon(QtWidgets.QMessageBox.Warning)
            mesaj.exec()
            
    return wrap_function


#@hatayakala
def veribirlestir():

    df = pd.read_csv("TarihselVeriler_main.csv")
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    """df.dropna(inplace=True)"""
    
    SonTarih = df["Tarih"].max()
    
    
    dfy = pd.read_csv("TarihselVeriler.csv")
    dfy["Tarih"] = pd.to_datetime(dfy["Tarih"], format="%d.%m.%Y")
    dfy.dropna(inplace=True)
    
    dfy["nxFiyat"] = 0
    
    dfy = dfy[dfy["Tarih"]>SonTarih]
    
    
    if len(dfy)>0:
        dfy["sil"] = dfy['Fon Adı'].apply(lambda x : ("ÖZEL FON" in x) or ("SERBEST" in x))
        dfy.drop(dfy[dfy['sil']].index, inplace = True) 
        dfy.drop('sil', axis=1, inplace=True)
        
        df = pd.concat([df, dfy], ignore_index = True)
        
        
    """ BEGIN - Tahmin için eklendi"""
    df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
    df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
        
    dfy["Fiyat"]= dfy["Fiyat"].apply(lambda x: str(x).replace(",","."))
    dfy["Fiyat"] = pd.to_numeric(dfy["Fiyat"], downcast="float")
    
    
    tmpdf = pd.DataFrame()
    
    for fon in df["Fon Kodu"].unique():
        
        fdf = df[df["Fon Kodu"] == fon ] 
        
        fdf["ho_short"] = fdf["Fiyat"].rolling(window =30).mean()
        fdf["ho_middle"] = fdf["Fiyat"].rolling(window =50).mean()
        fdf["ho_long"] = fdf["Fiyat"].rolling(window =200).mean()
        
        tmpdf = pd.concat([tmpdf, fdf], ignore_index = True)
        
    
    df = tmpdf.copy()
    #df["nxFiyat"] = 0 #ilk çalıştırmada kullanıldı
    for index, row in df.iterrows():
        
        if row["nxFiyat"]==0:
        
            Tarih = df[df["Tarih"] > row["Tarih"] ]["Tarih"].min()
            
            Fiyat = df[(df["Tarih"] == Tarih) & (df["Fon Kodu"]==row["Fon Kodu"]) ]["Fiyat"].mean()
            
            df.loc[index, "nxFiyat"] = Fiyat
            
            print(row["Fiyat"], "  ", Fiyat)
        
    """ END - Tahmin için eklendi"""

    df.to_csv("TarihselVeriler_main.csv", index=False)
    
@hatayakala   
def veriYukle():


    df = pd.read_csv("TarihselVeriler_main.csv")
    
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    """df.dropna(inplace=True)"""
    
    
    return df
  
@hatayakala            
def fonAnaliz(fon_kod, df, Baslangic, Bitis, HO1 = 30, HO2 = 50, HO3 = 200):

    
    tmpdf = df[df["Fon Kodu"] == fon_kod ]  
    tmpdf["Tarih"] = pd.to_datetime(tmpdf["Tarih"], format="%d.%m.%Y")
    tmpdf.sort_values("Tarih", inplace=True)
    
    
    tmpdf["Fiyat"]= tmpdf["Fiyat"].apply(lambda x: str(x).replace(",","."))
    tmpdf["Fiyat"] = pd.to_numeric(tmpdf["Fiyat"], downcast="float")
    
    
    #veri birleştirilirken sabit oluşturuldu. Bu onları ekrandan alınana göre tekrar hesaplıyor
    if HO1!=30 :
        tmpdf["ho_short"] = tmpdf["Fiyat"].rolling(window =HO1).mean()
    if HO2!=50 :
        tmpdf["ho_middle"] = tmpdf["Fiyat"].rolling(window =HO2).mean()
    if HO3!=200 :
        tmpdf["ho_long"] = tmpdf["Fiyat"].rolling(window =HO3).mean()
    
    
    tmpdf["SELLs"] =  tmpdf["Fiyat"]<tmpdf["ho_short"] 
    tmpdf["BUYs"] = tmpdf["Fiyat"]>tmpdf["ho_long"] 
    
    tmpdf["BUY"] =  (tmpdf["BUYs"] == True)  & (tmpdf["BUYs"].rolling(window =2).min() == False)
    tmpdf["SELL"] =  (tmpdf["SELLs"] == True)  & (tmpdf["SELLs"].rolling(window =2).min() == False)
    
    
    tmpdf["BUY"] = tmpdf["BUY"].astype(int)
    tmpdf["SELL"] = tmpdf["SELL"].astype(int)
    
    tmpdf["UP"] = ( (tmpdf["ho_short"] > tmpdf["ho_middle"] ) & (tmpdf["ho_short"] > tmpdf["ho_long"] ) )
    tmpdf["DOWN"] = ( (tmpdf["ho_short"] < tmpdf["ho_middle"] )  & (tmpdf["ho_short"] < tmpdf["ho_long"] )  )
    
    
   

    condition1 = tmpdf['Tarih'] >= Baslangic 
    condition2 = tmpdf['Tarih'] <= Bitis 
    tmpdf = tmpdf.loc[condition1]
    tmpdf = tmpdf.loc[condition2]
    
    return tmpdf
    
 
@hatayakala            
def fonGrafik(fon_kod, df):
   
    tmpdf = df.copy()
    
    tmpdf["BUY"]=  tmpdf["Fiyat"] * tmpdf["BUY"]
    tmpdf["SELL"]=  tmpdf["Fiyat"] * tmpdf["SELL"]
    tmpdf["BUY"].replace(0, np.nan, inplace=True)
    tmpdf["SELL"].replace(0, np.nan, inplace=True)
    
    tmpdf = pd.melt(tmpdf, id_vars=['Tarih', 'BUY','SELL'], value_vars=['Fiyat', 'ho_short', 'ho_middle', 'ho_long'])
    
    fig, ax = plt.subplots()
    
    sns.lineplot(ax = ax, x ="Tarih", y = "BUY",  data=tmpdf, marker="^", color="green")  
    sns.lineplot(ax = ax, x ="Tarih", y = "SELL",  data=tmpdf, marker="v", color="red")  
    
    sns.lineplot(ax = ax,  x ="Tarih", y = "value", hue="variable", data=tmpdf, linewidth=.80)   # 'AES')
    plt.xticks(rotation='vertical')
    
    #today = date.today()
    #plt.savefig('./plots/'+ fon_kod + today.strftime("%Y%m%d") + '.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
    
    return fig
  
@hatayakala
def fonTrend(fon_kod, df):

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
    
@hatayakala
def fonHaftalik(fon_kod, df):
    tmpdf = df.copy()
    
    
    tmpdf["Tarih"] = pd.to_datetime(tmpdf["Tarih"], format="%Y.%m.%d")
    
    
    tmpdf["Fiyat"]= tmpdf["Fiyat"].apply(lambda x: str(x).replace(",","."))
    tmpdf["Fiyat"] = pd.to_numeric(tmpdf["Fiyat"], downcast="float")
        
    tmpdf = tmpdf.resample("W", on="Tarih",closed="left", label="left"        
                      ).apply({ "Fiyat": lambda g: (g.iloc[-1] - g.iloc[0])/g.iloc[0]*100})
    
        
    fig, ax = plt.subplots()
    
    graph = sns.lineplot(ax = ax,  x ="Tarih", y = "Fiyat", data=tmpdf, linewidth=.80)   # 'AES')
    
    graph.axhline(0)
    
    return fig
  
