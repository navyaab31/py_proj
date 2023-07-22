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
print(s)
l1=[]
for i in s:
    l1.append(i)
print(l1)
insert_str=input("insert string:")
for i in range(len(l1)):
    if 32<=ord(l1[i])<=47 and 32<=ord(l1[i+1])<=47:
        l1.insert(i+1,insert_str)
print("".join(l1))

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
        

# 27. remove existing indentation from all of the lines in a given text
import textwrap
s="""
    Python is a widely used high-level, general-purpose,
    interpreted, dynamic programming language. 
    Its design philosophy emphasizes code"""

print(s)
s1=textwrap.dedent(s)
print(s1)

# 28. to add a prefix text to all of the lines in a string
sample_text ='''
# Python is a widely used high-level, general-purpose, interpreted, dynamic
# programming language. Its design philosophy emphasizes code readability,
# and its syntax allows programmers to express concepts in fewer lines of
# code than possible in languages such as C++ or Java.
'''
import textwrap

text_line=textwrap.fill(sample_text,initial_indent='>',subsequent_indent=">",width=50)
print(text_line)




# 29. to set the indentation of the first line
sample_text ='''
# Python is a widely used high-level, general-purpose, interpreted, dynamic
# programming language. Its design philosophy emphasizes code readability,
# and its syntax allows programmers to express concepts in fewer lines of
# code than possible in languages such as C++ or Java.
'''
import textwrap

text_line=textwrap.fill(sample_text,initial_indent='',subsequent_indent=" "*4,width=50)
print(text_line)



# 30. to print the following floating numbers upto 2 decimal places
x = 3.1415926
y = -12.9999
print(round(x,2))
print(round(y,2))
print("{:.2f}".format(x))
print("{:.2f}".format(y))


# 31.print the following floating numbers upto 2 decimal places with a sign
x = 3.1415926
y = -12.9999
print("{:+.2f}".format(x))
print("{:.2f}".format(y))

# 32. print the following floating numbers with no decimal places
x = 3.1415926
y = -12.9999
print("{:.0f}".format(x))
print(round(y))


# 33. print the following integers with zeros on the left of specified width
x=5
print(str(x).ljust(10,"0"))

# without using inbuilt
print(str(x)+"0"*10)


# 34. print the following integers with '*' on the right of specified width
x=5
print(str(x).rjust(10,"0"))

# without using inbuilt
print("0"*10+str(x))


# 35. to display a number with a comma separator
x = 3000000
y = 30000000
print("{:,}".format(x))
print(f"{y:,}")


# 36. to format a number with a percentage
# num=0.33
num=2/3

print("percentage of a number is:","{:.2%}".format(num))




# 37. to display a number in left, right and center aligned of width 10
x=10
print(str(x).ljust(10," "))
print(str(x).rjust(10," "))
print(str(x).center(10))

# 38. to count occurrences of a substring in a string
s="python is easy to learn hi python how are you"
sub_str="python"
print(s.count(sub_str))

# or 
s="python is easy to learn hi python how are you".split()
sub_str="python"
count=0
for i in s:
    if i==sub_str:
        count+=1
print(f"{sub_str}:{count}")


# 39. reverse a string
s="python is easy to learn hi python how are you".split()
print(" ".join(s[::-1]))


# 40. reverse words in a string
s="python is easy to learn hi python how are you".split()
s1=[]
for i in s:
    s1.append(i[::-1])
print(" ".join(s1))


# 41. strip a set of characters from a string
s="Hello world"
print(s.strip("eHd"))


# 42.count repeated characters in a string
s="Hello world"
d={}
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    d[i]=count
print(d)
for j in d:
    # print(j)
    if d[j]>=2:
        print(f"{j}:{d[j]}")


# 43.  square and cube symbol in the area of a rectangle and volume of a cylinder




# 44. print the index of the character in a string
s="Hello World"
character=input()
for i in range(len(s)):
    if s[i]==character:
        print(f"index:{i}")

# or 
print(s.index(character))


# 45. check if a string contains all letters of the alphabet
import string
s="The quick brown fox jumps over the lazy dog"
s1=string.ascii_lowercase
flag=True
# print(s1)
for i in s1:
    if i in s:
        falg=True
    else:
        falg=False
        break
print(flag)

# 46. convert a string in a list
s="The quick brown fox jumps over the lazy dog".split()
print(s)
s1="hello"
print(list(s1))
s2="Hello world"
l1=[]
for i in s2:
    l1.append(i)
print(l1)


# 47. lowercase first n characters in a string
s=input("enter the string: ")
n=int(input("n: "))
l1=[]
count=0
for i in range(len(s)):
    count+=1
    if count<=n:
        if "A"<=s[i]<="Z":
            l1.append(chr(ord(s[i])+32))
    else:
        l1.append(s[i])
