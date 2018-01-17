from elements import *

class Pam :
    """Class map qui doit contenir une map conforme"""

    def __init__(self, name, path):
        self.name = name
        self.carte = self.load(path)
        print(type(self.carte))

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

    def __repr__(self):
        chain = "Map : %s \n" % self.name
        for line in self.carte :
            for e in line :
                if e :
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


p = Pam("h","Cartes\\Facile.txt")
print(p)
