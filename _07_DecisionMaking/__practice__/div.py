#REQ: check the number is divisible by 5 or not
'''
state: user enter number
behavior: check the given number 
                ==>if is divisible by 5 or not

Functional Analysis:
---------------------
1. user enter the n8umber   :state
2. check if it is divisible by 5  :behavior
3. if val%5==0 ==> print it


Technical Analysis:
---------------------
STATE: Datatypes/Datastructures   :state
BEHAVIOR : operators,   DM  ,   Loop    :check if it is divisible by 5
                %,==    if else
'''
# state
num=int(input("enter number: "))
# behavior
if num%5==0:
    print(num ,"is divisible by 5")
else:
    print(num ,"is not divisible by 5")
    
