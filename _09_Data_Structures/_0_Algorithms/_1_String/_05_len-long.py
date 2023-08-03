# length of the longest string
'''REQ: length of the longest string'''

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
    

I. REQUIREMENT GATHERING : length of the longest string  
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
           find the length of the longest string
           Once he clicks on Submit button, display substring(longest).
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "enter the string which is having more than one character"
               ii. Single word     Ex: "Hello" : "display substring(longest)"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: length of the longest substring

            State   : Data types/strs:  STRING INT
           
            Behavior: Operators      :  = +=  
                      DM             :  if 
                      Loops          :  Yes (For Loop)

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
'Hello World hello python'            str1 = 'Hello World hello python'
    

                                    BEHAVIOR:
                                    ----------
2.Count the length of the each      2. initialise dict 
   word in string                   3. use for loop to traverse count the length of the each word in the string            
3. check which one is logest        4. chech which is longest
4. diplay the len of                5. display the len of the sunstring to user
        substring to user          
                                      


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
message = 'Hello world hello python'  # static way
# message = input("Enter any string : ")
# no bulit in methods


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'hello world Hello python'.split()
ans=0
for i in range(len(message)-1):
    # print(len(message[i]))
    if len(message[i])>len(message[i+1]):
        ans=len(message[i])
    else:
        ans=len(message[i+1])
print(ans)


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
