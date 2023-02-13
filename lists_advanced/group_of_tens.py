import math

given_numbers = [int(x) for x in input().split(", ")]
max_num = max(given_numbers)
groups = math.ceil(max_num / 10)
starting_index = 1
end_index = 10

for ind in range(1, groups + 1):
    current_list = []
    for el in given_numbers:
        if starting_index <= el <= end_index:
            current_list.append(el)
    print(f"Group of {end_index}'s: {current_list}")
    starting_index += 10
    end_index += 10
