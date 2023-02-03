def order_calculation(product, quantity):
    result = 0
    if product == "coffee":
        result = quantity * 1.5
    elif product == "coke":
        result = quantity * 1.4
    elif product == "water":
        result = quantity * 1
    else:
        result = quantity * 2
    return result


order = input()
products_counter = int(input())

final_result = order_calculation(order, products_counter)
print(f"{final_result:.2f}")
