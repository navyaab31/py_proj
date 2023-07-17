''''
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
salary=int(input("enter your salary: "))
y_o_s=int(input("enter your year of experience: "))

if y_o_s>=5:
    print("bonus is add: ",salary+((salary*5)/100))
else:
    print("bonus is not added")

#  Take values of length and breadth of a rectangle from user and check if it is square or not.
length=int(input("enter the length: "))
breadth=int(input("enter the breadth: "))

rect=length*breadth

if rect==length**2:
# if length==breadth
    print("it is square")
else:
    print("it is not a square")


# Take two int values from user and print greatest among them
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))

if num1>num2:
    print("greater is ",num1)
else:
    print("greater is ",num2)


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user
quty=int(input("enter the quantity: "))
if quty*100>1000:
    print("your bill is: ",(quty*100)-(quty*100*0.1))
else:
    print("your bill is: ",quty*100)


# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade
marks=int(input("enter the marks: "))
if marks<25:
    print("grade is F")
elif marks>=25 and marks<45:
    print("grade is E")
elif marks>=45 and marks<50:
    print("grade is D")
elif marks>=50 and marks<60:
    print("grade is C")
elif marks>=60 and marks<80:
    print("grade is B")
elif marks>=80:
    print("grade is A")


# Take input of age of 3 people by user and determine oldest and youngest among them.
p1=int(input("p1: "))
p2=int(input("p2: "))
p3=int(input("p3: "))

if p1>p2 and p1>p3:
    print("oldest is p1")

elif p2>p1 and p2>p3:
    print("oldest is p2")
elif p3>p1:
    print("oldest is p3")
else: 
    print("all are same")


# Write a program to print absolute vlaue of a number entered by user
number=int(input("nuber: "))
if number < 0:
    print(number*-1)
else:
    print(number)
'''
# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
class_held=int(input("enter the no. of classes held: "))
class_attended=int(input("enter the no. classes attended: "))

perc=(class_held/class_attended)*100
if perc >= 75:
    print("this student is allow to sit in the exam")
else:
    mediacl=input("enter Y or N:" ).upper()
    if mediacl=="Y":
        print("student is allow to sit in exam")
    else:
        print("student are allow to sit in the exam")

# Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
    

