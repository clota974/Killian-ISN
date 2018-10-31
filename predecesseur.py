def prev(n):
    return n-1

def somme(n1,n2):
    return n1+n2

def saluer(prenom,langue):
    salut = "Bonjour"
    if(langue == "es"):
        salut = "Hola"
    if(langue == "en"):
        salut = "Hello"
    return salut+" "+prenom+"!"

print(prev(4))
print(somme(2,3))
print(saluer("Killian","es"))