given_numbers_list = [int(x) for x in input().split(", ")]
even_list = [el for el in range(len(given_numbers_list)) if given_numbers_list[el] % 2 == 0]

print(even_list)
