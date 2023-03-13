from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    has_banned_char = False
    for char in username:
        if char not in allowed_chars:
            has_banned_char = True
            break
    if has_banned_char:
        continue

    print(username)
