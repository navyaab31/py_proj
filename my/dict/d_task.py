# 1. Prints each item and its corresponding type from the following list.
'''
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],{"class":'V', "section":'A'}]
for i in datalist:
    print("item:",i,"item type:",type(i))

# 2.To sort (ascending and descending) a dictionary by value
my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}
l=[]
for i in my_dict:
    l+=[my_dict[i]]
# print(l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
# print(l)
d={}
for i in l:
    for j in my_dict:
        if i==my_dict[j]:
            d[j]=i
print(d)

# using list comprehension
my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}
l1={my_dict[k]:i for k in my_dict for i in [sorted(val for key, val in my_dict.items())] if i==my_dict[k]}
print(l1)


# 3.Add a key to a dictionary
dict = {'key1': 'hi', 'key2': 'hello'}
dict['key3']='Good'
dict['key4']='Morning'
print(dict)

# using update method
dict.update({'key5':'python'})
print(dict)


# 4.Check if a given key already exists in a dictionary.
dict1={'a':100,'b':200,'c':300,'d':400}
key=input()
if key in dict1:
    print(key,"value:",dict1[key])


# 5.Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
n=int(input())
d1={i:i*i for i in range(1,n+1)}  
print(d1)


# 6. Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
d={i:i*i for i in range(1,16)}
print(d)

# 7. Merge two Python dictionaries
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
for i in dict2:
    dict1[i]=dict2[i]
print(dict1)

# using update
dict1.update(dict2)
print(dict1)


# 8. Sum all the items in a dictionary
dict = {'a': 100, 'b': 200, 'c': 300}
sum=0
for i in dict:
    sum+=dict[i]
print(sum)

# using values()
s=0
for i in dict.values():
    s+=i
print(s)

# 9. Multiply all the items in a dictionary
dict = {'a': 1, 'b': 2, 'c': 3}
mul=1
for i in dict:
    mul*=dict[i]
print(mul)


# 10. Map two lists into a dictionary
keys = ["Rash", "Kil", "Varsha"]
values = [1, 4, 5]
d={}
for i in keys:
    for j in values:
        d[i]=j
        values.remove(j)
        break
print(d)

# or using dictionary comprehension
d1={keys[i]:values[i] for i in range(len(keys))}
print(d1)

# or using Zip
res = dict(zip(keys, values) )
print(res)

# 11. Sort a dictionary by key
d={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
l1=[]
for i in d:
    l1+=[i]
# print(l1)
for i in range(len(l1)-1):
    if l1[i]>l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
# print(l1)
d1={}
for i in l1:
    for j in d:
        if i==j:
            d1[i]=d[j]
print(d1)


# 12.Get the maximum and minimum value in a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
l1=list(my_dict.values())
print(sorted(l1))
# print(l1[-2])
for i in my_dict:
    if my_dict[i]==l1[-2]:
        print("maximum:",my_dict[i])
    elif my_dict[i]==l1[0]:
        print("minimum:",my_dict[i])

'''
# 13. Remove duplicates from Dictionary
dict = {'hg': 10, 'is': 15, 'be': 20, 'for': 10, 'hi': 20}
d1={}
for i in dict:
    if dict[i] not in d1:
        d1[i]=dict[i]
print(d1)