def add(a, b):
    return a + b


def subtract(a, b):
    return  a - b


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = add(first_num, second_num)
result = subtract(result, third_num)

print(result)
