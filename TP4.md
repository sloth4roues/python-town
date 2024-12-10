# README - Introduction aux Matrices en Mathématiques et Programmation

## Contexte

Les matrices sont des structures mathématiques qui permettent d'organiser des nombres ou des objets dans un tableau bidimensionnel - un tableau en deux dimensions.

---

# 1. Qu'est-ce qu'une matrice ?

Une matrice est définie par sa taille, qui est donnée par un couple de nombres : n x m, où :
- n est le nombre de lignes.
- m est le nombre de colonnes.

Dans ce TP, nous utilisons des matrices carrées, c'est-à-dire où le nombre de lignes est égal au nombre de colonnes (n x n).

Exemple : A = 
- ( 1   2   3 ) 
- ( 4   5   6 )
- ( 7   8   9 )

Cette matrice a 3 lignes et 3 colonnes, donc elle est de taille 3 x 3.

---

# 2. Opérations de base sur les matrices

## a. Addition de matrices
Si A et B sont deux matrices de même taille, alors la matrice résultante C = A + B est obtenue en ajoutant chaque élément A[i][j] à B[i][j].

Exemple d'addition : A =
- ( 1   2   3 )
- ( 4   5   6 )
- ( 7   8   9 )

B = 
- ( 9   8   7 )
- ( 6   5   4 )
- ( 3   2   1 )

A + B = 
- ( 1+9   2+8   3+7 )
- ( 4+6   5+5   6+4 )
- ( 7+3   8+2   9+1 )

= 
- ( 10   10   10 )
- ( 10   10   10 )
- ( 10   10   10 )

---
## b. Multiplication de matrices
La multiplication de matrices implique le produit scalaire des lignes de la première matrice avec les colonnes de la deuxième matrice. Pour multiplier deux matrices A de taille n x m et B de taille m x p, la matrice résultante C = A x B sera de taille n x p.

Chaque élément C[i][j] de la matrice résultante est calculé par la somme des produits des éléments correspondants de la ligne i de la matrice A et de la colonne j de la matrice B.

Exemple :

A = 
- ( 1   2 )
- ( 3   4 )

B = 
- ( 5   6 )
- ( 7   8 )

A x B = 
- { (1x5 + 2x7)  (1x6 + 2x8) }
- { (3x5 + 4x7)  (3x6 + 4x8) }

= 
- ( 19   22 )
- ( 43   50 )

---


# 3. Conclusion

Les matrices sont des outils puissants et fondamentaux pour résoudre des problèmes. Dans ce TP, nous allons mettre en œuvre des opérations de base sur les matrices, ce qui nous permettra d'appréhender leur structure et leur manipulation en programmation.

---

Ce document a pour but de définir cette notion de matrice d'un point de vue mathématique.
