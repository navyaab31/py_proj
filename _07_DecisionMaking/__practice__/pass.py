'''
entity:password
------------------
STATE:
Attributes: password
values: characters,number,special caharacter
type:   str   ,   int   ,   str

# REQ: print if password is valid

state: given password
behaviour: print it
            ==> if it is having a length 8
            ==> if it is having a Uppercase
            ==> if it is having a Lowercase
            ==> if it is having a special caharacter

Functional Analysis:
-----------------------
1.user enter the pass word
2.check if it satisfies a all the condition the print it


Technical Analysis:
--------------------------
1. STATE : Datatypes/Datastructures  :user enter the password
2. BEHAVIOR  : operatord , DM  ,  Loops  :check if it valid
                >=,==      if elif else

entity : Customer
State : given password
brhavior: print it if it is valid
            ==> if it is having a length 8
            ==> if it is having a Uppercase
            ==> if it is having a Lowercase
            ==> if it is having a special caharacter

'''
password=input("enter the password: ")
def passwrd(password):
    if len(password)==8:
        if "A"<=password<="Z":
            if "a"<=password<="a":
                if 0<=password<=9:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else: return False

print("password is valid" if passwrd(password) else "not a valid password")
