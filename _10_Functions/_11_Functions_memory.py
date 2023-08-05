
x = 10
print("x details : ", x, id(x), type(x))


# Function memory allocation

def get_data():   # Function definition
    print("Welcome to my method")
    return "Hello World"

#1 Function Call
print("Result is : ", get_data())

#2 Function Call
result = get_data()   # Function calling
print("Result is : ", result)

# Print function name
print("Function details ", get_data, id(get_data), type(get_data))  # Get function body address
x = 10
print("X : ", x)
print("X : ", id(x))


# Mutable,Immutable :: Pass by value ,Pass by reference
# Copy : Shallow copy,Deep copy
# Lambda with map,filter,reduce functions

# Check whether number is even or odd

def check_num(val):
    print("Hello World1")
    if val % 2 == 0:
        return "Even"
    else:
        return "Odd"
    print("Hello World2")


res = check_num(23432)
print("Number is : ", res)


# STATE     : Data types/structures   Noun
# BEHAVIOR  : Functions               Verb/Adverb