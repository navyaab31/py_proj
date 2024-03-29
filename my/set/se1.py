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

# 2.
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

# 3.Output the total number of distinct country stamps on a single line.
# Sample Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
n=int(input())
s=set()
print(type(s))
for i in range(n):
    country=input()
    s.add(country)
print(len(s))

# 4.Print the sum of the elements of set  on a single line.
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
n=int(input())
s=set(map(int,input().split()))
print(s)
m=int(input())

for i in range(m):
    cmd=input().split()
    if cmd[0]=="pop":
        s.pop()
    elif cmd[0]=="remove":
        s.remove(int(cmd[1]))
    elif cmd[0]=="discard":
        s.discard(int(cmd[1]))
print(sum(s))

# Output the total number of students who have at least one subscription.
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

n=int(input())
m=set(map(int,input().split()))
a=int(input())
b=set(map(int,input().split()))

s=m.union(b)
print(len(s))
    
# Output the total number of students who have subscriptions to both English and French newspapers.
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8    
n=int(input())
m=set(map(int,input().split()))
a=int(input())
b=set(map(int,input().split()))

s=m.intersection(b)
print(len(s))

# subset
t=int(input())
for i in range(t):
    n=int(input())
    a=set(map(int,input().split()))
    m=int(input())
    b=set(map(int,input().split()))
    print(a.issubset(b))


# Print True if set  is a strict superset of all other  sets. Otherwise, print False.
# Sample Input 0
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
n=set(map(int,input().split()))
m=int(input())
for i in m:
    a=set(map(int,input().split()))
    

# Output the sum of elements in set .
# Sample Input
# 16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66
n=int(input())
A=set(map(int,input().split()))
m=int(input())
for i in range(m):
    cmd,length=input().split()
    set1=set(map(int,input().split()))
    if cmd=='intersection_update':
        A.intersection_update(set1)
    elif cmd=='symmetric_difference_update':
        A.symmetric_difference_update(set1)
    elif cmd=='update':
        A.update(set1)
    elif cmd== 'difference_update':
        A.difference_update(set1)
print(sum(A))

# 
k=int(input())
list1=input().split()
# s1=set(list)
for i in list1:
    if list1.count(i)==1:
        print(i)

'''
# sample input:
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12 
# False
a=set(map(int,input().split()))
n=int(input())
count=0
for i in range(n):
    set1=set(map(int,input().split()))
    if set1.issubset(a):
        count+=1
    # else:
    #     flag = False
if count==n:
    print("True")
else:
    print("False")
