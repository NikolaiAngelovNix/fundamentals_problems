given_products = input()
products_price = {}
products_quantity = {}

while given_products != "buy":
    name, price, quantity = given_products.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products_price:
        products_price[name] = price
        products_quantity[name] = quantity
    else:
        products_price[name] = price
        products_quantity[name] += quantity

    given_products = input()

for product in products_price:
    total_price = products_price[product] * products_quantity[product]
    print(f"{product} -> {total_price:.2f}")
