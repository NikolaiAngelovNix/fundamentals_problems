import sys

list_of_numbers = input().split()
numbers_to_remove = int(input())
for _ in range(numbers_to_remove):
    min_num = sys.maxsize
    for index in range(len(list_of_numbers)):
        current_num = int(list_of_numbers[index])
        if current_num < min_num:
            min_num = current_num
    min_num = str(min_num)
    list_of_numbers.remove(min_num)

print(list_of_numbers[0], end="")
for ind in range(1, len(list_of_numbers)):
    current_num = list_of_numbers[ind]
    print(f", {current_num}", end="")
