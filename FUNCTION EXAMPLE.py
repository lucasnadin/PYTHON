def maior_numero(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a1 = int(input("a:"))
a2 = int(input("b:"))
a3 = int(input("c:"))

Maior = maior_numero(a1,a2,a3)

print("O maior número é",Maior)