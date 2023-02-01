list_of_gifts = input().split()
command = input()

while command != "No Money":
    command_list = command.split()
    command_string = command_list[0]
    command_gift = command_list[1]
    if command_string == "OutOfStock":
        for ind in range(len(list_of_gifts)):
            if command_gift == list_of_gifts[ind]:
                list_of_gifts[ind] = "None"
    elif command_string == "Required" and 0 <= int(command_list[2]) < len(list_of_gifts):
        index_of_gift = int(command_list[2])
        list_of_gifts[index_of_gift] = command_gift
    elif command_string == "JustInCase":
        list_of_gifts.pop(len(list_of_gifts) - 1)
        list_of_gifts.append(command_list[1])
    command = input()

for gift in list_of_gifts:
    if gift == "None":
        continue
    else:
        print(gift, end=" ")
