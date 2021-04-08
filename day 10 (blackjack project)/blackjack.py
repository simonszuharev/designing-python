import random

total_cards = {"hearts" : [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "diamonds" : [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "clubs" : [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "spades" : [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
}


def draw_the_card(dictionary):
    try:
        deck = [] #suit of the card that is going to be removed
        card_counter = len(dictionary)
        card_key = 0
        suit = random.choice(list(total_cards))
        deck = total_cards[suit]
        item = random.choice(total_cards[suit])
        card = {suit : item}
        deck.remove(item)
        if not deck:
            total_cards.pop(suit)
        card_counter += 1
        card_key += card_counter
        dictionary.update({card_key : card})
    except:
        print("no more cards")

    return dictionary

def print_card(cards_dict):
    for suit, card in cards_dict.items():
        print(card, suit, " " )

def get_sum(cards_dict):
    sum = 0
    for key, card in cards_dict.items():
        for value in card:
            sum += card[value]
    return sum    
    
def get_winner(user_cards, computer_cards):
    if get_sum(user_cards) > get_sum(computer_cards) and get_sum(user_cards) <= 21:
        print("Computer cards are: ")
        for i in computer_cards:
                print_card(computer_cards[i])
        print("You won! The sum of the computer is ", get_sum(computer_cards), ".")
    elif get_sum(user_cards) < get_sum(computer_cards) and get_sum(computer_cards) <= 21:
        print("Computer cards are: ")
        for i in computer_cards:
                print_card(computer_cards[i])
        print("Computer won! The sum of the computer is ", get_sum(computer_cards), ".")
    elif get_sum(user_cards) > 21 and get_sum(computer_cards) < 22:
        print("Computer cards are: ")
        for i in computer_cards:
                print_card(computer_cards[i])
        print("Computer won! The sum of the computer is ", get_sum(computer_cards), ".")
    elif get_sum(user_cards) < 21 and get_sum(computer_cards) > 22:
        print("Computer cards are: ")
        for i in computer_cards:
                print_card(computer_cards[i])
        print("You won! The sum of the computer is ", get_sum(computer_cards), ".")
    elif get_sum(user_cards) == get_sum(computer_cards):
        print("Computer cards are: ")
        for i in computer_cards:
                print_card(computer_cards[i])
        print("Y'all are even at ", get_sum(user_cards), ". Draw again!")

def computer_choice(computer_cards):
    choice = random.randint(0,1)#0 - draw, 1 - stand
    if get_sum(computer_cards) < 12:
        computer_cards = draw_the_card(computer_cards)
    elif choice == 0:
        computer_cards = draw_the_card(computer_cards)
    return computer_cards
    

def draw_or_stand_check(user_cards, computer_cards):
    draw = True
    draw_or_stand = str(input("Would you like to draw or stand? 'd' for draw and 's' for stand: "))
    while draw == True:
        if draw_or_stand.lower() == "d":
            user_cards = draw_the_card(user_cards)
            print("Your cards are:")
            for i in user_cards:
                print_card(user_cards[i])
            print("Which means, your sum is ", get_sum(user_cards))
            if get_sum(user_cards) > 21:
                get_winner(user_cards, computer_cards)
                return True
            else:
                computer_choice(computer_cards)
                print("Computer cards to see: ")
                computer_cards_can_see = len(computer_cards)-1
                for i in computer_cards:
                    try:
                        print_card(computer_cards[computer_cards_can_see])
                        computer_cards_can_see -= 1
                    except:
                        None
                draw_or_stand = str(input("Would you like to draw or stand? 'd' for draw and 's' for stand: "))        
        elif draw_or_stand.lower() == "s":
            print("Which means, your sum is ", get_sum(user_cards), ".")
            get_winner(user_cards, computer_cards)
            if get_sum(user_cards) == get_sum(computer_cards):
                user_cards_even = {}
                computer_cards_even = {}
                draw_the_card(user_cards_even)
                draw_the_card(computer_cards_even)
                get_winner(user_cards_even, computer_cards_even)
            draw = False
            return True



end_of_game = False

while end_of_game == False:
    card = {}
    user_cards = {}
    computer_cards = {}
    print("Welcome to the BlackJack game! Let's play!\n")
        
    i = 0    
    while i < 2: #initial number of cards
        user_cards = draw_the_card(user_cards)
        computer_cards = draw_the_card(computer_cards)
        i+=1
    print("Your cards are:")
    for i in user_cards:
        print_card(user_cards[i])
        
    print("\nComputer's card that you can see is:")
    print_card(computer_cards[1])
    draw_or_stand_check(user_cards, computer_cards)
    again = str(input("Wanna play again? For yes type 'y' or any other key to quit: "))
    if again.lower() == "y":
        print("\n\n\n")
    else: 
        print("Good bye!")
        end_of_game = True
        
    
            
#print(random.choice(list(user_cards.values())))

