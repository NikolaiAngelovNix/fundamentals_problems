given_numbers = [int(x) for x in input().split(", ")]
positive_nums_list = []
negative_nums_list = []
even_nums_list = []
odd_nums_list = []
for num in given_numbers:
    if num % 2 == 0:
        even_nums_list.append(str(num))
    else:
        odd_nums_list.append(str(num))
for num in given_numbers:
    if num >= 0:
        positive_nums_list.append(str(num))
    else:
        negative_nums_list.append(str(num))
print("Positive: ", end="")
print(", ".join(positive_nums_list))
print("Negative: ", end="")
print(", ".join(negative_nums_list))
print("Even: ", end="")
print(", ".join(even_nums_list))
print("Odd: ", end="")
print(", ".join(odd_nums_list))
