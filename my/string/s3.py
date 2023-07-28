l1=[2,3,45,6,7,1]
mn=l1[0]
mx=l1[0]
for i in l1:
    if mn>i:
        mn=i
    if mx<i:
        mx=i
print("maximum:",mx)
print("minimum:",mn)
