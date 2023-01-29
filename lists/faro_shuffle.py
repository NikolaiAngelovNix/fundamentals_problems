deck = input().split()
shuffles = int(input())

first_card = deck[0]
last_card = deck[len(deck) - 1]
deck.remove(first_card)
deck.remove(last_card)

shuffled_deck = deck
half_of_deck = len(deck) // 2

for _ in range(shuffles):
    current_shuffle = []
    first_half_index = 0
    for index in range(half_of_deck, len(shuffled_deck)):
        current_card = shuffled_deck[index]
        current_shuffle.append(current_card)
        current_shuffle.append(shuffled_deck[first_half_index])
        first_half_index += 1
    shuffled_deck = current_shuffle
shuffled_deck.append(last_card)
shuffled_deck.insert(0, first_card)

print(shuffled_deck)
