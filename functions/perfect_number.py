def perfect_num(a):
    dividers_sum = 0
    for n in range(1, a):
        if a % n == 0:
            dividers_sum += n
    return dividers_sum == a


given_num = int(input())

if perfect_num(given_num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
