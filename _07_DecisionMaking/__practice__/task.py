# Python program that takes an input from the user and determines if it is an even number or an odd number.

'''
# REQ:check if user given number is prime or not

state: user given number
Behavior: check it
            ==> if is prime or not

Functional Analysis:
----------------------
1.user will give number   :STATE
2. check if it is prime or not   :Behavior
3. if val%2==0 print "prime" else "not prime"

Technical Analysis:
---------------------
1.STATE   : Datatypes/Dtastructures  :user given number   
2.BEHAVIOR: operators,              :check if it prime or not
            %  ==     
            DM, Loops 
                if <conditon>:
                    pass
                else:
                    pass
entity  : User
state   :given number
behavior:check and print number is prime or not

'''
n=int(input("enter the number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")

'''
REQ: check the person is minor or adult or citizen.

state: customer given age
Behavior: print 
            ==> if age less than 18 -minor
            ==> if age between 18-65 -adult
            ==> if age greater than 65 -senior citizen

Functional Analysis:
----------------------
1. customer will give age   :STATE
2. check if age is less than, between, greater than  :Behavior
3. if age<18 ==>print-minor
   if 18<=age<=65  ==>print-adult
   if age>65 ==>print-senior citizen

Technical Analysis:
---------------------
1.STATE     :Datatypes/Datastructures   :customer given number
2.BEHAVIOR  :Operators
                <= >=
            DM
                if <condition>:
                    pass
                elif <condition>:
                    pass
                elis <condition>:
                    pass
'''

# create a program that prompts the user to enter their age. Based on the input, the program should display different messages according to the following conditions:

# If age is less than 18: "You are a minor."
# If age is between 18 and 65: "You are an adult."
# If age is 65 or older: "You are a senior citizen."

age=int(input("enter the age: "))
if age<18:
    print("you are a minor")
elif 18<=age<=65:
    print("you are an adult")
else:
    print("you are a senior citizen")
'''
# REQ: Calculates the discount amount for the shopping cart

state: given total amount
Behavior: calculated discount amount and print it 
            ==>if total amount >= 100 discount 10%
            ==>if total amount 50-99.99 discount 5%
            ==>if total amount < 50 no discount

Functional Analysis:
----------------------
1. Given total amount    :STATE
2. check if it is greater than, between, less than  :Behavior
3. print discount amount

Technical Analysis:
----------------------
1.STATE: Datatypes/Datastrctures    : given total amount
2.BEHAVIOR: Operators
            > <= <
            DM
            if <condition>:
                pass
            elif <condition>:
                pass
            elif <condition>:
                pass
'''
# should develop a program that calculates the discount amount for a shopping cart based on the following conditions:

# If the total price is greater than or equal to $100, apply a 10% discount.
# If the total price is between $50 and $99.99, apply a 5% discount.
# If the total price is less than $50, no discount is applied.

total_price=float((input("enter the total price: ")))
if total_price >= 100:
    print(total_price+(total_price*0.1))
elif 50<=total_price<=99.99:
    print(total_price+(total_price*0.1))
else:
    print("no discount is applied")
'''
REQ:simulate simple quiz, keep track of their score

state: answer to the question
Behavior: check answer is correct or not
            ==>print score in percentage

Functional Analysis:
----------------------
1.user will answer to the question  :STATE
2.check that answer is correct or not  :Behavior
3. if correct add the marks ==>print score

Technical Analysis:
---------------------
1.STATE: Datatypes/Datastructures  :user gives answer
2.BEHAVIOR: Operators
             + =
            DM
                if <condition>:
                    pass
                    add the marks
'''
# 4.create a program that simulates a simple quiz. The program should present a series of multiple-choice questions to the user 
# and keep track of their score. 
# At the end of the quiz, display the user's score as a percentage.
print("Quiz")
score=0
print("1.Which of the following is not valid variable name in Python?")
print(" 1._var 2.var_name 3.var11 4.11var")
ans1=int(input("ans: "))
if ans1==4:
    score+=1
# print(score)
print("2.Which of the following will give error?")
print(" 1.a=b=c=1 2.a,b,c=1 3.a,b,c=1, python, 1.5 4.None of the above")
ans2=int(input("ans: "))
if ans2==2:
    score+=1
# print(score)
print("3.How many keywords are there in python 3.7?")
print(" 1.32 2.33 3.31 4.30")
ans3=int(input("ans: "))
if ans3==2:
    score+=1
# print(score)
print("4.All keyword in python are in.")
print(" 1.Lowercase 2.Uppercase 3.Both uppercase & Lowercase 4.None of the above")
ans4=int(input("ans: "))
if ans4==3: 
    score+=1
print("total percentage is: ",(score/4)*100)

'''
# REQ: Guess the random number

state: user will guess the number
behavior: check if guessed number is equals to random number or not
            ==>if it is correct guess print==>guess is correct

Functional Analysis:
---------------------
1. customer will the number   :STATE
2. chech that number is correct or not   :Behavior
3.if it correct ==>print guess is correct
            else==>mention it is far or near

Technical Analysis:
----------------------
1.STATE: Datatypes/Datastructures    :customer enter guessed number
2.BEHAVIOR: Operators
                == > <
            DM 
                if r==g:
                    pass
                elif <condition>:
                    pass
                elif:
                    pass
'''
# 5.create a program that generates a random number between 1 and 100. 
# The user should guess the number, and the program should provide feedback on whether the guess is too high or too low. 
# The program should continue until the user guesses the correct number.
import random
# play="Y"
while True:
    num=(int(input("guess the number: ")))
    n=random.randint(1,100)
    if num<n:
        print("guess is too low")
    elif num>n:
        print("guess is too high")
    elif num==n:
        print("correct")
        break
    # print(n)
'''
# REQ:print sum of given number, if values are equals print 3*sum

State: User enter the three number
Behavior: check if numbers or equal or not
        ==>if equals print-3*sum
        ==>else print-sum

Functional Analysis:
----------------------
1. user will enter the three number  :STATE
2. check if the three numbers are equals nor not   :Behavior
3. if equals ==>print 3*sum
        else:==>print sum

Technical Analysis:
---------------------
1.STATE: Datatypes/Datastructures     :given three numbers
2. BEHAVIOR: Operators
                + == =
            DM
                if n1==n2==n3:
                    pass
                else:
                    pass
'''
# 6. Calculate the sum of three given numbers, if the values are equal then return thrice of their sum
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if num1==num2==num3:
    print("sum is: ",3*(num1+num2+num3))
else:
    print("sum is: ",num1+num2+num3)

'''
REQ:chech the number is singal,two ,or three number

state: user enter a number
Beahvior: count the digits in number
            ==>print singal,two,three digit number

Functional Analysis:
----------------------
1. user will enter a number
2. chech if the number is single,two,three digit number
3. if it is single digit==> print singal digit number
            two digit==>print two digit number
            three digit==>print three digit number

Technical Analysis:
---------------------
1. STATE: Datatypes/DataStructures   :user enter the number
2. BEHAVIOR: Operators
                == % // +
            DM
                if elif
            Loop
                while
            while <condtion>:
                pass
            if <condition>:
                pass
            elif <condition>:
                pass
            elif <condition>:
                pass
'''
# 7. Python program to test whether a number is within 100 of 1000 or 2000.
n=int(input("enter the numner: "))
count=0
while n>0:
    # rem=n%10
    count+=1
    n=n//10
print(count)
if count==1:
    print("it a single digit number")
elif count==2:
    print("it's a two digit number")
elif count==3:
    print("it's a 3 digit number")
elif count==4:
    print("it's a 4 digit number")

'''
# REQ: given list count the specified number

state: given list and specified number
Behavior: check if the number is in list or not
        ==> print if it present in the list

Functional Analysis:
-----------------------
1. user enter the list and the number
2. check if the number is in list
3. if present 
    ==>print number

Technical Analysis:
---------------------
1. STATE   :Datatypes/Datastrucutre   :user enter list and number
2. BEHAVIOR:Operators
            =
            DM 
                if <condition>:
                    pass
                else:
                    pass
            Loops:
                for var in range():
                    if <condition>:
                        PASS
                
'''
# 8. Python program to count the number 4 in a given list.
l1=[2,3,4,5,6,7]
count=0
for i in range(len(l1)):
    if l1[i]==4:
        count+=1
        print(f"number: {l1[i]}  index: {i} count: {count}")
'''
# REQ: test passed letter is vowel or not

state: user will enter the letter
Behavior: check if that number is vowel or not
        ==>if it is vowel, print vowel

Functional Analysis:
----------------------
1. user will enter the letter   :State
2. check if it is vowel or nor   :Behavior
3. if it is vowel ==> print its vowel

Technical Analysis:
-----------------------
1. STATE: Datatypes/Datastructure   :user entered letter
2. BEHAVIOR: Operators              :check if letter is vowel or not
                == in
            DM
                if <condition>:
                    pass
                else:
                    pass

'''
# 9.Python program to test whether a passed letter is a vowel or not
n=input("enter the letter: ")
if n in ['a','e','i','o','u']:
    print("it's vowel")
else:
    print("not vowel")

'''
REQ: check their age and determines if they are eligible to vote or not

state: user enter the age
behavior: check age if it is greater than 21
            ==>print eligible

Functional Behavior:
1. user will enter the age          :STATE
2. check if age is greater than 21  :Behavior
3. if age>=21 print==> eligible

Technical Analysis:
1.STATE: Datatypes/Datastructure        :user enter the age
2.BEHAVIOR: Operators
                >=
            DM
                if <condition>:
                        pass
                else:
                    pass

'''

# 10. Voting Eligibility
# Description: Write a program that prompts the user to enter their age and determines if they are eligible to vote or not.
# Example Input: 21
# Example Output: "You are eligible to vote."

age=int(input("enter the age: "))
if age<18:
    print("not eligible to vote")
else:
    print("you are eligible to vote")
'''
REQ: check leap year or not

state: user enter year
Behavior: check if it is leap year or not
            ==>print leap year or not

Functional Analysis:
------------------------
1.user will enters the year         :state
2.check if it is leap year or not   :behavior
3. if year==leap ==>print it

Technical Analysis:
----------------------
1.STATE: Datatypes/Datastructure        :user enter the year
2.BEHAVIOR: Operators                   :check year is leap year or not
                % == !=
            DM
                if <condition>:
                    pass
                else:
                    pass

'''

# 11. Leap Year Checker
# Description: Create a program that checks if a given year is a leap year or not.
# Example Input: 2024
# Example Output: "2024 is a leap year."
year=int(input("enter the year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not leap year")


# 12. Grade Calculator
# Description: Develop a program that accepts a student's score as input and returns their corresponding grade according to a grading scale.
# Example Input: 87
# Example Output: "Your grade is B."
score=int(input("enter the score: "))
if score>90:
    print("your grade is A")
elif 80<=score<=89:
    print("your grade is B")
elif 70<=score<=79:
    print("your grade is c")
else:
    print("your grade is D")


# 13. BMI Calculator
# Description: Create a program that calculates a person's Body Mass Index (BMI) based on their height and weight.
# Example Input: Height = 1.75m, Weight = 68kg
# Example Output: "Your BMI is 22.2."
height=float(input("height: "))
weight=float(input("weight: "))
print("your BMI is ",round(weight/(height**2),2))




# 14. Data Validation
# Description: Develop a program that validates user input to ensure it meets specific criteria (e.g., length, format).
# Example Input: "abc123"
# Example Output: "The input is valid."
n=input("enter the input: ")
if n.isalpha():
    print("enter correct input")
elif n.isnumeric():
    print("not valid")
elif n.isalnum():
    print("the input is valid")


# 15. Temperature Converter
# Description: Write a program that converts a given temperature from Celsius to Fahrenheit or vice versa.
# Example Input: 32°F
# Example Output: "0°C"
# C = 5/9(F-32)
# °F = (°C x 1.8) + 32
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

fahrenheit=float(input("enter temperature in fahrenheit: "))
celsius = 5/9*(fahrenheit-32)
print("%.2f fahrenheit is: %0.2f celsius" %(fahrenheit,celsius))


# 16. User Authentication
# Description: Create a program that verifies a user's login credentials (e.g., username and password).
# Example Input: Username = "john_doe", Password = "pass123"
# Example Output: "Login successful."
t1=("john_doe",'pass123')
username=input("enter the user name: ")
password=input("enter the password: ")
if username==t1[0] and password==t1[1]:
    print("login successful")
else:
    print("wrong input")



# 17. String Manipulation
# Description: Develop a program that performs different operations on a given string based on user input (e.g., length, reverse, uppercase).
# Example Input: "Hello, World!"
# Example Output: "The string has 13 characters."
s=input("enter the string: ")
print("length of the string ",len(s))
s2=" "
s1=" "
for i in s:
    s1=i+s1
    if ord(i)>=97 and ord(i)<=122:
        i=chr(ord(i)-32)
        # print(i)
        s2+=i
    else: s2+=i
print("Upper Case:",s2)

print("Reverse: ",s1)


# 18. Discount Calculator
# Description: Create a program that calculates the final price of a product after applying a discount.
# Example Input: Original price = $100, Discount percentage = 20%
# Example Output: "The final price is $80."

original_price=int(input("original value: "))
discount_percentage=20

if original_price>=100:
    print("discount add")
    final= round(original_price-(original_price*20)/100,2)
    print("the final price is ",final)
else:
    print("no discount")


# 19. Email Validation
# Description: Create a program that validates if a given email address is correctly formatted.
# Example Input: "john.doe@example.com"
# Example Output: "The email address is valid."
t1=("john.doe@example.com")
email=input("enter the mail: ")
if email==t1:
    print("valid email")
else:
    print("invalid email")

# 20. Number System Converter
# Description: Develop a program that converts a given number from one number system to another (e.g., binary to decimal).
# Example Input: Binary number = "10101"
# Example Output: "The decimal equivalent is 21."

n=int(input("enter the binary number: "))
dec=0
p=0
while n>0:
    rem=n%10
    dec=rem*2**p+dec
    p+=1
    n=n//10
print(dec)


# 21. Rock, Paper, Scissors Game
# Description: Write a program that allows two players to play the classic game of rock, paper, scissors and determines the winner.
# Example Input: Player 1: "rock", Player 2: "scissors"
# Example Output: "Player 1 wins!"
# player1=input("enter your choice: ")
# player2=input("enter your choice: ")
player1_count=0
player2_count=0
play="Y"
while play=="Y":
    player1=input("enter your choice: ")
    player2=input("enter your choice: ")
    if player1=="rock" and player2=="scissors":
        print("player1 wins")
        player1_count+=1
    elif player1=="scissors" and player2=="paper":
        print("player1 wins")
        player1_count+=1
    elif player1=="paper" and player2=="rock":
        print("player1 wins")
        player1_count+=1
    else:
        print("player2 wins")
        player2_count+=1
    print("do you want to play again (Y/N): ")
    play=input().upper()
    # if ord(player1)==32 or ord(player2)==32:
    #     break

print("score of player1: ",player1_count)
print("score of player2: ",player2_count)


# 22. Currency Converter
# Description: Create a program that converts an amount of money from one currency to another based on current exchange rates.
# Example Input: Amount = $100, Currency = USD to EUR
# Example Output: "The converted amount is €85.62." 
# 1 USD = 0.898877 EUR
# 1 EUR = 1.112499263 USD
Amount=int(input("enter the amount: "))
currency=input("USD TO: ").upper()
if currency=="EUR":
    con_amount=round(Amount*0.89,2)
    print("the converted amount is: ",con_amount)
elif currency=="EUR":
    con_amount=round(Amount*82.4)
    print("the converted amount is: ",con_amount)


# 23. Password Strength Checker
# Description: Develop a program that evaluates the strength of a user's password based on certain criteria (e.g., length, complexity).
# Example Input: "Pa$$w0rd"
# Example Output: "The password is strong."
password=input("enter the password: ")
U,S,I=False,False,False
for i in password:
    if "A"<=i<="Z":
        U=True
    elif "a"<=i<="z":
        S=True
    elif "0"<=i<="9":
        I=True
if S and U and I and len(password)==8:
    print("it's a strong password")
else:
    print("not strong password")


# 24. Error Handling
# Description: Write a program that handles different types of errors and displays appropriate error messages to the user.
# Example Input: "5" (when expecting an integer)
# Example Output: "Invalid input. Please enter a valid integer."
n=input("enter the input: ")
if n=="1":
    print("invalid input. please enter a valid integer")
elif n=="2":
    print("attribute assignment is failed")
elif n=="3":
    print("the variable is not defined.")
elif n=="4":
    print("the wrong index of a list is retrieved.")


# 25. Game Character Decision-Making
# Description: Create a program that simulates decision-making for a game character based on different scenarios (e.g., fight or flee, choose a weapon).
# Example Input: Scenario = "Encounter enemy"
# Example Output: "You decide to fight the enemy."
print("welcome to the game")
print("let start the game with your name")
name=input()
print("good luck" +name+ ".")
scenario=["fight","flee"]
print("option: fight/flee")
userinput=input()
if userinput==scenario[0]:
    print("you have decided to fight the enemy")
    print("choice the a weapon")
    print("1/2/3")
    weapon=['1','2','3']
    wep=input()
    if wep=='1' or wep=='2' or wep=='3':
        print("fight!!!")
elif userinput==scenario[1]:
    print("flee")
else:
    print("you didn't choice anything...")
        
