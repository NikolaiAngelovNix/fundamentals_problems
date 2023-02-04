import sys


def calc_smallest_num(numbers):
    result = sys.maxsize
    for num in numbers:
        if num < result:
            result = num
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(calc_smallest_num([first_num, second_num, third_num]))
