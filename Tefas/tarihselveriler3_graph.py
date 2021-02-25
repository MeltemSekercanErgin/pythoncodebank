# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd
"""veri dosyasını okuyoruz"""
df = pd.read_csv("TarihselVeriler_gd.csv")

"""verilerimizi tutan dataframein bir kopyasını alıyoruz. 
içindeki NA/Nan değerleri siliyoruz.
Bunu yapmamızın sebebi hesaplanamayan ve NaN olarak kaydedilen g_degisim değerlerinin grafiği bozmaması için"""
tmpdf = df.copy()
tmpdf.dropna(inplace=True)

"""Veritabanındaki form kodlarını unique olarak alıyoruz.
Bu sayede sorgu oluşturup bir tür gruplama yapmış olacagız"""
for i in df["FON KODU"].unique():
    
    """Tarih ve g_degisim grafiği çiziyoruz.
    g_degisimde null değerleri çıkardığımız tmpdf dataframeini kullanıyoruz
    içerisine sorgu olarak fon kodu içinde bulunduğumuz for adımının fon kodunu taşıyanları getirtiyoruz.
    grafiği oluşturmak için de pandas dataframe nesnelerinin sahip olduğu plot fonksiyonunu kullanıyoruz"""
    tmpdf[tmpdf["FON KODU"] == i ].plot(x="TARİH", y= "g_degisim", sort_columns="TARİH", title=i)
    
    """Tarih ve Fiyat grafiğini çiziyoruz.
    bir önceki satırdaki gibi işlem yapıyoruz.
    burada df dataframeini kullanmamızın sebebi değişimdeki null değerlerin bizi ilgilendirmemesi.
    değişimi hesaplanamamış olsa bile fiyata sahip olan satırları da gösterebilmek"""
    df[df["FON KODU"] == i ].plot(x="TARİH", y= "FİYAT", sort_columns="TARİH", title=i)

