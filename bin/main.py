import random
import time
#declare the variables needed
guessed_number = 0
rolled_number = 0
result = ''
match_going = False
guessed = False
#functions to be called throughout
def RollNumber(difficulty):
    if difficulty == 1:
        rolled_number = round(random.uniform(0,50))
        print("DEBUG: Rolled number: ",rolled_number )

    if difficulty == 2:
        rolled_number = round(random.uniform(0,100))
        print("DEBUG: Rolled number: ",rolled_number )
        
    if difficulty == 3:
        rolled_number = round(random.uniform(0,175))
        print("DEBUG: Rolled number: ",rolled_number )

    return rolled_number
def GuessNumber():
    guessed_number = int(input("What number am I thinking of?\n"))
   # time.sleep(5)
    message()
    guessed = True
    return guessed_number, guessed
def CheckNumber(rolled_number):
    if rolled_number == guessed_number:
        print("Wow! You got me, my number was:",rolled_number)
        result = True
    if rolled_number > guessed_number:
        print('Yikes! You were wrong, my number was: ', rolled_number)
        result = False
    if rolled_number < guessed_number:
        print("Yikes you're wrong! My number was: ", rolled_number)
        result = False
    return result 
def matchStart():
    match_going = True
    return match_going
def message():
    messages = ["Ooooo, is your number my number?", \
                "hmmm i guess there's only one way to find out if ur right",\
                "Heh, good guess, i don't think you got it let's check.",\
                "Wow what a guess, let's see if you win!", \
                ]
    random_choice = round(random.uniform(0,2))
    print(messages[random_choice])
def reset_variables():
        guessed_number = 0
        rolled_number = RollNumber(1)
        result = ''
        match_going = False
        guessed = False
        return guessed_number, rolled_number, result, match_going, guessed
def endgamePrompt():
    player_choice = str.upper(input("Thanks for playing! Would you like to play again? Y/N"))
    if player_choice == "Y":
        reset_variables()
        match_going = matchStart()
    if player_choice == "N":
        match_going = False
    return match_going
# loop

match_going = True
while match_going:
    GuessNumber()
    RollNumber(1)
    CheckNumber(rolled_number)
    endgamePrompt()
