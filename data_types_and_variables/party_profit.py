group_size = int(input())
adventure_days = int(input())
copy_group_size = group_size
days_counter = 1
total_coins = 0
for _ in range(adventure_days):
    if days_counter % 10 == 0:
        copy_group_size -= 2
    if days_counter % 15 == 0:
        copy_group_size += 5
        total_coins -= copy_group_size * 2
    total_coins += 50
    total_coins -= copy_group_size * 2
    if days_counter % 3 == 0:
        total_coins -= copy_group_size * 3
    if days_counter % 5 == 0:
        total_coins += copy_group_size * 20
    days_counter += 1
coins_per_companion = int(total_coins / copy_group_size)
print(f"{copy_group_size} companions received {coins_per_companion} coins each.")
