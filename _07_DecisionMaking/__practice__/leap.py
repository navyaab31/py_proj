# REQ: check if it is leap year or not
'''
state: user enter the year
behavior: print it 
            ==> if it is a leap year

Functional Analysis:
-------------------------
1.user will enter the year  :state
2.Check if it is leap year  :behavior
3. if year%100!=0 and year%4==0 or year%400==0 ==> it a leap year

Technical Analysis:
-----------------------
1. STATE : Datatypes/Datastructures  :user enter the pass word
2. BEHAVIOR: operators,  DM  , Loop    :check if it is leap year
                %,==     if else

Entity : user
state : given year
behavior: check if it is leap year or not

'''
# state
year = int(input("enter the year: "))

# behavior
if (year%4==0 and year%100!=0) or year%400==0:
    print("it is leap year")
else:
    print("it is not a leap year")

