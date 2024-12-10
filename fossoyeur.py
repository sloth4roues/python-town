from humain import Humain
from couleurs import Couleurs as C


class Fossoyeur(Humain):
    def __init__(self, nom, boisson="absinthe", enterrement=0):
        super().__init__(nom, boisson)
        self.__enterrement = enterrement

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"J'ai enterré en tous, {self.__enterrement}, j'aime préparer les lits pour l'éternité")

    def enterrer(self, personne) :
        self.parle(f"Je vais enterrer {personne.nom}")

    def manger(self):
        self.parle("Mmm, j'ai l'habitude de manger au couché de soleil, près du cimetière")