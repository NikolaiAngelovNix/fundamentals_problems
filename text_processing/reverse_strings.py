given_word = input()

while given_word != "end":
    reverse_word = given_word[::-1]
    print(f"{given_word} = {reverse_word}")
    given_word = input()
    