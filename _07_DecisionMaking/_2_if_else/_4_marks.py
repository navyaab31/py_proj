''''''
# 1. REQ: Get student result based on marks
'''
2. ANALYSIS:
---------------
    Functional Analysis :
       - Get student marks 
       - If marks greater than or equal to 35, result is PASS else FAIL 
       - If marks greater than or equal to 60, first class, 
                  greater than or equal to 50, second class,
                  greater than or equal to 35, third class
       - Distinction
       - Cent marks 
    Technical Analysis :
        STATE : int 
        BEHAVIOR: Create
                : Validations 
                : Business Logic 
                       - Operators      :  == > >=  
                       - Decision Making: if 
                                            if 
                                                if 
                                                    if 
                                            elif 
                                            else 
                                          else 
                                            
                       - Loops           : NO 
'''
# STATE
marks = int(input("Enter marks : "))

# BEHAVIOR
# i.Validation  # -20 230 45 -1 0 1 99 100 101
if marks >= 0 and marks <= 100:
    print("Valid Marks")
    if marks >= 35:  # 34 35 36 20 70
        print("---PASS----")
        if marks >= 60:   # 59 60 61 80 99 100
            print("First Class")
            if marks >= 90:  # 89 90 91
                print("Distinction")
                if marks == 100:
                    print("Congratulations!!!")
        elif marks >= 50:  # 49 50 51
            print("Second Class")
        else:   # 34 35 36 40
            print("Third Class")
    else:
        print("---FAIL----")
else:
    print("Invalid Marks")