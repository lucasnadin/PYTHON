import sys  

usuario_errado = True
chances = 5

while usuario_errado and chances > 0:
    usuario = input("Insira o usuário:")
    usuario_errado = usuario != "AnaNadin"
    if usuario_errado:
        print("Usuário não encontrado!Tente novamente!")
        chances -= 1
        if chances == 4:
            print("Restam 4 tentativas")
        elif chances == 3:
            print("Restam 3 tentativas")
        elif chances == 2:
            print("Restam 2 tentativas")
        elif chances == 1:
            print("Resta 1 tentativa")
        else:
            print("Não restam mais tentativas")
            
if chances == 0:
    print("Limite de tentativas de Login atingido! Tente novamente mais tarde")
    sys.exit()
else:
    print("Agora a senha!")



senha_errada = True
chances = 5

while senha_errada and chances > 0:
    senha = input("Insira a senha:")
    senha_errada = senha != "123"
    if senha_errada:
        print("Senha incorreta!")
        chances -= 1
        if chances == 4:
            print("Restam 4 tentativas!")
        elif chances == 3:
            print("Restam 3 tentativas!")
        elif chances == 2:
            print("Restam 2 tentativas!")
        elif chances == 1:
            print("Resta 1 tentativa!")
        else:
            print("Não restam mais tentativas!")
            
if chances == 0:
    print("Limite de senhas erradas inseridas atingido! Tente novamente mais tarde")
else: 
    print("Obrigado por acessar!")
    
def login1(x):
    return x

def login2(y):
    return y

dados1 = login1(usuario)
dados2 = login2(senha)

print("O seu login é:",dados1)
print("O sua senha é:",dados2)

print("Bem vindo ao app que calcula o cubo dos números!")

def cubo(t):
    s = t**3
    return s
    
seu_numero = float(input("Insira o seu numero:"))

a = cubo(seu_numero)

print("O seu numero é",a)
    
    