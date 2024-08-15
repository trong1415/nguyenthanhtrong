# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:54:28 2024

@author: ThanhTrong
"""
import math
# Phương trình bậc 2
a = float(input("Nhập số tự nhiên a: "))
b = float(input("Nhập số tự nhiên b: "))
c = float(input("Nhập số tự nhiên c: "))
delta = b**2-4*a*c  
if a==0:
    print("Phương trình không phải phương trình bậc 2")   
elif delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("phương trình có nghiệp kép: ")
    print("Nghiệm 1 = Nghiệm 2 =", -b/2*a)
elif delta > 0:
    x1=(-b + math.sqrt(delta)) / (2*a)
    x2=(-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có 2 nghiệm")
    print("Nghiệm 1 = ", x1)
    print("Nghiệm 2 = ", x2)