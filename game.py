from pam import *
import random

class Game(Pam):
    """Classe qui gère la carte et les joueurs"""

    def __init__(self, carte, joueurs) :
        Pam.__init__(self, carte.name, "Cartes\\"+carte.name+".txt")
        self.players = joueurs
        self.placer_robots()

    def placer_robots(self):
        for joueur in self.players :
            x , y = 0 , 0
            x_max , y_max = len(self.carte[0]) - 1 , len(self.carte) - 1
            while self.carte[y][x] != None or (x,y) in self.robots.values() :
                x , y = random.randint(0, x_max) , random.randint(0, y_max)
            self.robots[joueur.robot] = (x,y)
