import argparse
import requests
import json

# function which fetches given seasons from online database and stores them locally
def fetch_seasons(s1: str, s2: str = None):
    # importing all teams
    f = open("data/teams.json", 'r')
    teams_dict = json.load(f)
    f.close()
    teams = [teams_dict[str(id)]["code"] for id in teams_dict]

    # list of all seasons from s1 to s2
    seasons = None
    if s2 is None:
        seasons = s1
    else:
        seasons = [str(yr)+str(yr+1) for yr in range(int(s1[0:4]), int(s2[4:8]))]

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


# function which fetches given seasons from online database and stores them locally
def fetch_active_players(s: str):
    # importing all teams
    f = open("data/teams.json", 'r')
    teams_dict = json.load(f)
    f.close()
    teams = [teams_dict[str(id)]["code"] for id in teams_dict]

    season = 'current' if s == 'now' else s


    players = {}

    for team in teams:
        # fetching all team data for 2023/2024 season
        url = f'https://api-web.nhle.com/v1/roster/{team}/' + season
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








parser = argparse.ArgumentParser(
                            prog='LocalDatabase',
                            description='Update the local database with latest online data.'
)
parser.add_argument('-s', '--schedule', nargs='*', type=str, help='Fetch and store list of all games locally. Specify the season (ex.: 20232024 for 2023-2024 season), or specify two seasons for a range.')
parser.add_argument('-p', '--players', nargs='*', type=str, help='Fetch and store a list of all active players locally. Specify the season (ex.: 20232024 for 2023-2024 season).')
args = parser.parse_args()

# *********************** test inputs ****************************
# args = vars(parser.parse_args(['-s', '20142015']))
# args = vars(parser.parse_args(['-s', '20142015', '20232024']))
# args = vars(parser.parse_args(['-p', 'now']))
# args = vars(parser.parse_args(['-p', '20232024']))
# ****************************************************************

exceptions_caught = 0

# deal with schedule
try:
    temp = len(args['schedule'])
    if temp == 1:
        fetch_seasons(args['schedule'][0])
    else:
        fetch_seasons(args['schedule'][0], args['schedule'][1])

except:
    exceptions_caught += 1
    pass

# deal with active players
try:
    if len(args['players'][0]) > 0:
        fetch_active_players(args['players'][0])
    else:
        print('Invalid input, try agian.')
        raise Exception('Check input and try again.')

except:
    exceptions_caught += 1
    pass

# print help if no arguments given
if exceptions_caught == 2:
    print('****')
    print('ERROR: at least 1 argument is required. See help below.\n')
    print('****')
    parser.parse_args(['--help'])







