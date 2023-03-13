given_strings = input().split()

first_string = given_strings[0]
second_string = given_strings[1]

result = 0

if len(first_string) > len(second_string):
    smaller_string = second_string
    bigger_string = first_string
else:
    smaller_string = first_string
    bigger_string = second_string

for index in range(len(smaller_string)):
    result += ord(first_string[index]) * ord(second_string[index])

for ind in range(len(smaller_string), len(bigger_string)):
    result += ord(bigger_string[ind])

print(result)