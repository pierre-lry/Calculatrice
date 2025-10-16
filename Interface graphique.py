from tkiteasy import *
from calculatrice import calculatrice
class Affichage:
    def __init__(self):
        self.fenetre = ouvrirFenetre(1000,1000)

    def affichageGraphique(self):
        self.fenetre.dessinerRectangle(100,100,800,100,'White')

g = Affichage()
g.affichageGraphique()
g.fenetre.actualiser()
g.fenetre.attendreClic()
