def check_if_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                 print(str(year) + " is a leap year :)")
            else:
                print(str(year) + " is not a leap year :(")
        else:
            print(str(year) + " is a leap year :)")
    else:
        print(str(year) + " is not a leap year :(")
        
        
print("Let's check if your year is a leap year!")
year = int(input("What year would you like to check? "))
check_if_leap(year)