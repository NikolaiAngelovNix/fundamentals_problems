starting_string = input()
encrypted_string = ""

for letter in starting_string:
    encrypted_char_num = ord(letter) + 3
    encrypted_char = chr(encrypted_char_num)
    encrypted_string += encrypted_char

print(encrypted_string)
