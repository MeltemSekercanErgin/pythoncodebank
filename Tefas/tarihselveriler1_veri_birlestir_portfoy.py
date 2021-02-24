# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""
""" 5 yıllık tüm veriyi birleştirip bir cesv dosyası olarak kaydediyoruz"""

import pandas as pd

"""ilk veri dosyası okunuyor. 
Diğer tüm okunan veriler bunun üzerine eklenecek.
Bunu for döngüsü dışında yaparak for içerisinde bir koşul cümlesinden kurtuluyoruz."""
df = pd.read_excel("TarihselVeriler1.xlsx", sheet_name =1)

"""ÖZEL FON ve SERBEST kelimelerini içeren fonlar bir kolon üzerinde True olarak işaretleniyor.
sil kolonu True olanlar dataframeden siliniyor"""
df["sil"] = df["Fon Adı"].apply(lambda x : ("ÖZEL FON" in x) or ("SERBEST" in x))
df.drop(df[df['sil']].index, inplace = True) 
  
""" kalan diğer xlsx dosyaları (ki 2,3,4,5,6 olarak isimlendirilmişlerdi indirirken)
okuma ve ÖZEL FON ve SERBEST içerenlerin silinmesi işlemi yapılıyor."""
for i in range(2,7):
    df2 = pd.read_excel("TarihselVeriler" + str(i) +".xlsx", sheet_name =1)
    df2["sil"] = df2["Fon Adı"].apply(lambda x : ("ÖZEL FON" in x) or ("SERBEST" in x))
    df2.drop(df2[df2['sil']].index, inplace = True) 
    
    """verilen iki dataframei (df ve df2) birleştirip df dataframeine tekrar atıyoruz."""
    df = pd.concat([df, df2], ignore_index = True)

"""geçici olarak oluşturduğumuz sil kolonunu siliyoruz"""
df.drop('sil', axis=1, inplace=True)

"""Dataframe içeriğini csv dosyaya kaydediyoruz.
sonraki işlemlerde sürekli oluşturmak yerine bu csv dosyayı okuyarak devam edeceğiz."""
df.to_csv("TarihselVeriler_portfoy.csv", index=False)