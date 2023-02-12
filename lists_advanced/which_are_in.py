first_list = input().split(", ")
second_list = input().split(", ")
result = []

for word in first_list:
    for el in second_list:
        if word in el:
            result.append(word)
            break

print(result)
