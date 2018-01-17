

class Element :
    """Classe parente de tous les elements sur la carte """

    solide = False
    symbole = ''

    def __repr__(self):
        return self.symbole

    def __str__(self):
        return self.__repr()

class Mur(Element):
    """Classe représentant un mur"""

    symbole = 'O'
    solide = True

class Porte(Element):
    """Classe représentant un mur"""

    symbole = '.'

class Sortie(Element):
    """Classe représentant un mur"""

    symbole = 'X'

GRAPHISMES = {
    'O' : Mur,
    '.' : Porte,
    'X' : Sortie,
    ' ' : None
}
