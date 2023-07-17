check_prime = int(input("enter a num:  "))
flag = True
if check_prime == 2:
    flag = True

for i in range(3,check_prime):
    #print(f"i is {i}")
    # for j in range(1,i):
        #print(f"j is{j}")
    # print(check_prime%i)
    if check_prime%i == 0:
        flag = False
        break
    else:
            
        flag = True
if flag == True:
    print("prime")
else:
    print("not prime")