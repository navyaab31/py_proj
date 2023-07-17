# multiplication

''''''

# Requirement* / Task* / Ticket* / Incident / Service Request
''' Requirement : Adding Numbers 
    =================================
        1. Count   : Only 2 numbers or more
        2. Type    : Only Positive or both Pos,Neg
        3. Datatype: Only Int. Int/Float
        4. Zero    : 0 is allowed or not 

        Scenarios:      I. Based on count
                            1. 2 numbers  (Robot)  4 + 5 = __9___
                            2. 3/4/5 numbers
                        II. Based on type
                            1. Both positive 
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number, 0 (pos/neg)
                        III. Based on datatype
                            1. Both int
                            2. Both float 
                            3. int + float 
                            4. float + int


'''
# based on count
x=2
y=3

res=x+y

print("multiplication: ",res)

# 2/3 numbers

x=3
y=2
z=6

res = x*y*z

print("multiplication: ",res)

# based on type
# both positive
x=2
y=3

res=x*y

print("multiplication: ",res)

# both negative
x=-2
y=-3

res=x*y

print("multiplication: ",res)

# first positive, second negative
x=2
y=-3

res=x*y

print("multiplication: ",res)

# first negative, second positive
x=-2
y=3

res=x*y

print("multiplication: ",res)

# both int
x=2
y=3

res=x*y

print("multiplication: ",res)

# both float
x=2.2
y=3.2

res=x*y

print("multiplication: ",res)

# int+float
x=2
y=3.2


res=x*y

print("multiplication: ",res)

# float+int
x=3.2
y=2

res=x*y

print("multiplication: ",res)