from random import choice
from datetime import datetime, timedelta

# Variables qui sont destinées à être constantes après initialisation
# Paramètres de personnalisation du jeu
### ATTENTION nom_j1 correspond à noms[0]
nom_j1 = ""
nom_j2 = ""
noms = []
nbr_batons = 10

### Constantes
baton_img = "|"

### Variables "systèmes"
tour_j = 0 # 1 ==> Tour J1
nbr_tour = 0
heureDepart = -1


### Début déclarations de fonctions ###
def choisirParams():
    global noms, nbr_batons
    nom_j1 = input("Entrez le nom du J1 : ")
    nom_j2 = input("Entrez le nom du J2 : ")

    nom_j1 = nom_j1 or "J1"
    nom_j2 = nom_j2 or "J2"

    noms = [nom_j1, nom_j2]

    try:
        nbr_batons = int(input("Entrez le nombre de bâtons ( 2<x<21 ; défaut: 10): "))
        if(not 2<nbr_batons<21):
            raise ValueError("Non compris entre 2 et 20")
    except:
        nbr_batons = 10
        print("Nombre de bâtons non valide")

    print("Nombre de bâtons : ", nbr_batons)


def commencerNvJeu():
    global tour_j, heureDepart
    tour_j = choice([0,1]) # Choisit quel joueur commence
    
    heureDepart = datetime.now()


def play(tour):
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
    while(input_joueur == -1):
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
            print(msg)
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
    global nbr_batons
    
    # Si erreur : return Error
    # Si pas erreur : return True
    if(nbr_batons-input_joueur<1):
        interval_batons_max = 3
        if(nbr_batons<4):
            interval_batons_max = nbr_batons-1
            if(interval_batons_max==1):
                return ["PlusDeBaton", "Vous ne pouvez pas enlever tous les bâtons! Vous pouvez enlever 1 bâton uniquement"]
            else:
                return ["PlusDeBaton", "Vous ne pouvez pas enlever tous les bâtons! Vous pouvez enlever 1 à "+str(interval_batons_max)+" bâtons"]

       
    else:
        nbr_batons -= input_joueur
        return True

def afficherBatons():
    str_batons = ""

    for i in range(nbr_batons):
        str_batons += baton_img

    return str_batons


def terminerTour():
    global tour_j
    if(siJeuTermine()):
        terminerJeu(tour_j)
        return True # Jeu terminé
    else:
        tour_j = 0 if tour_j==1 else 1 # Changer de tour
    
    return False # Jeu NON terminé 
 

def siJeuTermine():
    global nbr_batons
    return nbr_batons == 1 # True ou False

def terminerJeu(gagnant):

    heureFin = datetime.now()
    tempsJeu = heureFin - heureDepart + timedelta(minutes=1)

    print("\n\n")
    print("FIN DU JEU")
    print("Bravo " + noms[gagnant])
    print("Nombre de tours : ", nbr_tour)

    print("Temps : {minutes} mins et {secs}s".format( minutes=int(tempsJeu.seconds%60) , secs=int(tempsJeu.seconds/60) ) )


### Début du jeu

choisirParams()
commencerNvJeu()

finDuJeu = False
while(not finDuJeu):
    play(tour_j)
    finDuJeu = terminerTour()