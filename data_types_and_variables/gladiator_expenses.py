total_losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmets = 0
broken_swords = 0
broken_shields = 0
broken_armors = 0

losses_counter = 1

for _ in range(total_losses):
    if losses_counter % 2 == 0:
        broken_helmets += 1
    if losses_counter % 3 == 0:
        broken_swords += 1
    if losses_counter % 6 == 0:
        broken_shields += 1
    losses_counter += 1
broken_armors = broken_shields // 2
total_expenses = broken_helmets * helmet_price + broken_swords * sword_price + broken_shields * shield_price + broken_armors * armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
