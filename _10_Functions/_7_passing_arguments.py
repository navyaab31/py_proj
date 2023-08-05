# Passing Arguments ***
'''
1. Positional Arguments (Required arguments)
2. Default Arguments
3. Keyword Arguments (Named arguments)
'''
x = 10    # int x = 10

list1 = [1, 2, 3, 4, 5]
list1.append(100)  # int float boolean string list tuple dictionary set
# list1.append()  # ERROR
# list1.append(10, 20)  # ERROR
# list1.insert(2, 23, 100)  # ERROR
print("After insertion: ", list1)

val1 = list1.pop()
val2 = list1.pop(2)


# list1.append()  list1.remove(100) list1.pop(3)
# Find sum of 3 numbers
# Find division of 2 numbers : def divide(n1,n2):

# 1. Positional Arguments (Required arguments)
print("--------1. Positional Arguments--------------")
# int x = 10;
# def sum(int n1, int n2, int n3):
# def sum(int n1, String n2, List n3):

def sum(n1, n2, n3):
    print("In sum method : with vals :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20, 30)
# sum(10, 20)            # TypeError: sum() missing 1 required positional argument: 'n3'3#
# sum(10, 20, 30, 40)    # TypeError: sum() takes 3 positional arguments but 4 were given

list1 = [1, 2, 3, 4, 4, 6, 6]
list1.pop()
list1.pop(3)

x = 10
x = 20

'''
While calling function we dont have clarity regarding data 
Solution1: def sum(n1:int, n2:float, n3:str): 
Solution2: Default arguments


'''



# 2. Default Arguments

print("--------2. Default Arguments-------------")
list1 = [11, 22, 33, 46, 53, 62, 71]
'''
def pop(ind = -1):
    return val
'''
val = list1.pop()
val = list1.pop(3)



def sum(n1, n2, n3 = 1000):   # int float bool str  list tuple dict set
    res = n1 + n2 + n3
    print("Sum is : ", res)

# sum(10)        # # sum() missing 1 required positional argument: 'n2'
sum(10, 20)      # n3 = 1000
sum(10, 20, 30)  # n3 = 1000 will be overriden with 30
# sum(10, 20, 30, 40)  # Additional argument

list1 = [10, 32, 43, 32, 63, 32, 13, 56]
list1.pop(3)
list1.pop()   # def pop(ind = -1):
                   # body
'''
Function Overloading***:   
------------------------
When a function can be called in minimum 2 or more ways
 (based on number of arguments), then it is called as Function Overloading***. 

'''
def sum(n1, n2=500, n3=1000):
    res = n1 + n2 + n3
    print("Result : ", res)

# sum()
sum(10)
sum(150, 250)
sum(150, 250, 350)
# print("Zero argument    :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
#print("Extra arguments  :",sum(10,20,30,40))

def sum(n1 = 100, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res


print("Zero argument    :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
n2 = 2
print("Three argument   :", sum(10, n2, n3=30))

print("Two arguments    :", sum(n1=10, n3=30))  # keyword arguments
print("Two arguments    :", sum(n3=30))         # keyword arguments


'''
def sum(n1=2000, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)
'''

'''
-----------------------------------------------------------------------
|                     Feedback:                                        |
|                    ==============                                    |
|    Enter rating*: 1--2--3--4--5--6--7--8--9--|10|                     |
|    Enter comments: _______________                                   |
|                Submit                                                |
-----------------------------------------------------------------------
    
    def feedback(rating = 10, comments = None):
        print(rating, comments)
    
Feedback: 4 Ways          Rating: 10  Comments: <>   1---2----3----------10
------------------
1. Directly Submit                                 : 10, None
2. Change Rating      Rating:3                     : 3, None
3. Comments           Comments='Good'              : 10, 'Good'
4. Rating,Comments    Rating:5, Comments='Average' : 5, 'Average'
'''
def feedback(rating=10, comments=None):
    print(rating, comments)

print("Feedback : ", feedback())            # directly submitting
print("Feedback : ", feedback(6))           # changed rating
# print("Feedback : ", feedback('Very Good'))
print("Feedback : ", feedback(comments='Good'))
print("Feedback : ", feedback(4, 'Bad'))
print("Feedback : ", feedback(comments="Bad", rating=1))

# print("Feedback : ", feedback("Good", 5)) it will work but no meaning



# insert into employee values(100,'Madhu',3000)
# insert into employee(eid, sal, ename ) values(100,3000, 'Madhu')

# 3. Keyword Arguments (Named argument)
print("--------3. Keyword Arguments-------------")

# Usecase 1 : For code readability while calling function
# Usecase 2 : If we don't want to maintain order while passing arguments
# Usecase3 : If we want to pass argument only for specific parameter


# Usecase 1 : For code readability while calling function

def get_order_info(mobile, ref_no, order_no, quantity, price):
    print("Order details :")
    print(order_no, ref_no, quantity, price, mobile)

get_order_info(8975435643, 9865432132, 1234, 40, 65876)

get_order_info(mobile=8975435643,
               ref_no=9865432132,
               order_no=123,
               quantity=40,
               price=65876
               )

# Usecase 2 : If we don't want to maintain order while passing arguments

def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum1 is : ", res)

sum(10, 20, 30)           # 1.Positional/Required
sum(n1=10, n2=20, n3=30)  # UC1: code readability
sum(n3=20, n1=30, n2=10)  # UC2: don't want to maintain order

# Usecase3 : If we want to pass argument only for specific parameter
#  1 2 3 4 5


def feedback(rating=10, comments=None):
    print(rating, comments)

print("Feedback : ", feedback())
print("Feedback : ", feedback(7))
print("Feedback : ", feedback(comments='Good'))  # Keyword Arguments
print("Feedback : ", feedback(1, "Bad"))
print("Feedback : ", feedback(rating=1, comments="Bad"))
print("Feedback : ", feedback(comments="Bad", rating=1))



list1 = [1, 2, 3, 4]

list1.pop()             # def pop(index = -1):
list1.pop(2)
print(list1)

def append(n1,n2):
    print("Appending to list", n1+n2)

print("Append : ", append(10,20))



def get_order_info(mobile: int, ref_no: int, order_no: int, quantity: int, price:float):
    print("Order details :")
    print(order_no, ref_no, quantity, price, mobile)

get_order_info()
