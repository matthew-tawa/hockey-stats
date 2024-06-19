import requests
import pandas as pd
import json

import matplotlib.pyplot as plt

player_first = "Connor"
player_last = "McDavid"
season = "20232024"
game_type = 2

# fetching list of players
f = open("data/players.json", 'r')
players_dict = json.load(f)
f.close()
for id in players_dict.keys():
    if players_dict[id]["firstName"] == player_first and players_dict[id]["lastName"] == player_last:
         

# fetching all team data for 2023/2024 season
url = f'https://api-web.nhle.com/v1/player/{player_id}/game-log/{season}/{game_type}'
raw = requests.get(url).content
schedule = json.loads(raw)

my_shots = df.Shots.SHOTS.values
plt.hist(my_shots, bins=max(my_shots), rwidth=0.5, align='left')
plt.show()

