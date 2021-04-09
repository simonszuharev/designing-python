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


#instructor's code:

"""

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  #checks answer against guess. Returns the number of turns remaining.
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game() """
