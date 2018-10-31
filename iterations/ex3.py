# KILLIAN CLOTAGATIDE / Iterations : Ex 3

# On représente un point par une liste à deux éléments

# a = [x,y]
# b = [x,y]
def milieu(a,b):
    x = (a[0]+b[0])/2
    y = (a[1]+b[1])/2
    return [x,y]

def distCarre(a,b):
    return (b[0] - a[0])**2 + (b[1] - a[1])**2 # ==>(xB – xA)² + (yB – yA)²

def estIsocele(a,b,c):
    AB2 = distCarre(a,b)
    BC2 = distCarre(b,c)
    CA2 = distCarre(c,a)

    cotesEgaux = 1 # Un côté est égal à soi même

    if(AB2==BC2):
        cotesEgaux += 1
    if(AB2==CA2):
        cotesEgaux += 1
    if(BC2==CA2):
        cotesEgaux += 1
    
    return cotesEgaux>1

print(estIsocele( [0,0] , [5,6] , [10,0]))