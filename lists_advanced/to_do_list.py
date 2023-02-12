to_do_list = [0] * 10
to_do_notes = input()
while to_do_notes != "End":
    to_do_notes = to_do_notes.split("-")
    note = to_do_notes[1]
    to_do_list.pop(int(to_do_notes[0]) - 1)
    to_do_list.insert(int(to_do_notes[0]) - 1, note)
    to_do_notes = input()
updated_to_do_list = [task for task in to_do_list if task != 0]
print(updated_to_do_list)

