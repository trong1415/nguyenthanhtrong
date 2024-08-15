# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:52:48 2024

@author: ThanhTrong
"""
# phương trình bậc nhất
a = float(input("Nhập số tự nhiên a: "))
b = float(input("Nhập số tự nhiên b: "))
if a!=0:
    print("Phương trình có nghiệm là: ",-b/a)
elif a==0 and b==0:
    print("Phương trình có vô số nghiệm: ")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm: ")
    

    