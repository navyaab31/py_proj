# Smallest number from list

'''REQ:Smallest number from list'''

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
    

I. REQUIREMENT GATHERING : Smallest number from list 
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
            each element should be string or int 
            get smallest number in the list
            display result to the user.
           
    Scenarios:     Empty list       Ex: ""    : "Invalid list"
                i. Single item      Ex: "H"   : "length of the list is more than one"
              iii. Multiple item    Ex: [1,2,3,4,5,6]
               iv. Comb of string and interger    Ex: [1,25,'hi','45','hello',6,'to'] 
                v. Only Numbers allowed ?  Yes
               vi. strings consider ?: yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: smallest elements from the list 

            State   : Data types/strs:  LIST  ELEMENT
           
            Behavior: Operators      : =  <
                      DM             : if
                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
l=[1,2,3,4,5,6,7]                       list1 = [1,2,3,4,5,6,7]
    
                                    BEHAVIOR:
                                    ----------
2. take the first ele               2. use the for loop traverse through list
                                                
3. compare with next ele            3. compare the each ele with the next ele     
    if it first ele is greater              if it is greater swap
    swap the ele                                                                
4. diplay result to the user        4. display result to user        
           
                                      

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
list1 = [1,2,3,6,7,4,5]  # static way
print("smallest element is:",min(list1))


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
# list1= [1,2,3,4,5,6]
if list1=="":
    print("empty list")
elif len(list1)==1:
    print("length of the list1 is more than one")
else:
    l1=[7,6,1,2,8,3,4]
    mn=l1[0]
    for i in l1:
        if mn>i:
            mn=i
    print("smallest element is:",mn)
        

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
