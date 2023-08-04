# Mulitply of elements

'''REQ: multiply of the elements in the list'''

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
    

I. REQUIREMENT GATHERING : multiply of the elements in the list 
        ------------------------------------
        |    Enter list: |_________|        |
        |                                   |               
        |            Submit                 |
        |___________________________________|
        
II. ANALYSIS:
==============
    1. Functional Analysis:
    -------------------------
    Notes: Customer will give a list which can contain any  no. elements
            that is integer if it's a numerical string convert into a integer
           multiply all elemets in the list display the result multiple of all the 
           elements in the list
           
    Scenarios:     Empty list       Ex: ""    : "Invalid list"
                i. Single item      Ex: "H"   : "length of the list is more than one"
              iii. Multiple item    Ex: [1,2,3,4,5,6,7]
               iv. Comb of chars    Ex: "Hello1234%^&%$!bangalore" 
                v. Only Numbers allowed ?  Yes
               vi. strings consider ?: No
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: multiply of all the elements in the list

            State   : Data types/strs:  LIST  INTEGER
           
            Behavior: Operators      : =  *

                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
    l=[1,2,3,4,5]                    list1 = [1,2,3,4,5]
    
                                    BEHAVIOR:
                                    ----------
2. initialise mul=1             2. use the for loop traverse through list
                                                
3. multiply all the item        3. find the mul of item
in list     

4. diplay result to the user       4. display result to user        
           
                                      

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
list1 = [1,2,3,4,5,6]  # static way
# message = input("Enter any string : ")
# no inbuilt method

# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
# list1= [1,2,3,4,5,6]
if list1=="":
    print("empty list")
elif len(list1)==1:
    print("length of the list1 is more than one")
else:
    mul=1
    for i in list1:
        if type(i)!=int:
            mul*=int(i)
        else:
            mul*=i
print(mul)

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
