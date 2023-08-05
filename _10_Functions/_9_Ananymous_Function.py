# Lambda function or Ananymous Function

# REQ: Find Square of given value.

      # 1mark : Find square of given value 5

print("Square of value : ", 5 ** 2)

       # 2 mark : Find square of given value 5
val = 5
sq = val ** 2
print("Square of value : ", sq)

# 5 marks : Find square of given value 5

val = int(input("Enter value : "))
def find_square(num):
    res = num ** 2
    return res

out = find_square(val)
print("Square of value : ", out)

# 10 marks : Find square of given value 5

class SquareVal:
    def __init__(self, val):
        self.val = val

    def get_square(self):
        res = self.val ** 2
        return res

obj = SquareVal(5)
sq = obj.get_square()
print("Square value is : ", sq)








# OR

print("Square of value : ", find_square(val))

'''
sq_val = num * num
return sq_val
'''


'''
Syntax: Lambda arguments: expression
'''
def find_square(num):
    return num ** 2

# Lambda or Ananymous function

sq_val = lambda num: num ** 2
print("Lambda  : Square of value : ", sq_val(10))






sq_val = lambda x, y: x * y
print("Lambda  : Square of value : ", sq_val(10, 20))


# Covert to function
def sq_val(x, y):
    return x*y

print("Function : Square of value : ", sq_val(5,10))

# Use lambda functions  ==> map filter reduce
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

# 1. Lambda with map:


# lambda x: x ** 2
def get_sq(x):
    return x**2

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_list = list(map(lambda x: x ** 2, li))


print("Using map: ", final_list)


# 2. Lambda with filter:
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

def filter_list(li1):
    li2 = []
    for val in li1:
        if val % 2 == 0:
            li2.append(val)
    return li2
print("Even numbers1: ", filter_list(li))


print("Even numbers2: ", list(filter(lambda x: (x % 2 == 0), li)))

ev_list = list(filter(lambda x: (x % 2 == 0), li))
print("Even numbers3: ", ev_list)


# 3. Lambda with reduce:

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print("Reduce data ", sum)


x = 'Hello'
print("Value   : ", x)
print("Address : ", id(x))
print("Type    : ", type(x))