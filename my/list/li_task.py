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


# 18. All permutations of list elements




# 19. Difference betweeen 2 lists
l1=["abc",'xy','mno','op']
l2=['abc','xy','op']
diff=set(l1).difference(set(l2))
print(list(diff))

# or
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)

# 20. To access index of list
l1=["abc",'xy','mno','op']
n=int(input())
for i in range(len(l1)):
    if i==n:
        print(f"{i}:{l1[i]}")


# 21. List of characters into string
l1=['p','y','t','h','o','n']
print("".join(l1))

# or 
s=""
for i in l1:
    s+=i
print(s)


# 22. Finding index of an item in specified list
l1=['p','y','t','h','o','n']
n=input("enter the item: ")
for i in range(len(l1)):
    if l1[i]==n:
        print(f"{l1[i]}:{i}")


# 23. Flatten a shallow
l1=[[2,4,3],[1,5,6], [9], [7,9,0]]
l2=[]
for i in l1:
    for j in i:
        l2.append(j)
print(l2)


# 24. Append a list to second list
l1=[2,3,4,5,6]
l2=['ab','xy','mn']
for i in l2:
    l1.append(i)
print(l1)


# 25. Select an item randomly
import random
l=[10,20,30,40,50,60,20,30,50,70,90]
l=set(l)
l1=random.choice(list(l))
print(l1)

# or 
l1=random.sample(list(l),3)
print(list(l1))


# 26. Check circularly identical in two lists
l1=[10,10,0,0,10]
l2=[10,10,10,0,0]
l3=l1+l1
for i in range(len(l1)):
    z=0
    for j in range(i,i+len(l1)):
        if l2[z]==l3[j]:
            z+=1
        else:
            break
if z==len(l1):
    print("True")
else:
    print("False")
        

# 27. Finding a second smallest number
l1=[2,3,4,5,6,7,8,9]
for i in range(len(l1)-1):
    if l1[i]>l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1[1])


# 28. Finding a second largest number
l1=[4,6,2,1,8,5]
for i in range(len(l1)-1):
    if l1[i]<l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1[-2])


# 29. Get unique values
l1=[20,40,60,10,20,80,70,40,10]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# 30. Frequency of elements
l1=[1,2,5,6,8,9,7,6,4,5,3,2,1,3]
count=0
n=int(input("enter the val: "))
for i in l1:
    if i==n:
        count+=1
print(f"frequency of {n}:{count}")

# 31. Counting number elements within a specified ranges
l1=[1,2,3,4,5,6,7,8,9,2,3,4,7,8,9]
nm=input("enter the range: ").split()
n=int(nm[0])
m=int(nm[1])
print(m)
count=0
for i in range(n,m+1):
    count+=1
print("number of elements in range: ",count)


# 32. Check a list contains sublist
l1=[1,2,3,4,5,6,7,8,9]
l2=[4,5,7]
for i in range(len(l1)):
    if l1[i]==l2[0]:
        n=1
        while(n<len(l2) and l1[i+n]==l2[n]):
            n+=1
        if n==len(l2):
            print("True")
            break
else:
    print("False")

# 33.Generate all sublists

l1=[1,2,3,4,5,6]
l2=[]
for i in range(len(l1)+1):
    for j in range(i):
        l2.append(l1[j:i])
print(l2)



# 34. Printing elements in ascending order
l1=[2,5,3,7,8,1,4]
l1.sort()
print(l1)

# or 
for i in range(len(l1)-1):
    if l1[1]>l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1)


# 35. Create a list by concatenating a given list which range goes from 1 to n
r=input("enter the range: ").split()
r1=int(r[0])
r2=int(r[1])
l1=[]
for i in range(r1,r2+1):
    l1.append(i)
print(l1)


# 36. Variable unique identification number


# 37. Finding common items from two lists
l1=[1,2,3,4,5,6]
l2=[9,8,7,6,5]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

# 38. Change the position of every nth value with (n+1)th value
l1=[0,1,2,3,4,5]
for i in range(0,len(l1),2):
    l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1)

# 39. Converting multiple integers into single integer
l1=[2,3,4,5]
s=''
for i in l1:
    s+=str(i)
print(s,type(s))
s1=int(s)
print(s1,type(s1))


