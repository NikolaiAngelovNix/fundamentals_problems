dungeon_rooms = input().split("|")
total_bitcoins_mined = 0
max_health = 100
current_health = 100
hero_is_alive = True

for room in dungeon_rooms:
    current_room = room.split()
    if current_room[0] == "potion":
        amount_healed = int(current_room[1])
        current_health += amount_healed
        if current_health > max_health:
            amount_healed = max_health - (current_health - amount_healed)
            current_health = max_health
        print(f"You healed for {amount_healed} hp.")
        print(f"Current health: {current_health} hp.")
    elif current_room[0] == "chest":
        current_bitcoins = int(current_room[1])
        total_bitcoins_mined += current_bitcoins
        print(f"You found {current_bitcoins} bitcoins.")
    else:
        current_health -= int(current_room[1])
        if current_health <= 0:
            hero_is_alive = False
            best_room = dungeon_rooms.index(room) + 1
            print(f"You died! Killed by {current_room[0]}.")
            print(f"Best room: {best_room}")
            break
        else:
            print(f"You slayed {current_room[0]}.")

if hero_is_alive:
    print("You've made it!")
    print(f"Bitcoins: {total_bitcoins_mined}")
    print(f"Health: {current_health}")