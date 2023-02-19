given_numbers = [int(x) for x in input().split()]
command = input()

while command != "Finish":
    current_task = command.split()
    task = current_task[0]
    if task == "Add":
        current_num = int(current_task[1])
        given_numbers.append(current_num)
    elif task == "Remove":
        current_num = int(current_task[1])
        if current_num in given_numbers:
            given_numbers.remove(current_num)
    elif task == "Replace":
        current_num = int(current_task[1])
        replacement_num = int(current_task[2])
        for index in range(len(given_numbers)):
            if current_num == given_numbers[index]:
                given_numbers.remove(current_num)
                given_numbers.insert(index, replacement_num)
                break
    elif task == "Collapse":
        current_num = int(current_task[1])
        copy_list = [num for num in given_numbers if num >= current_num]
        given_numbers = copy_list

    command = input()

for el in given_numbers:
    print(el, end=" ")
