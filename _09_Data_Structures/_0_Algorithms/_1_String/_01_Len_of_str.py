'''REQ: Find length of String'''

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
    

I. REQUIREMENT GATHERING : Find length of given string. 
        ------------------------------------
        |    Enter String: |_________|      |
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           Once he clicks on Submit button, length should be displayed.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "Enter at least 2 characters"
               ii. Single word     Ex: "Hello" : 5
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Including space?  ==> Don't Include
               vii. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: StringLength

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
   'Hello World'                     str1 = 'Hello World'
    
                                  BEHAVIOR:
                                  ----------
2. Initial count is 0.            2. Initialize counter as 0
3. Traverse through each char     3. Use for loop to iterate through each char
4. Incrementing count value       4. Increment count var in each iteration
                                      (Operators / Loops)
'''


"""
IV. DEVELOPMENT:
=================
        1. Builtin Functions
        2. Algorithm **
        3. Functions  : 40
        4.OOPS        : 20     5. EH  : 10    6. FH  : 5       
        7.Database    : 3      8. UI  : 3
"""
    # 1.Builtin functions

print("-----1. Builtin Functions--------")

message = 'Hello World'  # static way
# message = input("Enter any string : ")

print("Length of given string : ", len(message))


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'Hello World'

# BEHAVIOR
le = 0
for char in message:
    le += 1
print("Length of given string : ", le)

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
