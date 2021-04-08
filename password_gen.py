#Password Generator Project
import random

def password_gen(nr_letters, nr_symbols, nr_numbers, list_let, list_symb, list_num):
    password = ""
    password += character_gen(nr_letters, list_let) + character_gen(nr_symbols, list_symb) + character_gen(nr_numbers, list_num)
    return ''.join(random.sample(password,len(password)))
    
    
def character_gen(num_char, list_of_items):
    password = ""
    for i in range(num_char):
        password += str(list_of_items[random.randint(0, len(list_of_items)-1)])
    return password    

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = password_gen(nr_letters, nr_symbols, nr_numbers, letters, symbols, numbers)
print("Your auto-generated password is " + password + ". Please, use it safely.")
