# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

"""Birleştirilmiş verilerimizi tutan csv dosyasını pandas dataframe içine alıyoruz."""
df = pd.read_csv("TarihselVeriler.csv")

"""Aramalarda bir önceki tarihi araken düzgün sıralama yapsın diye 
TARİH kolonunun tipini datetime yapıyoruz"""
df['TARİH'] = pd.to_datetime(df['TARİH'], format="%Y-%m-%d")

df['gun'] = df['TARİH'].dt.dayofweek

df = df[df["gun"]==4]

df["fark"] = 0
df["h_degisim"] = 0

"""dataframein tüm satırlarını tek tek gezecek şekilde bir for döngüsü oluşturuyoruz"""
for index, row in df.iterrows():
    
    """dataframe içinde Tarihi üzerinde bulunduğumuz kolondan küçük olan tarihleri bulup
    max fonksiyonu vasıtasıyla en büyüğünü alıyoruz. Ki bu içinde bulunduğumuz satırın tarihinden 
    bir önceki tarih demek olacak, ve bizim bir önceki fiyatı bulmamıza yarayacak"""
    Tarih = df[df["TARİH"] < row["TARİH"] ]["TARİH"].max()
    
    """Bir önceki tarihi ve içinde bulunduğumuz satırın fon adını taşıyan kaydın fiyat değişkenini alıyoruz
    mean fonksiyonunu kullanmam kafanı karıştırmasın. Value çalışmadı ben de ortalamasını veren mean fonksiyonunu kullandım değerini alabilmek için. """
    Fiyat = df[(df["TARİH"] == Tarih) & (df["FON KODU"]==row["FON KODU"]) ]["FİYAT"].mean()
    
    """ içinde bulunduğumuz kaydın şimdiki fiyatından bulduğumuz bir önceki fiyatı çıkarıp
    bulunduğumuz satırın fark kolonuna yazıyoruz"""
    deger = row["FİYAT"] - Fiyat
    df.loc[index, "fark"] = deger 
    
    if Fiyat !=0 :
        df.loc[index, "h_degisim"] = deger / Fiyat
    print(deger)
       


"""Değiştirdiğimiz dataframe başka bir csv dosyasına kaydediliyor."""
df.to_csv("TarihselVeriler_hd.csv", index=False)
