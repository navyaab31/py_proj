'''
For a particular value 
                    1. Print it 
                    2. Assign to variable 
                    3. Perform operation
'''
# sort()

list1 = [10, 54, 23, 53, 2, 24, 58]
print("Before sort : ", list1)
list1.sort()
print("After sort  : ", list1)

# sorted()
list2 = [10, 54, 23, 53, 2, 24, 58]
print("Before sorted : ", list2)
list3 = sorted(list2)
print("After sorted  : ", list2)
print("After sorted  : ", list3)

100  # Garbage collection

print(200)  # single time usage

x = 300     # multiple times
print("Value : ", x)

'Hello World'  # Garbage collection

print(10)  # one time usage

x = 10
print("Value of x :", x)  # multiple usage
print("X one more time : ", x)
x = 10 + 20  # Operation

# 1. capitalize() :: Returns a string with the first character as upper case.
                    # hello --> Hello
print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello'
print("Normal string           :", str1)   # hello
str1.capitalize()  # Hello                * No action here *
print("String after capitalize1 :", str1)  # hello
# Onetime
print("String after capitalize2 :", str1.capitalize())   # Hello
print("String after capitalize3 :", str1)                # hello

# Assigning to new variable
str2 = str1.capitalize()   #  : If we want both old,new values(hello, Hello)
print("String after capitalize4 :", str1)    # hello
print("String after capitalize3 :", str2)    # Hello

# Assigning to same variable
str1 = str1.capitalize()   # : If we don't want old value
print("String after capitalize4 :", str1)    # Hello


