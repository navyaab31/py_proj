'''
# Output the symmetric difference integers in ascending order, one per line.
# Sample Input
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
m=int(input())
a=set(map(int,input().split()))

n=int(input())
b=set(map(int,input().split()))

x=a.symmetric_difference(b)

for i in x:
    print(i)
'''
n,m=map(int,input().split())
arr=set(input().split)
a=set(input().split())
b=set(input().split())
x=0
for i in arr:
    if i in a:
        x+=1
    elif i in b:
        x-=1
    else:
        continue
print(x)
