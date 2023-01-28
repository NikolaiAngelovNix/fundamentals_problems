a_team = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
b_team = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

cards_string = input().split()

for index in range(len(cards_string)):
    current_card = cards_string[index]
    current_card = current_card.split("-")
    team = current_card[0]
    number = current_card[1]
    if team == "A":
        if number in a_team:
            a_team.remove(number)
    else:
        if number in b_team:
            b_team.remove(number)
    if len(a_team) < 7 or len(b_team) < 7:
        break
a_team_players = len(a_team)
b_team_players = len(b_team)
print(f"Team A - {a_team_players}; Team B - {b_team_players}")
if a_team_players < 7 or b_team_players < 7:
    print("Game was terminated")
