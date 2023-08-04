# 1. append() :: used for appending and adding the elements at the end of the list
#               list.append(val)
                    
print("------------- 1. append() -----------------")
print("used for appending and adding the elements at the ned of the list")


l1=[1,2,3,4,5]
print("Normal list         :",l1)      # l1=[1,2,3,4,5,6]
l1.append(6)            # append 6 to list
print("list after the append",l1)        # l1=[1,2,3,4,5,6]

# 2. copy() :: it returns shallow copy of list
#               list.copy()
                    
print("------------- 2.copy() -----------------")
print("it return shallow copy of list")


l1=[1,2,3,4,5]
print("Normal list         :",l1)      # l1=[1,2,3,4,5,6]
l1.copy()      # no action 
print("list after the copy",l1)        # l1=[1,2,3,4,5,6]

# Assigning to the new variable
l2=l1.copy()
print("first list after copy:",l1)            # l1=[1,2,3,4,5]
print("second list after copy:",l2)          # l1=[1,2,3,4,5]

# 3. clear() :: it removes all the items in the list
#               list.clear()

print("------------- 3.clear() -----------------")
print("it removes all the items in the list")

l1=[1,2,3,4,5]
print("Normal list         :",l1)      # l1=[1,2,3,4,5,6]
l1.clear()      
print("list after the clear",l1)        # l1=[]


# 4. count() :: it returns the count of how many times object occure in the list 
#               list.count(val)-->integer

print("------------- 4.count() -----------------")
print("it returns the count of how many times object occure in the list")

l1=[1,2,3,4,5,4,7,8,9]
print("Normal list         :",l1)      # l1=[1,2,3,4,5,4,7,8,9]
l1.count(4)      
print("list after the count",l1)        # 2

# 5. extend() :: Adds each elements of the iterables at the end of the list
#               list.extend(val)-->integer

print("------------- 5.extend() -----------------")
print("Add each elements of the iterable at the end of the list")

l1=[1,2,3,4,5,6]
print("Normal list         :",l1)      # l1=[1,2,3,4,5,6]
l1.extend("abc")      
print("list after the extend",l1)        # l1=[1,2,3,4,5,6,'a','b','c]

# 6. index() :: return the elements of the perticular index
#               list.index(inedxno.)-->items

print("------------- 6.index() -----------------")
print("Add each elements of the iterable at the end of the list")

l1=[1,2,3,4,5,6]
print("Normal list         :",l1)      # l1=[1,2,3,4,5,6]
l1.extend("abc")      
print("list after the extend",l1)        # l1=[1,2,3,4,5,6,'a','b','c]


