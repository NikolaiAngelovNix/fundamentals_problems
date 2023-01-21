budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25
loaf_price = flour_price + eggs_price + milk_price
loaf_counter = 0
coloured_eggs_count = 0
total_loafs_price = loaf_price

while budget > total_loafs_price:
    loaf_counter += 1
    coloured_eggs_count += 3
    if loaf_counter % 3 == 0:
        coloured_eggs_count -= loaf_counter - 2
    total_loafs_price += loaf_price

remaining_money = budget - loaf_counter * loaf_price
print(f"You made {loaf_counter} loaves of Easter bread! Now you have {coloured_eggs_count} eggs and {remaining_money:.2f}BGN left.")
