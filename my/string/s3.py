"""
message = '''We can also put a lambda definition anywhere a function is expected, 
    and we don’t have to assign it to a variable at all.
        This is the simplicity of lambda functions.
                The reduce() function in Python takes in a function and a list as an argument. '''.split("\n")

# BEHAVIOR
# print(message)
l1=[]
for i in message:
#     print(i)
    s=" "
    for j in i:
        print(j)
        if j!='  ':
            s+=j

    l1.append(s)
# print(l1)
# print("".join(l1))

list1= [1,2,5,6,3,4]
if list1=="":
    print("empty list")
elif len(list1)==1:
    print("length of the list1 is more than one")
else:
    for i in range(len(list1)):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list[i]
    print(list1)
# 
list1=[1,2,5,3,7,6,8]
for i in range(len(list1)):
        print(list1[i],type(list1[i]))
        print(list1[i+1],type(list1[i+1]))
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list[i]
print(list1)
"""
# 
l1=[7,6,1,2,8,3,4]
mn=l1[0]
for i in l1:
    if mn>i:
        mn=i
print(mn)