# 40. Split a list based on first character of word
word_list = ['be','string','have','do','done','seem','feel','leave','call','come','say']

import itertools
"""
l='aabbbfffghhyysf'
x=itertools.groupby(l)
for i,j in x:
    pass
    # print(i, list(j))

l = ['aaa', 'bbb', 'ccc', 'a', 'b', 'aa', 'bb']
x=itertools.groupby(l)
for i,j in x:
    # print(i,list(j))
    pass
print([(i,list(j)) for i,j in itertools.groupby(l,key=lambda x:x)])

l=[0,2,4,6,8]
print([(i,list(j)) for i, j in itertools.groupby(l,key=lambda x:x%2==0)]) 
"""
# print([(i ,list(j)) for i,j in itertools.groupby(sorted(word_list),key=lambda x:x[0])])
for i,j in itertools.groupby(sorted(word_list,key=lambda x:x[0])):
    print(i)
    for k in j:
        print(list(k)) 

# 41. Create multiple list




# 42. Find missing and additional values
list1 = [1, 2, 3, 4, 5, 6] 
list2 = [4, 5, 6, 7, 8] 
l1=[]
l3=[]
for i in list1:
    if i not in list2:
        l1.append(i)
print(l1)
# print(l2)
for j in list2:
    if j not in list1:
        l3.append(j)
print(l3)
print("additional value in list1:",l1)
print("missing values in list1:",l3)
print("additional value in list1:",l3)
print("missing values in list1:",l1)

# or
l1=set(list1).difference(set(list2))
print(list(l1))

l2=set(list2).difference(set(list1))
print(list(l2))

# 43. Split a list into different variables
l1=[(1,3,5),(2,4,6),(7,8,9)]
var1,var2,var3=l1
print(var1)
print(var2)
print(var3)


# 44. Generate group of five consecutive numbers in a list
l1=[]
n=int(input("enter the number: "))
for i in range(1,n+1):
    l1.append(i)
# print(l2)
# print(l1)
l2=[]
l3=[]
for j in l1:
    l2.append(j)
    if j%5==0 and j!=1:
        l3.append(l2)
        l2=[]
print(l3)

# or
l2=[] 
for i in range(5):
    l1=[]
    for j in range(1,6):
        l1.append(5*i+j)
    l2.append(l1)
print(l2)

# or 
l=[[5*i+j for j in range(1,6)] for i in range(5)]
print(l)


#45. Convert a pair of values into a sorted unique array
L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4)]
l1=[]
for i in L:
    for j in i:
        l1.append(j)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(sorted(l2)) 


# 46. Select odd items of a list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1=[]
for i in x:
    if i%2!=0:
        l1.append(i)
print(l1)

# 47. Insert an element before each element of a list
l=[1,2,3,4,5]
j=0
for i in l[::]:
    l.insert(j,'a')
    j+=2
print(l)

# or 
l1=[]
for ele in range(len(l)):
    for var in ('c',l[ele]):
        l1.append(var)
print(l1)


# 48. Print a nested lists (each list on a new line) using the print() function
l=[['red'],['yellow'],['green']]
for i in l:
    for j in i:
        print(j,sep='\n')

# or 
for i in l:
    print(*i)
    # print('\n'.join(str(i)))


# 49. Convert list to list of dictionaries
k = ['a','b','c','d','e']
v = [1,2,3,4,5]

# using zip() method
my_dict={i:j for i, j in zip(k,v)}
print(my_dict)

# using dictionary comprehension
my_dict={i:j for i in k for j in v}
print(my_dict)

# or
d={}
for i in k:
    for j in v:
        d[i]=j
print(d)

# 50. Sort a list of nested dictionaries
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
l1=[]
for i in my_list:
    print(i)
    for j,k in i.items():
        print(k)
        for key,val in k.items():
            print(val)
            l1.append(val)
print(l1)
l1.sort(reverse=True)
print(l1)
for n in l1:
    for i in my_list:
        # print(i)
        for j,k in i.items():
            # print(k)
            for key,val in k.items():
                # print(val)
                # l1.append(val)
                if n==val:
                    # print("True")


# 51. Split a list every Nth element
l1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']
n=int(input())
l2=[]
for i in range(0,len(l1),n):
    print(i)
    l2.append(l1[i:i+n])
print(l2)

'''
# 52. Compute the similarity between two lists