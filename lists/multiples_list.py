factor = int(input())
counter = int(input())
multiples_list = []
for multiplier in range(1, counter + 1):
    current_num = multiplier * factor
    multiples_list.append(current_num)
print(multiples_list)
