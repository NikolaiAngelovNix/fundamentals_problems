given_words = input().split()
given_palindrome = input()
palindrome_list = []

for el in given_words:
    reversed_string = el[::-1]
    if el == reversed_string:
        palindrome_list.append(el)

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(given_palindrome)} times")
