from humain import Humain

# Classe Cowboy, héritée de Humain.
class Cowboy(Humain):
    def __init__(self, nom, boisson="Whisky", reputation=0, caractere="vaillant"):
        super().__init__(nom, boisson)
        self.__reputation = reputation
        self.__caractere = caractere

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Voyez mon indice de popularité, qui est de {self.__reputation}")
        self.parle(f"Je suis {self.__caractere}")

    def augmenter_reputation(self):
        self.__reputation += 1
        print(f"{self.nom} a désormais {self.__reputation} points de réputation.")

    def liberer_dame(self, dame):
        self.parle(f"Je vous libère {dame.nom}")
        dame.se_liberer(self)
        self.augmenter_reputation()
        self.parle(f"{dame.nom} J'aime beaucoup la couleur {dame.get_couleur_robe()} de votre robe")
        dame.remercier(self)

    def tirer(self, brigand):
        self.parle("Prend ça, rascal ! ")
        print(f"Le {self.__caractere} {self.nom} tire sur {brigand.nom}")

    def manger(self):
        self.parle("Je mange rapidement, la ville a besoin de moi")
