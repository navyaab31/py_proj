# remove existing indentation from all of the lines in a given text
'''REQ: remove the existing indentation from string'''

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
    

I. REQUIREMENT GATHERING : remove the existing indentation from the string. 
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
           remove the indentation from the string
           Once he clicks on Submit button, indentation removed string.
           
    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "Enter at least 2 characters"
               ii. Single word     Ex: "Hello" : "you have enter the multiple lines"
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
   input:multiple lines               input:multiple lines
    
                                  BEHAVIOR:
                                  ----------
2. check if indentation is there.  2. split the line
3. if we have remove               3. remove the space traverse through the loop
4. display indentation removed     4. display indentation removed string to user
    string to user        
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

message = 'Hello World'  # static way
# message = input("Enter any string : ")
# no built-in methods


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
message = '''Enumerating objects: 5, done.
        Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
            Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 302 bytes | 302.00 KiB/s, done.
        Total 3 (delta 2), reused 0 (delta 0), pack-reused 0'''.split("  ")

# BEHAVIOR
l1=[]
for i in message:
    print(i)
    # for j in i:
    if i!='':
        l1.append(i)
        print(l1)
print("".join(l1))

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
