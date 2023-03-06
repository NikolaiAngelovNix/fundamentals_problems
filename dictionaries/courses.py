data = input()
courses = {}

while data != "end":
    course_name, student_name = data.split(" : ")
    if course_name in courses:
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]
    data = input()

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for student in names:
        print(f"-- {student}")
