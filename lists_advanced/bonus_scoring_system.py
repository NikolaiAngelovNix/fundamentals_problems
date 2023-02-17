students_count = int(input())
total_lectures = int(input())
additional_bonus = int(input())

highest_bonus = 0
highest_attendance = 0

for _ in range(students_count):
    current_attendances = int(input())
    if current_attendances > highest_attendance:
        highest_attendance = current_attendances

if total_lectures != 0:
    highest_bonus = highest_attendance / total_lectures * (5 + additional_bonus)

print(f"Max Bonus: {round(highest_bonus)}.")
print(f"The student has attended {highest_attendance} lectures.")
