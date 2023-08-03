# Count words in a string
'''REQ: Count words in a string'''

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
    

I. REQUIREMENT GATHERING : Count words in a string  
        ------------------------------------
        |    Enter String: |_________|      |
        |                                   |               
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           count how many words are in the string
           Once he clicks on Submit button, display count.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "enter the string which is having more than one character"
               ii. Single word     Ex: "Hello" : "display count of words"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Only Numbers allowed ?  Yes
               vii.space consider ?: no
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: count words in the strings

            State   : Data types/strs:  STRING STRING
           
            Behavior: Operators      : = += 
                      DM             :if 
                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
    'Hello python'                    str1 = 'Hello python'
    
                                    BEHAVIOR:
                                    ----------
2. initialise count=0                2. initialise count=0 
                                                
3. increase count by each word       3. Traverse through the for loop 
4. diplay the count to the user      4. display the count to user        
           
                                      


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
# singal string
message = 'Hello python'  # static way
# message = input("Enter any string : ")
# no bulit in methods


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'Hello python'.split()
if message=="":
    print("empty string")
elif len(message)==1:
    print("len should be greater than one")
else:
    count=0
    for i in message:
        count+=1
    print(count)


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
