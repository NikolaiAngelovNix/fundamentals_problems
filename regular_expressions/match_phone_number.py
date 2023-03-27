import re

phone_numbers = input()
pattern = r"\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\b"
matches = re.findall(pattern, phone_numbers)
print(", ".join(matches))
