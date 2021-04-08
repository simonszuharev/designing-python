#from replit import clear

bidders = {}

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def winner_check(bidders):
    winner = ""
    money = 0
    for i in bidders:
        winner = i
        try:
            if money < int(bidders[i]):
                money = int(bidders[i])
        except:
            print("The bidder named " + winner + " typed a wrong price")
            bidders[winner] = str(input("What price are you willing to bid? $ "))
    return winner       

print("Welcome to the Blind Bidder Auction!")

end = False
again = ""

while end == False:
    name = str(input("What is the name of this bidder? "))
    price = str(input("What price are you willing to bid? $"))
    bidders[name] = price
    again = str(input("Are there other players? 'yes' or 'no'")).lower()
    if again == "no":
        end = True
    elif again != "yes":
        error = True
        while error == True:
            again = str(input("PLease, type either 'yes' or 'no'")).lower()
            if again == "yes":
                error = False
            elif again == "no":
                error = False
                end = True
    #clear()
    
winner = winner_check(bidders)
print("The winner of this bid is " + winner + " with the bid of $" + bidders[winner] + "!")
