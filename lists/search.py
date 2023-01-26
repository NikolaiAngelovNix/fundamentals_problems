number_of_lines = int(input())
given_word = input()
base_list = []

for _ in range(number_of_lines):
    current_string = input()
    base_list.append(current_string)

print(base_list)

for i in range(len(base_list)-1, -1, -1):
    element = base_list[i]
    if given_word not in element:
        base_list.remove(element)

print(base_list)
