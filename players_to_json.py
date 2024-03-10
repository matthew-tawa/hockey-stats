from pathlib import Path
import json

# # ***** IMPORT INPUT FILE *****
# # obtaining the proper relative path
# script_location = Path(__file__).absolute().parent
# file_name = 'players.txt'
# myfile = script_location / file_name

# # read the file into a list, split by the newline characters
# # note:  read_text() automatically closes file when done 
# players = [player.split('\t') for player in myfile.read_text().split('\n')]
# # *****************************

# players_dict = {player[2]: {"name": player[0], "team": player[1]} for player in players}
# myjson = json.dumps(players_dict, indent=4)

# f = open("players.txt", 'w')
# f.write(myjson)

with open("players.json", 'r') as myjson:
    parsed = json.load(myjson)

print(parsed["23476"])