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


if Y1 != Y2 then, VVT_Displacement = Sloped
"""
#Variables
##Integer Variables
x1 = 2   #Initial X/Y Values# **SET FOR TESTING PURPOSES**
x2 = 4   #"                "# **SET FOR TESTING PURPOSES**
y1 = 4   #"                "# **SET FOR TESTING PURPOSES**
y2 = 2   #"                "# **SET FOR TESTING PURPOSES**
Rise = 0 #     Y2 - Y1      #
Run = 0  #     X2 - X1      #
##Variables For Velocity vs. Time Displacement
lowerY = 0 #The Smaller Y Value#
VVT_Triangle = 0 #Area Under Curve, Triangle at top#
VVT_Base = 0 #Area Under Curve, Base#
VVT_Displacement = 0 #The Total Displacement For VVT (Area Under Curve)
##Variables For Position vs. Time Displacement
PVT_Displacement = 0 #The Total Displacement For PCT (Area Under Curve)
##True/False for Loops                                       |Done? |  | Edited? |  |Default|
#get_Ones = True #Get X/Y(1) information from user            |Y/P-GV|  |*CHANGED*|  | False |
#get_Twos = False #Get X/Y(2) information from user           |Y/P-GV|  |         |  | False |
#get_Time = False #Get Time information from user             |Y/P-GV|  |         |  | False |
#get_Direction = False #Get Direction information from user   |Y/P-GV|  |         |  | False |
#var_Confirm = False #Confirm ALL variables set by user       |Y/P-GV|  |         |  | False |
get_Math_Info = True #Finding other info for math loops      |Y/P-DE| |*CHANGED*|  | False |
math_Slope = False #Doing the math to get the slope          | N/A  |  |         |  | False |
math_Acceleration = False #Doing math to get acceleration    | N/A  |  |         |  | False |
math_Displacement = False #Doing math to get displacements   |Y/P-DE|  |         |  | False |
ask_Confirm = False #Asking if sub-info is correct           | N/A  |  |         |  | False |
##Other Variables
VVT_Sloped = "No" #If Displacement Segment is sloped for VvT
confirm_Yes = ("Yes", "Y", "Ye", "Yea", "Yeah", "Yup")
confirm_No = ("No", "N", "Nope", "Naw", "Na")
usr_Confirm = "" #Asking user for confirmation




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




####PRINT FOR TESTING####
print("x1: " + str(x1))
print("x2: " + str(x2))
print("y1: " + str(y1))
print("y2: " + str(y2))
print("Rise/Run: " + str(Rise) + "/" + str(Run))
print("Sloped?: " + VVT_Sloped)
print("VVT-Tri: " + str(VVT_Triangle))
print("VVT_Base: " + str(VVT_Base))
print("VVT_Displacement: " + str(VVT_Displacement))
print("PVT_Displacement: " + str(PVT_Displacement))