# 91-100_outstanding
# 81-90_exceed expectations
# 71-90_acceptable
# 70 to lower fail


# FIRST MAKE TABLE FROM NAMES AND SCORE WITH A DICTIONRY
table = {}
members = int(input('how many members your class have ? '))

for i in range(members):
    name = input('enter the name of student : ')
    score = int(input(f'enter the score of {name} : '))
    table[name] = score

# NOW WE GANNA GRADE THE STUDENTS WITH THEIR SCORES
student_grades = {}

for i in table:
    tt = int(table[i])

    if tt >= 91 and tt <= 100:
        student_grades[i] = "Outstanding"

    elif tt >= 81 and tt <= 90:
        student_grades[i] = "Exceeds Expectations"

    elif tt >= 71 and tt <= 80:
        student_grades[i] = "Acceptable"

    elif tt <= 70:
        student_grades[i] = "Fail"

print(student_grades)