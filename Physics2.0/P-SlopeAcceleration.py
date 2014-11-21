#!/usr/local/bin/python3.3
#PHYSICS GRAPH DOER THING
"""
Equations:
    - Slope/Velocity : (y2-y1)/(x2 - x1)
    - Acceleration : ((y2 - y1)/(x2 - x1))/Time
    - Displacement :
             -  V vs T :   if line is sloped : ((y2 - y1)*(x2 - x1)/2) + (bottomY * (x2 - x1)
                           if line not sloped: (bottomY * (x2 - x1))
             -  P vs T : (y2 - y1)
"""
#Variables
##Integer Variables (Entered By User)
x1 = 2   #Initial X/Y Values# **CHANGED FOR TESTING**
x2 = 4   #"                "# **CHANGED FOR TESTING**
y1 = 2   #"                "# **CHANGED FOR TESTING**
y2 = 4   #"                "# **CHANGED FOR TESTING**
direction = '' #Initial Direction Value
#Integer Variables (Found By Computer)
time = 2 #Initial Time Value
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
##True/False for Loops                                       |Done? |  | Edited? |  |Default|
gather_Info = True #Sets Main Loop To Getting Info From user |Y/P-GV|  |         |  | True  |
get_Ones = True #Get X/Y(1) information from user            |Y/P-GV|  |*CHANGED*|  | False |
get_Twos = False #Get X/Y(2) information from user           |Y/P-GV|  |         |  | False |
get_Time = False #Get Time information from user             |Y/P-GV|  |         |  | False |
get_Direction = False #Get Direction information from user   |Y/P-GV|  |         |  | False |
var_Confirm = False #Confirm all variables set by user       |Y/P-GV|  |         |  | False |
get_Math_Info = True #Finding other info for math loops      |Y/P-DE|  |*CHANGED*|  | False |
math_Velocity = True #Doing the math to get the slope        |Y/P-VA|  |*CHANGED*|  | False |
math_Acceleration = False #Doing math to get acceleration    |Y/P-VA|  |         |  | False |
math_Displacement = False #Doing math to get displacements   |Y/P-DE|  |         |  | False |
ask_Confirm = False #Asking if sub-info is correct           |Y/P-GV|  |         |  | False |
print_Answers = False #Tells When To Print Answers           |N/ NA |  |         |  | False |
##Other Variables
VVT_Sloped = "No" #If Displacement Segment is Sloped for VvT
confirm_Yes = ("Yes", "Y", "Ye", "Yea", "Yeah", "Yup") #Acceptable input to say yes
confirm_No = ("No", "N", "Nope", "Naw", "Na") #Acceptable input to say no
usr_Confirm = "" #Asking user for confirmation


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
    print("###############################")      #  ###############################
    print("###         ANSWERS         ###")      #  ###         ANSWERS         ###
    print("###############################")      #  ###############################
    print("       X1: " + str(x1), end="   |   ") #         X1: 2   |   X2: 4
    print("X2: " + str(x2))                       #         Y1: 2   |   Y2: 4
    print("       Y1: " + str(y1), end="   |   ") #
    print("Y2: " + str(y2))                       #
