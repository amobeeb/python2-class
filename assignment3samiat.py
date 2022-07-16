
import math
from unicodedata import decimal
#this program will print the area of a regular polygon
#s=lenght of a side
#n=number of sides
#apothem=s/(2tan(180/n))
#perimeter=s*n
# AreaOfPolygon=(perimeter*apothem)/2
# s=float(input('lenght of a side: '))
# n=float(input('number of sides: '))
# perimeter=s*n
# a=180/n
# b=math.tan(a)
# apothem=s/(2*b)
# AreaOfPolygon=(perimeter*apothem)/2
# # print(a)
# print(b)
# print(perimeter)
# print(apothem)
# print(AreaOfPolygon)

#This program will convert binary number to decimal number.

b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	print(digit)
	# if b_num[i] == '1':
        #  print(digit)
		# value = value + pow(2, i)
		# print(value)
# print("The decimal value of the number is", value)