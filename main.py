from humain import Humain
from brigand import Brigand
from dame import Dame
from cowboy import Cowboy
from barman import Barman
from sherif import Sherif
from couleurs import Couleurs as C

# méthode histoire() - teste les personnages et leurs interactions
def histoire():
    print(C.VERT + "\n---------------------------------")
    print("L'histoire commence...")
    print("---------------------------------\n" + C.RESET)
    
    # création des personnages avec leurs noms et boissons préférées
    cowboy = Cowboy("Jotaro", "thé glacé")
    brigand = Brigand("Pucci", "vin")
    dame = Dame("Jolyne", "limonade")
    barman = Barman("Speedwagon", "liqueur de pêche")
    sherif = Sherif("Josuke", "jus")
    
    # présentation des personnages
    print(C.CYAN + "Nos personnages se présentent : \n" + C.RESET)
    cowboy.se_presenter()
    brigand.se_presenter()
    dame.se_presenter()
    barman.se_presenter()
    sherif.se_presenter()
    
    print(C.CYAN + "\n### Le calme avant la tempête ###\n" + C.RESET)
    print(C.CYAN + "Tout semble aller bien dans la ville, jusqu'à ce que...\n" + C.RESET)
    
    # le brigand prépare son mauvais coup
    brigand.parle(f"Je vais kidnapper {dame.nom} et lui faire une proposition qu'elle ne pourra pas refuser !")
    brigand.kidnapper(dame)  # le brigand kidnappe la dame
    print(C.MAGENTA)
    dame.afficher_etat()  # montre si la dame est enlevée
    print(C.RESET)
    
    print(C.CYAN + "\n### La réaction du cowboy ###\n" + C.RESET)
    cowboy.parle("Je ne laisserai pas ce brigand faire de mal à une innocente !")
    cowboy.liberer_dame(dame)  # le cowboy libère la dame
    print(C.MAGENTA)
    dame.afficher_etat()  # montre si elle est libre
    print(C.RESET)
    dame.changer_robe("verte")  # la dame change de robe après sa libération
    
    print(C.CYAN + "\n### Au bar ###\n" + C.RESET)
    print(C.CYAN + "Le barman, voyant la scène, décide d'intervenir..." + C.RESET)
    barman.se_presenter()
    barman.servir(cowboy)  # le barman sert un verre au cowboy pour fêter ça
    
    print(C.CYAN + "\n### Un retournement de situation ###\n" + C.RESET)
    brigand.parle(f"Cette fois, personne ne m'arrêtera !")
    brigand.kidnapper(dame)  # nouvelle tentative du brigand
    dame.afficher_etat()  # vérification de son état
    
    print(C.CYAN + "\n### L'intervention du sheriff ###\n" + C.RESET)
    sherif.parle("Je ne vais pas laisser un brigand troubler l'ordre dans cette ville.")
    sherif.emprisonner(brigand)  # le sheriff enferme le brigand
    brigand.parle("Tu ne m'as pas eu, sheriff ! Ce n'est qu'un retardement !")
    
    print(C.CYAN + "\n### Finalement, tout le monde se retrouve au bar ###\n" + C.RESET)
    sherif.manger()  # le sheriff profite d'un repas tranquille
    cowboy.parle("Cette journée a été pleine de rebondissements !")
    dame.parle("J'ai bien failli perdre ma robe !")
    barman.parle("Je vais devoir changer le nom de mon bar après tout ça, c'était intense !")
    
    print(C.CYAN + "\n### La fin... ou peut-être le début d'une nouvelle aventure ? ###\n" + C.RESET)

    # Globalement l'histoire montre toutes les actions réalisables par le TP, mais à l'avenir, pourquoi ne pas ajouter un système de combat ?
    # Avec un système de point de vie pour chaque classe et d'attaque, c'est largement réalisable, surtout en POO :) !
if __name__ == "__main__":
    histoire()
