class Matrice:
    def __init__(self, valeurs):
        self.valeurs = valeurs
        self.n = len(valeurs)
        self.m = len(valeurs[0]) if valeurs else 0

    def afficher_matrice(self):
        print("Affichage de la matrice :")
        for ligne in self.valeurs:
            print(ligne)

    def __add__(self, Matrice_B):
        if self.n != Matrice_B.n or self.m != Matrice_B.m:
            raise ValueError("Les deux matrices n'ont pas la même taille")
        
        resultat = [[0 for _ in range(self.m)] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                resultat[i][j] = self.valeurs[i][j] + Matrice_B.valeurs[i][j]
        
        return Matrice(resultat)

    def __sub__(self, Matrice_B):
        if self.n != Matrice_B.n or self.m != Matrice_B.m:
            raise ValueError("Les deux matrices n'ont pas la même taille")
        
        resultat = [[0 for _ in range(self.m)] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                resultat[i][j] = self.valeurs[i][j] - Matrice_B.valeurs[i][j]
        
        return Matrice(resultat)

    def __mul__(self, Matrice_B): # Note ce n'est pas une multiplication matricielle, mais élément par élément
        if self.n != Matrice_B.n or self.m != Matrice_B.m:
            raise ValueError("Les deux matrices n'ont pas la même taille")
        
        resultat = [[0 for _ in range(self.m)] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                resultat[i][j] = self.valeurs[i][j] * Matrice_B.valeurs[i][j]
        
        return Matrice(resultat)


if __name__ == "__main__":
    matA = Matrice([[2, 6], [0, 8]])
    matB = Matrice([[2, 0], [0, 5]])
    matD = Matrice([[1, 2, 3], [4, 5, 6]])

    print("Matrice A :")
    matA.afficher_matrice()
    print("\nMatrice B :")
    matB.afficher_matrice()

    print("\nAddition des matrices A et B :")
    matC = matA + matB
    matC.afficher_matrice()

    print("\nSoustraction des matrices A et B :")
    matC = matA - matB
    matC.afficher_matrice()

    print("\Multiplication des matrices A et B :")
    matC = matA * matB
    matC.afficher_matrice()