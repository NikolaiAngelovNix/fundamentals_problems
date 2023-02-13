secret_message = input().split()

for word in secret_message:
    current_word = ""
    first_index = int(word[0])
    second_index = 1
    if first_index == 1:
        second_index = 2
    first_char = ""
    for el in range(second_index + 1):
        first_char += word[el]
    current_word += chr(int(first_char))
    current_word += word[-1]
    for ch in range(second_index + 2, (len(word)) - 1):
        current_word += word[ch]
    if first_index == 1 and len(word) > 4:
        current_word += word[second_index + 1]
    elif first_index != 1 and len(word) > 3:
        current_word += word[second_index + 1]
    print(current_word, end=" ")
