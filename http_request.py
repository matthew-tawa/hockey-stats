import requests
import pandas as pd
import json

url = 'https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=seasonId=20232024%20and%20gameTypeId=2'
raw = requests.get(url).content
parsed = json.loads(raw)
print(json.dumps(parsed, indent=4))

f = open("output.txt", 'w')
f.write(str(json.dumps(parsed, indent=4)))

class OnlineDatabase:
    def get_player_data(name: str):
        pass

    def get_team_data(name: str):
        pass


