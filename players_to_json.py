import requests
import json

# importing all teams
f = open("data/teams.json", 'r')
teams_dict = json.load(f)
f.close()
teams = [teams_dict[str(id)]["code"] for id in teams_dict]

players = {}

for team in teams:
    # fetching all team data for 2023/2024 season
    url = f'https://api-web.nhle.com/v1/roster/{team}/current'
    raw = requests.get(url).content
    roster = json.loads(raw)

    # for all forwards, defensemen, goalies, add to players list
    for player in roster["forwards"]:
        players[player["id"]] = player
        players[player["id"]]["teamCode"] = team # for each player, add attribute of teamCode

    for player in roster["defensemen"]:
        players[player["id"]] = player
        players[player["id"]]["teamCode"] = team

    for player in roster["goalies"]:
        players[player["id"]] = player
        players[player["id"]]["teamCode"] = team

# format for visual prettiness
players_json = json.dumps(players, indent=4)

# save file
f = open("data/players.json", 'w')
f.write(players_json)

print("Created players.json")