print("".join(l1))


# 48. swap comma and dot in a string
s="3,456,789"
m_k=str.maketrans(',','.')
print(s.translate(m_k))

# or 
print(s.replace(',','.'))


# 49. count and display the vowels of a given text
s="hello python"
count=0
for i in s:
    if i in "aeiou":
        count+=1
        print(i)
print("count: ",count)


# 50. split a string on the last occurrence of the delimiter
s="hello"
print(s[:-1]+","+s[-1:])
l2=[]
s='a,b,c,d'
# for i in range(len(s)):
#     if i<=len(s)-2:
#         l2.append(s[i])
#     else:
#         s.append(i)
# print(l2)
# print(s)
# print(" ".join(l2))
print(s.rsplit(",",1))

# 51. find the first non-repeating character in given string
s="hello python"
d={}
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    d[i]=count
print(d)
l1=[]
for i in d:
    if d[i]==1:
        l1.append(i)
print(l1[0])

# or
l1=[]
for i in s:
    if s.count(i)==1:
        l1.append(i)
print(l1[0])
      

# 52. print all permutations with given repetition number of given string
import itertools
s=input("enter the string: ")
s1=list(itertools.permutations(s,3))
print(s1)


# 53. find the first repeated character in a given string
s="hello python how are you"
l1=[]
for i in s:
    if s.count(i)>1:
        l1.append(i)
print(l1[0])

# 54. find the first repeated character of a given string where the index of first occurrence is smallest
s="hello python how are you"
d=[]
for i in s:
    if s.count(i)>1:
        d.append(i)
print(f"{d[0]},index:{s.index(d[0])}")


# 55. find the first repeated word in a given string
s="hello python how are you, python is to learn.".split()
l1=[]
print(s)
for i in set(s):
    count=s.count(i)
    if count>1:
        l1.append(i)
print(l1[0])


# 56. find the second most repeated word in a given string
s="python string loops Operators string  list set string python list dict python string".split()
d={}
l=[]
for i in s:
    count=s.count(i)
    if count>1:
        d[i]=count
        # l.append(d[i])
# print(d)
for i in d:
    l.append(d[i])
l=sorted(l)
# print(l)
for i in d:
    if d[i]==l[-2]:
        print(f"{i}:{d[i]}")


# 57. remove spaces from a given string
s="python string loops Operators string  list set string python list dict python string"
s1=''
for i in s:
    if i==" ":
        continue
    else:
        s1+=i
print(s1)

# 58. move spaces to the front of a given string
s="hello python. "
s1=''
for i in s:
    if i!=' ':
        s1+=i
print(s1)
l_s=len(s)-len(s1)
print(" "*l_s+s1)


# 59.  find the maximum occurring character in a given string
s="python loops string lists tuples"
d={}
l=[]
for i in s:
    count=0
    if s.count(i)>1:
        d[i]=s.count(i)
print(d)
for i in d:
    l.append(d[i])
l=sorted(l)
for i in d:
    if d[i]==l[-1]:
        print(f"{i}:{d[i]}")


# 60. capitalize first and last letters of each word of a given string
s="python loops string lists tuples".split()
l1=[]
for i in s:
    # print(i)
    # print(ord(i[0]))
    if 97<=ord(i[0])<=122 or 97<=ord(i[-1])<=122:
        val1=chr(ord(i[0])-32)
        val2=chr(ord(i[-1])-32)
        s1=''
        s1+=val1+i[1:-1:]+val2
        l1.append(s1)
   
print(" ".join(l1))


#61. remove duplicate characters of a given string
s="hello python how are you"
print(set(s)) 

# or
l1=[]
for i in s:
    if i==" ":
        l1.append(" ")
    elif i not in l1:
        l1.append(i)
print("".join(l1))


# 62. compute sum of digits of a given string
s="hello8761"
sum=0
for i in s:
    if i.isdigit():
        x=int(i)
        sum+=x
print(sum)


# 63. remove leading zeros from an IP address
s="001.200.001.004".split(".")
# print(s)
l1=[]
for i in s:
    if i.isdigit():
        x=int(i)
        # print(x)
        l1.append(str(x))
print(".".join(l1))


# 64. Reverse a given string  Input : "Python"   Output : "nohtyP"
s="python"
print(s[::-1])


# 65. Reverse each word in given string Input 
s="python string loops list".split()
print(" ".join(s[::-1]))


# 66. Reverse each word and reverse word again. Input
s="python string loops list".split()
l1=[]
for i in s[::-1]:
    l1.append(i[::-1])
print(l1)


# 67. that accepts a string and calculate the number of digits and letters
s="12hello67"
digit_count=0
letter_count=0
for i in s:
    if i.isdigit():
        digit_count+=1
    else:
        letter_count+=1
print(f"digit count:{digit_count}\nletter count:{letter_count}")
'''