'''3 Ways'''
print("----Way 1--------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'hello'
print("String     : ", str1)
print("Capitalize : ", str1.capitalize())  # print(10)
print("String     : ", str1)

# 2 : Current string should be used as is, new string used in "multiple places"
x = 10
y = x ** 3
print("----Way 2--------")
str1 = 'hello'              # x = 10
print("String     : ", str1)
str2 = str1.capitalize()         #  y = x + 5
print("String     : ", str1)
print("String     : ", str2)     # print(x)

# 3 : Current string should get modified
print("----Way 3--------")
x = 10
# ..........
x = x ** 2
str1 = 'hello'
print("String     : ", str1)
str1 = str1.capitalize()  # Hello
print("String     : ", str1)

print("-------------------------------------------------------------------------------------")

#2.casefold():: returns a string where all the characters are lower case
                # HeLLo-->hello
print("------------------2.casefold()---------------------")
print("casefold(): convert upper case to lower case")

str1='HeLLo'
print("normal string :",str)        
# HeLLo
str1.casefold()
print("string after the casefold:",str1)
# HeLLo
# one time
print("string after casefold:",str1.casefold())
# hello
print("string aftre casefold:",str1)
# HeLLo

# Assigning to new variable
str2 = str1.casefold() 
# if we want both old,new values
print("string agter casefold:",str1)
# HeLLo
print("string after casefold:",str2)
# hello

# Assigning to same variable
str1=str1.casefold()
# if we don't want old value
print("string after casefold:",str1)
# hello

# 3. center() :: Returns a string padded with specified fillchar 
# and it doesn’t modify the original string.
                # str.center(length,fillchar[optional])
                # hi.center(20,0)-->000000000hi000000000

print("---------------3. Center()------------------")
print("center() : string padded with specified fillchar")
str1="hi"
print("normal string  :",str1)  # hi
str1.center(20,"$")
print("string after center:",str1)  # hi

# onetime
print("string after center:",str1.center(20,"$"))   # $$$$$$$$$hi$$$$$$$$
print("string after center:",str1)     # hi

# Assigning to new variable
str2=str1.center(20,"$")   # if we wanr old, new values
print("string after center:",str1)  # hi
print("string after center:",str2) # $$$$$$$$$hi$$$$$$$$

# Assigning to same variable
str1=str1.center(20."$")    # if we don't want old values
print("string after center:",str1)  # $$$$$$$$$hi$$$$$$$$

# 4.count() ::returns an integer that denotes the number of times 
# a substring occurs in a given string.
                    # x=str.count(substring,start,end)-->3(integer)

print("--------------3.count()--------------------")
print("the number of times substring present in a given string")

str1="hello python"
sub_str="h"
print("normal string:",str1)     # hello python
str1.count("h")     # no action

# onetime 
print("count of substring:",str1.count(sub_str))
# 2
print("string after count:",str1)
# hello python

# Assigning to new variable
cnt=str1.count(sub_str)      
print("cnt after count:",cnt)    # 2
print("string after the count:",str1)   # hello python

string="python how are you"
print(string.count('o',5))      # 2

string="python how are you"
print(string.count('o',5,10))      # 1

string="red green orange yellow red"
print(string.count('red'))     # 2

string="red green orange yellow red"
print(string.count('red',2))        # 1


# 5. encode()  :: return encoded version of string
                # str1.encode()-->"encoded version"

print("--------------5.encode------------------")
print("returns encoded version of the string")

str1="hello"
print("normal string       :",str1)    # hello
str1.encode()   # no action
print("string after the encode: ",str1)   # hello

# onetime
print("string after the encode:",str1.encode())   # b'hello'
print("string after the encode:",str1)    # hello

# Assigning to new variable
str2=str1.encode()       # if we want both old, new values
print("string after encode:",str1)    # hello
print("string after the encode:",str2)   # b'hello'

# Assigning to same variable
str1=str1.encode()      # if we don't want old value
print("string after encode:",str1)    # b'hello'

# 6. endswith():: return True if the string ends with given suffix otherwise False
                # str1.endswith(suffix,start,end)
                # suffix-string that needed to be check
                # start-staring position
                # end-ending position
print("---------------6.endswith()------------------")
print("return True if string endswith suffix otherwise false")

str1="hello python"
print("normal string      :",str1)   # hello python
str1.endswith("n")       # no actions
print("string after endswith:",str1)     # hello python

# onetime
print("result after endswith:",str1.endswith("n"))   # True
print("string after the endswith:",str1)    # hello python

# Assigning to new variable
str2=str1.endswith("n")      # if we want both result and old value
print("result after the endswith:",str2)  # True
print("string after endswith:",str1)    # "hello python"

# Assigning to same variable
str1=str1.endswith("n")    # if we don't want old value"
print("result after endswith:",str1)   # True

# 7. expendtab() :: return the modified string replace tab with the space
# bydefault it's 8
#                       str1.expandtab(space_size)

print("-------------------7.expandtab()------------------------")
print("modified string replace tab with space_size")

str1="hello\tpython"
print("normal string   :",str1)      # "hello\tpython"
str1.expandtabs(3)
print("string after expandtab:",str1)        # hello   python

# onetime
print("string after expandtabs:",str1.expandtabs())   # hello   python
print("string after expandtabs:",str1)                # hello        python

# Assigning to new variable
str2=str1.expandtabs(3)      # if we want both new value (b/c it modifies the string)
print("string after expandtabs:",str1)      # hello        python(8-space)
print("string after expandtabs:",str2)      # hello   python

# Assigning to same variable
str1=str1.expandtabs(3)
print("string after expandtabs:",str1)    # hello   python

# 8. find() :: returns lowest index or first occurence of the substring if it is not found it returns the -1
#               find(sub_str,start,end)-->integer
print("-------------------8.find()------------------------")
print("returns lowest index or firat occrence of the substring")
str1="hello world"
print("normal string:   ",str1)   #hello world
str1.find("o")    #no action
print("string after find:",str1)

# onetime
print("result after find:",str1.find("o"))          # 4


# Assigning to new variable
str2 = str1.find("o")   #  : If we want both values(multiple times)
print("String after capitalize4 :", str1)    # hello python
print("String after capitalize3 :", str2)    # 4

# Assigning to same variable
str1 = str1.find("o")   
print("String after capitalize4 :", str1)    # 4

print("result after find:",str1.find("o",5))        # 7

print("result after find:",str1.find("o",8))        # -1

print("result after count:",str1.count("o",2,8))     # 2

print("strong after the find:",str1)                # hello world

# 9. format() :: Returns a formatted string with the value passed as parameter in the placeholder position.
#           {}.format(values)-->formatted string

print("---------------9.format()--------------------")
print("return formated string with value passed a s parameter to placeholder")

str1="hello python how {} you"
print(str1.format("are"))
# hello python how are you
x=str1.format("are")
print(x)
# hello python how are you
x=33.95436
y=99.99
print("{:.2f}".format(x))             # 33.95
print("{1:.0f}".format(x,y))           # 100
print("{1:} {0:}".format(x,y))          # 99.99 33.95436
print("{} {}".format(x,"hello"))           # 33.95436 hello
print("{1} {0}".format(x,"hello"))         # hello 33.95436

# 10.format_map() :: which is use to return dictionary key's value
#                       str1.format_amp(z)

print("10.-----------------format_map()-----------------")
print("used to return dictionary key's value")
a = {'x':'John', 'y':'Wick'}
print("{x}s last name is {y}".format_map(a))
# John's last name is Wick

# 11. index() :: retruns position of first occrence of sub_string in the string
# if sub_string not found it raise value error
#               str1.index(sub_string,start_pos,end_pos)
print("11.--------------index()---------------------")
print("returns position of the first occrence of sub_string")

str1="hello world"
print("normal string   :",str1)    # hello world
str1.index("r")            # no action

x=str1.index("r")   # 8
y=str1.index("o",5)    # 7
x=str1.index("l",2,5)     # 2

# 12. isalnum():: it's check weather all the characters in string are alphabet or numeric
#                   str1.isalnum()-->True/False

print("12.---------------isalnum()-----------------")
print("checks weather all the character in the string are alphanumeric")

str1="hello world"
print("normal string:   ",str1)   #hello world
str1.isalnum()    #no action
print("string after find:",str1) 

# onetime
print("result after find:",str1.isalnum())          # False

# Assigning to new variable
str2 = str1.isalnum()   #  : If we want both values(multiple times)
print("String after capitalize4 :", str1)    # hello python
print("String after capitalize3 :", str2)    # False

# Assigning to same variable
str1 = str1.isalnum()        # if we don't want old value
print("String after capitalize4 :", str1)    # False

str1="hello123"
print("normal string: ",str1)    # hello123
str1.isalnum()       # no action

x=str1.isalnum()    # True

str2="hello"
y=str2.isalnum()      # False

string = "abc 123"
print(string.isalnum())     # False

string = "abc_123"
print(string.isalnum())      # False

string = "000"
print(string.isalnum())              # True
 
string = "aaaa"
print(string.isalnum())               # True

# 13. isalpha():: it returns True if all character in the strings are alphabet
#                   str1.isalpha()-->True/False

print("13.---------------ialpha()-----------------")
print("returns True if all characters in strings are alphabet")

str1="hello"
print("normal string: ",str1)    # hello
str1.isalpha()       # no action

x=str1.isalpha()    # True

str2="hello123"
y=str2.isalpha()      # False
print(x)     # True
print(y)     # False

# 14.isdecimal():: it returns True if all character in the strings are decimal
#                   str1.isdecimal()-->True/False

print("14.---------------isdecimal()-----------------")
print("returns True if all characters in strings are decimal")

s = "12345"
print(s.isdecimal())     # True
  
# contains alphabets
s = "12geeks34"
print(s.isdecimal())       # False
  
# contains numbers and spaces
s = "12 34"
print(s.isdecimal())         # False

# 15.isdigit():: it returns True if all character in the strings are digit
#                   str1.isdigit()-->True/False

print("15.---------------isdigit()-----------------")
print("returns True if all characters in strings are digit")

# checking for digit
string = '15460'
print(string.isdigit())     # True
 
string = '154ayush60'
print(string.isdigit())      # False

# 16.isidentifier():: it check weather the string is a valid identifier or not
#                   str1.isidentifier()-->True/False
print("16.---------------isisidentifier()-----------------")
print("it check weather the string is valid identifier or not")

# String with spaces
string = "sub string"
print(string.isidentifier())       # False
 
# A Perfect identifier
string = "sub_string"
print(string.isidentifier())        # True
 
# Empty string
string = ""
print(string.isidentifier())      # False
 
# Alphanumerical string
string = "string234"
print(string.isidentifier())        # True
 
# Beginning with an integer
string = "54string"
print(string.isidentifier())        # False

# 17.islower():: it check all character in the strings are in lowercase
#                   str1.islower()-->True/False
print("17.---------------isislower()-----------------")
print("it check all character in the strings are in lowercase")

str1="hello world"
print("normal string:   ",str1)   #hello world
str1.islower()    #no action
print("string after islower:",str1) 

# onetime
print("result after islower:",str1.islower())          # True

# Assigning to new variable
str2 = str1.islower()   #  : If we want both values(multiple times)
print("String after islower:", str1)    # hello python
print("result after islower :", str2)    # True

# Assigning to same variable
str1 = str1.islower()        # if we don't want old value
print("String after islower :", str1)    # True

string = "sub string"
print(string.islower())       # True
 
string = "Sub_String"
print(string.islower())        # False

string="good morning03"
print(string.islower())         # True

string="good morning$03"
print(string.islower())           # True
 
# 18.isnumeric():: it check all character in the strings are numeric
#                   str1.isnumeric()-->True/False
print("18.---------------isnumeric()-----------------")
print("it check all character in the strings are numeric")

str1="hello 123"
print("normal string:   ",str1)   #hello 123
str1.isnumeric()    #no action
print("string after isnumeric:",str1) 

# onetime
print("result after isnumeric:",str1.isnumeric())          # False

# Assigning to new variable
str2 = str1.isnumeric()   #  : If we want both values(multiple times)
print("String after isnumeric:", str1)    # hello 123
print("result after isnumeric :", str2)    # False

# Assigning to same variable
str1 = str1.isnumeric()        # if we don't want old value
print("String after isnumeric :", str1)    # False

string = "12345"
print(string.isnumeric())       # True
 
string = "12 34"
print(string.isnumeric())        # False

string="12abc456"
print(string.isnumeric())           # False

string=" "
print(string.isnumeric())     # False


# 19.isprintable():: it check all character in the strings are printable or empty string
#                   str1.isprintable()-->True/False
# The only whitespace character which is printable is space or ” “,
#  otherwise every whitespace character is non-printable and the function returns “False”.
print("19.---------------isprintable()-----------------")
print("it check all character in the strings are printable")

string = "python"
print(string.isprintable())       # True
 
string = "python \n code"
print(string.isprintable())        # False

string=" "
print(string.isprintable())           # True

# 20.isspace():: it check all character in the strings are space
#                   str1.ispace()-->True/False
# it return True only  string contains whitespace character
print("20.---------------isspace()-----------------")
print("it check all character in the strings are space")

str1="hello 123"
print("normal string:   ",str1)   #hello 123
str1.isspace()    #no action
print("string after isspace:",str1) 

# onetime
print("result after isapace:",str1.isspace())          # False

# Assigning to new variable
str2 = str1.isspace()   #  : If we want both values(multiple times)
print("String after isspace:", str1)    # hello 123
print("result after isspace :", str2)    # False

# Assigning to same variable
str1 = str1.isspace()        # if we don't want old value
print("String after isspace :", str1)    # False

string = " "
print(string.isspace())       # True
 
string = "python \n"
print(string.isspace())        # False

string="\n\t\n"
print(string.isspace())           # True

string="\nhello\npython\n"
print(string.isspace())           # False

# 21.istitle():: it check the strings is title-cased or not
#                   str1.istitle()-->True/False

print("21.---------------istitle()-----------------")
print("it check string is title-cased or not")

s = 'Hello Python'
print(s.istitle())     # True
 
# First character in first word is lowercase
s = 'hello Python'
print(s.istitle())     # False
 
# Third word has uppercase characters at middle
s = 'How Are YOU'
print(s.istitle())     # False

# Ignore the digit 6041, hence returns True
s = '6041 Hello Python'
print(s.istitle())     # True
 
# word has uppercase characters at middle
s = 'PYTHON'
print(s.istitle())     # False

# 22.isupper():: checks if all character in the strings are upper
#                   str1.isupper()-->True/False

print("22.---------------isupper()-----------------")
print("it returns True if all the characters in the strings are in upper case")

str1="Hello"
print("normal string:   ",str1)   #Hello 
str1.isupper()    #no action
print("string after isupper:",str1) 

# onetime
print("result after isupper:",str1.isupper())          # False

# Assigning to new variable
str2 = str1.isupper()   #  : If we want both values(multiple times)
print("String after isupper:", str1)    # Hello 
print("result after isupper:", str2)    # False

# Assigning to same variable
str1 = str1.isupper()        # if we don't want old value
print("String after isspace :", str1)    # False

s = 'HELLO PYTHON'
print(s.isupper())     # True
 
s = 'hello Python'
print(s.isupper())     # False

# 23.join():: returns a concatenated string
#                   "-".join(str1)-->concatenated string
#                   hello-->h-e-l-l-o

print("23.---------------join()-----------------")
print("returns a concatenated strings")

s = ['1','2','3','4','5']
print("-".join(s))      # 1-2-3-4-5
 
s=" python "
print("#".join(s))       # p#y#t#h#o#n

dic = {'hi': 1, 'hello': 2, 'python': 3}
print("-".join(dic))            # hi-hello-python

# 24.ljust() :: returns the new string of given length after substituting a given character in the left side of the original string.
#                   str1.ljust(size,fillchar)-->new string
#                   hello.ljust(10)-->hello     

print("24.---------------ljust()-----------------")
print("Returns a new string of given length after substituting a given character in left side of original string.")


s = "python"
print(s.ljust(10,"#"))      # python####
 
s=" python "
print("#".ljust(10,"#"))       # python ##


# 25.lower() :: converts all characters in a string to lowercase
#                   str1.lower()
#                   heLLo-->hello     

print("25.---------------lower()-----------------")
print("coverts all the characters in a string to lowercase")


str1= "PyThonN"
print("Normal string          :",str1)     # PyThonN
str1.lower()          # no action
print("string aftre lower:",str1)     # PyThonN

# onetime
print("string after lower:",str1.lower())   # python
print("string after lower:".str1)     # PyThonN

# Assigning to new variable
str2=str1.lower()    # if we want both old,new values
print("string after lower:",str1)    # PythoN
print("string after lower:",str2)     # python

# Assigning to same variable
str1=str1.lower()    # we don't want old value
print("string after lower",str1)    # python

s="pYth0n"
print(s.lower())       #pyth0n

s="HELLO WORLD"
print(s.lower())    # hello world

s="hell0 PYthoN 3"
print(s.lower())      # hell0 python 3

s="my name is Peter"
print(s.lower())   # my name is peter

# 26.lstrip():: Returns a copy of the string with leading characters stripped.
#                   str1.lstrip()-->string
print("26.---------------islstrip()-----------------")
print("returns a copy of the string with leading character stripped")

string = "   python" 
# Removes spaces from left.
print(string.lstrip())         # python

string = "...*,,, python"
 
# Removes given set of characters from left.
print(string.lstrip(",*.p"))       # python

# 27.maketrans():: Returns the translation table
#                   str1.maketrans(original_str,sub_str,new_str)-->translation table
print("27.---------------maletrans()-----------------")
print("it returns translation table")

# 28.translate():: Returns the translation table
#                   str1.maketrans(original_str,sub_str,new_str)-->translation table
print("28.---------------translate()-----------------")
print("it returns translation table")


# 29.partition():: split the string at the first occrence of the character
#                   str1.partition()-->string
print("29.---------------partition()-----------------")
print("slipt the string at the first occrence of the seperator")

string = "hello python how are you" 
print(string.partition("are"))         # ('hello python how ', 'are', ' you')

string = "I am happy, I am proud"
print(string.partition("am"))       # ('I ', 'am', ' happy, I am proud')


# 30.replace():: replace all the occrence of substring with other sub_string
#                   str1.replace(old,new,count)-->string
print("30.---------------replace()-----------------")
print("returns a copy of string replace all the occrence of substring with other substring")

str1= "python"
print("Normal string          :",str1)     # python
str1.replace('t','a')          # no action
print("string aftre replace:",str1)     # python

# onetime
print("string after replace:",str1.replace('t','a'))   # pyahon
print("string after repace:".str1)     # python

# Assigning to new variable
str2=str1.replace('t','a')    # if we want both old,new values
print("string after replace:",str1)    # Python
print("string after replace:",str2)     # pyahon

# Assigning to same variable
str1=str1.replace()    # we don't want old value
print("string after replace",str1)    # pyahon

string = "hello python how are you" 
print(string.replace("are","xyz"))         # hello python how xyz you

string = "hello python how are you"
print(string.replace("e","x"))       # hxllo python how arx you

string="hello python how are you"
print(string.replace('o','o',2))   # hellx pythxn how are you


# 31.rfind():: returns the right-most index of the sub string if it is found in the given string
#                   str1.rfind(old,start,end)-->index number
# if it is not found it returns -1
print("31.---------------rfind()-----------------")
print("returns the right-modt index of the sub string if it found in the given string")

string = "hello python how are you" 
print(string.rfind("o"))         # 22

string = "hello python how are you"
print(string.rfind("e",1,11))       # 10

string="hello python how are you"
print(string.rfind('l',6))   # -1

# 32.rindex():: returns the highest index of the substring  in the given string if it is found substring
#                   str1.rindex(old,start,end)-->index number
# if the substring not present it gives you error
print("32.---------------rindex()-----------------")
print("returns the highest index of the sub string in the given string if it found sub_string")

string = "hello python how are you" 
print(string.rindex("o"))         # 22

string = "hello python how are you"
print(string.rindex("e",0,-6))        # 1

string="hello python how are you"
print(string.rindex('h',5,))       # 13

# 33.rjust():: return new string of a given length after substituting a given character at the left side of the original string
#                   str1.rjust(length,fillchar)-->string

print("33.---------------rjust()-----------------")
print("returns ner string of given length after substituting given character at left side of the string")

string = "hello" 
print(string.rjust(7))         #  hello   

string = "python"
print(string.rjust(10,"*"))        #****python

# 34.rpartition():: split the string into a three part
#                   str1.rpartition(separator)-->string
# it consider from the right-most end
print("34.---------------rportition()-----------------")
print("split the string into three parts")

string = "hello world" 
print(string.rpartition("o"))         # ('hello w', 'o', 'rld')  

# returns first 2 arguments as empty String if separator is not present in String
string = "hello python"
print(string.rjust(10,"*"))        #('', '', 'hello python')

# TypeError: If a separator argument is not supplied, it will raise TypeError
'''
string = "Bruce Waine is Batman"
  
# Nothing is passed as separator
print(string.rpartition())
'''

# ValueError: If the separator is an empty String, then rpartition() Method raises ValueError
'''
string = "Bruce Waine is Batman"

# Nothing is passed as separator
print(string.rpartition(""))
'''
# 35.rsplit():: split the string from the right by the specified separators
#                   str1.rsplit(separator,max_split)-->string

print("35.---------------rsplit()-----------------")
print("split the string from the right by the specified separartors")

string = "hello world" 
print(string.rsplit(" "))         # ['hello', 'world']  

word = 'abc@for@xyz'
print(word.rsplit('@', 1))        #['abc@for', 'xyz']

word = 'abc@for@xyz'
print(word.rsplit('@', 1))         # ['abc', 'for', 'xyz']

# 36.rstrip():: remove the trailing character of the string
#                   str1.rstrip(character)-->new_string

print("36.---------------rstrip()-----------------")
print("removes the trialing character of the string")

string = "pythonnn" 
print(string.rstrip("n"))         # pytho 

string = "hello python hello world"
 
# Removes given set of characters from right.
print(string.rstrip('dlr'))       #hello python hello wo

# Python String rstrip() returns the original String 
# if the string cannot be stripped of provided characters

# 37.splitlines():: returns a list of lines in the string, breaking at line boundaries
#                   str1.rstrip(keepends)-->list of lines

print("37.---------------splitlines()-----------------")
print("returns a list of lines in the string, breaking at line boundaries")

string = "Cat\nBat\nSat\nMat\nXat\nEat"
  
print (string.splitlines( ))
# ['Cat', 'Bat', 'Sat', 'Mat', 'Xat', 'Eat']

# 38.startswith():: returns True if the string startswith given prefix 
#                    str1.startswith(prefix,start,end)-->True/False

print("38.---------------startswith()-----------------")
print("returns True if the string startswith given prefix")

string = "hello python"
print (string.startswith("p"))  # False

print(string.startswith("h"))   # True

print(string.startswith("h",2,7))   # False

# pass tuple
string = "apple"
res = string.startswith(('a', 'e', 'i', 'o', 'u'))
print(res)       # True

# 39.strip():: returns copy of the string  with both trailing and leading characters removed 
#                    str1.strip(char)-->string

print("39.---------------strip()-----------------")
print("returns copy of the string with both trailing and leading character removed")

my_string = "   Hello, world!   "
stripped_string = my_string.strip()
print(stripped_string)      #Hello, world!

my_string = "python or python"
stripped_string = my_string.strip("python")
print(stripped_string)         # or

# 40.swapcase():: convert uppercase to lowercase and lowercase to uppercase 
#                    str1.swapcase()-->string
#                       HeLLo-->hEllO

print("40.---------------swapcase()-----------------")
print("convert uppercase to lowercase and lowercase to uppercase")

str1="PythoN"
print("string after uppercase:",str1.swapcase())    # pYTHOn

str1="python"
print("string after uppercase:",str1.swapcase())    # PYTHON

str1="PYTHON"
print("string after uppercase:",str1.swapcase())    # python

# 41.title():: string converted to title case 
#                    str1.title()-->string
#                       hello-->Hello

print("41.---------------title()-----------------")
print("string converted to title case")

str1="PythoN"
print("string after uppercase:",str1.title())    # Python

str1="python"
print("string after uppercase:",str1.title())    # Python

str1="PYTHON"
print("string after uppercase:",str1.title())    # Python

# 42.upper():: convert all lowercase into uppercase 
#                    str1.upper()-->string
#                       hello-->HELLO

print("42.---------------upper()-----------------")
print("string converted to title case")

str1="python"

print("Normal string    :",str1)   # python
str1.upper()    # no action
print("string after upper:",str1)     # python

# onetime
print("string after upper:",str1.upper())    # PYTHON
print("string after upper:",str1)     # python

# Assigning to new variable
str2=str1.upper()    # if we want both new,old values
print("string after the upper:",str1)   # python
print("string after the upper:",str2)   # PYTHON

# Assigning to same 
str1=str1.upper()    # if we don't want old value
print("string after the upper:",str1)    # PYTHON

string="Hello World"
print(string.upper())      # HELLO WORLD

string="Hello123 PythoN"
print(string.upper())      # HELLO123 PYTHON

string="PYThon"
print(string.upper())      # PYTHON

string="pythoN03"
print(string.upper())     # PYTHON03

# 43.zfill():: returns copy of the string with '0' characters padded at the left side of the string 
#                    str1.zfill(length)-->string


print("43.---------------zfill()-----------------")
print("returns copy of the string with '0' characters padded at the left side of the string")

str1="Python"
print("string after uppercase:",str1.zfill(10))    #0000Python

# 44.split():: returns list of string after breaking a given string by specified by separator
#                    str1.split(separator,max_split)-->list of string
#                      

print("44.---------------split()-----------------")
print("returns list of string after breaking given string by specified by separator")

str1="hello world"

print("Normal string    :",str1)   # hello world
str1.split()    # no action
print("string after split:",str1)     # hello world

# onetime
print("string after split:",str1.split())    # ['hello','world']
print("string after split:",str1)     # hello world

# Assigning to new variable
str2=str1.split()    # if we want both new,old values
print("string after the split:",str1)   # hello world
print("string after the split:",str2)   # ['hello','wolrd']

# Assigning to same 
str1=str1.split()    # if we don't want old value
print("string after the split:",str1)    #['hello','world'] 

string="CatBatSatFatOr"
print(string.split('t'))    # ['Ca', 'Ba', 'Sa', 'Fa', 'Or']

string="list:tuples:set:dict:string"
print(string.split(':',3))     # ['list', 'tuples', 'set', 'dict:string']

string="list:tuples:set:dict:string"
print(string.split(':',1))     # ['list', 'tuples:set:dict:string']

string="list,string"
print(string.split(","))       # ['list','string']

# 45.split():: returns list of string after breaking a given string by specified by separator
#                    str1.split(separator,max_split)-->list of string
#                      

print("44.---------------split()-----------------")
print("returns list of string after breaking given string by specified by separator")

str1="hello world"

print("Normal string    :",str1)   # hello world
str1.split()    # no action
print("string after split:",str1)     # hello world

# onetime
print("string after split:",str1.split())    # ['hello','world']
print("string after split:",str1)     # hello world

# Assigning to new variable
str2=str1.split()    # if we want both new,old values
print("string after the split:",str1)   # hello world
print("string after the split:",str2)   # ['hello','wolrd']

# Assigning to same 
str1=str1.split()    # if we don't want old value
print("string after the split:",str1)    #['hello','world'] 

string="CatBatSatFatOr"
print(string.split('t'))    # ['Ca', 'Ba', 'Sa', 'Fa', 'Or']

string="list:tuples:set:dict:string"
print(string.split(':',3))     # ['list', 'tuples', 'set', 'dict:string']

string="list:tuples:set:dict:string"
print(string.split(':',1))     # ['list', 'tuples:set:dict:string']

string="list,string"
print(string.split(","))       # ['list','string']