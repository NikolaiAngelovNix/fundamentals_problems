rooms = int(input())
all_chairs = 0
game_is_on = True
for current_room in range(1, rooms + 1):
    chairs = input().split()
    if len(chairs[0]) < int(chairs[1]):
        needed_chairs = int(chairs[1]) - len(chairs[0])
        print(f"{needed_chairs} more chairs needed in room {current_room}")
        game_is_on = False
    else:
        all_chairs += len(chairs[0]) - int(chairs[1])

if game_is_on:
    print(f"Game On, {all_chairs} free chairs left")
