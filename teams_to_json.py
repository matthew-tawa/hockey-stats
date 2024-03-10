import requests
import json

# fetching all team data for 2023/2024 season
url = 'https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=seasonId=20232024%20and%20gameTypeId=2'
raw = requests.get(url).content
parsed = json.loads(raw)

num_teams = parsed["total"]
data = parsed["data"]

teams = {team["teamId"]: {"name":team["teamFullName"], "code":""} for team in data}

teams_json = json.dumps(teams, indent=4)

f = open("data/teams.json", 'w')
f.write(teams_json)

print("Created teams.json")