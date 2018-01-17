import random

class Utilisateur :
    """Classe qui represente un utilisateur avec:
        -son nom
        -sa position
        -son Symbole
        -son socket ?"""

    name = ''
    robot = ''
    x = 0
    y = 0

    def __init__(self, client, pam) :
        self.link = client
        x_max , y_max = len(pam[0]) - 1 , len(pam) - 1
        while pam[self.y][self.x] != None:
            self.x , self.y = random.randint(0, x_max) , random.randint(0, y_max)
            print("x : %i, y : %i" % (self.x,self.y))

    def __repr__(self):
        chain = "Utilisateur : %s , Robot : %s en position <%i,%i> " % (self.name, self.robot, self.x, self.y)
        return chain

    def __str__(self):
        return self.__repr__()
