
print(100)
print(40+60)


# Student result based on marks
# Validation

'''
Function can be defined without parameters, with any no of parameters

list1 = [1,2,3,4]
list1.remove(1)      # remove expecting argument.  def remove(var):
list1.copy()         # copy - 0 arguments          def copy():
list1.insert(1, 100) # 2 arguments                 def insert(ind, val):
int x = 10
String x = get_data()
'''
list1 = [1, 2, 3]
print("Before : ", list1)
list1.insert(1, 100)  # (index,value)
print("After : ", list1)
res = list1.insert(2, 33)
print("Insertion is : ", res)
print("After : ", list1)
res = list1.pop(2)  # pop function has return type inside function
print("Pop value is :", res)
# res = list1.remove(23)
print("Remove value is :", res)


print("-----------Return type demo------------")
def get_data(eid, name, sal, address):
    print("Emp data : ", eid, name, sal, address)

# Wrong way
print("Get data : ", get_data(100, 'Madhu', 103.4, 'Bangalore'))
res = get_data(100, 'Madhu', 103.4, 'Bangalore') # NO

# Correct way
get_data(100, 'Madhu', 103.4, 'Bangalore')

print("--------Without return type--------")
def sum(n1, n2):
    result = n1 + n2  # Business Logic
    print("Addition is  :", result)  # Print it

print("SUM Operation : ", sum(10,20))  # NO
sum(10, 20)

print("--------With return type--------")
def sum(n1, n2):
    result = n1 + n2  # Business Logic
    return result     # return end value

print("SUM Operation : ", sum(10, 20))    # print(10)
print("---------------------------------")
output = sum(10, 20)                             # x = 10 print(x)
print("SUM Operation : ", output)
print("---------------------------------")


print(10)
# OR
x = 10
print("Value : ", x)


# ERRORS
# print("Get data : ", get_data(100, 'Madhu', 103.4, 'Bangalore', 'Hyd'))
# print("Get data : ", get_data(100, 'Madhu', 103.4))


# Find even numbers in a list

# STATE
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# BEHAVIOR
# getevennums()

def get_even_nums(li):
    ev_nums = []
    for each in li:
        if each % 2 == 0:
            ev_nums.append(each)
    # print("Even numbers : ", ev_nums)
    return ev_nums

result = get_even_nums(list1)
print("Even numbers1: ", result)

# OR

def get_even_nums(li):
    ev_nums = []
    for each in li:
        if each % 2 == 0:
            ev_nums.append(each)
    print("Even numbers2 : ", ev_nums)

get_even_nums(list1)

# This is not proper way
def get_even_nums(li):
    ev_nums = []
    for each in li:
        if each % 2 == 0:
            ev_nums.append(each)
    # print("Even numbers3 : ", ev_nums)
    return ev_nums

output = get_even_nums(list1)


print("---------------------------------------------------")

10
"Hello World"
10+20

# DATA : STATE: 2 actions: 1.Print it 2.Assign it
print(10)
# OR
x = 10
print("Value of x: ", x)

print(x+20)
print(x+30)

print("Addition is ", 10+20)

# OR
x = 10 + 20
print("Value is : ", x)

10  # neither giving to variable nor printing it
10+20

res = 10+3-5*4%4-4
print("Value : ", res)

# Not proper
for each in '45435FDASFSF$@#QADSfdsafasf#@$#@RFASDFDSAFDSf':
    print("Value : ", each)

# Proper
str1 = '45435FDASFSF$@#QADSfdsafasf#@$#@RFASDFDSAFDSf'
for each in str1:
    print("Value : ", each)




# Get student result based on marks.
# User Criteria : <Pending>


def find_studentresult(marks):
    pass

find_studentresult(x)


print("-----------With out return type------------")
# Adding 2 numbers
    # 1. STATE
num1 = 10
num2 = 20
    # 2. BEHAVIOR
def sum(n1, n2):
    result = n1 + n2              # 1. Implementing the business logic
    print("Addition : ", result)  # 2. Handling the end result/output

sum(10, 20)  # Correct approach

output = sum(10, 20)  # dont use as function is not returing us anyting
print("Addition is : ", output)


print("--------With Return type------------")
'''
Here sum function is taking 2 responsibilities
    1. Implementing the business logic
    2. Handling the end result/output
'''


# with return type
# I will implement business logic, and return the output
def sum(n1, n2):
    result = n1 + n2
    return result

sum(11, 22) # don't do function call like this, because it is returning us value

# 1. Return value : one time usage
print("Addition2 is  :: ", sum(25, 10))  # print(10)

# Correct approach
# Return value : Two or more places
output = sum(25, 10)              # eid = 10    print(eid)
print("Addition1 is  :: ", output)


# Dont
print("Addition operations : ", sum(25, 10) + 100)
# Do
res = sum(25, 10) + 100
print("Addition operations : ", res)

di = {'eid': 100, 'name': "Madhu"}

# Increment age of employee by 5
# di['age']  or di.get('age')

age = di.get('age', 18)
print("Employee age : ", age + 5)

if not di.get('age'):
    di['age'] = 18
    print("After validation : ", di)




print("----Return type examples----")
# Find sum of 2 numbers

def sum(n1, n2):
    result = n1 + n2
    return result   # int float bool string list tuple dict set None

sum(10,20) # Invalid statement

# one time usage
print("Sum of 2 numbers : ", sum(10, 20))

# Perfect approach
out = sum(10, 20)
print("Sum of 2 numbers : ", out)

# Find student result PASS/FAIL >= 35 PASS else FAIL

# STATE
s_marks = int(input("Enter marks : "))
# BEHAVIOR

def get_st_result(marks):
    print("---------Function start---------")
    if marks >= 35:
        return "PASS"
    else:
        return "FAIL"
    print("---------Function End---------")

result  = get_st_result(s_marks)
print("Student result : ", result)













print("-------List with return=------------")
li = [12, 32, 43, 24, 15]

print("Insertion: ", li.insert(2, 100))  #  no return type
print("Remove   : ", li.remove(24))  # no return value
print("Pop      : ", li.pop(2))  # it returns removed value


list1 = [1, 2, 3, 4, 5]
print("Before append : ", list1)
list1.append(50)  # It will append 50 to list1 and returns nothing
print("Append 100 :", list1.append(100))

app = list1.append(200)
print("Append 54 :", app)

print("After append  : ", list1)

print("-----Pop operations-------")
list1 = [1, 2, 43, 65, 23, 46, 78, 29, 83, 23, 3, 4]
print(list1.pop())  # It will remove last element and returns the element to us
print("Removed values1 is :", list1.pop())
print("LIST : ", list1)

val = list1.pop(5)
print("Values is :", val)
print(val)
print()
print("Removed value is2 : ", val)

print("Removed value is3 :", list1.remove(65))

print("Index is : ", list1.index(29))


# sort vs sorted
# sort function
li = [5, 6, 4, 7, 3, 9, 2, 1]
print("Before sorting : ", li)
li.sort()
print("After sorting  : ", li)

# sorted function
li = [5, 6, 4, 7, 3, 9, 2, 1]
li2 = sorted(li)
print("After sorting  : ", li)
print("After sorting  : ", li2)

str1 = 'hello'
str2 = str1.capitalize()
str1 = str1.capitalize()

