input_year = int(input())
input_year += 1
input_as_string = str(input_year)

while len(input_as_string) != len(set(input_as_string)):
    input_year += 1
    input_as_string = str(input_year)
print(input_year)
