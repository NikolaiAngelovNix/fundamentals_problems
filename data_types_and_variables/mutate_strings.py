first_string = input()
second_string = input()
first_string_count = 0
second_string_count = 0
last_mutated_string = first_string
result_mutated_String = ""

for char in range(len(first_string)):
    first_mutated_string = ""
    first_string_count += 1
    for first_char in range(first_string_count, len(first_string)):
        first_mutated_string += first_string[first_char]

    second_mutated_string = ""
    second_string_count += 1
    for second_char in range(second_string_count):
        second_mutated_string += second_string[second_char]
    result_mutated_String = second_mutated_string + first_mutated_string
    if result_mutated_String != last_mutated_string:
        print(result_mutated_String)
    last_mutated_string = result_mutated_String
