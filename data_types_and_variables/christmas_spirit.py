quantity_of_decorations_per_shop = int(input())
days_till_christmas = int(input())
shopping_days = 2
spirit_points = 0
ornament_set_pieces = 0
tree_skirt_pieces = 0
tree_garland_pieces = 0
tree_lights_pieces = 0
total_cost = 0
copy_quantity_of_decorations = quantity_of_decorations_per_shop

while days_till_christmas >= shopping_days:
    if shopping_days % 11 == 0:
        copy_quantity_of_decorations += 2
    if shopping_days % 2 == 0:
        ornament_set_pieces += copy_quantity_of_decorations
        spirit_points += 5
    if shopping_days % 3 == 0:
        tree_skirt_pieces += copy_quantity_of_decorations
        tree_garland_pieces += copy_quantity_of_decorations
        spirit_points += 3 + 10
    if shopping_days % 5 == 0:
        tree_lights_pieces += copy_quantity_of_decorations
        spirit_points += 17
    if shopping_days % 15 == 0:
        spirit_points += 30
    if shopping_days % 10 == 0:
        spirit_points -= 20
        tree_skirt_pieces += 1
        tree_garland_pieces += 1
        tree_lights_pieces += 1
    shopping_days += 1

if days_till_christmas % 10 == 0:
    spirit_points -= 30
total_cost = ornament_set_pieces * 2 + tree_skirt_pieces * 5 + tree_garland_pieces * 3 + tree_lights_pieces * 15

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points}")
