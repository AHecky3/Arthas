#!/usr/local/bin/python3.3
#Variables
##Integer Variables
x1 = 0   #Initial X/Y Values#
x2 = 0   #"                "#
y1 = 0   #"                "#
y2 = 0   #"                "#
Rise = 0 #     Y2 - Y1      #
Run = 0  #     X2 - X1      #
direction = '' #Initial Direction Value
time = 0 #Initial Time Value
##Variables For Velocity vs. Time Displacement
lowerY = 0 #The Smaller Y Value#
VVT_Triangle = 0 #Area Under Curve, Triangle at top#
VVT_Base = 0 #Area Under Curve, Base#
VVT_Displacement = 0 #The Total Displacement For VVT (Area Under Curve)
##Variables For Position vs. Time Displacement
PVT_Displacement = 0 #The Total Displacement For PCT (Area Under Curve)
##True/False for Loops                                       |Done? |  | Edited? |  |Default|
gather_Info = True #Sets Main Loop To Getting Info From user |Y/P-GV|  |         |  | True  |
get_Ones = True #Get X/Y(1) information from user            |Y/P-GV|  |*CHANGED*|  | False |
get_Twos = False #Get X/Y(2) information from user           |Y/P-GV|  |         |  | False |
get_Time = False #Get Time information from user             |Y/P-GV|  |         |  | False |
get_Direction = False #Get Direction information from user   |Y/P-GV|  |         |  | False |
var_Confirm = False #Confirm all variables set by user       |Y/P-GV|  |         |  | False |
get_Math_Info = True #Finding other info for math loops      |Y/P-DE|  |*CHANGED*|  | False |
math_Velocity = False #Doing the math to get the slope          | N/A  |  |         |  | False |
math_Acceleration = False #Doing math to get acceleration    | N/A  |  |         |  | False |
math_Displacement = False #Doing math to get displacements   |Y/P-DE|  |         |  | False |
ask_Confirm = False #Asking if sub-info is correct           | N/A  |  |         |  | False |
##Other Variables
VVT_Sloped = "No" #If Displacement Segment is Sloped for VvT
confirm_Yes = ("Yes", "Y", "Ye", "Yea", "Yeah", "Yup") #Acceptable input to say yes
confirm_No = ("No", "N", "Nope", "Naw", "Na") #Acceptable input to say no
usr_Confirm = "" #Asking user for confirmation


#############################################################################################
###                          GATHERING X/Y, TIME, and DIRECTION Info                      ###
#############################################################################################

while gather_Info == True:
    get_Ones = True
    print("\n\nPlease enter the information below. ")
    #Getting X/Y(1) information from user
    while get_Ones == True:
        try:
            x1 = int(input("X1: ")) #User sets X1
            y1 = int(input("Y1: ")) #User sets Y1
            ask_Confirm = True #To Enter Confirm Loop
        except ValueError:
            print("Please enter valid numbers. ")
        #Confirmation Loop
        while ask_Confirm == True :
            usr_Confirm = input("Correct? ").title()
            if usr_Confirm in confirm_Yes: #Changing Variables For Yes
                ask_Confirm = False #Exit Confirm Loop
                get_Ones = False #Have information on Ones
                get_Twos = True #Get Information on Twos
                print()
            elif usr_Confirm in confirm_No: #Changing Variables For No
                ask_Confirm = False #Exit Confirm Loop
                print()
            else: #Else 
                print("Please enter 'Yes' or 'No'. ")


    #Getting X/Y(2) information from user
    while get_Twos == True:
        try:
            x2 = int(input("X2: ")) #User Sets X2
            y2 = int(input("Y2: ")) #User Sets Y2
            ask_Confirm = True #To Enter Confirm Loop
        except ValueError:
            print("Please enter valid numbers. ")
        #Confirmation Loop
        while ask_Confirm == True:
            usr_Confirm = input("Correct? ").title()
            if usr_Confirm in confirm_Yes: #Changing Variables For Yes
                ask_Confirm = False #Exit Confirm Loop
                get_Twos = False #Have Information on Twos
                get_Time = True #Get Information on Time
                print()
            elif usr_Confirm in confirm_No: #Changing Variables For No
                ask_Confirm = False #Exit Confirm Loop
                print()
            else: #Else
                print("Please enter 'Yes' or 'No'. ")


    #Getting Time information from user
    while get_Time == True:
        time = x2 - x1 #Finding Time 
        get_Time = False #Have Information on Time
        get_Direction = True #Get Information On Direction
        print()

    #Getting Direction information from user
    while get_Direction == True:
        direction = input("Direction: ").title() #User Sets Direction
        if (direction == "Positive") or (direction == "Negative"): #If Valid Direction
            get_Direction = False #Have information on Direction
            var_Confirm = True #Get User Confirmation on All Variables
        else :
            print("Please enter 'Positive' or 'Negative' for the direction. ")
        
    #Getting Confirmation On All Variables
    while var_Confirm == True:
        print("\n---------------------------------")
        print(" |          VARIABLES          |  ")
        print("--------------------------------- ") 
        print("       X1: " + str(x1), end="   |   ")
        print("X2: " + str(x2))
        print("       Y1: " + str(y1), end="   |   ")
        print("Y2: " + str(y2))
        print("       Time: " + str(time) + " seconds. ")
        print("       Direction: " + direction)
        print()
        #Confirmation Loop
        print("Is This Information Correct? ")
        ask_Confirm = True
        while ask_Confirm == True:
            usr_Confirm = input("Correct? ").title()
            if usr_Confirm in confirm_Yes: #Changing Variables For Yes
                ask_Confirm = False #Exit Confrim Loop
                var_Confirm = False #Have users confirmation
                gather_Info = False #Have All Information Needed From User
                
            elif usr_Confirm in confirm_No: #Changing Variables For No
                ask_Confirm = False #Exit Confirm Loop
                var_Confirm = False #Have users Confirmation
                get_Ones = True #Going Back To Get All Info Again
            else:
                print("Please enter 'Yes' or 'No'. ")
            


