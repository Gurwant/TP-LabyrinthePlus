import random

class Utilisateur :
    """Classe qui represente un utilisateur avec:
        -son nom
        -sa position
        -son Symbole
        -son socket ?"""

    name = ''
    robot = ''

    def __init__(self, client) :
        self.link = client

    def __repr__(self):
        chain = "Utilisateur : %s , Robot : %s" % (self.name, self.robot)
        return chain

    def __str__(self):
        return self.__repr__()
