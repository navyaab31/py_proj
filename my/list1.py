90#  If there are multiple students, order their names alphabetically and print each one on a new line.
n=int(input("enter the number os student: "))
# name=input("enter the name of the student: ")
# score=int(input("enter the score: "))
l1=[]
l2=[]
for i in range(n):
    name=input("enter the name of the student: ")
    score=int(input("enter the score: "))
    l1.append(name)
    l1.append(score)
    l2.append(l1)
    l1=[]
    # print(l2)
# print(l2)
# list1=sorted([i[1] for i in l2])
list1=sorted(l2, key=lambda x:x[1], reverse=True)
v1=list1[1][1]
name_list=[]
for i in list1:
    if v1==i[1]:
        name_list.append(i[0])
name_list=sorted(name_list)
for i in name_list:
    print(i)

