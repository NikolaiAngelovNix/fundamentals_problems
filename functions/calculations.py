def calculations(command, num_1, num_2):
    result = 0
    if command == "multiply":
        result = num_1 * num_2
    elif command == "divide":
        result = num_1 // num_2
    elif command == "add":
        result = num_1 + num_2
    elif command == "subtract":
        result = num_1 - num_2
    return result


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculations(input_operator, first_num, second_num))
