n=input("enter the item: ").split()
print(n)
l1=[]
l2=[]
l3=[]
for i in n:
    if i.isalpha():
        l3.append(i)
    elif i.isdigit():

        num=int(i)
        l1.append(i)
    else:
        num=float(i)
        l2.append(i)
print(l1)
print(l2)
print(l3)
