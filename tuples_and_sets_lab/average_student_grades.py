def average_grade(list_of_grades):
    aver_grade = sum(list_of_grades) / len(list_of_grades)
    return aver_grade


number_of_students = int(input())

students_record = {}

for _ in range(number_of_students):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_record:
        students_record[student] = []
    students_record[student].append(grade)
for name, grades in students_record.items():
    print(f"{name} -> {' '.join(map(lambda grade: f'{grade:.2f}', grades))} (avg: {average_grade(grades):.2f})")

