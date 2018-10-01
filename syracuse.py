def syracuse(n):
    #isPair = True if n%2==0 else 0
    if(n%2==0):
        return int(n/2)
    else:
        return int(3*n+1)

print(syracuse(1))