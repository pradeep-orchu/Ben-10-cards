import random
from aliens import aliens

class Players:

    nameP1 = str(input("Name of Palyer1: "))
    nameP2 = str(input("Name of Palyer2: "))


    cardsP1 = random.sample(list(aliens),len(list(aliens)))
    cardsP2 = random.sample(list(aliens),len(list(aliens)))

    players = {
        'player1':{
            'name': nameP1,
            'cards': cardsP1
        },
        'player2':{
            'name': nameP2,
            'cards': cardsP2
        }
    }
