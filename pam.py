from elements import *

class Pam :
    """Class map qui doit contenir une map conforme"""

    robots = {}

    def __init__(self, name, path):
        self.name = name
        self.carte = self.load(path)

    def __repr__(self):
        chain = "Map : %s \n" % self.name
        for y, line in enumerate(self.carte) :
            for x, e in enumerate(line) :
                if (x,y) in self.robots.values() :
                    for key in self.robots :
                        if self.robots[key] == (x,y) :
                            chain += key
                elif e :
                    chain += e.symbole
                else :
                    chain += ' '
            chain += '\n'
        return chain

    def __str__(self):
        return  self.__repr__()

    def __getitem__(self, index):
        return self.carte[index]

    def __setitem__(self, index, value):
        self.carte[index] = value

    def __len__(self):
        return self.carte.__len__()

    def load(self,path):
        """Recoit le chemin du .txt et renvoie une liste des listes des elements"""
        pam = []
        with open(path, "r") as fhand:
            for i,line in enumerate(fhand):
                pam.append([]) #On rajoute une ligne
                for e in line.strip() :
                    if e in GRAPHISMES : #On verifie que le symbole existe
                        pam[i].append(GRAPHISMES[e])
                    else :
                        raise ValueError("Symbole inconnu :" + e)
        return pam

    def robot(self, chain):
        r , x , y = chain.split(",")
        self.robots[r] = (int(x),int(y))

x = Pam("lol", 'Cartes\\Facile.txt')
x.robot("v,5,5")
print(x)
