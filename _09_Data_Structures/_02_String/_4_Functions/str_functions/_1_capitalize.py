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
                    # x=str.count("substring")-->3(integer)

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
cnt=str1.count(sub_str)       # if we want both old, new values
print("cnt after count:",cnt)    # 2
print("string after the count:",str1)   # hello python

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

str1="hello world"
print("normal string:   ",str1)
#hello world
str1.find("o")
#no action
print("string after find:",str1)

# onetime
print("result after find:",str1.find("o"))          # 4
print("result after find:",str1.find("o",5))        # 7
print("result after find:",str1.find("o",8))        # -1
print("strong after the find:",str1)                # hello world

# Assigning to new variable
str2 = str1.find("o")   #  : If we want both values(multiple times)
print("String after capitalize4 :", str1)    # hello python
print("String after capitalize3 :", str2)    # 4

# Assigning to same variable
str1 = str1.find("o")   # : If we don't want old value
print("String after capitalize4 :", str1)    # 4

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

# 10.