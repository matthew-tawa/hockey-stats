import requests
import json

# importing all teams
f = open("data/teams.json", 'r')
teams_dict = json.load(f)
f.close()
teams = [teams_dict[str(id)]["code"] for id in teams_dict]

# list of all seasons from 2014/2015 to 2023/2024 (10 seasons)
seasons = [str(yr)+str(yr+1) for yr in range(2014, 2024)]

season_counter = 0
for season in seasons:
    season_counter += 1

    schedules = {}
    schedules[season] = {}
    team_counter = 0
    for team in teams:
        team_counter += 1

        # fetching all team data for 2023/2024 season
        url = f'https://api-web.nhle.com/v1/club-schedule-season/{team}/{season}'
        raw = requests.get(url).content
        schedule = json.loads(raw)

        for game in schedule["games"]:
            if game["id"] not in schedules[season].keys():
                schedules[season][game["id"]] = game

        print(f"Finished team {team_counter}.")

    # format for visual prettiness
    schedules_json = json.dumps(schedules, indent=4)

    print(f"Saving file...")

    # save file
    my_f = open(f"data/schedules/schedule_{season}.json", 'w')
    my_f.write(schedules_json)
    my_f.close()

    print(f"Finished season {season_counter}.")



print("Created schedules.")