'''
Valid marks
    - Pass(5)
    - Fail
Invalid marks (<0 >100)



'''
marks = int(input("Enter marks :"))   # Dynamic way

    # 2.BEHAVIOR
if marks < 0 or marks > 100:
    print("------- Invalid marks -------")
else:
    if marks >= 35:
        print("Result is : PASS ")
        if marks >= 60:
            print("First Class")
        elif marks >= 50:
            print("Second Class")
        else:
            print("Third Class")
    else:    # elif marks < 35:
        print("Result is : FAIL ")
print("----------------------------------")
'''
if marks >= 0 and marks <= 100:
    print("Valid Marks")
    if marks >= 35:
        print("Result PASS")
        if marks >= 60:
            print("First Class")
            if marks >= 90:
                print("Distinction")
                if marks == 100:
                    print("Congratulations")
        elif marks >= 50:
            print("Second Class")
        else:
            print("Third Class")
    else:
        print("Result FAIL")
else:
    print("Invalid Marks")
'''

#  Student result:  Validation, Pass/Fail, First/Second/Third Distinction Cent marks

# STATE
marks = int(input("Enter marks3 : "))

if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:
        print("Result PASS")
        if marks >= 60:
            print("---First Class---")
            if marks == 100:
                print("CENT Marks... Congratulations")
        elif marks >= 50:
            print("---Second Class---")
        else:
            print("---Third Class----")
    else:
        print("Result FAIL")
else:
    print("Invalid marks")


print("--------------End of DM-------------------")


# BEHAVIOR

if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:

        print("Result is PASS")
        if marks >= 60:
            print("---First Class--")
            if marks >= 90:
                print("Distinction")
                if marks == 100:
                    print("Cent marks")
        elif marks >= 50:
            print("---Second Class--")
        else:
            print("---Third Class---")
    else:
        print("Fail")
else:
    print("Invalid marks")


print("-----Employee Salary Hike Program------------------")

sal = int(input("Enter salary : "))
rating = int(input("Enter rating : "))

if rating >= 1 and rating <= 5:
    print("Valid Rating")
    if rating == 1:
        incr = sal * 10/100
        sal += incr
    elif rating == 2:
        pass   # 20% hike
    elif rating == 3:
        pass  # 30 hike
    elif rating == 4:
        pass  # 40% hike
    else:
        pass  # 50% hike
    print("Final salary : ", sal)
else:
    print("Invalid Rating")