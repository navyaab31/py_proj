
# 2. BOOLEAN:
is_active = True
print("Are you active ??", is_active, type(is_active))

x = 0
print("Normal value : ", x, type(x))
x = bool(0)
print("Boolean value : ", x, type(x))


x = 1
print("Normal value : ", x, type(x))

x = bool(1)
print("Boolean value : ", x, type(x))

x = False
print(x, type(x))

'''
if False -->  False
if None  -->  False
if 0     -->  False 
    
if True    --> True
if non None -> True
if -5      --> True

You are a good person - You are not a good person 
You are a bad person  - You are not a bad person 
'''
print("-------------Boolean----------")
# Boolean
# True nonZero non None
# False 0 None
x = 0
print("Normal val : ", x, type(x))
x = bool(0)
print("Boolean val : ", x, type(x))

y = 1
print("Normal val : ", y, type(y))
x = bool(y)
print("Boolean val : ", x, type(x))

x = 232
x = bool(232)
print("Boolean value : ", x, type(x))
