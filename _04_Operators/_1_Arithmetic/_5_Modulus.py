# modules
# based on count
# 1. two numbers
x=6
y=3

res=x%y

print("modulus:",res)

# 2. three numbers
x=10
y=3
z=2

res=x%y

print("modulus:",res)

# based on type
# both positive
x=6
y=3

res=x%y

print("modulus:",res)

# both negative
x=-6
y=-4

res=x%y

print("modulus:",res)
# -2

# first postive, second negative
x=6
y=-4

res=x%y

print("modulus:",res)
# -2

# first negative, second positive
x=-7
y=3

res=x%y

print("modulus:",res)
# -1

# 0, number(pos/neg)
x=0
y=3

res=x%y

print("modulus:",res)
# 0

# number(pos/neg), 0
x=6
y=0

res=x%y

print("modulus:",res)
# zerodivisionerror: integer modulo by zero