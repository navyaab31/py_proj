# Take 10 integer inputs from user and store them in a list. Now, 
# copy all the elements in another list but in reverse order.
'''
l1=[]
for i in range(10):
    a=int(input("enter the number: "))
    l1.append(a)
# print(l1)
l2=[]
for i in l1[::-1]:
    l2.append(i)
print(l2)
   
# Write a program to find the sum of all elements of a list.
l1=[2,3,4,5,6,7]
sum=0
product=1
for i in l1:
    sum+=i
    product*=i
print("sum is:",sum)
print("product is:",product)

# Find largest and smallest elements of a list
l1=[1,2,3,4,5,6,7,8,9]
mx,mn=0,9
for i in l1:
    if i>mx:
        mx=i
    if i<mn:
        mn=i
print("maximum: ",mx)
print("minimum: ",mn)

# Initialize and print each element in new line of a list inside list.
l1=[[2,3,4],[5,6,7]]
for i in l1:
    for j in i:
        print(j,end=" ")


# Write a program to check if elements of a list are same or not it read from front or back. E.g.-
# 2	3	15	15	3	2
a=[2,3,15,15,3,2]
mid=len(a)//2
for i in range(mid):
    if a[i]==a[len(a)-i-1]:
        print("yes")
        break
else:
    print("numbers are not same")

# Make a list by taking 10 input from user. Now delete all repeated elements of the list.
n=input("enter the 10 integer numbers: ")
l1=list(map(int,n.split()))
# with set function
print(list(set(l1)))

# without using set
i=0
while i<len(l1):
    j=i+1
    while j < len(l1):
        if l1[i]==l1[j]:
            del l1[j]
        j+=1
    i+=1
print(l1)

# take a list of 10 elements. Split it into middle and store the elements in two dfferent lists.
a=[1,2,3,4,5,6,7,8,9,2]
b=[]
c=[]
mid=len(a)//2
print(mid)
for i in range(mid):
    b.append(a[i])
print(b)
for j in range(mid,len(a)):
    c.append(a[j])
print(c)

# without using for loop
print(a[:int(len(a)/2)])
print(a[int(len(a)/2):])
'''
# Ask user to give integer inputs to make a list. Store only even values given and print the list.
# n=int(input("enter the integer number: "))
l1=[]
while True:
    n=int(input("enter the integer number: "))
    if n%2==0:
        l1.append(n)
    print(l1)


