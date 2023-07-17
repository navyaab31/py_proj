# Write a program that reads three positive numbers a, b, c and determines whether they can form the three sides of a triangle.
# REQ:check values are forms a triangle or not
'''
state:three values by the user
behavior:check those values forms a triangle or not

Functional Analysis:
----------------------
1.user enter the three numbers   :state
2.check if that values are forms a triangle or not   :behavior
3. (val1+val2)<=val3 ==>print it

Technical Analysis:
----------------------
1.STATE : Datatypes/Datastructure     :user enter the values
2.BEHAVIOR: operators,DM,loops     :check if it is forms a triangle or not
            <=         if else

Entity:user
state:given numbers
behavior: chech it if val1+val2 <= val3
'''

# state
a=int(input("enter num1: "))
b=int(input("enter num2: "))
c=int(input("enter num3: "))

if (a+b)<=c or (b+c)<=a or (a+c)<=b:
    print("it forms a triangle")

else: 
    print("it not forms a triangles")