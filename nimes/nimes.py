# Variables qui sont destinées à être constantes après initialisation
# Paramètres de personnalisation du jeu
nom_j1 = ""
nom_j2 = ""
nbr_batons = 15


# Variables "systèmes"
nbr_tour = 0


### Début déclarations de fonctions ###
def choisirParams():
    nom_j1 = input("Entrez le nom du J1 : ")
    nom_j2 = input("Entrez le nom du J2 : ")
    try:
        nbr_batons = int(input("Entrez le nombre de bâton"))
    except expression as identifier:
        pass