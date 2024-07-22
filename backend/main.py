import random
from players import Players
from match import Match


player1 = Players.players['player1']
player2 = Players.players['player2']

Match(player1,player2).round()

