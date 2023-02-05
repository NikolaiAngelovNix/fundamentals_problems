def length_validator(password):
    is_valid = False
    if 6 <= len(password) <= 10:
        is_valid = True
    return is_valid


def only_letters_and_digits_validator(password):
    is_valid = True
    for char in password:
        if ord(char) < 48 or 57 < ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
            is_valid = False
            break
    return is_valid


def two_or_more_digits_validator(password):
    digits_counter = 0
    is_valid = False
    for char in password:
        if 47 < ord(char) < 58:
            digits_counter += 1
    if digits_counter >= 2:
        is_valid = True
    return is_valid


given_password = input()

password_is_valid = True

if not length_validator(given_password):
    print("Password must be between 6 and 10 characters")
    password_is_valid = False
if not only_letters_and_digits_validator(given_password):
    print("Password must consist only of letters and digits")
    password_is_valid = False
if not two_or_more_digits_validator(given_password):
    print("Password must have at least 2 digits")
    password_is_valid = False
if password_is_valid:
    print("Password is valid")
