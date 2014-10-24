"""
1) Write a program that counts for the user. Let the user enter the starting number, then ending number, and the amount by wich to count.
"""
#Andrew Hecky
#10/23/2014

#Opening Regards
print("""
         Hello There!
     I will count for you!
  Please enter the number you
 wish to start at, end at, and
  what we will be counting by.
""")
#Getting Info From User
while True :
    try:
        startingNum = int(input("Starting Number: "))
        break
    except ValueError:
        print("Please enter a valid input. \n")
while True :
    try:
        endingNum = int(input("Ending Number: "))        
        break
    except ValueError:
        print("Please enter a valid input. \n")
while True :
    try:
        countBy = int(input("Count By: "))                
        break
    except ValueError:
        print("Please enter a valid input. \n")

#Counting Loop
for i in range (startingNum,endingNum+1,countBy):
    print(i)

for i in reversed(range(endingNum,startingNum+1,countBy)):
    print(i)
