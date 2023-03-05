key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk_materials = {}
is_crafted = False

while not is_crafted:
    given_materials = input().split()
    for index in range(0, len(given_materials), 2):
        key_mat = given_materials[index + 1].lower()
        quantity_mat = int(given_materials[index])
        if key_mat in key_materials:
            key_materials[key_mat] += quantity_mat
            if key_materials[key_mat] >= 250:
                key_materials[key_mat] -= 250
                is_crafted = True
                if key_mat == "shards":
                    print("Shadowmourne obtained!")
                elif key_mat == "fragments":
                    print("Valanyr obtained!")
                elif key_mat == "motes":
                    print("Dragonwrath obtained!")
                break
        else:
            if key_mat in junk_materials:
                junk_materials[key_mat] += quantity_mat
            else:
                junk_materials[key_mat] = quantity_mat

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")
