starting_string = input()
letter = starting_string[0]
output_string = letter

for char in starting_string:
    if char != letter:
        output_string += char
        letter = char

print(output_string)