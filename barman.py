from humain import Humain

# Classe Barman, héritée de la classe "Humain".
class Barman(Humain):
    def __init__(self, nom, boisson="Vin", bar=None):
        super().__init__(nom, boisson)  # Appel du constructeur parent
        self.__bar = f"Chez {self.nom}"  # Utilisation de la propriété nom

    @property
    def bar(self):
        return self.__bar

    def parle(self, texte):
        super().parle(f"{texte} Coco")

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Je suis également le barman du bar '{self.bar}'") 

    def servir(self, personne):
        print(f"Le barman {self.nom} sert un verre de {personne.boisson} à {personne.nom}")
        if hasattr(personne, 'boire'):
            print(personne.boire())  # Utilisation de la méthode boire()
        else:
            print(f"{personne.nom} ne peut pas boire !")

    def manger(self):
        self.parle("Je mange doucement, il ne faudrait pas s'étouffer")
