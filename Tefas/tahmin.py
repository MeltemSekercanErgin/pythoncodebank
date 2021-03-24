# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:35:44 2021

@author: SS
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

import pickle 
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt

from tarihselveriler import hatayakala

#veribirleştirme kısmında yapıldığından kullanılmayacak
@hatayakala
def verihazirla_ilk():
    
    df = pd.read_csv("TarihselVeriler_main.csv")
    
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    df.dropna(inplace=True)
    
    df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
    df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
        
    df["nxFiyat"] = 0
    
    
    for index, row in df.iterrows():
        
        Tarih = df[df["Tarih"] > row["Tarih"] ]["Tarih"].min()
        
        Fiyat = df[(df["Tarih"] == Tarih) & (df["Fon Kodu"]==row["Fon Kodu"]) ]["Fiyat"].mean()
        
        df.loc[index, "nxFiyat"] = Fiyat
        
        print(row["Fiyat"], "  ", Fiyat)
        
        
    df.to_csv("Tahmin.csv", index=False)

#veribirleştirme kısmında yapıldığından kullanılmayacak
@hatayakala
def verihazirla_2():
    
    df = pd.read_csv("Tahmin.csv")
    
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    df.dropna(inplace=True)
    
    df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
    df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
      
    df["nxFiyat"]= df["nxFiyat"].apply(lambda x: str(x).replace(",","."))
    df["nxFiyat"] = pd.to_numeric(df["nxFiyat"], downcast="float")
    
    
    tmpdf = pd.DataFrame()
    
    for fon in df["Fon Kodu"].unique():
        
        fdf = df[df["Fon Kodu"] == fon ] 
        
        fdf["ho_short"] = fdf["Fiyat"].rolling(window =30).mean()
        fdf["ho_middle"] = fdf["Fiyat"].rolling(window =50).mean()
        fdf["ho_long"] = fdf["Fiyat"].rolling(window =200).mean()
        
        tmpdf = pd.concat([tmpdf, fdf], ignore_index = True)
        
    """Son fiyatı sıfır olanlar varsa sil"""
    
    tmpdf = tmpdf[tmpdf["Fiyat"]>0]
    tmpdf = tmpdf[tmpdf["nxFiyat"]>0]
    tmpdf = tmpdf[tmpdf["ho_short"]>0]
    tmpdf = tmpdf[tmpdf["ho_middle"]>0]
    tmpdf = tmpdf[tmpdf["ho_long"]>0]
    
    tmpdf.to_csv("Tahmin_h.csv", index=False)

@hatayakala
def verihazirla(df):
    
    """Son fiyatı sıfır olanlar varsa sil"""
    
    df = df[df["Fiyat"]>0]
    df = df[df["nxFiyat"]>0]
    df = df[df["ho_short"]>0]
    df = df[df["ho_middle"]>0]
    df = df[df["ho_long"]>0]
    
    return df

