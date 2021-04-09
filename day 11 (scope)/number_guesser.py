import random

def get_number():
    return random.randint(1,100)
    
def low_high(guess, num):
    if guess > num:
        print("Too high")
    else:
        print("Too low!")



computer_number = 0
guess = 0
again = "y"

while again.lower() == "y":
    attempts = 5
    print("Welcome to the guesser game!")
    print("The rules are: computer thinks of a number between 1 and 100, and your job is to guess it!")
    computer_number = get_number()
    level = str(input("For easy level type 'easy', for hard type 'hard'"))
    
    if level.lower() == "easy":
        attempts += 5
        
    print("Thanks! Computer guessed a number. What do you think that is?")
    guess = int(input("Type it here: "))
    
    game_won = False
    
    while game_won == False:
        attempts -= 1
        low_high(guess, computer_number)   
        if guess != computer_number and attempts >0:
            print("You have ", attempts, " attemps left.")
            guess = int(input("Type it here your guess again: "))
        elif guess!= computer_number and attempts == 0:
            print("No attempts were left. Try playing again :) ", computer_number, " this was the number.")
            game_won = True
        else:
            print("CONGRATS! Computer number was ", computer_number, ".")
            game_won = True
    again = str(input("Wanna play again? 'y' for yes, 'n' for no: "))
    
print("BYE!!!")    


#in this version of the code I purpusefully left out catching user errrors.
