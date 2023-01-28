integers_string = input().split(", ")
beggars_count = int(input())

result = [0] * beggars_count
for index in range(len(integers_string)):
    beggar_index = index % beggars_count
    number = int(integers_string[index])
    result[beggar_index] += number

print(result)
