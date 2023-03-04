characters_list = input().split(", ")
char_dictionary = {}

for char in characters_list:
    char_dictionary[char] = ord(char)

print(char_dictionary)
