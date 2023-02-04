def even_nums_filter(input_string):
    result = input_string % 2 == 0
    return result


numbers = [int(x) for x in input().split()]
print(list(filter(even_nums_filter, numbers)))
