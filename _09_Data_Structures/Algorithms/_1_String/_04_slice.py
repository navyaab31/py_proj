# slice string
'''REQ: slice string'''

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
        |    start:|_______|,stop:|______|  |
        |     step:|_______|                |
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a string which can contain any  characters
           like numbers, alphabets, special symbols etc., and 
           It might have only one word or full statement or it can be multi line statement.
           then enter the start index stop index and step value
           Once he clicks on Submit button, display substring.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "enter the string which is having more than one character"
               ii. Single word     Ex: "Hello" : "display substring"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: slice string

            State   : Data types/strs:  STRING BOOL
           
            Behavior: Operators      :  =    
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
    start=2                         start=2(bydefault-0)            
    stop=6                          stop=6
    step=1                          step=1(by default=1)

                                    BEHAVIOR:
                                    ----------
2.Count the index from start to     2. traverse index through the for loop 
     end                                stop to stop-1(that is excluded)
                           
3. diplay the substring to user     5. display the sunstring to user     
                                      


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
message = 'Hello world'  # static way
# message = input("Enter any string : ")
start=2
stop=6
step=1            # static way
# sub_str=input("enter sub_string: ")
print("string after the slice : ",message.slice(2,6,1))


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = 'hello world Hello python'
start=2
stop=10
step=1

# BEHAVIOR

if message=="":
    print("invalid string")
elif len(message)==1:
    print("string length is greater than one")
else:
    s=''
    for c in message[2:6:1]:
       s+=c
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
