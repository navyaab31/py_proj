# nth index character from string

'''REQ: nth index character from string'''

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
    

I. REQUIREMENT GATHERING : convert given string to upper case 
        ------------------------------------
        |    Enter String: |_________|      |
        |        index: |_______|           |               
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           take index values find the value of the perticular index
           Once he clicks on Submit button, display val of the index.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "string length is more than one"
               ii. Single word     Ex: "Hello" : "display val of the perticular index"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Only Numbers allowed ?  Yes
               vii.space consider ?: yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: convert into upper case

            State   : Data types/strs:  STRING STRING
           
            Behavior: Operators      : =  
                      DM             : if
                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
    'HellO PyThon'                    str1 = 'HellO PyThon'
    index=3
                                    BEHAVIOR:
                                    ----------
2. initialise count=0           2. Traverse through the for loop using range
                                                
3. increase count if count      3. if range==index get the val
= index select that val
4. diplay the val  to user      4. display val to user        
           
                                      

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
index=3
# no inbuilt method

# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'HellO PyThon'
n=3
if message=="":
    print("empty strong")
elif len(message)==1:
    print("string length is more than one")
else:
    for i in range(len(message)):
        if i==n:
            print(message[i])

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
