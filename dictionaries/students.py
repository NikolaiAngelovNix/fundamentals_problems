student_data = input()
courses = {}

while ":" in student_data:
    student_name, student_id, course_name = student_data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name

    student_data = input()

course_name = " ".join(student_data.split("_"))
students = courses[course_name]

for student_id, student_name in students.items():
    print(f"{student_name} - {student_id}")
