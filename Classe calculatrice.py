import math
class calculatrice:
    def __init__(self):
        self.resultat = 0
    def addition(self,n2):
        self.resultat += n2
    def multiplication(self,n1):
        self.resultat *= n1
    def soustraction(self,n1):
        self.resultat -= n1
    def division(self,n1):
        self.resultat = self.resultat//n1


