''''''
'''
# Types 
1. Builtin / Predefined    : print() id() type()   int float str list tuple dict set
                             random math itertools datetime collections
                             
2. User defined Functions  : Programmer defined functions
'''

x = 10
'''
  x                =          10    
variable        Ass. Op.    Value
'''
print("Value of x : ", x)  # add(10,20)
'''
Function definition syntax :    def <func_name>() :    # f(x)   = 2*x*x+3*x+10
                                def sum(n1, n2):       # f(x,y) = 2x*x+3y+10   

n1,n2 are parameters not variables
'''

print("-----------Using functions--------")
# B. With Function
        # I. STATE
num1 = 10
num2 = 20
        # II. BEHAVIOR

# Function
def sum(n1, n2):       # a. Function Signature
    result = n1 + n2   # b. Function Body / Implementation
    print("Addition is : ", result)


# Function Calling/Invocation
sum(num1, num2)
sum(100, 200)



'''
from _07_DecisionMaking._2_if_else._2_Conditions import get_st_result

marks = 44
res = get_st_result(marks)
print("Student result : ", res)
'''
'''
1. Function definition:
                                def sum(n1, n2):
                                    result = n1 + n2 
                                    print("Addition is : ", result)

    -   Function signature:
                                def sum(n1, n2):

    -  Function body/implementation
                                result = n1 + n2 
                                print("Addition is : ", result)
'''