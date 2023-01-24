import sys

snowball_number = int(input())
highest_snowball_value = -sys.maxsize
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0
for _ in range(snowball_number):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = int(snowball_value)
        highest_snowball_weight = snowball_weight
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality
print(f"{highest_snowball_weight} : {highest_snowball_time} = {highest_snowball_value} ({highest_snowball_quality})")
