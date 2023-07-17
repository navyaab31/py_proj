# Write a Python program to append a list to the second list.

l1=[1,2,3,4,5]
l2=[2,3,4,6,7]

l1.extend(l2)
print(l1)


# Write a Python program to multiply all the items in a list
l1=[3,4,5,6]
mul=1
for i in l1:
    mul*=i
print("multipliactio is: ",mul)


# Write a Python program to get the largest number from a list
l1=[2,3,4,5,6,7,8]
l1.sort()
print(l1[-1])

# without using inbuilt method
mx=l1[0]
for i in l1:
    if i>mx:
        mx=i
print("largest value is: ",mx)

# 4. Write a Python program to get the smallest number from a list
l1=[2,3,4,5,6,7,8]
l1.sort()
print(l1[0])

# without using inbuilt method
mn=l1[0]
for i in l1:
    if i<mn:
        mn=i
print("largest value is: ",mn)

# 5.Write a Python program to count the number of strings where the string length is 2 or more and the 
# first and last character are same from a given list of strings
l1=["hi","hello","navya","ahga"]
for i in l1:
    # for j in i:
    #     print(j)
    if len(i)>=2 and i[0]==i[-1]:
        print(i)

# 6. Write a Python program to remove duplicates from a list
l1=[2,3,4,5,2,4,7,8]
print(list(set(l1)))


# with using the loops
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# 7. Write a Python program to check a list is empty or not
l=[1,2,3.4]
l1=[]
if len(l1)<=0:
    print("list is empty")
else:
    print("list have elemets")

    

# 8.rite a Python program to clone or copy a list
l1=[1,2,3,4]
l2=l1.copy()
print(l2)



# 9. Write a Python program to find the list of words that are longer than n from a given list of words
n=int(input("enter n: "))
l1=["navy","abcdef","xyz","pooja","hello","hi"]

for i in l1:
    if len(i)==n:
        print(i)

        

# 10. Write a Program that get two lists as input and check if they have at least one common member
n=input("enter the elements of first list: ")
list1=list(map(int,n.split()))
# print(list1)

m=input("enter the elements of second elements: ")
list2=list(map(int,m.split()))
# print(list2)
l3=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            l3.append(list2[j])
print(l3)


# 11.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# (enumerate)
l1=[2,3,4,5,6,7,8,9]
for i in range(len(l1)):
    if (i==0) or (i==4) or (i==5):
        del l1[i]
print(l1)


# 12. Write a Python program to print the numbers of a specified list after removing even numbers from it
l1=[2,3,4,5,6,7,8,9]
l2=[]
for i in l1:
    if i%2==0:
        del i
    else:
        l2.append(i)
    
print(l2)


# 13. Write a Python program to shuffle and print a specified list (shuffle)
import random
l1=[2,3,4,5,6]

random.shuffle(l1)

print(l1)


# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are
# square of numbers between 1 and 30
l1=[]
for i in range(31):
    l1.append(i*i)
print(l1[:5]+l1[-5::])



# 15. Write a Python program to generate all permutations of a list in Python. (itertools)
import itertools

l1=[2,3,4]

perm=list(itertools.permutations(l1))

print(perm)