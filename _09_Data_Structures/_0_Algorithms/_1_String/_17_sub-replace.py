# Substring replacement

'''REQ: Substring replacement'''

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
    

I. REQUIREMENT GATHERING : substring replacement. 
        ------------------------------------
        |    Enter String: |_________|      |
        |     old_str: |_________|          |
        |     new_str: |________|           |
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           we get some new and old string from user replce old string with new string
           Once he clicks on Submit button, diaplay string.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "Enter at least 2 characters"
               ii. Single word     Ex: "Hello" : "you have enter the multiple lines"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Including space?  ==> Include
               vii. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: StringLength

            State   : Data types/strs:  STRING STRING
           
            Behavior: Operators      :  =  +=  
                     
                      Loops          :  Yes (For Loop)

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
   str1=hello123                        str1=hello123
    old=123 new=python                   old=123 new=python
                                  BEHAVIOR:
                                  ----------
2. find old string in the       2. use the for loop to itirate string
original string       
3. replace old with new string  3. get old string replace old with new string  
4. display string to user       4. display string to user
         
'''


'''
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

message = 'Hello 123'  # static way
# message = input("Enter any string : ")
old="123"
new="python"
print(message.replace("123","python"))


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = "hello 123"

# BEHAVIOR
if message=="":
    print("empty strong")
elif len(message)==1:
    print("string length is more than one")
else:
    message+=" "
    for i in char:
        message+=i
    print(message)


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

