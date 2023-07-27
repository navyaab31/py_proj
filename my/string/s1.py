# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
'''
line=input("enter the text: ")
a=line.split()
a='-'.join(a)
print(a)


# Sample Input 0
# Ross
# Taylor
# Sample Output 0
# Hello Ross Taylor! You just delved into python

first=input("enter first name:")
second=input("enter the second name: ")
print("hello "+first+" "+second+ "!....")

# Read a given string, change 
# the character at a given index and then print the modified string.
str=input("enter the string: ")
i,c=input().split()
l=list(str)
l[int(i)]=c
str=''.join(l)
print(str)

string= "ABCDCCC"
sub_string = "CC"
count=0
count1=0
# len_sub=len(sub_string)
for i in range(len(string)-1):
    match=True
    if sub_string[0]==string[i]:
        for j in range(len(sub_string)):
            print(string[i+j])
            if sub_string[j]!=string[i+j]:
                match=False
                break
            else:
                count+=1
               
                if match==True and count==len(sub_string):
                    count1+=1
print("no. of occrence is: ",count1)


string= "TestCaseTestCase"
sub_string = "CaseT"
count=0
count1=0
for i in range(len(string)-2):
    if sub_string[0]==string[i]:
        j=0
        count=0
        for j in range(len(sub_string)):
            if i+j<len(string)  and sub_string[j]==string[i+j]:
                count+=1
                # print(count)
                if count==len(sub_string):
                    count1+=1
            else:
                break
        # if count==len(sub_string):
        #     count1+=1
print(count1)


# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, 
# alphabetical characters, digits, lowercase and uppercase characters.
s = input()
alnum=False
alpha=False
digit=False
upper=False
lower=False
for i in s:
    if i.isalnum():
        alnum=True
    if i.isalpha():
        alpha=True
    if i.isdigit():
        digit=True
    if i.isupper():
        upper=True
    if i.islower():
        lower=True
print(alnum)
print(alpha)
print(digit)
print(upper)
print(lower)

# textwrap:
# wrap()
# fill()
# shorten()
import textwrap

string=input("enter the text: ")
my_wrap=textwrap.TextWrapper(width=4)
wrap_list=my_wrap.wrap(text=string)
for line in wrap_list:
    print(line)

wrap_text=textwrap.fill(string,width=4)
print(wrap_text)

# text=textwrap.shorten(text=string,width=4)
# print(text)


n=int(input())
l1=[]
l2=[]
l3=[]
for i in range(1,n+1):
    oct=0
    p=0
    while i>0:
        rem=i%8
        oct=rem*10**p+oct
        i//=8
        p+=1
    l1.append(oct)
for j in range(1,n+1):
    bin=0
    p=0
    while j>0:
        rem=j%2
        # print(rem)
        bin=rem*10**p+bin
        # print(bin)
        j//=2
        p+=1
    l2.append(bin)

    # l3.append(bin)
for k in range(1,n+1):
    hex=""
    p=0
    while k>0:
        rem=k%16
        if rem>9:
            rem=(chr(rem+55))
        rem=str(rem)
        hex+=rem
        k//=16
        # P+=1
    l3.append(hex)
# print(*l1,sep="\n")
# print(*l2,sep="\n")
sp=" "*4
res = "\n".join("{} {} {} {} {}".format(x,sp, y, sp, z ) for x, y, z in zip(l1, l2, l3))
print(res)


# 

x = int(input())
k = int(input())
p=x**3 + x**2 +x**1
if p==k:
    print("True")
else:
    print("False")

# 
var=input()
if "print" in var:
    eval(var)
else:
    print(eval(var))


# 
nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())
# print(arr)
l1=[]
for i in arr:
    l1.append(i[k])
l1.sort()
# print(l1)
l2=[]
for i in l1:
    l3=[]
    for j in arr:
        if i==j[1]:
            l3.append(j[0])
            l3.append(j[1])
            l3.append(j[2])
    # print(l3)
    l2.append(l3)
            
print(*l2)
for i in range(len(l2)):
    print(l2[i][0],end=" ")
    print(l2[i][1],end=" ")
    print(l2[i][2],end=" ")
    print()

# patern
thickness=5
c='H'
for i in range(thickness):
    for j in range(thickness+i):
        if i+j>=thickness-1:
            print(c,end=" ")
        else:
            print("-",end=" ")
    print()
for i in range(thickness+1):
    for j in range(thickness+20):
        if 2<=j<=6 or 18<=j<=22:
            print(c,end=" ")
        else:
            print("-",end=" ")
    print()
for i in range(thickness-2):
    for j in range(thickness+20):
        if j>=2:
            print(c,end=" ")
        else:
            print("-",end=" ")
    print()
for i in range(thickness+1):
    for j in range(thickness+20):
        if 2<=j<=6 or 18<=j<=22:
            print(c,end=" ")
        else:
            print("-",end=" ")
    print()

for i in range(thickness):
    for j in range(thickness+20):
        if j-i>=16 and j+i<=24:
            print(c,end=" ")
        else:
            print(" ",end=" ")
    print()

'''
# pattren
n = int(input("enter the rows: "))
print(type(n))
m = 3*n
print(type(m))
for i in range(1,n//2):
    for j in range(m):
        print("-" * (m//(n*i)))
    print()
