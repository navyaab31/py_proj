#1. Count Characters in a String:
# Description: Write a program that counts the occurrences of each character in a given string.
# Example:
# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s=input("enter the input: ")
def count(n):
    count=0
    for i in s:
        if i==n:
            count+=1
    return count

d1={}
for i in s:
    d1[i]=count(i)
    # print(d1[i])
print(d1)

# without using function
for i in s:
    d={}
    count=0
    for j in s:
        if i==j:
            count+=1
    d[i]=count
print(d1)

# 2.Find Maximum and Minimum:
# Description: Write a program to find the maximum and minimum numbers in a given list.
# Example:
# Input: [4, 9, 2, 7, 5]
# Output: Maximum: 9, Minimum: 2
l1=[4,9,2,7,5]
mx,mn=0,9
for i in l1:
    if i>mx:
        mx=i
    if i<mn:
        mn=i
print("Maximum: ",mx)
print("minimum: ",mn)

# or 
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


# 3. Calculate Average:
# Description: Write a program that calculates the average of a given list of numbers.
# Example:
# Input: [2, 4, 6, 8]
# Output: 5.0
l1=[2,4,6,8,9]
c=0
for i in l1:
    c+=1
sum=0
for i in l1:
    sum+=i
avg=sum/c
print("average: ",avg)


# 4. Check Palindrome:
# Description: Write a program to check if a given string is a palindrome.
# Example:
# Input: "racecar"
# Output: True
s=input("enter the string: ")

s1=" "
for i in s:
    # print(s1)
    s1=i+s1
    # print(s1)
print(s1)
# print(a)
if (s==s1):
    print("palindrom")
else:
    print("not a palindrom")


# 5. Remove Duplicates:
# Description: Write a program that removes duplicates from a given list.
# Example:
# Input: [1, 2, 3, 2, 4, 1, 5]
# Output: [1, 2, 3, 4, 5]
l1=[1,2,3,2,4,1,5]
l2=[]
for i in l1:
    if i not in l2:
        l2+=[i]
        # print(l2)
print(l2)


# 6. Reverse List Order:
# Description: Write a program that reverses the order of elements in a given list.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
l1=[1,2,3,4,5]
l2=[]
for i in l1[::-1]:
    l2+=[i]
print(l2)


# 7. Check Armstrong Number:
# Description: Write a program to check if a given number is an Armstrong number.
# Example:
# Input: 153
# Output: True
n=int(input("enter the number: "))
num=n
l=len(str(n))
sum=0

while n>0:
    rem=n%10
    a=rem**l
    sum+=a
    n=n//10
if sum==num:
    print("True")
else:
    print("False")

# 8. Remove Characters:
# Description: Write a program that removes specified characters from a given string.
# Example:
# Input: "Hello World", ['l', 'o']
# Output: "He Wrld"
s=input("enter the string: ")
n=input()
remove=[]
tmp=''
for i in n:
    if i==" ":
        remove+=[tmp]
        tmp=''
    else:
        tmp+=i
# print(remove)
s1=" "
for i in s:
    if i not in remove:
        s1+=i
print(s1)


