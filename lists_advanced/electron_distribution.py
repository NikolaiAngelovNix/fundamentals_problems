electrons = int(input())
shell_position = 1
electrons_list = []
while True:
    current_electrons = 2 * (shell_position ** 2)
    electrons -= current_electrons
    if electrons <= 0:
        electrons += current_electrons
        electrons_list.append(electrons)
        break
    electrons_list.append(current_electrons)
    shell_position += 1
print(electrons_list)
