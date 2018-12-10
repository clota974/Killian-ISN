# coding: utf8

from random import choice
from datetime import datetime, timedelta

# Variables qui sont destinées à être constantes après initialisation
# Paramètres de personnalisation du jeu
### ATTENTION nom du j1 correspond à noms[0]
noms = [] # Liste des deux noms des joueurs : permet d'accéder plus facilement aux deux variables et gérer la portée d'une seule variable
nbr_batons = 10 # Nombre qui peut changer

### Constantes
baton_img = "|"

### Variables "systèmes"
tour_j = 0 # 1 ==> Tour J1
nbr_tour = 0
heure_depart = -1 # -1 tant que pas initialisé


### Début déclarations de fonctions ###

def choisirParams():
    """
    Demande les paramètres de noms, de temps et de bâtons

    Args:
        None

    Returns:
        None

    """

    global noms, nbr_batons
    nom_j1 = input("Entrez le nom du J1 : ")
    nom_j2 = input("Entrez le nom du J2 : ")

    # Gestion du nom par défaut
    nom_j1 = nom_j1 or "J1"
    nom_j2 = nom_j2 or "J2"

    noms = [nom_j1, nom_j2]

    """
    Retirer les bâtons seulement si le nombre de bâtons est correct (2<x<21) 
    """
    try:
        nbr_batons = int(input("Entrez le nombre de bâtons ( 2<x<21 ; défaut: 10): "))
        if(not 2<nbr_batons<21):
            raise ValueError("Non compris entre 2 et 20")
    except:
        nbr_batons = 10
        print("Nombre de bâtons non valide")

    print("Nombre de bâtons : ", nbr_batons)


def commencerNvJeu():
    """
    Démarre un nouveau jeu en chosissant le tour du joueur et stocke l'heure de départ

    Args:
        None
    
    Returns:
        None
    """

    global tour_j, heure_depart
    tour_j = choice([0,1]) # Choisit quel joueur commence
    
    heure_depart = datetime.now()


def play(tour):
    """
    Fait jouer un tour à un joueur

    Args:
        tour (int): Numéro d'identification
    
    Returns: 
        bool: True si aucun problème
    """

    ### ATTENTION tour est une variable locale tandis que tour_j est une variable globales
    global tour_j, nbr_tour
    print("\n\n")

    nbr_tour += 1
    print("Tour n° : ",nbr_tour)
    print("C'est au tour de "+noms[tour])


    # Afficher les bâtons
    print("")
    print(nbr_batons, " bâtons restants")
    print(afficherBatons())

    input_joueur = -1 # Indique que le nombre de bâtons retirés est incorrect si -1
    while(input_joueur == -1): # Tant que le nombre de bâtons à retirer est incorrect
        try:
            input_joueur = int(input("Combien de bâtons voulez-vous retirer? (1 à 3) : "))

            if(not(0<input_joueur<4)): # Si le chiffre n'est pas compris entre 1 et 3
                raise ValueError("Interval")

            estCorrect = retirerBatons(input_joueur)
            if(estCorrect is True):
                return True
            else:
                print(estCorrect[1])
                raise ValueError(estCorrect[0])
            
        except Exception as msg:
            if(str(msg) == "Interval"):
                output_msg = "Chiffre non compris entre 1 et 3!"
            elif(str(msg) =="PlusDeBaton"):
                output_msg = "Vous avez retiré trop de bâtons"
            else:
                output_msg = "Ce n'est pas un chiffre!"

            print(output_msg)
            print("")
            input_joueur = -1


def retirerBatons(input_joueur):
    """
    Retire les bâtons

    Args:
        input_joueur (int): Nombre de bâtons à enlever

    Returns:
        bool: True si pas d'erreur
        list: Description de l'erreur ==> [Titre, Description]

    """

    global nbr_batons
    
    if(nbr_batons-input_joueur<1):
        interval_batons_max = 3
        if(nbr_batons<4):
            interval_batons_max = nbr_batons-1
            if(interval_batons_max==1):
                return ["PlusDeBaton", "Vous ne pouvez pas enlever tous les bâtons! Vous pouvez enlever 1 bâton uniquement"]
            else:
                return ["PlusDeBaton", "Vous ne pouvez pas enlever tous les bâtons! Vous pouvez enlever 1 à "+str(interval_batons_max)+" bâtons"]

       
    else:
        nbr_batons -= input_joueur # Enleve les bâtons
        return True

def afficherBatons():
    """
    Retourne le tableau de jeu (les bâtons) à afficher

    Args:
        None

    Returns:
        str: Le tableau de jeu (" ||| ")
    """

    str_batons = ""

    for i in range(nbr_batons):
        str_batons += baton_img

    return str_batons


def terminerTour():
    """
    Vérifie si le jeu est terminé et change de joueur

    Args:
        None
    
    Returns:
        bool: Si le jeu est terminé
    """

    global tour_j
    if(siJeuTermine()):
        terminerJeu(tour_j)
        return True # Jeu terminé
    else:
        tour_j = 0 if tour_j==1 else 1 # Changer de tour
    
    return False # Jeu NON terminé 
 

def siJeuTermine():
    """
    Returns:
        bool: Si le jeu est terminé
    """

    global nbr_batons
    return nbr_batons == 1 # True ou False

def terminerJeu(gagnant):
    """
    Termine le jeu en affichant le vainqueur et les variables

    Args:
        gagnant (int): ID du joueur

    Returns:
        None

    """


    heureFin = datetime.now() # ==> Timedelta
    tempsJeu = heureFin - heure_depart

    print("\n\n")
    print("FIN DU JEU")
    print("Bravo " + noms[gagnant])
    print("Nombre de tours : ", nbr_tour)

    minutes = int(tempsJeu.seconds/60)
    secs = tempsJeu.seconds%60
    print("Temps : {} mins et {}s".format(minutes, secs))


### Début du jeu ###

choisirParams()
commencerNvJeu()

fin_du_jeu = False
while(not fin_du_jeu): # Voir les difficultés rencontrées
    play(tour_j) # Joueur
    fin_du_jeu = terminerTour() # Test si le jeu est terminé, auquel cas, il le termine