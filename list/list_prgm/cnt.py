# counter()  and elements()
from collections import Counter
s="geeksforgeeks"
x=Counter(s)
for i in x.elements():
    pass
    # print(i,end=" ")

l1=[3,4,5,8,5,4,8,6,8,2,3]
d={}
x=Counter(l1)
for i in x.keys():
    print(i,":",x[i])
keys=list(x.keys())
val=list(x.values())
res=dict(zip(keys,val))
print(res)

# or

res={keys[i]:val[i] for i in range(len(keys))}
print(res)

# or 

for i in keys:
    for j in val:
        d[i]=j
        val.remove(j)
        break
print(d)