@hatayakala
def lr_model_egit():
    
    df = pd.read_csv("Tahmin_h.csv")
    
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    df.dropna(inplace=True)
    
    df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
    df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
      
    df["nxFiyat"]= df["nxFiyat"].apply(lambda x: str(x).replace(",","."))
    df["nxFiyat"] = pd.to_numeric(df["nxFiyat"], downcast="float")
    
    df["ho_short"]= df["ho_short"].apply(lambda x: str(x).replace(",","."))
    df["ho_short"] = pd.to_numeric(df["ho_short"], downcast="float")
    
    df["ho_middle"]= df["ho_middle"].apply(lambda x: str(x).replace(",","."))
    df["ho_middle"] = pd.to_numeric(df["ho_middle"], downcast="float")
    
    df["ho_long"]= df["ho_long"].apply(lambda x: str(x).replace(",","."))
    df["ho_long"] = pd.to_numeric(df["ho_long"], downcast="float")
    
    
    for fon in df["Fon Kodu"].unique():
        
        fdf = df[df["Fon Kodu"] == fon ] 
        
       
        
        x = fdf[["Fiyat", "ho_short", "ho_middle", "ho_long"]]
        y = fdf["nxFiyat"]
        
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30, random_state=42)
        
        lm = LinearRegression()
        model = lm.fit(x_train, y_train)
     
        pickle.dump(model, open("models\LinearRegression_" + fon + ".model","wb"))
        
        fondf = pd.DataFrame()
        
        fondf["x_test"] = x_test["Fiyat"]
        fondf["y_test"] = y_test
        fondf["y_pred"] = model.predict(x_test)
        fondf["GerçekFark"] = fondf["y_test"] -  fondf["x_test"]
        fondf["TahminFark"] = fondf["y_pred"] -  fondf["x_test"]
        fondf["Gerçek"] = fondf["GerçekFark"].apply(lambda x: x>0)
        fondf["Tahmin"] = fondf["TahminFark"].apply(lambda x: x>0)
        fondf["Ongoru"] = fondf["Gerçek"] * fondf["Tahmin"]
        fondf["Skor"] = model.score(x_test, y_test)
        
        mse = np.sqrt(mean_squared_error(y_test,fondf["y_pred"] ))
        fondf["mean_squared_error"] = mse
        
        
        print("mse", mse)
        print("Eğitim Skoru : " , model.score(x_train, y_train))
        print("Tahmin Skoru : " , model.score(x_test, y_test))
        fondf.to_csv("tahminler\LinearRegression_" + fon + ".csv", index=False)
        
        
        """Grafik"""
        
        fondf["Tarih"] = fdf["Tarih"]
        fondf = pd.melt(fondf, id_vars=['Tarih'], value_vars=['y_test', 'y_pred'])
    
        sns.lineplot(x ="Tarih", y = "value", hue="variable", data=fondf)
        plt.title(fon)
        
        plt.savefig('./plots/ln_'+fon+  '.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
    
       
        plt.show()
       
@hatayakala
def ridge_model_egit():
    
    df = pd.read_csv("Tahmin_h.csv")
    
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    df.dropna(inplace=True)
    
    df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
    df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
      
    df["nxFiyat"]= df["nxFiyat"].apply(lambda x: str(x).replace(",","."))
    df["nxFiyat"] = pd.to_numeric(df["nxFiyat"], downcast="float")
    
    df["ho_short"]= df["ho_short"].apply(lambda x: str(x).replace(",","."))
    df["ho_short"] = pd.to_numeric(df["ho_short"], downcast="float")
    
    df["ho_middle"]= df["ho_middle"].apply(lambda x: str(x).replace(",","."))
    df["ho_middle"] = pd.to_numeric(df["ho_middle"], downcast="float")
    
    df["ho_long"]= df["ho_long"].apply(lambda x: str(x).replace(",","."))
    df["ho_long"] = pd.to_numeric(df["ho_long"], downcast="float")
    
    
    for fon in df["Fon Kodu"].unique():
        
        fdf = df[df["Fon Kodu"] == fon ] 
        
       
        
        x = fdf[["Fiyat", "ho_short", "ho_middle", "ho_long"]]
        y = fdf["nxFiyat"]
        
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30, random_state=42)
        
        
        model = Ridge(alpha = 0.1).fit(x_train, y_train)
     
        pickle.dump(model, open("models\_ridge_" + fon + ".model","wb"))
        
        fondf = pd.DataFrame()
        fondf["x_test"] = x_test["Fiyat"]
        fondf["y_test"] = y_test
        fondf["y_pred"] = model.predict(x_test)
        fondf["GerçekFark"] = fondf["y_test"] -  fondf["x_test"]
        fondf["TahminFark"] = fondf["y_pred"] -  fondf["x_test"]
        fondf["Gerçek"] = fondf["GerçekFark"].apply(lambda x: x>0)
        fondf["Tahmin"] = fondf["TahminFark"].apply(lambda x: x>0)
        fondf["Ongoru"] = fondf["Gerçek"] * fondf["Tahmin"]
        fondf["Skor"] = model.score(x_test, y_test)
        
        mse = np.sqrt(mean_squared_error(y_test,fondf["y_pred"] ))
        fondf["mean_squared_error"] = mse
        
        
        print("mse", mse)
        print("Eğitim Skoru : " , model.score(x_train, y_train))
        print("Tahmin Skoru : " , model.score(x_test, y_test))
        fondf.to_csv("tahminler\_ridge_" + fon + ".csv", index=False)
        

