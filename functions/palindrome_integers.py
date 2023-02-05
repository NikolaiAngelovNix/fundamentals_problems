def palindrome_calc(number):
    reverse_num = ""
    for char in range(len(number) - 1, -1, -1):
        reverse_num += number[char]

    return reverse_num == number


given_numbers = input().split(", ")

for ind in given_numbers:
    print(palindrome_calc(ind))
