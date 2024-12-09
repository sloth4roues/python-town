from cowboy import Cowboy # ici on importe cowboy et non pas Humain ! car la classe est sur le modèle du cowboy

# Classe Sherif, un cowboy représentant l'autorité
class Sherif(Cowboy):
    def __init__(self, nom, boisson="Whisky", reputation=0, caractere="honnête"):
        super().__init__(nom, boisson, reputation, caractere)
        self.__reputation = reputation
        self.__caractere = caractere

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"J'ai coffré {self.__reputation} brigand, je dois faire mieux !")

    def avis_recherche(self, brigand):
        # affiche un avis de recherche pour un brigand
        self.parle(f"OYEZ OYEZ BRAVE GENS !! {brigand.obtenir_prime()} $ à qui arrêtera {brigand.nom} mort ou vif")

    def emprisonner(self, brigand):
        # action pour arrêter et emprisonner un brigand
        self.parle(f"Au nom de la loi, je vous arrête ! {brigand.nom}")
        brigand.aller_en_prison(self)

    def manger(self):
        self.parle("Miam ! Un petit donut avant de reprendre le service")
