# KILLIAN CLOTAGATIDE / Chapitre 5
from random import randint
toGuess = randint(1,100)
guessed = int(input("Devinez le nombre entre 1 et 100 : "))
while guessed != toGuess:
    if guessed>toGuess:
        guessed = int(input("C'est un chiffre inférieur à "+str(guessed)+" : "))
    else:
        guessed = int(input("C'est un chiffre supérieur à "+str(guessed)+" : "))
print("Bien ouèj !")