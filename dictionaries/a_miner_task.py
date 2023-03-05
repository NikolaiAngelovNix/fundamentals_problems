resource = input()
gathered_resources = {}

while resource != "stop":
    quantity = int(input())
    if resource in gathered_resources:
        gathered_resources[resource] += quantity
    else:
        gathered_resources[resource] = quantity
    resource = input()

for material, quantity in gathered_resources.items():
    print(f"{material} -> {quantity}")
