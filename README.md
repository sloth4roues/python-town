
# TP Python - Système de gestion de personnages (POO)

## Contexte

Le but de ce TP est de créer un système de gestion de personnages en utilisant la programmation orientée objet (POO). Les personnages interagissent entre eux, avec des actions comme : se présenter, boire et d'autres interventions, en fonctions des différentes classes.

## Objectifs

1. **Création de classes de base et dérivées** : 
    - Créer une classe `Humain` avec des attributs nom et boisson préférée.
    - Créer des classes dérivées comme `Cowboy`, `Brigand`, `Dame`, puis `Barman`, et `Sherif`.
    - Implémenter des méthodes comme `se_presenter`, `parle`, et des actions spécifiques aux classes, tel que `kidnapper`.

2. **Utilisation des propriétés et des méthodes privées** :
    - Utiliser des propriétés pour la gestion des attributs privés.
    - Implémenter des méthodes spécifiques pour gérer l'état des personnages, comme `se_faire_kidnapper`, `changer_robe`, et `manger`.

3. **Gestion des couleurs dans le texte** : 
    - Utilisation de couleurs dans les dialogues et l'affichage narratif pour améliorer la lisibilité de l'histoire.
    - Centralisation des couleurs dans un fichier `couleurs.py` pour rendre le code plus flexible et réutilisable.

4. **Reflexion sur les choix d'optimisation** : 
    - Par exemple, la méthode `quelEstTonNom()` a été supprimée et remplacée par un appel direct à l'attribut `nom`, car la méthode n'était plus nécessaire pour respecter les conventions Python et optimiser l'accès aux données.

## Structure du projet

Voici l'architecture du projet :

```
├── barman.py
├── brigand.py
├── couleurs.py
├── cowboy.py
├── dame.py
├── fossoyeur.py
├── humain.py
├── main.py
├── README.md
├── sherif.py
├── trappeur.py
└── test.py - inutile en l'état, c'est mon ancien main, je le laisse pour voir à quoi ressembler l'ancienne logique
```

### Fichiers principaux :

- **`humain.py`** : Contient la classe `Humain` qui définit les attributs et méthodes de base de tous les personnages (nom, boisson, présentation).
- **`brigand.py`**, **`cowboy.py`**, **`dame.py`**, **`barman.py`**, **`sherif.py`** : Ces fichiers contiennent les classes spécifiques à chaque personnage, chacune héritant de `Humain` et ayant des méthodes et comportements spécifiques.
- **`main.py`** : Le fichier principal où l'histoire est racontée en simulant des interactions entre les personnages.
- **`couleurs.py`** : Définit les couleurs à utiliser dans les affichages texte, permettant de rendre l'affichage avec des couleurs.

## Fonctionnalités

1. **Personnages** :
    - **Cowboy** : Un cowboy avec des actions comme `liberer_dame`.
    - **Brigand** : Un brigand qui peut `kidnapper` une dame.
    - **Dame** : Une dame qui peut être kidnappée, mais aussi `changer_robe` ou `hurler`.
    - **Sherif** : Un sherif qui peut `emprisonner` des brigands.
    - **Barman** : Le barman qui `sert` des boissons.

2. **Interaction et héritage** :
    - Utilisation de l'héritage pour créer des personnages dérivés de `Humain`, chacun ayant ses comportements uniques.
    - Méthodes comme `se_presenter`, `parle`, et des actions comme `kidnapper`, `liberer_dame`, et `emprisonner` qui interagissent entre les personnages.

3. **Couleurs dans le texte** :
    - Ajout de couleurs dans les dialogues et le texte narratif.
    - Le fichier `couleurs.py` permet de gérer facilement les couleurs pour chaque partie du texte.

## Optimisations et Justifications

- **Suppression de la méthode `quelEstTonNom()`** :
    Dans un souci d'optimisation et de simplification du code, la méthode `quelEstTonNom()` a été remplacée par l'accès direct à l'attribut privé `__nom`. Cela respecte plus les conventions Python récentes.

- **Gestion des couleurs** :
    Les couleurs ont été centralisées dans un fichier `couleurs.py` pour une gestion flexible et facile des affichages colorés. Cela rend l'ajout ou la modification de couleurs plus simple et permet d'éviter les répétitions de code.

- **Utilisation des propriétés et des méthodes privées** :
    L'utilisation de propriétés (`@property`) pour gérer les attributs privés comme `__nom` et `__boisson` garantit que ces valeurs sont protégées de modifications directes tout en permettant un accès contrôlé via des getters et setters.

- **En clair** : 
    Je n'ai pas oublié certaines fonctions, j'ai fait le TP une première fois, puis en recherche d'optimisation et de simplification, le code et la logique de code a un peu changé.

## Améliorations futures

- **Ajouter plus de personnages** : Nous pourrions ajouter d'autres personnages (par exemple, un "maire" ou un "villageois") avec des méthodes pour un système d'éléction.
- **Système de combat ou d'action** : Implémenter des interactions encore plus intéressante, comme un système de combat entre les personnages, ou des choix que le joueur pourrait faire pour influencer l'histoire.
- **Gestion d'événements aléatoires** : Ajouter des éléments de jeu, comme des événements aléatoires ou des missions secondaires.

## Conclusion

En conclusion, ce TP m'a énormément apporté.
J'ai beaucoup aimé le réaliser, je pense avoir bien géré le temps imparti, et avoir mieux appris.
Le sujet était assez motivant, et je pense très sincèrement continuer ce projet à l'avenir, avec un système de combat pour rentrer encore plus dans l'aspect jeu-vidéo qui me passionne.

Un très bon projet de POO en somme, qui m'a beaucoup apporté !
