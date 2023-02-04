def even_odd_sums(num):
    num = str(num)
    even_sum = 0
    odd_sum = 0
    for el in num:
        if int(el) % 2 == 0:
            even_sum += int(el)
        else:
            odd_sum += int(el)

    return [even_sum, odd_sum]


number_input = int(input())
even_odd_result = even_odd_sums(number_input)
print(f"Odd sum = {even_odd_result[1]}, Even sum = {even_odd_result[0]}")
