# Write a Python program to check if each number is prime in a given list of numbers. 
# Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
'''
n=[1,5,3]
flag=True
for i in range(len(n)):
    if n[i]<=1:
        flag=False
        break
    else:
        for j in range(2,n[i]):
            if n[i]%j==0:
                flag=False
                break
        flag=True
print("True" if flag==True else "Flase")


list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list=list(set(list1)-set(list2))
diff_list1=list(set(list2)-set(list1))

print(diff_list+diff_list1)
# print(diff_list1)

# 

# Write a Python program to find the index of an item in a specified list.
l1=[10,30,4,-6]
n=int(input("enter the item in specified list: "))
for i in range(len(l1)):
    if n==l1[i]:
        print("index of item is: ",i)


# Write a Python program to append a list to the second list.
l1=[1,2,3,4]
l2=["red","green","yellow"]
l1.extend(l2)
        
'''
# 