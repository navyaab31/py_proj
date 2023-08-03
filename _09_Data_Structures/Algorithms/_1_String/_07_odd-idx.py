# Remove odd index values
'''REQ: Remove the odd index values'''

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
    

I. REQUIREMENT GATHERING : Remove the odd index values  
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
           remove the odd index values from the string
           Once he clicks on Submit button, display the even value string.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "enter the string which is having more than one character"
               ii. Single word     Ex: "Hello" : "display even value string"
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
    Entity Name: remove the odd char

            State   : Data types/strs:  STRING STRING
           
            Behavior: Operators      :  = % 
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
2. intialise count=0                2. get first and the last char by using slice 
                                                
3. consider only even index value   3. string concatination
4. diplay the even index            4. display the even index value string to user
value string        
           
                                      


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
message = 'Hello python'
s=" "
for i in range(len(message)):
    if message[i]==" ":
        s+=message[i]
    elif i%2==0:
        s+=message[i]
print(s)


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
