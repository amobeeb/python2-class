stu1=int(input("attandance:"))
stu2=int(input("homework:"))
stu3=int(input("exam:"))

sum=stu1+stu2+stu3
totalMarks=300
percentage=(sum/totalMarks) * 100
Avg=(sum/3)
print("percentage is ",percentage)
print("Average is ",Avg)