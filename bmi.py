def bmi_check(bmi):
    if bmi <=18.5:
        print("Your bmi is " + str(round(bmi, 2)) + ", which means you're underweight.")
    elif bmi > 18.5 and bmi <= 25:
        print("Your bmi is " + str(round(bmi, 2)) + ", which means have normal weight.")
    elif bmi > 25 and bmi <= 30:
        print("Your bmi is " + str(round(bmi, 2)) + ", which means you're slightly overweight.")
    elif bmi > 30 and bmi <= 35:
        print("Your bmi is " + str(round(bmi, 2)) + ", which means you're obese.")
    else:
        print("Dude, your bmi is " + str(round(bmi, 2)) + ", which means you're clinically obese. Lose some weight!")
    
def calculate_bmi(height, weight):
    return weight/(height**2)

again = "y"
while again.lower() == 'y':
        height = float(input("enter your height in m: "))
        weight = float(input("enter your weight in kg: "))
        
        bmi = calculate_bmi(height, weight)
        
        bmi_check(bmi)
        again = input("Again? y/n ")
