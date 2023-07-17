# find the second largest number
'''
l1=[10,30,50,20,40]

for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)

# 
temp=0
for i in range(len(l1)):
    for j in range(i,len(l1)):
        if l1[i]>l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print(l1)


# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list. 

l = []
lis = []
N = int(input())
for _ in range(N): 
  
    n = input().split(' ')
    l.append(n)
print(l)

for i in range(len(l)):
    if l[i][0]=="append":
        lis.append(l[i][1])
    elif l[i][0]=="insert":
        lis.insert(int(l[i][1]),int(l[i][2]))
    elif l[i][0]=="remove":
        lis.remove(l[i][1])
    elif l[i][0]=="print":
        print(lis)
    elif l[i][0]=="sort":
        lis.sort(lis)
    elif l[i][0]=="reverse":
        lis.sort(lis)
    elif l[i][0]=="pop":
        lis.pop()


#  Python program to find all the Combinations in the list with the given condition
l1=['orange', 'red', 'green', 'blue']
l2=[]
for i in range(len(l1)):
    print(l1[i])
    l2.append(l1[i])


#  Python program to remove all the occurrences of an element from a list
l1=[2,3,4,5,6,2,4,7,1,3]

item=int(input("enter the item to remove: "))
l2=[]
for i in range(len(l1)):
    if l1[i]!=item:
        l2.append(l1[i])
print(l1)
print(l2)

'''
#  Python Program to Remove Consecutive K element records
l1= [(1,2),(2,2),(1,3),(2,4),(4,5)]
for i in range(len(l1)):
    print(l1[i])
    for j in range(len(l1)):
        if l1[i][j]==