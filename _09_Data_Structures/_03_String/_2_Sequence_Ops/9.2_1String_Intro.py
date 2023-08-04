'''
@author: mnettem
'''
'''
# Sequences: 
    String 
    List 
    Tuple 
    Range   
    bytearrays / buffers
'''
msg = 'hello world!'
      #012345678910
print("----message1-----", msg)

message2 = "PYTHON PROGRAMMING!"
print("----message2-----", message2)

'''
Operations on Sequence ***:
===========================
1. Indexing
2. Slicing
3. Adding
4. Multiplying 
5. Checking for Membership

6. len()  7. max()  8. min()

'''    #  ---theatre-------


msg = 'hello world'
     # 012345678.....   30

print("Message is  :", msg)

# 1 INDEXING
print("----- 1st index in message1 -----", msg[6])
print("----- 4th index in message1 -----  Positive : ", msg[1], "  Negative :  ", msg[-11])
print("------Last l -------------------- : ", msg[-2])

# 2 SLICING  # start(index) stop(position) step(diff)  str[start:stop:step]
# sequence[start:stop:step]
#          indexing:position:diff
msg = 'hello world'
'''         
                     -6 -5-4-3-2 -1   : Negative Indexing
            h e l l o   w  o r l d 
            0 1 2 3 4 5 6  7 8 9 10  : Indexing 
            1 2 3 4 5 6 7  8 9 10 11 : Position
 '''


print("Slicing positive : ", msg[0:4])   # 0 index  4 position
print("Slicing positive : ", msg[6:11])  # print from index 6 to position 11
print("Slicing Negative : ", msg[-6:-1]) #
print("Slicing with start stop step : ", message2[0:9:3], " == ", message2[0:13], "  ", message2[0:13:2], " ", message2[0:13:3])
print("Slicing without any positions + :", message2[::], "  ", message2[2::], " ", message2[:8:], " ", message2[::2], " ", message2[::3])
print("Slicing without any positions - :", message2[::], "  ", message2[-2::], " ", message2[:-8:], " ", message2[::-2], " ", message2[::-3])



# 3 ADDING CONCATINATION
str1 = 'Hello'
str2 = 'World'
print("Entire string : ", str1 + str2)

final_message = msg + " Welcome to " + message2

print("Concatenation :: ", final_message)



# 4 MULTIPLYING
print("Multiplication : ", msg * 4)
print("Multiplication : ", final_message * 4)


# 5 CHECKING FOR MEMBERSHIP
print("--Membership---- : ", "PYTHON" in message2)
print("--Membership---- : ", "N" in message2)
print("--Membership---- : ", "IAM" in message2)


# 6 len()

msg ='Hello World'

print("Length of string : ", len(msg))

# 7 max()  # ASCII Table a = 97    A = 65
print("Max value in string  : ", max(msg))
msg1 = '12345'
print("Max value in string  : ", max(msg1))
print("Max value in string  : ", max('abcd'))
print("Max value in string  : ", max('ABCD'))
print("Max value in string  : ", max('ABDFSDfdsasdas'))
print("Max value in string  : ", max('abfd212rd'))
print("Max value in string  : ", max('@$##@$#!%'))
print("Max value in string  : ", max('1234213e'))





# 8 min()
print("Min value in string  : ", min(msg))
msg1 = '12345'
print("Min value in string  : ", min(msg1))
