# 1.create a tuple. 
'''
t1=1,2,3
print(t1,type(t1))

# or
t1=1,
print(t1,type(t1))


# 2. create a tuple with different data types
t1=(1,"tuples",[1,2,3],{2:'two'})
print(t1)

# 3. create a tuple with numbers and print one item
t1=(1,2,3,4,5)
print(tuple(t1[0:1]))


# 4. unpack a tuple in several variables
t1=(1,2,3,4,5)
var1,var2,var3,var4,var5=t1
print(var1)


# 5. add an item in a tuple.
t1=(1,2,3,4,5)
n=int(input())
l1=list(t1)
# add item at the last
l1.append(n)
print(tuple(l1))

# add item at specified position
pos=int(input("position: "))
val=int(input("value: "))
l1.insert(pos,val)
print(tuple(l1))


# 6. convert a tuple to a string
t1=(1,2,3,4,5,6)
s1=''
for i in t1:
    s1+=str(i)
print(s1)


# 7. get the 4th element and 4th element from last of a tuple
t1=(1,2,3,4,5,6,7,8,9,1,4,5.6)
print(t1[4])
print(t1[-4])


# 8. create the colon of a tuple


# 9. find the repeated items of a tuple
t1=(1,2,3,4,5,6,7,2,3)
for i in set(t1):
    if t1.count(i)>1:
        print(i)


# 10. check whether an element exists within a tuple
t1=(1,2,3,4,5,6,7)
n=int(input())
if n in t1:
    print("yes")
else:
    print("no")

# or using for loop
for i in t1:
    if i==n:
        print("yes")
        break


# 11. convert a list to a tuple
l=[1,2,3,4,5,6]
print(tuple(l))

# 12. remove an item from a tuple
t1=(1,2,3,4,5,6,7,8,9)
n=int(input("item: "))
l1=list(t1)
print(l1)
for i in l1:
    if i ==n:
        l1.remove(i)
print(tuple(l1))

# or 
l1.remove(n)
print(tuple(l1))


# 13. slice a tuple
t1=(1,2,3,4,5,6,7)
print(t1[2:6])

# 14. find the index of an item of a tuple.
t1=(1,2,3,4,5,6,7)
n=int(input())
for i in range(len(t1)):
    if t1[i] ==n:
        print("index: ",i) 

# or 
print(t1.index(n))


# 15. find the length of a tuple
t1=(1,2,3,4,5,6)
print(len(t1))

# or
count=0
for i in t1:
    count+=1
print("length: ",count)


# 16. convert a tuple to a dictionary
t1=('python','loops','list','tuples')
d={}
for i,j in enumerate(t1,start=1):
    d[i]=j
print(d)

# or 
t2=(1,2,3,4)
d=[{i:j for i,j in zip(t2,t1)}]
print(d)


# 17.  unzip a list of tuples into individual lists.
l1=[('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
l2=[]
l3=[]
for i in l1:
    print(i)
    print(i[0])
    # for j in i:
        # print(j)
    l2.append(i[0])
    l3.append(i[1])
l2.append(l3)
print(l2)

#18. reverse a tuple.
t1=(1,2,3,4,5)
print(t1[::-1])

# or 
l1=list(t1)
l2=[]
for i in l1[::-1]:
    l2.append(i)
print(tuple(l2))


# 19. convert a list of tuples into a dictionary
"""
similar to 16
"""

# 20. print a tuple with string formatting
t1=(1,2,3)
print("tuple:{0}".format(t1))

# or
print("tuple:%s" %(t1,))



# 21.  replace last value of tuples in a list
t1=([1,2,3],[4,5,6],[7,8,9])
for i in t1:
    i[-1]=1
print(t1)

# 22.  to remove an empty tuple(s) from a list of tuples
l1=[(1,2,3),(1,5),(),(7,8,9)]
l2=[]
for i in l1:
    if len(i)!=0:
        l2.append(i)
print(l2)


# 23. sort a tuple by its float element.
l1=[('234', '9.4'), ('543', '16.9'), ('756', '5.5'), ('132', '4.2'), ('342', '7.3')]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if float(l1[i][1])>float(l1[j][1]):
            l1[i],l1[j]=l1[j],l1[i]
print(l1)


# 24.  count the elements in a list until an element is a tuple
l1=[4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
count=0
for i in l1:
    # print(type(i))
    if type(i)==tuple:
        break
    else:
        count+=1
print(count)
    
'''
    