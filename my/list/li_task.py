#1. Sum of elements
'''
l1=[2,4,6,8,3,5,7]
sum=0
for i in l1:
    sum+=i
print(sum)


#2.Mulitply of elements
l1=[2,4,6,8,3,5,7]
mul=1
for i in l1:
    mul*=i
print(mul)


# 3. Largest number from list
l1=[2,4,6,8,3,5,7]
l1.sort()
print(l1[-1])

# or
for i in range(len(l1)-1):
    if l1[i]>l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1[-1])


# 4. Smallest number from list
l1=[2,4,6,8,3,5,7]
l1.sort()
print(l1[0])

# or
for i in range(len(l1)-1):
    if l1[i]>l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1[0])

# 5. Count no of strings whose length is 2
l1=['ab','xyz','mn','pqr','asdf']
count=0
for i in l1:
    if len(i)==2:
        count+=1
print(f"no of strings whose length is 2:{count}")


# 6. Sort elements in increasing order
l1=[2,4,6,8,3,5,7]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)


# 7.Remove duplicates
l1=[2,3,4,5,6,7,2,4,8,9]
l2=[]
for i in l1:
    # print(i)
    if i not in l2:
        # print(i)
        l2.append(i)
print(l2)


# 8. Check list is empty or not
l=[]
if len(l)==0:
    print("empty list")
else:
    print("not an empty list")

# 9. Clone or copy
l=[2,4,6,8,1,3,5]
l1=l.copy()
print(l1)

# or 
l1=l
print(l1)


# 10. Words that are longer than any element
l1=['python','list','string','loops','tuples']
d={}
for i in l1:
    d[i]=len(i)
print(d)
l1=[]
for i in d:
    l1.append(d[i])
l1.sort()
for i in d:
    if d[i]==l1[-1]:
        print(f"{i}:{d[i]}")


# 11. Find common element from 2 lists
l1=[1,2,3,4,5,6]
l2=[9,8,7,6,5]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(j)
print(l3)


# 12. Remove specified index from list and print
l1=[1,2,3,4,5,6]
l2=[]
n=int(input("enter the specified index: "))
for i in range(len(l1)):
    if i==n:
        l1.pop(i)
    # if i!=n:
    #   l2.append(i)
print(l1)


# 13.Write 3D array




# 14. Remove even elements and print list
l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    if i%2!=0:
        l2.append(i)
print(l2)


# 15. Shuffle list and print
import random
l1=[1,2,3,4,5,6]
random.shuffle(l1)
print(l1)
 

# 16. First,Last elements whose square value is between 1 and 30
l1=[]
for i in range(1,31):
    l1.append(i*i)
print(l1[0]+l1[-1])


# 17. First,Last elements whose square value is between 1 and 30,except first 5
l1=[]
for i in range(1,31):
    l1.append(i*i)
print(l1[6:7:]+l1[-1::])

'''
# 18. All permutations of list elements




# 19. Difference betweeen 2 lists
l1=["abc",'xy','mno','op']
l2=['']
