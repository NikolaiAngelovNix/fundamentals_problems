def loading_bar(a):
    percentage_count = int(a / 10)
    remaining_load = 10 - percentage_count
    loading_string = percentage_count * "%" + remaining_load * "."
    return loading_string


given_load = int(input())

if given_load == 100:
    print(f"100% Complete!")
    print(f"[{loading_bar(given_load)}]")
else:
    print(f"{given_load}% [{loading_bar(given_load)}]")
    print(f"Still loading...")
