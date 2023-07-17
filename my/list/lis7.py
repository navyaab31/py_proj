# matrix Addition
l1=[[1,2,3],[3,4,5],[6,7,8]]
l2=[[10,20,30],[40,50,60],[70,80,90]]

l3=[]
for i in range(len(l1)):
   l4=[]
   for j in range(len(l1[i])):
      l4.append(l1[i][j]+l2[i][j])
   l3.append(l4)
print(l3)

# matric multiplication
l3=[]
for i in range(len(l1)):
   l4=[]
   for j in range(len(l1[i])):
      c=0
      for k in range(len(l2)):
         c+=(l1[i][k]*l2[k][i])
            
      l4.append(c)
   l3.append(l4)
print(l3)
   
   
   