

# list of all seasons from 2014/2015 to 2023/2024 (10 seasons)
seasons = [str(yr)+str(yr+1) for yr in range(2014, 2024)]

class Season:
    
    def __init__(self, teams: list, matches: list):
        self.teams = teams
        self.matches = matches

    # simulate the entire season
    # return: tbd
    def simulate_season(self):
        pass

    # simulate the entire season until date
    # date  : simulate until date (includes games day of date)
    # return: tbd
    def simulate_season(self):
        pass

    # simulate the entire season until date
    # num_games: simulate until any team has played num_games
    # return   : tbd
    def simulate_season(self):
        pass