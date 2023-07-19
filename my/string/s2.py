'''
#1. Length of string
s="Hello World!"
count=0
for i in s:
    count+=1
print(count)

# 2.Count characters in string
s="Hello World!"
count=0
for i in s:
    if "A"<=i<="Z":
        count+=1
    elif "a"<=i<="z":
        count+=1
print(count)

# 3.String slicing
s="Hello World!"
print(s[::-1])
for i in s[::-1]:
    print(i,end="")


# 4.Replace first occurance character
s="Hello World!"
for i in range(len(s)):
    if s[i]=='l':
        print(s[:i:]+"a"+s[i+1::])
        break
# using built-in methods
# s1=s.replace('l','a',1)
print(s.replace('l','a',1))


# 5.Swapping chars in string
s="Hello World!".split()
print(s)
# j=0
for i in s:
    l1=list(i)
    for j in range(len(l1)):
        print(l1[j])
        if l1[j]=='e':
            l1[j]='l'
# print(s)


# 6.Append chars to string at end
s="hello"
s1='hi'
s2=s+ " " +s1
print(s2)


# 7.Substring replacement
sub="ijk"
s=input("enter the string: ")
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2]=="ijk":
        print(s[:i:]+"abc"+s[i+3::])
# print(s)

# 8.Length of longest string in python
s=input().split()
d={}
for i in s:
    # print(i)
    count=0
    
    for j in i:
        count+=1
    d[i]=count
# print(d)
mx=max(d.values())
# print(min)
# for i in d:
for i in d:
    if d[i]==mx:
        print(f"{i} {d[i]}")

# 9. nth index character from string
n=int(input())
s="statements control loop decisionmaking datatypes"
for i in range(len(s)):
    if n==i:
        print(s[i])
    
# 10.First last chars swapping
s="statements control loop decisionmaking datatype"
print(s[-1]+s[1:-1:]+s[0])

# 11.Remove odd index values
s="hello world"
s1=''
for i in range(len(s)):
    if i%2==0:
        s1+=s[i]
print(s1)

# 12.Count words in a string
s="statements control loop decisionmaking datatype".split()
print(len(s))

# or 
count=0
for i in s:
    count+=1
print("length of the string is:",count)


# 13.Upper lower case of a string
s="Hello World"
# print(s.upper())

# print(s.lower())

# print(s.swapcase())

# or without using built in function
s1=[]
for i in range(len(s)):
    if "A"<=s[i]<="Z":
        s1.append(chr(ord(s[i])+32))
    elif "a"<=s[i]<="z":
        s1.append(chr(ord(s[i])-32))
    else:
        s1.append(s[i])
print("".join(s1))


# 14.Sort unique words alphanumerically
s=input()

l1=[]
s1=[]
for i in list(s):

    if i.isdigit():
        j=int(i)
        # print(type(j))
        if isinstance(j,int):
            l1.append(str(j))
            # print(l1)
    else:
        s1.append(i)
l1.sort()
s1.sort()
# print(l1)
# print(s1)
print("".join(l1+s1))
# print(s)

# 15.Create html from string



# 16. Insert string in middle of speical chars
s=input()
insert_str=input("insert string:")
for i in range(len(s)):
    if 32<=ord(s[i])<=47 and 32<=ord(s[i+1])<=47:
        print(s[:i:]+s[i]+insert_str+s[i+1]+s[i+2::])
# print(s)

# 17. 4 Copies of last 2 chars
s=input("enter the string: ")
s1=s[-2::]
print(s1*4)


# 18. Length of first 3 Words or last 3 words 
s="We can use Python loops and conditional statements to generate HTML content.".split()
print(s[0])
d={}
for i in s[:3:]:
    count=0
    for j in i:
        count+=1
    d[i]=count
print(d)

# 19. Last part of string
s="We can use Python loops and conditional statements to generate HTML".split()
print(s[-1])

# 20.  reverses a string if it's length is a multiple of 4
s="We can use Python.. loops and conditional statements".split()
d={}
for i in s:
    count=0
    for j in i:
        count+=1
    d[i]=count
# print(d)
l1=[]
for i in d:
    if d[i]%4==0:
        print(i[::-1])


# 21. Convert a given string to all uppercase
s=input("enter the string: ")
s1=""
for i in range(len(s)):
    if "a"<=s[i]<="z":
        s1+=chr(ord(s[i])-32)
    else:
        s1+=s[i]
print(s1)



# 22. program to sort a string lexicographically
s="Coders loves the algorithms".split()
print(s)
for i in range(len(s)):
    # print(s[i][0])
    for j in range(i+1,len(s)):
        # print(s[j][0])
        if s[i][0]>s[j][0]:
            s[i],s[j]=s[j],s[i]
print("\n".join(s))

# or
s=intpt().split()
sorted(s)
print("\n".join(s))

 
# 23. program to remove a newline in Python
s="hello python program \nhow are you"
print("\n".join(s.splitlines()))

# or
s1=""
for i in s:
    if i=="\n":
        continue
    s1+=i
print(s1)

# 24. program to check whether a string starts with specified characters
s="Remove spaces at the beginning and at the end of the string".split()
spc_char=input("enter the specific character to remove: ")
for i in s:
    # print(i)
    if i[0]==spc_char:
        print(i)
   
# 25. program to create a Caesar encryption
s="hello"
s1=""
for i in s:
    s1+=chr(ord(i)+3)
print(s1)


#26. display formatted text (width=50) as output
s="Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java."  
l1=[]
count=0
s1=''
for i in range(len(s)):
    
    s1+=s[i]
    # print(s1)
    count+=1
    if count%50==0:
        l1.append(s1)
        # print(l1)
        s1=''
# print(l1)
print("\n".join(l1))

# or 
import textwrap

print(textwrap.fill(s,width=50))
        
'''
# 27. remove existing indentation from all of the lines in a given text


# 28. to add a prefix text to all of the lines in a string
import textwrap


