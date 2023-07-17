# REQ: check number is didvisible by 3 and 7
'''
state:user enter the number
behavior: check it 
            ==> if it is divisible by 3 and 7

Functional Analysis:
---------------------
1. user enter a number              :state                   
2. check the number is divisible by 3 and 7 :behavior
3. if val%3==0 and val%7==0 ==> print it

Technical Analysis:
1.STATE  :  Datatypes/Datastructures   : Customer given number
2.BEHAVIOR: operators ,  DM ,   loop  :check if it is divisible by 3 and 7
                %,==     if elif else

entity : user
state : given numbers
behavior:check the number is divisible by 3 and 7 
'''

# state
num = int(input("enter number: "))

# behavior

if num%3==0 and num%7==0:
    print("number is divisible by 3 and 7")
else: 
    print("number is not divisible by 3 and 7")
    
