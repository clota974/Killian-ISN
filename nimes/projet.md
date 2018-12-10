## Calculer le temps de jeu :

...

Lors de la différence entre deux dates, il est retourné un objet timedelta, qui contient la différence de temps en secondes. Pour obtenir le nombres de minutes, 


```
from datetime import datetime, timedelta

# ...

def commencerNv():
    #global tour_j, heureDepart
    #tour_j = choice([0,1]) # Choisit quel joueur commence
    heureDepart = datetime.now()

# ...

def terminerJeu(gagnant):

    heureFin = datetime.now()
    tempsJeu = heureFin - heureDepart + timedelta(minutes=1)

    minutes=int(tempsJeu.seconds%60)
    secs=
    print("Temps : {minutes} mins et {secs}s".format( )

```