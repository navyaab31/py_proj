# Last part of string
'''REQ: last part of the string'''

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
    

I. REQUIREMENT GATHERING : last part of the string  
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
           Once he clicks on Submit button, display last part of the string.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "string length is more than one"
               ii. Single word     Ex: "Hello" : "display last part of the string"
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
    Entity Name: last part of the string

            State   : Data types/strs:  STRING INT
           
            Behavior: Operators      : =  
                     
                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
    'HellO PyThon'                    str1 = 'HellO PyThon'
    
                                    BEHAVIOR:
                                    ----------
2. count char in string             2. Traverse through the for loop/use slice
                                                
3. select last part                 3. get the last part 

4. diplay the last part to the user 4. display the last part to user        
           
                                      

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
message = 'HellO PyThon'  # static way
# message = input("Enter any string : ")
# no built-in

# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'HellO PyThon'
if message=="":
    print("empty strong")
elif len(message)==1:
    print("string length is more than one")
else:
    s=''
    for i in message[::-1]:
        if i ==" ":
            print(s)
            break
        s=i+s


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
