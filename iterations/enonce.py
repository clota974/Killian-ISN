# KILLIAN CLOTAGATIDE / Chapitre 5

#Compléter le programme suivant :
#le but est de faire deviner a l'utilisateur un entier choisi au hasard par python entre 0 et 100
#il a droit a autant d'essai que necessaire
#Si la reponse est supérieure au nombre cherché, l'indication : "l'entier à trouver plus petit" apparait
#Si la reponse est inférieure au nbr recherché, l'indication : "l'entier à trouver plus grand" apparait
#Si c'est la bonne reponse : le message "Bravo" apparait
import random

nb_secret=random.randint(0,100)

nb=int(input("nombre choisi? "))

while nb != nb_secret:
    if nb>nb_secret:
        nb = int(input("C'est un chiffre inférieur à "+str(nb)+" : "))
    else:
        nb = int(input("C'est un chiffre supérieur à "+str(nb)+" : "))

print("Bravo!")

