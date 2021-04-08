def find_area(a, b):
    return a*b

def calculate_cans(num):
    can_num = round(num/5)
    return can_num

print("Welcome to the calculate your paint cans program!")
width = int(input("What's your width? "))  
height = int(input("What's your height? "))

num_of_cans = calculate_cans(find_area(width, height))
print("Your number of cans is " + str(num_of_cans) + ".")