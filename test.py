# class Humain, toutes les autres classes SONT des 'Humain'.
class Humain:
    def __init__(self, nom, boisson="eau"):
        self.__nom = nom
        self.__boisson = boisson

# humain.parle(texte) 
    def parle(self, texte):
        print(f"{self.__nom} - {texte}")
# humain.parle()
    def presente(self):
        print(f"Bonjour, je suis {self.__nom} et ma boisson préférée est {self.__boisson}.")
# humain.boire()
    def boire(self):
        print(f"{self.__nom} *boit* - Ah ! un bon verre de {self.__boisson} ! GLOUPS !")
# humain.quel_est_ton_nom()
    def quel_est_ton_nom(self):
        return self.__nom
# humain.quelleEstTaBoisson()
    def quelleEstTaBoisson(self):
        return self.__boisson

# class Brigand, hérité de la classe Humain, comme toutes les autres classes avec le (Humain)
class Brigand(Humain):
    def __init__(self, nom, boisson="eau"):
        super().__init__(nom, boisson)

class Cowboy(Humain):
    def __init__(self, nom, boisson="eau"):
        super().__init__(nom, boisson)

class Dame(Humain):
    def __init__(self, nom, boisson="eau"):
        super().__init__(nom, boisson)

# Story 
def story():
    cowboy = Cowboy("John Wayne", "whisky")
    brigand = Brigand("Billy the Kid", "tequila")
    dame = Dame("Daisy", "limonade")

    cowboy.presente()
    cowboy.boire()
    cowboy.parle("Mais naaah la première partie du tp fini")

if __name__ == "__main__":
    story()
