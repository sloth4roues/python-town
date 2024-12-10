from humain import Humain
from couleurs import Couleurs as C


class Trappeur(Humain):
    def __init__(self, nom,  boisson="remontant", animal="Médor", nom_animal="chien",armes="arc"):
        super().__init__(nom, boisson)
        self.__armes = armes
        self.__animal = animal
        self.__nom_animal = nom_animal
    
    def get_armes(self):
        return self.__armes

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Je me balade toujours avec mon fidèle {self.__nom_animal} '{self.__animal}'")
        self.parle(f"Je me bats le plus souvent avec mon {self.get_armes()}")

    def cartographier(self):
        self.parle(f"Pour le moment, je manque d'information sur le terrain ...")

    def manger(self):
        self.parle("Ce que je mange, je l'ai chassé")