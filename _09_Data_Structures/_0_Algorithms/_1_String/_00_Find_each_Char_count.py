'''2. Find how many times each character is repeated in string '''
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


I. REQUIREMENT GATHERING : Check how many times each character got repeated in String 
        ------------------------------------
        |    Enter String: |_________|      |
        |            Submit                 |
        |___________________________________|

II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give String, Here we should count each character
    how many times it got repeated and should display result with characater
    and its count. 

    Scenarios:     Empty string    Ex: ""    : "Invalid String"
                i. Single char     Ex: "H"   : "Enter at least 2 characters"
               ii. Single word     Ex: "Hello" ==>  H:1, e:1, l:2, o:1
              iii. Multiple words  Ex: "Hello World Welcome to Python"
                                               ==> H:2, e:2...... " ":4
               iv. Comb of chars   Ex: "Hello1234%^&%$!bangalore"
                v. Multiline string Ex:  "hello world, bangalore, python 
                                         hello programming 
                                         world language
                                         "
               vi. Including space?  ==> Include
               vii. Only Numbers allowed ?  Yes
               viii. Special chars   ==> No


    2. Technical Analysis:
    ------------------------
    Entity Name: CharCount

            State   : Data types/strs:  STRING INT DICT

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
   'Hello World'                     str1 = 'Hello World'

                                  BEHAVIOR:
                                  ----------
2. Initial char count with table.            2. Initialize counter as 0
3. Traverse through each char     3. Use for loop to iterate through each char
4. Check current char in table or not.       4. Increment count var in each iteration
   If char in table increment counter.
   Else initialize char with count as 1
5. Print char count from table                            (Operators / Loops)

    Helloworldwelcometopython 
    
    
'''

'''
IV. DEVELOPMENT:
=================
        1. Builtin Functions
        2. Algorithm **
        3. Functions  
        4.OOPS     5. EH      6. FH       7.Database  8. UI 
'''
# 1.Builtin functions

print("-----1. Builtin Functions--------")

message = 'Hello World'  # static way
# message = input("Enter any string : ")

print("No Builtin Function : ")

# 2. Algorithm ***
print("--------2. Algorithm ***----------")
# STATE
message = 'Hello World Welcome Python #@$#@324324'

# BEHAVIOR
c_count = {}
if len(message) == 0:
    print("Invalid String")
elif len(message) == 1:
    print("Enter at least 2 characters")
else:
    for char in message:
        # Validation logic
        if char not in c_count.keys():
            c_count[char] = 1
        else:
            c_count[char] += 1
    print("Dictionary is : ", c_count)
    for ch, count in c_count.items():
        print(ch, "repeated : ", count, " times")





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
