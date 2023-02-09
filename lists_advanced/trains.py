wagons = int(input())
wagons_list = [0] * wagons
command = input()
while command != "End":
    command_as_list = command.split(" ")
    if command_as_list[0] == "add":
        wagons_list[len(wagons_list) - 1] += int(command_as_list[1])
    elif command_as_list[0] == "insert":
        wagons_list[int(command_as_list[1])] += int(command_as_list[2])
    elif command_as_list[0] == "leave":
        wagons_list[int(command_as_list[1])] -= int(command_as_list[2])
    command = input()

print(wagons_list)
