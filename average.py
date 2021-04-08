student_heights = input("Input a list of student heights ").split(", ")
counter = 0
sum = 0
for height in student_heights:
    sum += int(height)
    counter+=1

average = round(sum/counter, 2)
print("Your average value is " + str(average) + "!")