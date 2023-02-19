visited_cities = int(input())
total_profit = 0

for day in range(1, visited_cities + 1):
    current_city = input()
    current_profit = float(input())
    current_expenses = float(input())
    if day % 5 == 0:
        current_profit *= 0.9
    elif day % 3 == 0:
        current_expenses *= 1.5
    current_profit -= current_expenses
    total_profit += current_profit
    print(f"In {current_city} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
