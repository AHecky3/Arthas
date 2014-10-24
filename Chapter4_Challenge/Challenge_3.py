"""
3) Improve "Word Jumble" so that each word is paired with a hint.
   the player should be able to see the hint if he or she is stuck.
   Add a scoring system that rewards players who solve a jumble without
   asking for the hint
"""
#Andrew Hecky
#10/24/2014

#Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("a type of snake. ", "a random arrangement. ", "not hard. ", "not easy. ", "not a question. ", "a musical instrument. ")
#Setting Inital Values
randomNum = random.randint(0,6)
word = WORDS[randomNum]
hint = HINTS[randomNum]
points = 100
hintPoint = True
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
         Welcome to Word Jumble!
        
   Unscramble the letters to make a word.   
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    if guess[0].lower() == "h" :
        print("Hint: The jumbled word is " + hint)
        if points <= 0 :
            hintPoint = False 
        if hintPoint == True :
            points -= 5
        guess = input("\nYour guess: ")
    else :
        print("\nSorry, that's not it. \n(Type 'Hint' for a hint)  \n")
        guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!")
    print("You got " + str(points) + " points! \n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
