# based on count
# 1. two numbers
x=6
y=2

res=x**y

print("Exponential: ",res)

# 2. three numbers
x=10
y=2
z=3

res=x**y**z

print("Exponential: ",res)

# based on type
# 1.both positive
x=6
y=2

res=x**y

print("Exponential: ",res)

# 2.both negative
x=-6
y=-2

res=x**y

print("Exponential:",round(res,2))


# -3

# first negative, second positive
x=-6
y=2

res=x**y

print("Exponential: ",res)
# -3

# first positive, second negative
x=6
y=-2

res=x**y

print("Exponential: ",res)
# -3

# 0,number(pos/neg)
x=0
y=-3

res=x**y

print("Exponential: ",res)
# Error