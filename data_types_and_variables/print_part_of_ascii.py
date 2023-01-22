starting_num = int(input())
ending_num = int(input())

for char in range(starting_num, ending_num + 1):
    current_char = chr(char)
    print(current_char, end=" ")
