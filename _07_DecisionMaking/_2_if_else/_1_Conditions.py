''''''
# REQUIREMENT : Get student result(Pass/Fail) based on given input marks.
'''
  As given marks = 40
  If marks are greater than or equal to 35, then
        Result is PASS
  Else
        Result is FAIL
'''
# STATE : : given input marks. : Data types/structures
marks = int(input("Enter marks1 : "))

# BEHAVIOR : Operators, DM, Loops:   Get student result(Pass/Fail)
if marks >= 35:
    print("Result PASS")
else:
    print("Result FAIL")

# BEHAVIOR
 # 1. crud  : CREATE
 # 2. Validations : should be between 0 to 100
 # 3. Concept: Operators, DM,      Loops
 #             > <=       if else

if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:
        print("Result PASS")
    else:
        print("Result FAIL")
else:
    print("Invalid marks")






'''
Requirement: Find value of x for expression x**2+2x+1 when x = 10.

# STATE    : when x is 10              --->  As given x = 10
# BEHAVIOR : Find the value of x2+2x+1 --->  Substitute value of x in given expression
                                                 # Business Logic
                                             = x2+2x+1
                                             = (10)**2+2(10)+1
                                             = 100+20+1
                                             = 121
'''

'''
# REQUIREMENT : Get student result(Pass/Fail) based on given input marks.
  
  Condition/Validation: 
  -----------------------
  - Customer input data should not be less than 0  and greater than 100 
    
  User criteria: 
  --------------
  - If marks are greater than or equal to 35 then display as PASS else FAIL
                    >= 35 --> PASS
                    < 35  --> FAIL  
                    
Valid marks:  -1 0 1    99 100 101   
Invalid marks: -25   120
'''
'''
1.State
        Validation
2.Behavior
'''
# STATE
marks = int(input("Enter Marks : "))
    # Validation
if marks >= 0 and marks <= 100:
    print("-----Valid marks-----")
    if marks >= 35:
        print("Result : PASS")
        # Division
    else:
        print("Result : FAIL")
else:
    print("-----Invalid marks----")

# Other apporach
if marks < 0 or marks > 100:
    print("-----Invalid marks-----")
else:
    print("-----Valid marks----")



'''
Step1 : STATE    : Datatype/Data structures 
                            (int*/float/bool/string/list/tuple/dict/set)
Step2 : BEHAVIOR : Business Logic implementation
                            (Operators, DM, Loops)
                            Comparison,Logical + DecisionMaking(if else)
         
Client side validations
Server side validations  
                            
STATE       : S1: int : marks   
BEHAVIOR    : S2: Validation    : Decision Making
                  Implementation: Decision Making concept   
                                  (Get student result(Pass/Fail))
                     
'''
print("-----------Without Validation : Student Result-----------")
# Without validations

# STATE
marks = int(input("Enter marks :"))

# BEHAVIOR
if marks >= 35:
    print("Result is : PASS ")
else:  # elif marks < 35:
    print("Result is : FAIL ")


print("-----------With Validation : Student Result-----------")

# With validations
    # 1. STATE
# marks = 80  # static way of data initialization,  hardcoding data
marks = int(input("Enter marks :"))   # Dynamic way

    # 2.BEHAVIOR
if marks < 0 or marks > 100:
    print("------- Invalid marks -------")
else:
    if marks >= 35:
        print("Result is : PASS ")
    else:    # elif marks < 35:
        print("Result is : FAIL ")
print("----------------------------------")
# This is better
if marks >= 0 and marks <= 100:
    if marks >= 35:
        print("Result is : PASS ")
    else:    # elif marks < 35:
        print("Result is : FAIL ")
else:
    print("--------Invalid marks--------")
'''
Testcases :     -1    0     1
                99  100   101  
                34   35    36
               -10  120
                20   60
                
'''
# validation logic : customer input data should not be greater than 100 and less than 0



'''
REQ: Check whether given number is - positive or 
                                   - negative
                                   - neither positive nor negative
1 condition  : if 
2 conditions : if else
3 conditions : if elif else
4 conditions : if elif elif else
5 conditions : if elif elif elif else
'''
print("-----------Positive or Negative-----------")
#num = 10
num = int(input("Enter any number: "))

if num > 0:
    print("Number is positive")
elif num < 0:  # else if
    print("Number is negative")
else:     # elif num == 0
    print("Neither pos. nor Neg.")



'''   DEV vs Enhancement
Enhancement:
-------------
For PASS criteria, Find Student grade/class. 
                    First class  >= 60
                    Second class >= 50 and < 60
                    Third class  >= 35 and < 50
    - Validation code
    - User criteria pass/fail
    - Division/Class
    - Check cent marks
'''
print("-----------Result with class-----------")
# STATE
marks = int(input("Enter marks3 : "))

# BEHAVIOR
if marks >= 0 and marks <= 100:    # -1 0 1 99 100 101  45  -23 345
    print("---Valid marks-------")
    if marks >= 35:                # 34 35 36     20  60
        print("Result : PASS")
        if marks >= 60:            # 59 60 61    49 50 51  34 35 36   70  55  40
            print("First Class")
            if marks == 100:               # 99 100 101
                print("Congratulations")
        elif marks >= 50:
            print("Second Class")
        else:
            print("Third Class")
    else:
        print("Result: FAIL")
else:
    print("---Invalid marks------")


# Validation marks : Valid / Invalid
# Student Result   : Pass / Fail
# Division         : First / Second / Third
# Cent marks       : Cent


'''
  -1 0 1   99 100 101     -25  120
   59 60 61 
   49 50 51   
   34 35 36
   
int:    float 
        boolean string list 
        
'''






'''
if marks >= 0 and marks <= 100:
    if marks >= 35:
        print("Result: PASS")
        if marks >= 60:
            print("Result : FIRST CLASS")
            if marks == 100:
                print("-----SUPER..Congratulations-----")
            elif marks >= 90:
                print("----GOOD..Congratulations-------")
        elif marks >= 50 and marks < 60:
            print("Result: SECOND CLASS")
        elif marks >= 35 and marks < 50:
            print("Result: THIRD CLASS")
    else:
        print("Result: FAIL")
        if marks == 0:
            print("--------DOUBLE SUPER----------")
else: 
    print("Please enter valid marks between 0 to 100")
'''

'''
gmail id: userid: mad               : min 7 chars 
                  madhu nettem      : no space 
                  madhu@nettem      : @ is not allowed 

                  madhunettem       : serverside validation

        Client side     ServerSide   Database
        HTML CSS JS      Python      Oracle 
'''