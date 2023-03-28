import re

pattern = r"^>>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)$"

total_price = 0
bought_items = []
input_text = input()

while input_text != "Purchase":
    match = re.findall(pattern, input_text)
    if not match:
        input_text = input()
        continue

    items = match[0]
    furniture = items[0]
    price = float(items[1])
    quantity = int(items[3])
    bought_items.append(furniture)
    total_price += price * quantity
    input_text = input()

print("Bought furniture:")
if bought_items:
    print("\n".join(bought_items))
print(f"Total money spend: {total_price:.2f}")
