number_of_pours = int(input())
total_liters = 0
for _ in range(number_of_pours):
    current_liters = int(input())
    if total_liters + current_liters > 255:
        print("Insufficient capacity!")
        continue
    total_liters += current_liters

print(total_liters)
