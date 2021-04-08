import random

def r_p_s():
    
    #1 - rock, 2 - paper, scissors.
    return random.randint(1,3)
    
def compare(user_input, computer_output):
    if user_input == 1 and computer_output == 2:
        print("You have Rock, computer has Paper. Computer won!")
    elif user_input == 1 and computer_output == 3:
        print("You have Rock, computer has Scissors. You won!")
    elif user_input == 2 and computer_output == 1:
        print("You have Paper, computer has Rock. You won!")
    elif user_input == 2 and computer_output == 3:
        print("You have Paper, computer has Scissors. Computer won!")
    elif user_input == 3 and computer_output == 1:
        print("You have Scissors, computer has Rock. Computer won!")
    elif user_input == 3 and computer_output == 2:
        print("You have Scissors, computer has Paper. You won!")
    elif user_input == computer_output:
        if user_input == 1:
            print("Y'all both have Rocks!")
        elif user_input == 2:
            print("Y'all both have Papers!")
        else:
            print("Smells suspicious but y'all both have Scissors")
    else:
        print("Type in something valid, please!")
        
print("Welcome to Rock, Paper, Scissors! Are you feeling lucky? Let's see!")
print("To choose rock type in 1, for paper 2, for scissors 3. Let's go!")
        
user_input = int(input("1, 2, 3? "))
while True:
    computer_output = r_p_s()
    compare(user_input, computer_output)
    user_input = int(input("Let's play again! 1, 2, 3? "))
    
    if user_input == 1 or user_input == 2 or user_input == 3:
        True
    else:
        print("Good Bye!")
        break
        