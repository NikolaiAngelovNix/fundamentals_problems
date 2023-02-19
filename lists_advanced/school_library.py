books_list = input().split("&")
command = input()
while command != "Done":
    current_command = command.split(" | ")
    task = current_command[0]
    if task == "Add Book":
        book = current_command[1]
        if book not in books_list:
            books_list.insert(0, book)
    elif task == "Take Book":
        book = current_command[1]
        if book in books_list:
            books_list.remove(book)
    elif task == "Swap Books":
        first_book = current_command[1]
        second_book = current_command[2]
        if first_book in books_list and second_book in books_list:
            first_index, second_index = books_list.index(first_book), books_list.index(second_book)
            books_list[first_index], books_list[second_index] = books_list[second_index], books_list[first_index]
    elif task == "Insert Book":
        book = current_command[1]
        if book not in books_list:
            books_list.append(book)
    elif task == "Check Book":
        index = int(current_command[1])
        if 0 <= index < len(books_list):
            print(books_list[index])

    command = input()

print(", ".join(books_list))
