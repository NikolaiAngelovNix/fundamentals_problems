given_strings = input().split()
command = input()

while command != "3:1":
    current_command = command.split()
    task = current_command[0]
    if task == "merge":
        starting_index = int(current_command[1])
        end_index = int(current_command[2])
        if starting_index < 0:
            starting_index = 0
        merged_string = ""
        if end_index > len(given_strings) - 1:
            end_index = len(given_strings) - 1
        for el in range(starting_index, end_index + 1):
            merged_string += given_strings[el]
        for _ in range(starting_index, end_index + 1):
            given_strings.pop(starting_index)
        given_strings.insert(starting_index, merged_string)
    elif task == "divide":
        current_index = int(current_command[1])
        current_word = given_strings[current_index]
        partitions = int(current_command[2])
        divided_list = []
        parts = len(current_word) // partitions






        
    command = input()


print(given_strings)
