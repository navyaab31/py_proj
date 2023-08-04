# String Memory Allocation

# Python Programming
msg = "Python Programming"  # ASCII Table
    #  0 1 2 3 4 5 6 7 8 9 10 11 12 13  Indexing

'''
1. load RHS
2. Finds type, Indexing will be performed
3. Allocates main memory 
4. Loads index, and converts char to ASCII format, then to binary format 
   and allocates memory 
5. Main memory location address will be given to LHS Variable 

'''

for char in msg:
    print("Character : ", char)

print("Hello world")



# REQ: Print value 10 in console

    # Approach 1# Use the value only once
print(10)

    # Approach 2.1# Use the value in 2 or more places
x = 10  # Let us assume x = 10
print(x)
print(x+20)

    # Approach 2.2# Better version of A2
x = 10
print("Value of x : ", 10+[1,2,3])
print("Addition   : ", x+20)


str1 = 'hello world'   # ascii table  vs unicode
    #   0123456789