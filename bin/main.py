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
        rolled_number = random.randint(0,25)

    if difficulty == 2:
        rolled_number = random.randint(0,75)

    if difficulty == 3:
        rolled_number = random.randint(0,150)

    return rolled_number
def GuessNumber():
    guessed_number = int(input("What number am I thinking of?\n"))
    time.sleep(5)
    message()
    guessed = True
    return guessed_number, guessed
        
def CheckNumber():
    if rolled_number == guessed_number:
        print("Wow! You got me, my number was:",rolled_number)
        result = True
    else:
        result = False
    return result 
def matchStart():
    match_going = True
    return match_going
def message():
    messages = ["Ooooo, is your number my number? \
                hmmm i guess there's only one way to find out",\
                "Heh, good guess, i don't think you got it \
                but i'll check it anyway.", \
                "Wow what a guess, let's see if you win!", \
                ]
    random_choice = random.randint(0,2)
    print(messages[random_choice])
    

GuessNumber()
RollNumber(3)
CheckNumber()
natch_going = matchStart()
while match_going:
    GuessNumber()
    if guessed:
        RollNumber(1)
        CheckNumber()
    if result:
        print("Wow! You got me, my number was:",rolled_number)