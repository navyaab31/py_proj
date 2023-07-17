'''
# 1.REQ: Watching movie

2. Analysis:
-----------------
    Functional Analysis:
        -choose watching move or web series 
            -watching movie
                -check OTT/theatre/TV/Mobile or laptop
                -OTT==> Amazon/netflix
                -theatre==>book ticket
                        -online -choose Google pay/phone pay/paytm
                -TV==>Watch the movie in home
                -mobile/laptop==>choose the movie in list nd watch
            -watching webseries
                -choose the OOT :Amazon/netflix
        -warch the serials 
    
    Technical Analysis:
        STATE: string
        BEHAVIOR: Create
                : validations
                : Business logic
                    -operators   :  == !=
                    -Decision Making : if 
                                            if 
                                                if 
                                                    if
                                            elif
                                                if
                                                    if
                                            
                                        else
                    -loops          :NO

'''
# STATE
u_input=input("enter your choice: ")

# BEHAVIOR
# 1.validation
if u_input=="movie":
    print("option: 1.OTT 2.Theater")
    opt=input()
    if opt=="1":
        print("select Amazon/Netflix:")
        print("watch movie!!")
    elif opt=="2":
        print("book a ticket: 1.online 2.cash")
        b_t=input()
        if b_t=="1":
            print("book a ticket through a online payment.")
        else:
            print("take a ticket in theater")
    else:
        print("see the movie in TV")
else:
    print("watch serials")

# =====================><=========================
'''
REQ: employee salary hike 

2. Analysis
---------------------
Functional Analysis:
    -enter the salary
    -enter ratings
    -check the ratings
        -rating is 1 ==>10%
        -rating is 2 ==>20%
        -rating is 3 ==>30%
        -rating is 4 ==>40%
        -rating is grater than 5 ==> 50%
    -invalid rating
'''

