# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:57:01 2021

@author: SS
"""

import pandas as pd

""" csv dosyayı okuyup bir pandas dataframe yaratıyoruz"""
df = pd.read_csv("netflix_titles.csv")


print(df.columns)
"""buradan dataframe kolon isimlerine bakarak elimizde hangi veriler olduğunu öğreniyoruz.
['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description']
"""


print ("""    VERİ TABANI ÖZETİ\n
Kaç adet içerik var :""", len (df),
"""\nDizi Sayısı : """, len(df[df["type"] =="TV Show"]),
"""\nFilm Sayısı : """, len(df[df["type"] =="Movie"]),
)

""" kaç farklı oyuncu var.
Cast kolonunu direk alamıyoruz çünkü virgülle ayrılmış halde çoklu duruyorlar.
Bunları split ile ayırmak ve tek olmasını sağlamamız gerekiyor.

)"""


cast_set = set() #küme seçmemin nedeni tekrarlı eleman içermemeleri. Dolayısıyla unique olması için herhangi bir işlem yapmama gerek kalmayacak
for i in df.cast:
    cast_set |= set(str(i).split(","))

print("Oyuncu Sayısı : ", len(cast_set))


    
