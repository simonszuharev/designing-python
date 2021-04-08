def check_the_highest(student_student_scores):
    highest_score = int(student_student_scores[0])
    for score in student_student_scores:
        if highest_score < int(score):
            highest_score = int(score)
    return highest_score
            
    

student_scores = input("Input a list of student scores ").split(", ")
highest_score = check_the_highest(student_scores)

print("Your average highest score " + str(highest_score) + "!")