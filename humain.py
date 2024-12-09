from abc import ABC, abstractmethod

# Classe Humain, toutes les autres classes héritent de celle-ci.
class Humain(ABC):  # ABC pour inclure des méthodes abstraites
    def __init__(self, nom, boisson):
        self.__nom = nom
        self.__boisson = boisson

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nouveau_nom):
        if not isinstance(nouveau_nom, str) or not nouveau_nom.strip():
            raise ValueError("Le nom doit être une chaîne de caractères non vide.")
        self.__nom = nouveau_nom.strip()

    @property
    def boisson(self):
        return self.__boisson

    @boisson.setter
    def boisson(self, nouvelle_boisson):
        if not isinstance(nouvelle_boisson, str) or not nouvelle_boisson.strip():
            raise ValueError("La boisson doit être une chaîne de caractères non vide.")
        self.__boisson = nouvelle_boisson.strip()

    def parle(self, texte):
        print(f"{self.nom} - {texte}")

    def se_presenter(self):
        self.parle(f"Bonjour, je suis {self.nom} et ma boisson préférée est {self.boisson}.")

    def boire(self):
        return f"{self.nom} *boit* - Ah ! un bon verre de {self.boisson} ! GLOUPS !"

    @abstractmethod
    def manger(self):
        pass
