#  find the maximum occurring character in a given string

'''REQ: find the maximum occurring character in a given string'''

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
    

I. REQUIREMENT GATHERING : find maximum occurring character in a given string. 
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
           reverse each world in the string 
           Once he clicks on Submit button, diaplay string.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "Enter at least 2 characters"
               ii. Single word     Ex: "Hello" : "display maximum occuring char"
              iii. Multiple words  Ex: "Hello World Welcome to Python"
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Including space?  ==> no
               vii. Only Numbers allowed ?  Yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: StringLength

            State   : Data types/strs:  STRING char
           
            Behavior: Operators      :  =  +=  
                        DM           : if else
                      Loops          :  Yes (For Loop)

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
   str1=hello python                   str1=hello python
    h=2     o=2   n=1
    e=1     p=1
    l=2     t=1
                                    BEHAVIOR:
                                    ----------
2. take each char update to table  2. use the for loop to itirate string  
3. select max count char           3. get count of each char select the max count char 
4. display char to user            4. display char to user
         
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

message = 'Hello python'  # static way
# message = input("Enter any string : ")
# no built-in method


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
# message = "hello 123"

# BEHAVIOR
if message=="":
    print("empty strong")
elif len(message)==1:
    print("string length is more than one")
else:
    s="hello python hi"
    d={}
    for i in s:
        if i ==" ":
            continue
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    val=0
    key=0
    for i in d:
        if d[i]>val:
            val=d[i]
            key=i
    print(key)
    
# print(s)

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
