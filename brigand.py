from humain import Humain

# Classe Brigand, héritée de Humain.
class Brigand(Humain):
    def __init__(self, nom, boisson="Tord-Boyaux", look="méchant", dames_kidnappees=0, prime=100, en_prison=False):
        super().__init__(nom, boisson)
        self.__look = look
        self.__dames_kidnappees = dames_kidnappees
        self.__prime = prime
        self.__en_prison = en_prison

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"J'ai l'air {self.__look} et j'ai kidnappé {self.__dames_kidnappees} dames !")
        self.parle(f"Ma tête est mise à prix à {self.__prime} $ !")

    def kidnapper(self, dame):
        print(f"{self.nom} décide de kidnapper la dame {dame.nom}.")
        self.parle("Ahah, tu es mienne désormais !")
        dame.se_faire_kidnapper()
        self.__dames_kidnappees += 1

    def afficher_prime(self):
        print(f"La prime pour {self.nom} est de {self.__prime} $.")

    def aller_en_prison(self, sherif):
        self.parle(f"Damned, je suis fait ! {sherif.nom}  Tu m’as eu !")
        self.__en_prison = True

    def verifier_prison(self):
        if self.__en_prison:
            print(f"{self.nom} est en prison.")
        else:
            print(f"{self.nom} n'est pas en prison.")

    def obtenir_prime(self):
        return self.__prime

    def obtenir_dames_kidnappees(self):
        return self.__dames_kidnappees

    def obtenir_look(self):
        return self.__look

    def manger(self):
        self.parle("MIAM MIAM JE MANGE *se salit*")
