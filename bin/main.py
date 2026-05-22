import random
import time
#declare the variables needed
playerNumber = 0
randomNumber = 0
result = ''
match_going = False
guessed = False
difChoice = 0
#functions to be called throughout
def CheckNumber():
    if playerNumber == randomNumber:
        print("Wow! You got me, my number was:",randomNumber)
        result = True
    if randomNumber > playerNumber:
        print('Yikes! You were wrong, my number was: ', randomNumber)
        result = False
    if randomNumber < playerNumber:
        print("Yikes you're wrong! My number was: ", randomNumber)
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
        playerNumber = 0
        randomNumber = 0
        result = ''
        match_going = False
        guessed = False
        difChoice = 0
        return playerNumber, randomNumber, result, match_going, guessed, difChoice


def endgamePrompt():
    player_choice = str.upper(input("Thanks for playing! Would you like to play again? Y/N"))
    if player_choice == "Y":
        reset_variables()
        match_going = matchStart()
    if player_choice == "N":
        match_going = False
    return match_going



def GrabInput():
    difChoice = int(input("What difficulty do u wanna play?\n"
                    "It'll be any number between & including the two\n"
                    "[1: 0,25]\n[2:0,100]\n[3:0,175]\n"))
    playerNumber = int(input("What number am I thinking of?\n"))
   # time.sleep(5)
    message()
    return playerNumber, difChoice
# loop

def RollNumber(difficulty):
    if difficulty == 1:
        randomNumber = round(random.randint(0,25))
    if difficulty == 2:
        randomNumber = round(random.randint(0,50))
    if difficulty == 3:
        randomNumber = round(random.randint(0,95))
    
    return randomNumber
    pass




match_going = True
while match_going:
    GrabInput()
    RollNumber(difChoice)
    CheckNumber()
    endgamePrompt()
