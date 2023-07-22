l1=[3,4,5,8,5,4,8,6,8,2,3]
d={}
for i in l1:
    count=0
    for j in l1:
        if i==j:
            count+=1
    d[i]=count
print(d)
l1=[]
for i in d:
    l1.append(d[i])
l1.sort()
l1.reverse()
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
l3=[]
for j in range(len(l2)):
    for i in d:
        if d[i] == l2[j]:
            # l3=[]
            for k in range(d[i]):
                l3.append(i)
                
print(l3)

# [8, 8, 8, 3, 3, 4, 4, 5, 5, 6, 2]