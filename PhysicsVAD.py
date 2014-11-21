#!/usr/local/bin/python3.3
#PHYSICS GRAPH DOER THING

#Variables
##Integer Variables (Entered By User)
x1 = 0   #Initial X/Y Values#
x2 = 0   #"                "#
y1 = 0   #"                "#
y2 = 0   #"                "#
direction = '' #Initial Direction Value
##Integer Variables (Found By Computer)
time = 0 #Initial Time Value
Rise = 0 #     Y2 - Y1      #
Run = 0  #     X2 - X1      #
Velocity = 0 #Answer to Velocity
Acceleration = 0 #Answer to Acceleration
##Variables For Velocity vs. Time Displacement
lowerY = 0 #The Smaller Y Value#
VVT_Triangle = 0 #Area Under Curve, Triangle at top#
VVT_Base = 0 #Area Under Curve, Base#
VVT_Displacement = 0 #The Total Displacement For VVT (Area Under Curve)
##Variables For Position vs. Time Displacement
PVT_Displacement = 0 #The Total Displacement For PCT (Area Under Curve)
##True/False for Loops                                        |Done? |  | Edited? |  |Default|
run_Program = True #Run The Program?                          |Y/P-MF|  |         |  | True  |
ask_Again = False #Asks user if they want to do another       |Y/P-MF|  |         |  | False |
gather_Info = False #Sets Main Loop To Getting Info From user |Y/P-GV|  |         |  | False |
get_Ones = False #Get X/Y(1) information from user            |Y/P-GV|  |         |  | False |
get_Twos = False #Get X/Y(2) information from user            |Y/P-GV|  |         |  | False |
get_Time = False #Get Time information from user              |Y/P-GV|  |         |  | False |
get_Direction = False #Get Direction information from user    |Y/P-GV|  |         |  | False |
var_Confirm = False #Confirm all variables set by user        |Y/P-GV|  |         |  | False |
get_Math_Info = False #Finding other info for math loops      |Y/P-DE|  |         |  | False |
math_Velocity = False #Doing the math to get the slope        |Y/P-VA|  |         |  | False |
math_Acceleration = False #Doing math to get acceleration     |Y/P-VA|  |         |  | False |
math_Displacement = False #Doing math to get displacements    |Y/P-DE|  |         |  | False |
ask_Confirm = False #Asking if sub-info is correct            |Y/P-VA|  |         |  | False |
##Other Variables
again = '' #Asking If User Wants To Do Another Equation
VVT_Sloped = "No" #If Displacement Segment is Sloped for VvT
confirm_Yes = ("Yes", "Y", "Ye", "Yea", "Yeah", "Yup") #Acceptable input to say yes
confirm_No = ("No", "N", "Nope", "Naw", "Na") #Acceptable input to say no
usr_Confirm = "" #Asking user for confirmation


while run_Program == True:
    gather_Info = True
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
                    get_Math_Info = True #Setting True To Run Next Partt Of Program                
                elif usr_Confirm in confirm_No: #Changing Variables For No
                    ask_Confirm = False #Exit Confirm Loop
                    var_Confirm = False #Have users Confirmation
                    get_Ones = True #Going Back To Get All Info Again
                else:
                    print("Please enter 'Yes' or 'No'. ")

