def split_bill_calc(bill, group_count, tip_perc):
    per_person_bill = (bill/group_count)*(1 + tip_perc/100)
    per_person_bill = round(per_person_bill, 1)
    return per_person_bill

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("How many people split the bill to? "))
tip_percentage = float(input("What tip percentage are you going to leave? "))

personal_share = split_bill_calc(total_bill, number_of_people, tip_percentage)
print("Your share is $" + str(personal_share) + ".")