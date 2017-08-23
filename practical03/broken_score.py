def score_to_grade(score):
    if score > 100 or score < 0:
        grade = "Invalid score."
    elif score >= 90:
        grade = "Excellent."
    elif score >= 50:
        grade = "Passable."
    else:
        grade = "Bad."
    return grade

user_score = float(input("Enter score: "))
result = score_to_grade(user_score)
print(result)