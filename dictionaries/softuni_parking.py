number_of_commands = int(input())
registered_users = {}

for index in range(number_of_commands):
    command = input().split()
    task = command[0]
    username = command[1]
    if task == "register":
        plate_num = command[2]
        if username in registered_users:
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            registered_users[username] = plate_num
            print(f"{username} registered {plate_num} successfully")
    elif task == "unregister":
        if username in registered_users:
            print(f"{username} unregistered successfully")
            registered_users.pop(username)
        else:
            print(f"ERROR: user {username} not found")

for username, plate_num in registered_users.items():
    print(f"{username} => {plate_num}")
