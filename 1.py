# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:02:27 2024

@author: ThanhTrong
"""
# Tính GPA
print("Hello, World!")
GPA = float(input("Nhập điểm trung bình (GPA): "))
if GPA < 3.5:
    print("Học lực kém")
elif 3.5 <= GPA <5.0:
    print("Học lực yếu")
elif 5.0 <= GPA < 7.0:
    print("Học lực trung bình")
elif 7.0 <= GPA < 8.0:
    print("Học lực khá")
elif 8.0 <= GPA < 9.0:
    print("Học lực giỏi")
elif 9.0 <= GPA <= 10:
    print("Học lực xuất sắc")