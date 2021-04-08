def prime_checker(num):
    if num % 2 != 0 and num != 2 and num % 3 != 0:
        print("Prime")
    elif num % 3 != 0 and num != 3 and num % 2 != 0:
        print("Prime")
    else:
        print("Not a Prime")

n = int(input("Check this number: "))
prime_checker(n)