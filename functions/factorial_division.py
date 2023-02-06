def factorial_calc(a):
    factorial_num = 1
    for x in range(1, a + 1):
        factorial_num *= x
    return factorial_num


first_num = int(input())
second_num = int(input())
factorial_division = factorial_calc(first_num) / factorial_calc(second_num)
print(f"{factorial_division:.2f}")
