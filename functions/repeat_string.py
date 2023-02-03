word = input()
n = int(input())

result = lambda string, repeats: string * repeats
print(result(word, n))
