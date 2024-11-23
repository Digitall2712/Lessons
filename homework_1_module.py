grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
average_grade = []
for i in range(len(grades)):
    a = grades[i]
    sum = 0
    for j in range(len(a)):
        b = len(a)
        sum = sum+a[j]
    average = sum / b
    average_grade.append(average)
students_grades = {}
for i in range(len(students)):
    students_grades.update({students[i]: average_grade[i]})
print(students_grades)
