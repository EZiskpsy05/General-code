import math
from math import sqrt

b = int(input("Độ dài cạnh b:"))
c = int(input("Độ dài cạnh c:"))
area = b*c/2
Pytago = math.sqrt(b*b + c*c)
print("Diện tích tam giác:", area)
print("Cạnh huyề tam giác:", round(Pytago, 4))

# Đáp án 
#Độ dài cạnh b:5    Độ dài cạnh c:10
#Diện tích tam giác: 25.0
#Cạnh huyền tam giác: 11.1803