#############################################################################################
###                       DISPLACEMENT  EQUATION / EXECUTION                           ###
#############################################################################################

    #Getting Other Information For Math Loops
    while get_Math_Info == True: ##**get_Math_Info was changed from Default(false) for testing
        #Finding Lower Y
        if y1 < y2 : #If Y1 is Lower
            lowerY = y1
        elif y2 < y1 : #If Y2 is Lower
            lowerY = y2
        elif y1 == y2 : #If Y1 & Y2 are Equal
            lowerY = y1
        else: #Else
            lowerY = 9999999999999999
        #Finding Rise and Run
        Rise = y2 - y1 #Getting The Rise of a graph
        Run = x2 - x1 #Getting The Run of a graph
        #Finding If Area Under Curve segment is sloped for VVT
        if Rise == 0 : #If Rise is '0' then line not sloped
            VVT_Sloped = "No" #Setting Line To Not Sloped
        elif Rise != 0: #If Rise is > or < 0 then line is sloped
            VVT_Sloped = "Yes" #Setting Line to SLoped
        else : # Else
            VVT_Sloped = "ERROR"
        get_Math_Info = False #Setting to Exit get_Math_Info
        math_Displacement = True #Set To Enter Math-Displacement

    #Doing Math For Displacement
    while math_Displacement == True:
        #Displacement for Velocity vs. Time
        if VVT_Sloped == "Yes": #Displacement If Segment Is Sloped
            VVT_Triangle = (Rise*Run)/2 #Finding Area For Sloped Portion
            if VVT_Triangle < 0 :
                VVT_Triangle = -VVT_Triangle
                VVT_Base = lowerY * Run #Finding Area For Non-Sloped Portion
        elif VVT_Sloped == "No": #Displacement If Segment is Not Sloped
            VVT_Triangle = 0 #Set To 0 Because Segment Not Sloped
            VVT_Base = lowerY * Run #Finding Area/Displacement
        VVT_Displacement = VVT_Triangle + VVT_Base #Setting Velocity vs. Time total Displacement
        #Displacement For Position vs. Time
        PVT_Displacement = Rise #Setting Position vs. Time Total Displacement
        if PVT_Displacement < 0 :
            PVT_Displacement = -PVT_Displacement
        math_Displacement = False #Setting To Exit Math_Displacement
        math_Velocity = True #Set to run Next Part of Program

###############################################################################################
###                           SLOPE and ACCELERATION EQUATION                               ###
###############################################################################################

    #Doing Math For Velocity/Slope
    while math_Velocity == True :
        try: 
            Velocity = (y2 - y1) / (x2 - x1)
            math_Velocity = False #Exiting math_Velocity Loop
            math_Acceleration = True #Set to Enter math_Acceleration Loop
        #if ZeroDivisionError is encountered
        except ZeroDivisionError:
            Velocity = 0 #Set Velocity to 0
            math_Velocity = False #Exiting math_Velocity Loop
            math_Acceleration = True #Set to Enter math_Acceleration Loop

    #Doing Math For Acceleration
    while math_Acceleration == True:
        try:
            Acceleration = Velocity/time #Finding The Acceleration
            math_Acceleration = False #Exiting math_Acceleration Loop
            print_Answers = True #Setting to print Answers
        #If ZeroDivisionError is encountered
        except ZeroDivisionError:
            Acceleration = 0 #Set Acceleration to 0
            math_Acceleration = False #Exiting math_Acceleration Loop
            print_Answers = True #Setting to print Answers

###############################################################################################
###                           PRINTING ANSWERS FOR PROBLEM                                  ###
###############################################################################################
    while print_Answers == True:
        print("\n\n")
        print("###############################")              # ###############################
        print("###         ANSWERS         ###")              # ###         ANSWERS         ###
        print("###############################")              # ###############################
        print(" - X1: " + str(x1), end="   |   ")             #   - X1: 2   |   X2: 4
        print("X2: " + str(x2))                               #   - Y1: 2   |   Y2: 4
        print(" - Y1: " + str(y1), end="   |   ")             #   - Time: 3 Seconds 
        print("Y2: " + str(y2))                               #   - Rise/Run: 2/2
        print(" - Time: " + str(time) + " seconds")           #   - Velocity: 3.0 m/s
        print(" - Rise/Run: "+str(Rise)+"/"+str(Run))         #   - Acceleration: 3.0 m/s^2
        print(" - Velocity: " + str(Velocity)+" m/s")         #   - PvT Displacement: 3.0 Meters, Positve
        print(" - Acceleration: "+ str(Acceleration)+" m/s^2")#   - VvT Displacement: 3.0 Meters, Negative
        print(" - PvT Displacement: "+str(PVT_Displacement) + " Meters, " + direction)
        print(" - VvT Displacement: "+str(VVT_Displacement) + " Meters, " + direction)
        print("\n\n")
        print_Answers = False
        ask_Again = True

    #Asking user if they want to do another problem
    while ask_Again == True:
        again = input("Another? ").title()
        if again in confirm_Yes: #If user says yes
            ask_Again = False    #Exiting ask_Again loop
            run_Program = True   #Setting to run program again
        elif again in confirm_No:  #If user says no
            ask_Again = False      #Exiting ask_Again loop
            run_Program = False    #Setting to not run program again
        else:print("Please enter 'Yes' or 'No'.")
            
input("\n\n\t<press enter to exit>")
