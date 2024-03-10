import requests
import json

class OnlineDatabase:

    endpoint1 = "https://api.nhle.com/stats/rest"
    lang = "en"
    
    # private method
    # used by other functions to perform https requests
    def __access_odb(self, url: str) -> json:
        raw = requests.get(url).content
        return json.loads(raw)


    # ping server to check connectivity
    # return: True if ping succeeds, False otherwise
    def ping_db(self):
        url = f"{self.endpoint1}/ping"
        result = False
        try:
            result = self.__access_odb(url)["success"]
        except:
            pass
        return result

    # get the definition of all available stat terms
    def get_glossary(self):
        url = f"{self.endpoint1}/{self.lang}/glossary"
        return self.__access_odb(url)

    # get a list of all available seasons
    def get_all_seasons(slef):
        pass

    # get stats about a player
    def get_player_stats(self):
        pass

    # get stats about a team
    def get_team_stats(self):
        pass

    # get team roster for a given season
    # team  : team code to check
    # season: season to check 
    # return: tbd
    def get_team_roster(self):
        pass


my_odb = OnlineDatabase()
result = my_odb.ping_db()
print(result)
