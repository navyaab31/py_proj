x = 10
print(x)
x = 10.5
print(x)
x = True   # 1 nonzero nonNone
print(x)
x = False  # 0  None
print("---------------------")

x = 0.1
y = 0.2
print("True or not :", x == y)
print(x+y)

'''
Requirement : If user entered number is greater than or equal to 10, 
              then display "Two digit number"  
              else print " One digit number"           
'''
# STATE
val = int(input("Enter value : "))
# BEHAVIOR
if val >= 10:
    print("Two digit number")
else:
    print("One digit number")
print("-------End of if-------")



# Find given number is even or odd
# Solution : If any number is divisible by 2 and remainder is 0, it is Even number,
# else odd number.

# STATE
num = int(input("Enter number : "))
print("Given number : ", num)
# BEHAVIOR
if num % 2 == 0:
    print("Even number")  # 4 spaces indentation
else:
    print("Odd number")   # block of statements

'''
If the condition is True program exuection will go inside of if block,
else it will go inside of else block
'''
'''
if num % 2 == 0{
print("Even number");
}
else{
print("Odd number");
}
'''
# REQ: Confirm whether user entered value is Positive, Negative or Zero
# STATE
x = int(input("Enter number: "))
# BEHAVIOR
if x < 0:
    print("Negative number")
elif x > 0:
    print("Positive number")
else:  # elif x == 0
    print("ZERO : NEITHER POS NOR NEG")

'''
Project types:
--------------
DEVELOPMENT
ENHANCEMENT
PRODUCTION SUPPORT

Requirement/Story/Ticket/Incident/Service Request:
Requirement: Get Student Result
User Criteria : User Input       --- Between 0 to 100
                Conditional Data --- Student result -- >=35 PASS
                                                       <35 FAIL

marks >= 0  and marks <=  100
Validations: Client side: UI Side
             Server side: Backend
'''

# Get Student result
'''
1. CRUD     : Create
2. STATE    : int float bool string list tuple dict set
3. Validation(Client/Server)
4. BEHAVIOR : 
'''
# 1. STATE   -  Receive User input
marks = int(input("Enter marks: "))

'''
I. If marks greater than or equal to 0 and marks less than or equal to 100 then 
    - It is valid marks 

II. If marks greater than or equal to 35 then result is PASS
       else FAIL
'''
if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:
        print("Result : PASS")
    else:
        print("Result : FAIL")
else:
    print("Invalid marks")

# Negative scenario based
if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    print("Valid marks")
    # Business logic
    if marks >= 35:
        print("Result : PASS")

    else:
        print("Result : FAIL ")
'''
# Validation
# 2. BEHAVIOR
if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:
        print("Result is PASS")

    else:  # elif marks < 35
        print("Result is FAIL")
else:
    print("Invalid marks")

print("--------------------------")


Requirement:
--------------
REQ: Get student division
        # Enhancement: Get Division 1st 2nd 3rd
As part of enhancement for student result, 
we need to implement new feature. We should find
division(1st,2nd,3rd) based on marks if the result is PASS.
Criteria: 1st : >= 60
          2nd : >= 50 and < 60
          3rd :  >= 35 and < 50


'''
# STATE
marks = int(input("Enter marks : "))

# BEHAVIOR
if marks >= 0 and marks <= 100:
    print("Valid Marks")
    if marks >= 35:
        print("Result : PASS :", marks)
        if marks >= 60:
            print("First Class")
            if marks >= 90:
                print("Distinction")
                if marks == 100:
                    print("----Congratulations----")
        elif marks >= 50:
            print("Second Class")
        else:
            print("Third Class")
    else:
        print("Result : FAIL :", marks)
else:
    print("Invalid Marks")

# -1 0 1 34 35 36   59 60 61 89 90 91 99 100 101 49 50 51    -43 456


a = 11
if a == 10:
    print("Welcome to Hello World")
    print("Welcome again")
print("-----End of if-----")

print("-----------------------------------")

age = 10
# and = 10

And = 10
'''
# True ==> non-zero         non None
           -5,6,4.5,-3.6    'M' [1,2] (1,) {1:1,2:2}, {1,2,3}
# False ==> 0               None
                           ''  [] () {} {}
'''

# if 10+'hello':
#     print("ERROR")
'''
Operators:
-----------
Arithmetic ops ==> add/sub/mul/div/mod/floordiv 
                                ----> VALUE ==> zero(False)/nonzero(True)

Assignment ===>  x = 10         ----> VALUE ==> zero(False)/nonzero(True)

Comparison ===> == != > < >= <= ----> True/False
Logical   ====>  and or not     ----> True/False
Membership ===>  in not in      ----> True/False
Identity   ===>  is is not      ----> True/False

Water and Coffee
------------------
True and True*   = True
True and False*  = False
False* and True   = False
False* and False  = False

Coffee or Tea:
----------------
True* or True = True
True* or False = True
False or True* = True
False or False* = False

True --> nonZero              nonNone 
         10 -10 10.4 -3.4     'Hello' [1,2,3] (1,2,3) {1:1,2:2} {1,2,3}

False --> 0                   None 
                              '' [] ()  {} set({})
if True{
print("Executed");
}
'''

