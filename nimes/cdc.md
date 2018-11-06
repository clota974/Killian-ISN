# Cahier des charges

## Règles du jeu

### But du jeu
Un certain nombre de bâtons sont disposés sur le plateau de jeu.
Chacun son tour, chaque joueur pourra prendre jusqu'à 3 bâtons d'un coup.
Le perdant est celui qui prend le dernier bâton.

### Déroulement du jeu

#### Paramètrage
Le programme sera personnalisable et demandera :
1) Le nom du J1 et du J2
2) Le nombre de bâtons voulu (Par défaut : 10)

#### Jeu
Le joueur qui commence sera choisi au hasard.

Le jeu se déroulera dans cet ordre :

1) Afficher les bâtons
2) Demander à J1/J2 de tirer un 1 à 3 bâtons d'un coup
3) Enlever X bâtons (0<X<4)
4) Vérifier s'il reste un bâton
    + Si oui : Fin du jeu (cf. plus bas)
    + Si non : Le jeu continue --> Recommencer pour le joueur suivant 

#### Fin du jeu
Il est affiché :

+ Bravo J1/J2
+ Nombre de tours
+ (Temps qu'ils ont pris)

### Spécificités techniques

#### Variables utilisées
- Nom du J1 : `nom_J1`
- Nom du J2 : `nom_J2`
- Nombre de bâtons : `nbr_batons`
- Nombre de tours : `nbr_tours`
- Nombre de bâtons à enlever : `input_joueur` 

#### Réprésentation du plateau de jeu
Le nombre de bâtons sera stocké dans une variable nommée nbr_batons.

#### Initialisation
Le nombre de bâtons sera stocké avant le jeu

##### Affichage des bâtons
Nous afficherons les bâtons restant sur une même ligne grâce au caractère ASCII 124 (Barre verticale) : `|`

#### Enlever des bâtons
On soustraira le nombre de bâtons enlevé au nombre de bâtons présents : `nbr_batons = input_joueur - nbr_batons`

Il faudra faire attention à ne pas enlever plus de bâtons qu'il en reste.

Il faudra vérifier si le Joueur n'enlève pas plus de bâtons qu'il n'en reste.

