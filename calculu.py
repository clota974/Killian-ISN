def calculu(n):
    if n==0:
        return 1
    else:
        return calculu(n-1) + 2

print(calculu(100))