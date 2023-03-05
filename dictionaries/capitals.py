countries = input().split(", ")
capitals = input().split(", ")
countries_dict = {}

for index in range(len(countries)):
    countries_dict[countries[index]] = capitals[index]

for country, capital in countries_dict.items():
    print(f"{country} -> {capital}")
