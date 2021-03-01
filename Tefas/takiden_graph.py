# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_excel("Takiden.xlsx")


df = df[1:] 

df.columns = ['TARİH', 'devlettahvili', 'eurobond',
       'finansmanbonosu', 'fonkatilmabelgesi',
       'hissesenedi', 'kamukirasertifikalari',
       'kiymetlimadenler', 'ozelsektorkirasertifikalari',
       'ozelsektortahvili', 'turevaraclari', 'tpp',
       'tersrepo', 'vadelimevduat', 'yabancihissesenedi']

df['TARİH'] = pd.to_datetime(df['TARİH'], format="%Y-%m-%d")
    
df.sort_values("TARİH", inplace=True)
    
kolonlar = df.columns[1:]


df = pd.melt(df, id_vars=['TARİH'], value_vars=kolonlar)
df.columns = ["TARİH", "variable", "value"]
df["value"] = df["value"].astype(float)

"""
#sns.lineplot(x ="TARİH", y = "value", hue="variable", data=df)
sns.barplot(x ="TARİH", y = "value", hue="variable", data=df)

plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.xticks(rotation=90)

plt.show()

"""

"""3d"""
from mpl_toolkits.mplot3d import Axes3D


sns.set(style = "darkgrid")

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = df['TARİH']
y = df['value']
z = df['variable']

"""ax.set_xlabel("Happiness")
ax.set_ylabel("Economy")
ax.set_zlabel("Health")"""

ax.scatter(x, y, z)

plt.show()