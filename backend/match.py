import random

class Match:
    def __init__(self, player1: dict, player2:dict,) :
        self.player1 = player1
        self.player2 = player2
        
    def round(self):
        card1 = self.player1['cards'][0]
        card2 = self.player2['cards'][0]
        chance = random.choice([self.player1,self.player2])
        if(chance == self.player1):
            print(self.player1['name'],'got the chance')
            print('1 - Power:',card1['Power'])
            print('2 - Intelligence',card1['Intelligence'])
            print('3 - Speed',card1['Speed'])
            choiseP1 = int(input())
            return choiseP1
        elif(chance == self.player2):
            print(self.player2['name'],'got the chance')
            print('1 - Power:',card2['Power'])
            print('2 - Intelligence',card2['Intelligence'])
            print('3 - Speed',card2['Speed'])
            choiseP2 = int(input())
            return choiseP2
        else:
            return chance
        
    def winner(self,attacker,defender):
        
        return
            