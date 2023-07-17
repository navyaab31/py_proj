# Take 20 integer inputs from user and print the following:
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.
l1=[]
pos_list=[]
neg_list=[]
z_list=[]
ev_list=[]
od_list=[]
n*=int(input("enter the numner in list: "))

for i in n:
    l1.append(i)
for i in l1:
    if i>0:
        pos_list.append(i)
    elif i<0:
        neg_list.append(i)
    elif i==0:
        z_list.append(i)
    elif i%2==0:
        ev_list.append(i)
    else:
        od_list.append(i)
print("positive number in the list: ",*pos_list)
print("negative number in the list: ",*neg_list)
print("zero's in the list: ",*z_list)
print("even number in the list: ",*ev_list)
print("odd number in the list: ",*od_list)

       
