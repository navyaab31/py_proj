'''
class my_list:
    def __init__(self):

        my_list=[]
    def print():
        print(my_list)
    
    def insert(val,i):
        my_list.insert(val,i)
        print(my_list)

    def remove(val):
        my_list.remove(val)
        print(my_list)

    def pop():
        my_list.pop()
        print(my_list)

    def sort():
        my_list.sort()
        print(my_list)

    def reverse():
        my_list.reverse()
        print(my_list)
li=my_list()
li.print()
# li.insert(3,0)
'''

# second largest values of the list
l1=[6,2,5,8,10,25,15]
# l2=[]
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]==l1[j],l1[i]
    print(l1)
