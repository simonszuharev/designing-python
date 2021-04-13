from celeb_data import data
import random



def get_celeb():
    return random.choice(data)
    
def check_if_equal(celeb1, celeb2):
    while celeb1 == celeb2:
        celeb1 = get_celeb()
    return celeb1
    
def compare(bet, celeb1, celeb2):
    if bet.lower() == "a":
        if celeb1["follower_count"] > celeb2["follower_count"]:
            return True
        else:
            return False
    elif bet.lower() == "b":
        if celeb1["follower_count"] < celeb2["follower_count"]:
            return True
        else:
            return False        

def game():
    
    score = 0
    
    print("Welcome to the guess the follower count game!")
    print("Choose, which celebrety has more Instagram followers.")
    print("For celebrety 'A' type A, for celebrety 'B' type B:")
    
    celeb1 = get_celeb()
    celeb2 = get_celeb()
    check_if_equal(celeb1, celeb2)
    
    print("Who has more followers: ", celeb1["name"], " or ", celeb2["name"], "?")
    
    user_choice = str(input("Choice: "))
    while compare(user_choice, celeb1, celeb2) != False:
        score += 1
        print("You got it! Your score is ", score, ".")
        celeb1 = get_celeb()
        celeb2 = get_celeb()
        check_if_equal(celeb1, celeb2)
        print("Who has more followers: ", celeb1["name"], " or ", celeb2["name"], "?")
        user_choice = str(input("Choice: "))
        
    print("Your score is ", score)    
        
        
game()    
    
