# Take 10 integer inputs from user and store them in a list. Again ask user to give a number. 
# Now, tell user whether that number is present in list or not.
n=input("enter the 10 numbers: ")
score=list(map(int,n.split()))
flag=True
num=int(input("enter the number to be search: "))
for i in score:
    if i==num:
        # flag=True
        print(f"{num} is present")
        break
        
    
else:
    print(f"{num} is not present")
    