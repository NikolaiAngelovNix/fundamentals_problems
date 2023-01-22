number_of_chars = int(input())
ascii_sum = 0
for _ in range(number_of_chars):
    current_char = input()
    ascii_sum += ord(current_char)
print(f"The sum equals: {ascii_sum}")
