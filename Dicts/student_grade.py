student_scores = {
"Argishti": 81,
"Maldini": 78,
"Baresi": 99,
"Baggio": 74,
"Olmo": 62,
                }

student_grade = {}

for name, score in student_scores.items():
    if 91 <= score <= 100:

        student_grade[name] = "Outstanding!"
    elif 81 <= score <= 90:

        student_grade[name] = "Exceeds Expectations!"
    elif 71 <= score <= 80:

        student_grade[name] = "Acceptable"
    elif  score < 70:

        student_grade[name] = "Fail"


for name, score in student_grade.items():
    print(name,score)