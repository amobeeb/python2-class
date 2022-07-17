# a=input("attendance")
# b=imput("hommework")
# c=input("exams")

# Answer=int((attandance+homework+Exam)/3)

# Textbox4.Tex ="The Answer=" & Answer & "The grade ia A "

# Textbox4.Text ="The Answer=" & Answer & "The grade ia B "

# Textbox4.Text="The Answer=" & Answer & "The grade ia c "


sub1=int(input("get here sub1 marks:"))
sub2=int(input("get here sub2 marks:"))
sub3=int(input("get here sub3 marks:"))

sum=sub1+sub2+sub3
totalMarks=300
percentage=(sum/totalMarks) * 100
Avg=(sum/3)
print("percentage is ",percentage)
print("Average is ",Avg)