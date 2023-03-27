import re

given_text = input()
pattern = r"\b(?P<day>\d{2})([.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
matches = re.finditer(pattern, given_text)
for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
