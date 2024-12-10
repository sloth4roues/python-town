class Matrice:
    def __init__(self, valeurs):
        self.valeurs = valeurs
        self.n = len(valeurs)
        self.m = len(valeurs[0]) if valeurs else 0

    def afficher_matrice(self):
        print("Affichage de la matrice :")
        for ligne in self.valeurs:
            print(" ".join(map(str, ligne)))

    def __add__(self, Matrice_B):
        if self.n != Matrice_B.n or self.m != Matrice_B.m:
            print("Erreur Taille Matrice : ")
            raise ValueError("Il faut que les deux matrices fassent la même taille ")
        
        resultat = [
            [
                self.valeurs[i][j] + Matrice_B.valeurs[i][j]
                for j in range(self.m)
            ]
            for i in range(self.n)
        ]
        return Matrice(resultat)




if __name__ == "__main__":
    matA = Matrice([[1, 2], [3, 4]])
    matB = Matrice([[5, 6], [7, 8]])
    matD = Matrice([[1, 2, 3], [4, 5, 6]])

    print("Matrice A :")
    matA.afficher_matrice()
    print("\nMatrice B :")
    matB.afficher_matrice()

    print("\nAddition des matrices A et B :")
    matC = matA + matB  # Utilisation de l'opérateur `+`
    matC.afficher_matrice()
