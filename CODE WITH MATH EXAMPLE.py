import math
    
def perimetro(a,b,c):
    y = a + b + c
    return y

a1 = float(input("Insira o primeiro lado:"))
b1 = float(input("Insira o segundo lado:"))
c1 = float(input("Insira o terceiro lado:"))

triangulo = perimetro(a1,b1,c1)

print("O perimetro do triangulo é",triangulo)

#A função a baixo calcula a area dessa maneira: a area(a,b,c) é a função que tem seus parametros, que depois vai ser substituidos pelos valores que recebemos nos inputs (a1,a2,a3), depois chamamos a função do perimetro e colocamos, no lugar dos parametros, os valores do input tbm (a1,a2,a3), depois dividimos por 2 e temos a variavel e a colocamos na formula e assim temos a função da formula de Heron!
def area(a,b,c):
    s = perimetro(a,b,c)/2
    V = math.sqrt(s*(s-a1)*(s-b1)*(s-c1))
    return V

Resultado = area(a1,b1,c1)

print(f"O resultado da area é {Resultado:.1f}")
