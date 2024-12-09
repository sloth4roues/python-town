from humain import Humain

# Classe Dame, héritée de Humain.
class Dame(Humain):
    def __init__(self, nom, boisson="Lait", couleur_robe="rouge", etat=False):
        super().__init__(nom, boisson)
        self.__couleur_robe = couleur_robe  # Attribut privé
        self.__etat = etat  # Attribut privé

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Regardez ma robe {self.__couleur_robe}")

    def get_couleur_robe(self):
        return self.__couleur_robe

    def hurler(self):
        self.parle(f"AAAAAAH")

    def remercier(self, cowboy):
        self.parle(f"Merci {cowboy.nom}")

    def changer_robe(self, couleur):
        self.__couleur_robe = couleur
        self.parle(f"Regardez ma nouvelle robe {couleur} !")

    def se_faire_kidnapper(self):
        self.__etat = True
        self.hurler()

    def se_liberer(self, cowboy):
        self.__etat = False
        self.remercier(cowboy)

    def afficher_etat(self):
        if self.__etat:
            print(f"La dame {self.nom} est kidnappée ! Il faut la secourir :/")
        else:
            print(f"La dame {self.nom} n'est pas kidnappée, tout va bien :)")

    def manger(self):
        self.parle("Je mange calmement, je ne prends pas le risque de me salir")