# 9. Check Perfect Number:
# Description: Write a program to check if a given number is a perfect number.
# Example:
# Input: 28
# Output: True
n=int(input("enter the number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print(sum)
print(n)
if n==sum:
    print("True")
else:
    print("False")


# 10. Prime Factors:
# Description: Write a program that prints all the prime factors of a given number.
# Example:
# Input: 24
# Output: 2, 3
n=int(input("enter the number: "))
i=1
while (i<=n):
    if n%i==0:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(i)
    i+=1

#11. Calculate GCD:
# Description: Write a program to calculate the greatest common divisor (GCD) of two given numbers.
# Example:
# Input: 24, 36
# Output: 12
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
if num1<num2:
    mn=num1
else:
    mn=num2
gcd=1
for i in range(1,mn+1):
    if (num1%i==0) and (num2%i==0):
        gcd=i
print(f"gcd of {num1} and {num2} is {gcd}")


# 12. Count Words in a Sentence:
# Description: Write a program that counts the number of words in a given sentence.
# Example:
# Input: "Hello, how are you?"
# Output: 4
n=input("enter the string: ")
s=[]
tmp=''
for i in n:
    if i==" ":
        s+=[tmp]
        tmp=''
    else:
        tmp+=i
# print(remove)
# print(s)
count=0
for i in s:
    count+=1
print("count: ",count)

# 13. Common Elements:
# Description: Write a program that finds common elements between two given lists.
# Example:
# Input: [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
# Output: [4, 5]
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l=[]
for i in l1:
    for j in l2:
        if i==j:
            l+=[i]
print(l)

# 14. Square Root:
# Description: Write a program to calculate the square root of a given number using the Newton-Raphson method.
# Example:
# Input: 16
# Output: 4.0
n=int(input())
x=n
while (1):
    root=0.5*(x+(n/x))
    if (round(root,3)==round(x,3)):
        break
    x=root
print(round(root,2))

# 15. Swap Case:
# Description: Write a program that swaps the case (upper to lower and vice versa) of each character in a given string.
# Example:
# Input: "Hello, World!"
# Output: "hELLO, wORLD!"
s=input("enter the string: ")
s1=" "
for i in s:
    
    if ord(i)>=97 and ord(i)<=122:
        i=chr(ord(i)-32)
        # print(i)
        s1+=i
    elif ord(i)>=65 and ord(i)<=90: 
        i=chr(ord(i)+32)
        s1+=i
    elif ord(i)>=32 and ord(i)<=47:
        s1+=i
print(s1)


# 16. Password Strength Checker:
# Description: Write a program that checks the strength of a password based on the following criteria:

# Contains at least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Example:
# Input: "Passw0rd"
# Output: Strong password

password=input("enter the password: ")
upper=False
lower=False
digit=False
# print(len(password))
if (len(password)==8):
    for i in password:
        if ord(i)>=65 and ord(i)<=90:
            upper=True
        if ord(i)>=97 and ord(i)<=122:
            lower=True
        if "0"<=i<="9":
            digit=True
# print(upper)
# print(lower)
# print(digit)
if upper and lower and digit:
    print("Strong password")
else:
    print("not a Strong password")


# 17. Sentence Capitalizer:
# Description: Write a program that capitalizes the first letter of each word in a given sentence.
# Example:
# Input: "hello world"
# Output: "Hello World"
n=input("enter the sentence: ")
s=[]
tmp=''
for i in n:
    if i==" ":
        s+=[tmp]
        tmp=''
    else:
        tmp+=i
print(s)
# print(s,type(s))
count=0
for i in s:
    count+=1
l1=[]
for i in range(count):
    # print(s[i][0])
    var=chr(ord(s[i][:1:])-32)
    var1=var+s[i][1::]
    l1.append(var1)

# print(" ".join(l1))      
for i in l1:
    print(i,end=" ") 

# 18. Word Frequency Counter:
# Description: Write a program that counts the frequency of each word in a given text.
# Example:
# Input: "Hello world. Hello Python Python is awesome."
# Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}
n=input("enter the senctence: ")
s=[]
tmp=''
for i in n:
    if i==" ":
        s+=[tmp]
        tmp=''
    else:
        tmp+=i
print(s)
# print(n)
d={}
for i in s:
    
    count=0
    for j in s:
        if i==j:
            count+=1
    d[i]=count
print(d)


# 19.Anagram Checker:
# Description: Write a program that checks if two given strings are anagrams of each other.
# Example:
# Input: "listen", "silent"
# Output: True
# print(sorted("listen"))
# print(sorted("silent"))
    
def sort_string(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(0, n-i-1):
            if chars[j] > chars[j+1]:
                chars[j], chars[j+1] = chars[j+1], chars[j]
    return ''.join(chars)
 
s1 = input("enter the string1: ")
s2 = input("enter the string2: ")
# print("Original string:", s)
a=sort_string(s1)
b=sort_string(s2)
# print(a)
# print(b)
if a==b:
    print("True")
else:
    print("False")

# or

s1="listen"
s2="silent"
flag=False
for i in s1:
    if i in s2:
        flag=True
    else:
        Flag=False
if flag==True:
    print("True")
else:
    print("False")


# 20.Matrix Transpose:
# Description: Write a program that calculates the transpose of a given matrix.
# Example:
# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
x=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
c=0
for i in x:
    c+=1
for i in range(c):
    # result1=[]
    for j in range(c):
        result[j][i]=x[i][j]
        # result1.append(x[j][i])
    # print(result1)
    # result.append(result1)
print(result)
    



# 21. Binary to Decimal Converter:
# Description: Write a program that converts a binary number to its decimal equivalent.
# Example:
# Input: "1010"
# Output: 10
n=int(input())
dec=0
p=0
while n>0:
    rem=n%10
    dec=rem*2**p+dec
    p+=1
    n//=10
print(dec)

# 22.Caesar Cipher:
# Description: Write a program that encrypts a given string using the Caesar cipher technique.
# Example:
# Input: "Hello", shift=3
# Output: "Khoor"
s=input("enter the text: ")
# l=list(s)
s1=""
# print(l)
for i in s:
    var=chr(ord(i)+3)
    # print(var)
    s1+=var
    # print(s)
print(s1)

