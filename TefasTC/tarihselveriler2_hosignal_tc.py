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
df["Tarih"] = pd.to_datetime(df["Tarih"], format="%Y-%m-%d")
df.dropna(inplace=True)

condition3 = df['Tarih'] >= '2017-01-01' # YIL  AY GÜN ALIYOR
df = df.loc[condition3]

# 'HYV' HEDEF PORTFÖY PARA PIYASASI FONU YENİ PARAPİYASASI FONU İLK AYI TAKİP EDİLECEK
# 'FIL' ESKİ PERFORMANSLI PARA PİYASASI FONU 5YO:%20 (MIN%11)
# 'FCV' FİBA PORTFÖY ÇOKLU VARLIK DEĞİŞKEN FON 5YO:%20 (MIN:15)
# 'IDY' TEB PORTFÖY İKİNCİ DEĞİŞKEN FON 5YO:%20 (MIN:16)
# 'TGE' İŞ PORTFÖY YABANCI EMTIA FONU METAL ENERJİ PETROL DOĞALGAZ FONU
# 'AFO' AK PORTFÖY ALTIN FONU : %90INI KAMU KİRA SERTİFİKASI OLUŞTURUYOR 5YO:%44
# 'AFS' AK PORTFÖY YABANCI SAĞLIK HİSSESİ FONU 5YO:%68
# 'AFT' AK PORTFÖY YABANCI YENİ TEKNOLOJİLER 5YO:%130 GETİRİ
# 'AKE' AK PORTFÖY YABANCI EUROBOND BORÇLANMA ARAÇLARI FONU 5YO:%36
# 'DBH' DENİZ PORTFÖY EUROBOND (DÖVİZ) BORÇLANMA ARAÇLARI FONU 5YO:%40
# 'EIB' QİNVEST PORTFÖY DEĞİŞKEN FON 5YO:%26
# 'FIB' FİBA PORTFÖY ALTIN FONU 5YO:%44
# 'FNO' QNB FINANS BIRINCI DEĞIŞKEN FON, ÇOOK GÜZEL KARIŞIK 5YO:%24
# 'FPE' FİBA PORTFÖY EUROBOND BORÇARAÇLARI (DÖVİZ)FONU 5YO:%40
# 'FUB' QNB FINANS PORTFÖY EUROBOND BORÇARAÇLARI FONU 5YO:%40
# 'GBG' GEDİK PORTFÖY G-20 ÜLKELERİ YABANCI HİSSE SENEDİ FONU 5YO:%60
# 'GMA' AZİMUT PYŞ ÇOKLU VARLIK DEĞİŞKEN FON ÇOOK GÜZEL KARIŞIK 5YO:%46
# 'GPB' GARANTİ PORTFÖY BİRİNCİ DEĞİŞKEN FON RİSKSİZ STABİL 5YO:%22

for i in df["Fon Kodu"].unique():
    
    tmpdf = df[df["Fon Kodu"] == i ]  #'GUH'] # i ] #
    #tmpdf["ho5"] = tmpdf["FİYAT"].ewm(span =10).mean()
    tmpdf["Tarih"] = pd.to_datetime(tmpdf["Tarih"], format="%Y-%m-%d")
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
    plt.xticks(rotation='vertical')
    plt.savefig('./plots/'+i+'_2016_Ocak.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
    plt.show()

    condition35 = tmpdf['Tarih'] >= '2020-01-01'  #  YIL AY GÜN ALIYOR
    tmpdf2 = tmpdf.loc[condition35]
    
    sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf2, linewidth=.80).set_title(i)   # 'AES')
    plt.xticks(rotation='vertical')
    plt.savefig('./plots/'+i+'_2020_Ocak.png') # önce kayıt etmek şart, sonra kayıt edince olmuyor...
    plt.show()
    
    condition4 = tmpdf['Tarih'] >= '2020-12-01'  #  YIL AY GÜN ALIYOR
    tmpdf2 = tmpdf.loc[condition4]

    sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf2, linewidth=.80).set_title(i)   # 'AES')
    plt.xticks(rotation='vertical')
    plt.savefig('./plots/'+i+'_2020_Aralik.png')
    plt.show()




    condition5 = tmpdf['Tarih'] >= '2021-02-01' #  YIL AY GÜN ALIYOR
    tmpdf3 = tmpdf.loc[condition5]

    sns.lineplot(x ="Tarih", y = "value", hue="variable", data=tmpdf3, linewidth=.80).set_title(i)   # 'AES')
    plt.xticks(rotation='vertical')
    plt.savefig('./plots/'+i+'_2021_Subat.png')
    plt.show()


    
   