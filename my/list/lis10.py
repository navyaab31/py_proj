# . Write a python program to check whether two lists are circularly identical
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print((" ".join(map(str,list2))) in (" ".join(map(str,list1*2))))

print((" ".join(map(str,list3))) in (" ".join(map(str,list1*1))))

# without using map function:
def circularly_identical(list1,list2):

    list3=list1*2
    for i in range(len(list1)):
        z=0
        for j in range(i,i+len(list1)):
            if list2[z]==list3[j]:
                z+=1
    
        if z==len(list1):
            return True
    return False

list1=[10,10,0,0,10]
list2=[10,10,10,0,0]
list3=[1,10,10,0,0]

print("compare list1 and list2")
if (circularly_identical(list1,list2)):
    print("identical")
else:
    print("not identical")

print("compare list1 and list3")


if (circularly_identical(list1,list3)):
    print("identical")
else:
    print("not identical")


# . Write a Python program to find the second smallest number in a list and second largest in the list.
l1=[2,3,4,5,6,7,8]
l1.sort()
print("second largest: ",l1[-2])
print("second smallest: ",l1[1])



# Write a Python program to get unique values from a list
my_list = [10, 20, 30, 40, 20, 50, 60, 40]

my_list=set(my_list)

print("unique elements of the list:",list(my_list))


# program to get the frequency of the elements in a list.
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
n=int(input("enter the element: "))
print(my_list.count(n))


# Create a list by concatenating a given list which range goes from 1 to n
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
n=int(input("entre the index value: "))
l1=[]
for i in range(n):
    l1.append(my_list[i])

print(l1)


#  Python program to find common items from two lists
l1=[2,3,4,5,6]
l2=[4,7,8,9,1]
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l3.append(l2[j])
print(l3)


#  Python program to split a list based on first character of word.
from itertools import groupby
a = ["cat","dog","cow","tiger","lion","Fox","Shark","Snake","turtle","mouse","monkey","bear"]
for letters, words in groupby(sorted(a),key=lambda x:x[0]):
    print(letters)
    for i in words:
        print(i)


# Python program to select the odd number of a list.
l=[2,3,4,5,6,7,8,9]
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print(l1)



#  Python Program to count unique values inside a list
l1=[2,3,4,5,2,4,6,7,8,7]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(len(l2))


# Python Program to List product excluding duplicates
l1=[1,2,3,4,5,2,4,6,4]
l2=[]
for i in set(l1):
        l2.append(i*i)
print(l2)


#  Python Program to Extract elements with Frequency greater than K
l1=[2,3,4,2,3,4,2,5,6,5,7,8,9]
k=int(input())
l2=[]
for i in l1:
    if l1.count(i)>=k+1 and i not in l2:
        # print(i)
        l2.append(i)
print(l2)
        # print(i)


# Python Program to Test if List contains elements in Range
l1=[2,3,4,5,6]
l2=[]
n=int(input())
for i in l1:
    if i<=n:
        l2.append(i)
print(l2)


# a Python program to check if the list contains three consecutive common numbers in Python
l1=[2,3,4,5,6,2,8,9]

for i in range(len(l1)-2):
    if l1[i]==l1[i+1]==l1[i+2]:
        print("list contains three consecutive numbers")
        break
else:
    print("no consecurive elements")



#  Python program to find the Strongest Neighbour
l1=[2,3,4,5,6,2,1]
l2=[]
for i in range(len(l1)):
    r=max(l1[i],l1[i-1])
    l2.append(r)
print(l2)