x = 10  # Direct/Final/Absolute value 10
print("Value of x: ", x)
x = 10 + 20  # addition ops 30
print("Value of x: ", x)
'''
After if <condition> can be:
True              False
--------------------------------------
10,10.4,'Hello'    None '' [] () {} {}
-10,-5
Any operation which gives final result as True/False   0/non0  None/notNone


'''
x = 10 + 5
print("----------------if conditions----------------")
if x == 15:
    print("Executed successfully")
    print("Condition is True")

print("------End of if-------")

if '':
    print("Will not execute2")

if 'hello':
    print("Hello executed")

if 10 < 20:
    print("Yes.Condition is True")

if 10 > 20:
    print("No. Condition is False1")

if not 10 > 20:
    print("No. Condition is False2")

if False:
    print("No execution.")

if True:
    print("Will execute1")

if not False:
    print("Will execute")

print("--Hello World---")

if None:
    print("None exec:")
if not None:
    print("Not none value : ")

if 'Madhu':  # [1,2,3], (1,2,3), {1:1,2:2}  {1,2,3,4}
    print("Name exececuted")
if '':  # []  () {}
    print("Empty string")

if not '':
    print("Empty string occurance")

print("Arithmetic :", 10 + 20)
print("Relational :", 10 >= 20)
print("10 and 20 :", 10 and 20)  # 20 True and True --> True
print("10 and 0  :", 10 and 0)  # 0 True and False --> False
print("0 and 20 :", 0 and 20)  # 0 False and True --> False
print("0 and 0 :", 0 and 0)  # 0 False and False --> False
print("10 or 20 :", 10 or 20)
print("10 or 0 :", 10 or 0)
print("0 or 20 :", 0 or 20)
print("0 or 0 :", 0 or 0)
print("Membership :", 10 in [10, 20, 30])
# print("Identity    :", 10 is 10)

x = 20
if x == 10:
    print("X value")

'''
Arithmetic ops: +-*/ // %       ==> 0 / nonzero 
Relational ops: > >= < <= == != ==> True/False
Assignment ops:                     x = 10  x = -10.4
                                    x = 0   x = None
Logical  ops   :                ==> True/False
Bitwise       :                 ==> 0 or 1   False/True
Membership    : in not in       ==> True/False
Identity      : is is not       ==> True/False

'''

'''
1. Single condition     : 1 ==> if 


2. Multiple conditions  : 2 ==> if else
                          3 ==> if elif else            # if   else if    else 
                          4 ==> if elif elif else
                          5 ==> if elif elif elif else
                          ....

3. nested conditions    : nested if 

                            10th exam   
                            -----------
L1:            1. PASS                            2. FAIL 
L2:         1.continue     2. disc.           1. retry    2. stop 
L3:    1.Inter   2.Diploma        
L4:  1.MPC  2. BiPC
L5:        1.Govt  2.Pvt

'''
'''
SDLC Process:
-------------
S1 : REQUIREMENT : If user entered value is 20,
                   then print  "Welcome to Python World" message

S2: ANALYSIS :   Functional Analysis
                 Technical Analysis

S3: DESIGN: 
            Step1 : Take the user input
            Step2 : Compare the user(customer) provided input with given value(20)
            Step3 : If True, print the message "Welcome to Python World"

S4 : Development
S5 : Testing
S6 : Deployment/Production
'''
print("----------if---------------")
# S4: DEVELOPMENT      # Business logic implementation

val = int(input("Enter number: "))  # S1
if val == 20:  # S2
    print("Welcome to Python World")  # S3

print("--------------------------------")

# S5 : Testing
'''
        Positive scenarios  : 20  
        Negative scenarios  : 15 25 0 -5  -20 -25
'''

'''
Condition : Success ==> True  nonZero nonNone
            Failure ==> False Zero    None
 True    / False 
 Non 0   / 0  
 nonNone / None

1. Single condition : if 
'''
# arithmetic
if 10 + 20:  # 30
    print("Successfully executed 10+20")  # Indentation

if True:
    print("True condition")

if False:
    print("False condition")

if not False:
    print("Print False condition")

if True or False:
    print("OR - condition ")

if True and True:
    print("AND - condition")

if 0:
    print("Value 0")
if None:
    print("Value None")
if not 0:
    print("Value 1")
if not None:
    print("Value not None")

if 10 - 20:
    print("Addition is success")

if 10 < 20:
    print("End of the program")

if 10 < 20 or 4 < 5:
    print("YES")



