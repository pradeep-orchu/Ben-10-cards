import random
from aliens import aliens

nameP1 = str(input("Name of Palyer1: "))
nameP2 = str(input("Name of Palyer2: "))


cardsP1 = random.sample(list(aliens),len(list(aliens)))
cardsP2 = random.sample(list(aliens),len(list(aliens)))

players = {
    nameP1:{
        'cards': cardsP1
    },
    nameP2:{
        'cards': cardsP2
    }
}
print(nameP1, "has :")
for i in players[nameP1]['cards']:
    print(i['Name'],i['Power'])
 

# print(nameP1,'Cards',players[nameP1]['cards'])
# print(nameP2,'Cards',players[nameP2]['cards'])