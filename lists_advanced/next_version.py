current_version = [int(x) for x in input().split(".")]
num = current_version[0] * 100 + current_version[1] * 10 + current_version[2]
next_version = str(num + 1)
print(f"{next_version[0]}.{next_version[1]}.{next_version[2]}")
