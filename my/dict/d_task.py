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
'''
# using list comprehension
my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}
l1={my_dict[k]:i for k in my_dict for i in [sorted(val for key, val in my_dict.items())] if i==my_dict[k]}
print(l1)