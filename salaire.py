def computepay(heures,taux):
    salaire = 0
    if heures>40:
        heuresSup = heures-40
        tauxSup = 1.5*taux
        salaire = 40*taux+heuresSup*tauxSup
    else:
        salaire = heures*taux

    return salaire


def paie():
    heures = input("Heures : ")
    try:
        heures = float(heures)

        try:
            taux = float(input("Taux horaire : "))

            print("Votre paie : ",computepay(heures,taux))
        except Exception as identifier:
            print("Erreur, s’il vous plaît entrez un numérique")

    except Exception as identifier:
        print("Erreur, s’il vous plaît entrez un numérique")

paie()



