# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:25:31 2024

@author: ThanhTrong
"""

# Ngày tháng 
y=float(input("Nhập năm sinh của bạn: "))
if y>0:
    if (y%4==0 and y%100!=0) or y%400==0:
        m=float(input("Nhập tháng sinh của bạn: "))
        if m>=1 and m<=12:
            if m==2:
                d=float(input("Nhập ngày sinh của bạn: "))
                if d>=1 and d<=29:
                    print(" Ê đúng rồi má")
                else:
                    print(" Mày định lừa ai ???")
            if m==4 or m==6 or m==9 or m==11:
                d=float(input("Nhập ngày sinh của bạn: "))
                if d>=1 and d<=30:
                     print("Ê đúng rồi má")
                else:
                     print(" Mày định lừa ai ???")
            if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
                d=float(input("Nhập ngày sinh của bạn: "))
                if d>=1 and d<=31:  
                    print("Ê đúng rồi má")
                else:
                    print(" Mày định lừa ai ???")
    else:
        m=float(input("Nhập tháng sinh của bạn: "))
        if m==2:
            d=float(input("Nhập ngày sinh của bạn: "))
            if d>=1 and d<=28:
                print("Ê đúng rồi má")
            else:
                print(" Mày định lừa ai ???") 
        if m==4 or m==6 or m==9 or m==11:
            d=float(input("Nhập ngày sinh của bạn: "))
            if d>=1 and d<=30:
                 print("Ê đúng rồi má")
            else:
                 print(" Mày định lừa ai ???")
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            d=float(input("Nhập ngày sinh của bạn: "))
            if d>=1 and d<=31:  
                print("Ê đúng rồi má")
            else:
                print(" Mày định lừa ai ???")
           
else:
     print(" Mày định lừa ai ???")
