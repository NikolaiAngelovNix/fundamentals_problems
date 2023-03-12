given_string = input()
digits = ""
letters = ""
symbols = ""

for char in given_string:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        symbols += char

print(f"{digits}\n{letters}\n{symbols}")
