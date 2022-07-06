import math
num = 8990.892002
format_num = "{:.2f}".format(num)
print(format_num)



a=4
b= -11
c=-21
d=(b**2)-(4*a*c)
ans1=(-b+ math.sqrt(d)/(2*a))
ans2=(-b- math.sqrt(d)/(2*a))
print('the roots are ', (ans1 , ans2) )