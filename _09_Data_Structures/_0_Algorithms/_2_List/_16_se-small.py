# Finding a second smallest number

'''REQ:second smallest number in the list'''

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
    

I. REQUIREMENT GATHERING : seconf smallest number ele in the list 
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
              iii. Multiple item    Ex: [1,2,4,5,6] "diplay the result"
               iv. Comb of string and interger    Ex: [1,25,'hi','45','hello',6,'to']  
                v. Only Numbers allowed ?  Yes
               vi. strings consider ?: yes
               
                                         
    2. Technical Analysis:
    ------------------------
    Entity Name: Append list to second list 

            State   : Data types/strs:  LIST  ELEMENT
           
            Behavior: Operators      : =  >
                    
                      LOOPS          :for

III. DESIGN (Sequence Diagrams):
=================================
Mathematics:                       Programming Language:
==========================        ============================= 
                                  STATE:
                                  ------
1. Write it on paper              1. Define string 
l1=[10, 15, 20,25, 30]                  l1=[10, 15, 20,25, 30] 
    
                                 
                                    BEHAVIOR:
                                    ----------
2. check each ele in list       2. use the for loop traverse through lists
                                                
3. get second smallest           3. compare the elements get second smallest   
                   
4. diplay result to the user      4. display result to user        
           
                                      

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
# list1 = [1,2,3,6,7,4,5]  # static way
list1=[10, 15, 20,25, 30]
# no built-in methods

# 2. Algorithm ***

print("--------2. Algorithm ***----------")
# STATE
# list1= [1,2,3,4,5,6]
if list1=="":
    print("empty list")
elif len(list1)==1:
    print("length is more than one")
else:
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list[i]>list[j]:
                list1[i],list[j]=list[j],list[i]
    print(list1[1])


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
