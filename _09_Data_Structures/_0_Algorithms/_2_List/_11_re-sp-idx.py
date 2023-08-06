# Remove specified index from list and print

'''REQ:remove specified index from list'''

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
    

I. REQUIREMENT GATHERING : remove specific index from list 
        ------------------------------------
        |    Enter list: |_________|        |
        |      index:|________|             |               
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
                i. Single item      Ex: "H"   : "length of the list is more than one"
              iii. Multiple item    Ex: [1,2,3,4,5,6] "remove the index of ele"
               iv. Comb of string and interger    Ex: [1,25,'hi','45','hello',6,'to'] 
                v. Only Numbers allowed ?  Yes
               vi. strings consider ?: yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: remove the specific index from list 

            State   : Data types/strs:  LIST  INDEX(INT)
           
            Behavior: Operators      : =  ==
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
   index=2                              index=2
                                    BEHAVIOR:
                                    ----------
2. initialise index =0               2. use the for loop traverse through list
                                                
3. increase each ele by one          3. compare index values if present remove     
    if index=sp-index remove ele              
    swap the ele                                                                
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
list1.pop(3)
print(list1)


# 2. Algorithm ***

print("--------2. Algorithm ***----------")
 # STATE
# list1= [1,2,3,4,5,6]
index=2
if list1=="":
    print("empty list")
elif len(list1)==1:
    print("length of the list1 is more than one")
else:
    for i in range(len(list1)):
        if i==index:
            del list1[i]
        

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
