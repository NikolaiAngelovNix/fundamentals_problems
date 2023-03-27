import re

input_names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(pattern, input_names)
print(" ". join(matches))
