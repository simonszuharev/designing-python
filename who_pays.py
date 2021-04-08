from random import randint

def who_pays(people):
    return (randint(0, len(people)-1))

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


print("Let me see who gets to pay. Hmm....")

payee = who_pays(names)

#or payee = random.choice(names)

print("Today it is going to be " + names[payee] + "! Congrats!!")