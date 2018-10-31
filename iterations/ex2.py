# KILLIAN CLOTAGATIDE / Iterations : Ex 2

def U(x):
    n = 0
    Un = 3
    while n<x:
        n += 1
        Un = 0.5*Un+5 # <==> U(n+1) = 0.5*U(n)+5
    return Un

p = float(input("Entrez la précision : "))

N = -1 # Initialisation pour que N==0 lors de la première boucle
f = -1
while not(f>p): # On cherche à arrêter quand f>p
    N += 1
    f = abs(10-U(N)) #<==> |10-U(N)|
    ##### !!!! Il etait ecrit dans l'exercice U(N)-10 : est-ce une erreur ?


print(U(N))
print(f)
print("Le programme a retourné", N)