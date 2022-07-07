
import math
#this program will print the area of a regular polygon
#s=lenght of a side
#n=number of sides
#apothem=s/(2tan(180/n))
#perimeter=s*n
#AreaOfPolygon=(perimeter*apothem)/2
s=float(input('lenght of a side: '))
n=float(input('number of sides: '))
perimeter=s*n
a=180/n
b=math.tan(a)
apothem=s/(2*b)
AreaOfPolygon=(perimeter*apothem)/2
print(a)
print(b)
print(perimeter)
print(apothem)
print(AreaOfPolygon)

