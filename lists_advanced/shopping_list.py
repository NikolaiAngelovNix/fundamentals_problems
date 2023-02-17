initial_list = input().split("!")

command = input()

while command != "Go Shopping!":
    current_command = command.split()
    if current_command[0] == "Urgent":
        product = current_command[1]
        if product not in initial_list:
            initial_list.insert(0, product)
    elif current_command[0] == "Unnecessary":
        product = current_command[1]
        if product in initial_list:
            initial_list.remove(product)
    elif current_command[0] == "Correct":
        old_product = current_command[1]
        new_product = current_command[2]
        for el in range(len(initial_list)):
            if initial_list[el] == old_product:
                initial_list.remove(old_product)
                initial_list.insert(el, new_product)
                break
    elif current_command[0] == "Rearrange":
        product = current_command[1]
        if product in initial_list:
            initial_list.remove(product)
            initial_list.append(product)
    command = input()

print(", ".join(initial_list))
