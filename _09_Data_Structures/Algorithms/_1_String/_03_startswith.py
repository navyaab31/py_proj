# program to check whether a string starts with specified characters
'''REQ: check whether a string starts with specified characters'''

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
    

I. REQUIREMENT GATHERING : string starts with specified characters. 
        ------------------------------------
        |    Enter String: |_________|      |
        |    Enter spc_char: |_______|      |
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           after giving a string they will specifies char we will if string starts with specified character or not
           Once he clicks on Submit button, display True if it starts with specified char otherwise False.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "enter the string which is having more than one character"
               ii. Single word     Ex: "Hello" : "display True of Flase"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: Starts with specified char

            State   : Data types/strs:  STRING BOOL
           
            Behavior: Operators      :  =  ==  
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
    spc_char='l'                     spe_char='l'             
    
                                    BEHAVIOR:
                                    ----------
2.if string contains single       2. if string is single word : check string is start with spe_str
world  check if starts with
spe_char       
3.if string is a sentence check   3. string is sentence split string and check every char through for loop
any word is startswith spe_char.      
                                  4. check if string startswith specified char 
                           
4. diplay the True/False to user  5. display True/False to user     
                                      


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
message = 'Hello'  # static way
# message = input("Enter any string : ")
sub_str='h'            # static way
# sub_str=input("enter sub_string: ")
print("count of sub_str : ",message.startswith(sub_str))

# sentence
message="hello world Hello python"
spe_str='H'
s=spe_str.split()
if len(message)==1:
    print(message[0].startswith(spe_str))
else:
    for i in s:
        if i.startswith(spe_str):
            print("True")

# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'hello world Hello python'.split()
sub_str='H'

# BEHAVIOR

if message=="":
    print("invalid string")
elif len(message)==1:
    if message[0]==sub_str:
        print("True")
else:
    for c in message:
        if c[0]==sub_str:
            print("True") 

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
