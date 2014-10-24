"""
4) Create a game where the computer picks a random word and the player has to guess that word.
    The computer tells the player how many letters are in the word. Then the player gets five
    chances to ask if a letter is in the word. The computer can only respond with "yes" or
    "no". Then, the player must guess the word.
"""
#Andrew Hecky
#10/24/2014

import random

#Words for Computer to choose
WORDS = ("clodhopping", "uncloak", "orchestra", "sunburn", "biocatalyst", "thieve", "abstain", "racker",
         "pyrotechnician", "tottle", "reduction", "hawker", "forceless", "boxfish", "weedy", "splice",
         "discursion", "ahull", "modelize", "scall", "idealist", "past", "organize", "panic", "auxiliary",
         "docible", "subtilty", "bacteria", "dictator", "castaway", "alligate", "tense", "flutter", "sensor")
#Selecting random word
randomWord = random.choice(WORDS)
wordLength = len(randomWord)
letinword = []
letnotinword = []
letterChance = 5
correct = False

print("""
               Guess My Word!
      I'm thinking of a random word and
    I want you to guess it! You have five
    chances to ask if a letter is in the
    word. But then you must guess my word! """)
print("\nOkay, I'm thinking of my word. There are " + str(wordLength) + " letters in my word. ")
while correct == False :
    print("")
    print("You know these letters are in my word: " + str(letinword))
    print("You know these letters aren't in my word: " + str(letnotinword))
    print("Do you want to guess a (l)etter, or the entire (w)ord? ")
    letorwor = input("(L)etter / (W)ord : ")
    if len(letorwor) >= 1 :
        letorwor = letorwor[0].lower()
    if letorwor == 'l' :
        if letterChance > 0 :
            print("\nOkay, guess a letter you think is in the word! ")
            letGuess = input("Letter: ")
            letterChance -= 1
            if letGuess in randomWord :
                print("The letter '" + letGuess + "' is in my word! ")
                letinword.append(letGuess)
            else :
                print("That letter is not in my word. ")
                letnotinword.append(letGuess)
        elif letterChance <= 0 :
            print("You can't guess any more letters! ")
    elif letorwor == 'w' :
        print("\nOkay, try to guess my word! ")
        wordGuess = input("Word: ")
        if wordGuess == randomWord :
            correct = True
        else :
            print("Sorry, that's not the word I'm thinking of. ")
    elif letorwor == '' :
        break
    else :
        print("Please enter a valid input. ")
if correct == True :
    print("\nWow! You guessed correctly! My word was " + randomWord + "! ")
else :
    print("\nIt seems you didn't get my word. It was kind of obvious if you thought about it.\nMy word was, " + randomWord)
print("\n\n(Press [Enter] to exit)")
