
# permutation of list
'''
itertools.permutations()- to generate permutations of list

'''
''''
import itertools

l1=[1,2,3]

perm= list(itertools.permutations(l1))

print(perm)
'''

# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

'''
Generate successive 'r' length permutations of a list: 
given list and length as an argument to itertools.permutations() function.
 It generates the permutations of the given length.


list1=[2,3,4,5]
r=2
perm=list(itertools.permutations(list1,2))
print(perm)
'''
# [(2, 3), (2, 4), (2, 5), (3, 2), (3, 4), (3, 5), (4, 2), (4, 3), (4, 5), (5, 2), (5, 3), (5, 4)]

'''
Generate Permutations of a list:
an empty list to store all permutations of all possible length of a given list. 
extend() function is used to add items to the empty list one after the other. 
Iterating over the elements of the list using for loop, the itertools.
permutations() function finds all the possible lengths.

'''
'''
list1=[2,3,4]
l1=[]
for i in range(1,len(list1)+1):
    l1.extend(list(itertools.permutations(list1,r=i)))
print(l1)

# [(2,), (3,), (4,), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (2, 3, 4), (2, 4, 3), (3, 2, 4), (3, 4, 2), (4, 2, 3), (4, 3, 2)]

def perm(start, end=[]):
    if(len(start) == 0):
        print(end)
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], end + start[i:i+1])
            
#function call
perm([1,2,3])

# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

# You are given a string S.
# Your task is to print all possible permutations of size K of the string in lexicographic sorted order.
s,k = input().split()
print(s)
print(k)
k=int(k)
for i in sorted(list(itertools.permutations(s,k))):
    print(' '.join(i))

    
# using combinations
from itertools import combinations
s,k = input().split()
s=list(s)
s.sort()
res=[]
for i in range(1,int(k)+1):
    res=list(combinations(s,i))
    # print(res)
    for j in res:
        print(" ".join(j))

'''
# combiantion with replacement
from itertools import combinations_with_replacement
s,k=input().split()
s=sorted(list(s))
k=int(k)

comb=list(combinations_with_replacement(s,k))
for i in comb:
    print(" ".join(i))
