# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:34:34 2024

@author: ThanhTrong
"""

# Kiểm tra tam giác
a = float(input("Nhập số tự nhiên a: "))
b = float(input("Nhập số tự nhiên b: "))
c = float(input("Nhập số tự nhiên c: "))
if  a == b or a == c or b == c:
    print("Tam giác cân")
elif a == b == c:
    print("tam giác đều")
elif a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
    print("Tam giác vuông")
else :
    print("Tam giác thường")