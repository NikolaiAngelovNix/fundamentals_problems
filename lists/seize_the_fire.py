employee_happiness = [int(x) for x in input().split()]
happiness_factor = int(input())
multiplied_happiness = [(el * happiness_factor) for el in employee_happiness]

total_happiness = 0
for el in multiplied_happiness:
    total_happiness += el

average_happiness = total_happiness / len(multiplied_happiness)
happy_employees = 0

for el in multiplied_happiness:
    if el >= average_happiness:
        happy_employees += 1

if happy_employees >= len(multiplied_happiness) / 2:
    print(f"Score: {happy_employees}/{len(multiplied_happiness)}. Employees are happy!")

else:
    print(f"Score: {happy_employees}/{len(multiplied_happiness)}. Employees are not happy!")
