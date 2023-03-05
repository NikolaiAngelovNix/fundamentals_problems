given_string = input().split()
chars_counter = {}

for word in given_string:
    for letter in word:
        if letter in chars_counter:
            chars_counter[letter] += 1
        else:
            chars_counter[letter] = 1

for char, count in chars_counter.items():
    print(f"{char} -> {count}")
