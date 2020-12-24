# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 20:44:19 2020
"""



# f-string and format usage
val1 = int(   input("Lütfen integer giriniz : ") )
val2 = float( input("Lütfen float   giriniz : ") )
val3 = bool(  input("Lütfen boolean  giriniz : ") )
val4 =        input("Lütfen string  giriniz : ")
print() 
print(f"1. değer :{val1} - tipi :{type(val1)}")
print(f"2. değer :{val2} - tipi :{type(val2)}")
print(f"3. değer :{val3} - tipi :{type(val3)}")
print(f"4. değer :{val4} - tipi :{type(val4)}")
print()
print("1. değer :{} - tipi :{}".format(val1, type(val1)) )
print("2. değer :{} - tipi :{}".format(val2, type(val2)) )
print("3. değer :{} - tipi :{}".format(val3, type(val3)) )
print("4. değer :{} - tipi :{}".format(val4, type(val4)) )
