def find_between_chars(char_1, char_2):
    between_chars = []
    for char_num in range(ord(char_1) + 1, ord(char_2)):
        between_chars.append(chr(char_num))

    return between_chars


first_char = input()
second_char = input()

chars_as_String = " ".join(find_between_chars(first_char, second_char))

print(chars_as_String)
