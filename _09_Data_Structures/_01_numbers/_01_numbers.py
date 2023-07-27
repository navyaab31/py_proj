''''''
# 01. NUMBERS:

'''
int 
float
complex : 3i+4j


          Y
         |        *
         |
---------------------------> X
         |
         |

'''

# 1.1 Integer:
print(10)
eid = 10
print(eid)   # f(x)
print("Value is :", eid)

x = 10 + 21 % 6.3 * 3
# LHS = RHS
print("Addition is : ", x, type(x))


# Naming conventions
   # variables always small letter

'''
REQUIREMENT / STORY / TICKET / INCIDENT / SERVICE REQUEST '''

# REQ: Receive employee id and print it.
'''
Step 1: Receive employee id 
Step 2: Print it
'''
     # Hard coding the value :: Static way
e_id = 4325  # emp_id empid eid e_id   st_rno strno prod_id
print("Employee id : ", e_id)

     # Receive the value dynamically
e_id = input("Enter your employee id :")    # '4500'
print("Employee id : ", e_id, type(e_id))

e_id = int(input("Enter your employee id :"))  # int('4500') --> 4500
print("Employee id : ", e_id, type(e_id))

'''
Expression in Mathematics
--------------------------
f(x) = 2x + 1. Get f(x) when x = 100
-------------  -------  ------------
BEHAVIOR         REQ       STATE 

f(10) = 2(10) + 1 = 20+1 = 21

Python function:
-----------------
def f(x):    # Function definition
    res = 2x + 1
    print("Result: ", res)
    
f(10) # Function call 
'''

print("--------------------type--------------")
print("Type of 10 :", type(10))
eid = 100
print("Employee details : ", eid, type(eid))

eid = input("Enter employee id :")
print("Employee details : ", eid, type(eid))

eid = int(input("Enter employee id :"))
print("Employee details : ", eid, type(eid))

e_sal = float(input("Enter employee salary :"))
print("Employee details : ", e_sal, type(e_sal))

eid = 100
print("Employee id and it address : ", eid, id(eid))

msg = 'Hello World'
print("Message is : ", msg, type(msg), id(msg))



