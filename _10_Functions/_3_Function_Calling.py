
# REQ : Find sum of 2 given numbers

    # 1. STATE
'''
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
'''
num1 = 10
num2 = 20
# sum(num1, num2)  # Function calling

'''
C,C++,Java,.Net
                public void sum(int n1, int n2){
                    pass
                 }
                 sum(10,20)
 
 https://www.digitalocean.com/community/tutorials/python-typing-module *
Python:
            def add(n1: int, n2: int) -> None :
                res = n1 + n2 
                print("Result is : ", res)
                
            def add(n1, n2):
                res = n1 + n2 
                print("Result is : ", res)
               

'''


def add(n1: int, n2: int) -> None:
    res = n1 + n2
    print("Addition Result is : ", res)

# add(10, "Hello")








   # 2. BEHAVIOR
def add(n1, n2):  # Parameters
    result = n1 + n2
    print("Addition : ", result)

add(10, 20)  # Arguments
add(num1, num2)
add(1 + 2, 3 + 4)

# sum(10)  ERROR
# sum(10, 20, 30)  ERROR
print("Type of sum : ", type(add))
output = add(10, 20)
print("Output is : ", output)  # None

add(5 + 5, 10 + 10)  # ==> sum(10, 20)


print(10)
x = 10
print(x)
x = 10+20+30
print(x)
print(10+20)
print(10+20+30)
print(10+30-54*5)

'''

9,10 lines : num1,num2  ==> Variables     : 10,20      ==> values
13         : n1,n2      ==> Parameters
18,19,21   :    (10,20) ==> arguments     
    
'''