@hatayakala
def ann_model_egit():
    
    df = pd.read_csv("Tahmin_h.csv")
    
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y.%m.%d")
    df.dropna(inplace=True)
    
    df["Fiyat"]= df["Fiyat"].apply(lambda x: str(x).replace(",","."))
    df["Fiyat"] = pd.to_numeric(df["Fiyat"], downcast="float")
      
    df["nxFiyat"]= df["nxFiyat"].apply(lambda x: str(x).replace(",","."))
    df["nxFiyat"] = pd.to_numeric(df["nxFiyat"], downcast="float")
    
    df["ho_short"]= df["ho_short"].apply(lambda x: str(x).replace(",","."))
    df["ho_short"] = pd.to_numeric(df["ho_short"], downcast="float")
    
    df["ho_middle"]= df["ho_middle"].apply(lambda x: str(x).replace(",","."))
    df["ho_middle"] = pd.to_numeric(df["ho_middle"], downcast="float")
    
    df["ho_long"]= df["ho_long"].apply(lambda x: str(x).replace(",","."))
    df["ho_long"] = pd.to_numeric(df["ho_long"], downcast="float")
    
    
    for fon in df["Fon Kodu"].unique():
        
        fdf = df[df["Fon Kodu"] == fon ] 
        
       
        
        x = fdf[["Fiyat", "ho_short", "ho_middle", "ho_long"]]
        y = fdf["nxFiyat"]
        
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30, random_state=42)
        
        scaler = StandardScaler().fit(x_train)
        
        x_train_sc = scaler.transform(x_train)
        x_test_sc = scaler.transform(x_test)
        
        
        
        model = MLPRegressor().fit(x_train_sc, y_train)
     
     
        pickle.dump(model, open("models\_ann_" + fon + ".model","wb"))
        
        fondf = pd.DataFrame()
        fondf["x_test"] = x_test["Fiyat"]
        fondf["y_test"] = y_test
        fondf["y_pred"] = model.predict(x_test)
        fondf["GerçekFark"] = fondf["y_test"] -  fondf["x_test"]
        fondf["TahminFark"] = fondf["y_pred"] -  fondf["x_test"]
        fondf["Gerçek"] = fondf["GerçekFark"].apply(lambda x: x>0)
        fondf["Tahmin"] = fondf["TahminFark"].apply(lambda x: x>0)
        fondf["Ongoru"] = fondf["Gerçek"] * fondf["Tahmin"]
        fondf["Skor"] = model.score(x_test, y_test)
        
        mse = np.sqrt(mean_squared_error(y_test,fondf["y_pred"] ))
        fondf["mean_squared_error"] = mse
        
        
        print("mse", mse)
        print("Eğitim Skoru : " , model.score(x_train, y_train))
        print("Tahmin Skoru : " , model.score(x_test, y_test))
        fondf.to_csv("tahminler\_ann_" + fon + ".csv", index=False)

@hatayakala    
def grafik_LinearRegression(fon, fondf):
    
    x = fondf[["Fiyat", "ho_short", "ho_middle", "ho_long"]]
    
    
    fondf["y_pred"] = fon_LinearRegression(fon, x)
    
    
    fondf = pd.melt(fondf, id_vars=['Tarih'], value_vars=['Fiyat', 'y_pred'])

    fig, ax = plt.subplots()
    
    sns.lineplot(ax = ax, x ="Tarih", y = "value", hue="variable", data=fondf)
    plt.title(fon)
    
    plt.xticks(rotation='vertical')
    
    return fig

@hatayakala
def fon_LinearRegression(fon, x):
    """ x  için gönderilmesi gereken değerlerin örneği
    x = fdf[["Fiyat", "ho_short", "ho_middle", "ho_long"]]
    ya da 
    x = pd.DataFrame([[1.36,1.55,1.49,1.557]])
    """
    
    model = pickle.load(open("models\LinearRegression_" + fon + ".model", "rb"))
    y_pred = model.predict(x)
    return y_pred
    

"""
x_deg = pd.DataFrame([[1.36,1.55,1.49,1.557]]) #"Fiyat", "ho_short", "ho_middle", "ho_long"
y_pred = fon_LinearRegression("ZPK", x_deg)
print("ZPK Tahmin Edilen Ertesi Gün Fiyatı : ", y_pred)
"""