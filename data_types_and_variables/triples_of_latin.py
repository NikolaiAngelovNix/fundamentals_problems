input_integer = int(input())

for first_char in range(input_integer):
    for second_char in range(input_integer):
        for third_char in range(input_integer):
            print(f"{chr(97 + first_char)}{chr(97 + second_char)}{chr(97 + third_char)}")