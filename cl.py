import random
import json
import pprint
import initcl


def drawTree():
    print("Drawing the champions league tree using some Turtle magic.....")

###### Starting Champions league ########


teams = ['MUN', 'MCI', 'LIV', 'CHE', 'RMA', 'ATM', 'FCB', 'JUV',
         'NAP', 'INT', ' MIL', 'PSG', 'POR', 'AJA', 'BAY', 'DOR']

# shuffle teams list
random.shuffle(teams)

print(teams)
print(f"Total number of teams in this competition = {len(teams)}")


# Read Game File
f = open('data.json')
game_data = json.load(f)

# Print game tree
pprint.pprint(game_data)

game_data['Final']['score']['L1']
