products = input()
products_dict = {}

while products != "statistics":
    products = products.split(": ")
    key = products[0]
    value = int(products[1])
    if key not in products_dict:
        products_dict[key] = value
    else:
        products_dict[key] += value
    products = input()

print(f"Products in stock:")
for key, value in products_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_dict.keys())}")
print(f"Total Quantity: {sum(products_dict.values())}")
