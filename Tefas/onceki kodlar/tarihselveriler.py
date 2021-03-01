# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:07 2021

@author: SS
"""

import pandas as pd

df = pd.read_csv("TarihselVeriler_gd.csv")

print(df[["FON ADI", "g_degisim"]].head())

