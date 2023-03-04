data = input().split()
products_dict = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products_dict[key] = value

print(products_dict)
