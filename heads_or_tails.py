import random

user_input = str(input("Heads or tails? press Y to play or N to quit: "))
while user_input.lower() == "y":
    heads_tails = random.randint(1,2)
    if heads_tails == 1:
        print("You have heads!")
    else:
        print("You have tails!")
    user_input = str(input("Wanna play again? Y to play or N to quit: "))

print("Bye!")

