# to count occurrences of a substring in a string
'''REQ: count occurrences of a substring in a string'''

'''
SDLC Phases:
------------
    I. REQUIREMENT GATHERING
    II. ANALYSIS
            1. Functional Analysis
            2. Technical Analysis        
    III. DESIGN
    IV. DEVELOPMENT
    V.  TESTING
    VI. DEPLOYMENT/PRODUCTION
    

I. REQUIREMENT GATHERING : count occurrences of a substring in a string. 
        ------------------------------------
        |    Enter String: |_________|      |
        |    Enter sub_string: |_______|    |
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           after giving a string customer enter the substring to count the occurence
           Once he clicks on Submit button, display the count of occurence of substring.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "display zero"
               ii. Single word     Ex: "Hello" : "display the count of substring"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Including space?  ==> display the count of space
               vii. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: count the occurence

            State   : Data types/strs:  STRING INT
           
            Behavior: Operators      :  =  +=  
                      DM             :  if 
                      Loops          :  Yes (For Loop)

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
   'Hello World'                    str1 = 'Hello World'
    sub_str='l'                     sub_str='l              
    
                                  BEHAVIOR:
                                  ----------
2.Traverse through each char    2. use for loop to iterate through each char    
3. make a table                 3. Initialize counter as 0               
   H    1                       4. check if enter sud_str present-increment count 
   e    1                       
   l    3                                         
   o    2
   w    1
   r    1
   d    1.                        
4. diplay the count to user    5. display count to user     
                                      




IV. DEVELOPMENT:
=================
        1. Builtin Functions
        2. Algorithm **
        3. Functions  : 40
        4.OOPS        : 20     5. EH  : 10    6. FH  : 5       
        7.Database    : 3      8. UI  : 3
'''
# 1.Builtin functions

print("-----1. Builtin Functions--------")

message = 'Hello World'  # static way
# message = input("Enter any string : ")
sub_str='l'            # static way
# sub_str=input("enter sub_string: ")

print("count of sub_str : ",message.count(sub_str))


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'Hello World'
sub_str='l'

# BEHAVIOR
if message=="":
    print("invalid string")
else:
    for char in message:
        count=0
        if char==sub_str:
            count+=1
print("count of sub_string : ", count)

# 3 Using Functions  ==>   40
print("--------3 Using Functions----------")
# 4 OOPS  ==> 10
print("--------4 Object Oriented----------")
# 5 Exception handling  ==> 5
print("--------5 Exception handling----------")
# 6 File Handling  ==> 3
print("--------6 File Handling----------")
# 7 Database interaction MVC  ==> 10
print("--------7 Database interaction----------")
# 8 UI Interaction   ==> 3
print("--------8 UI Interaction----------")
