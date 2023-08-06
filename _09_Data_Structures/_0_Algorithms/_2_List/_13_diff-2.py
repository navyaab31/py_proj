# Difference betweeen 2 lists

'''REQ:Difference between 2 list '''

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
    

I. REQUIREMENT GATHERING : diffrence between two list 
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
            
            display result to the user.
           
    Scenarios:     Empty list       Ex: ""    : "Invalid list"
                i. Single item      Ex: "H"   : "Invalid ele"
              iii. Multiple item    Ex: [1,2,3,4,5,6] "diplay the result"
               iv. Comb of string and interger    Ex: [1,25,'hi','45','hello',6,'to'] 
                v. Only Numbers allowed ?  Yes
               vi. strings consider ?: yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: remove the specific index from list 

            State   : Data types/strs:  LIST  LIST
           
            Behavior: Operators      : =  in
                      DM             : if
                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
l1=[10, 15, 20, 25, 30, 35, 40]         l1=[10, 15, 20, 25, 30, 35, 40]
l2=[25, 40, 35]                         l2=[25, 40, 35]
                                 
                                    BEHAVIOR:
                                    ----------
2. take two lists                   2. use the for loop traverse through lists
                                                
3. check all the ele in list1       3. check all the elements in list1 are in list2     
    are in list2               
4. diplay result to the user         4. display result to user        
           
                                      

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
# no built-in method


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
# STATE
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
# list1= [1,2,3,4,5,6]
if list1=="" or list2=="":
    print("empty list")
else:
    l1=[]
    for i in list1:
        if i not in list2:
            l1+=[i]
    print(l1)


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
