file_path = input().split("\\")

file_name_and_extension = file_path[-1]

file_list = file_name_and_extension.split(".")
file_extension = file_list[-1]
file_list.remove(file_extension)
file_name = ".".join(file_list)

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
