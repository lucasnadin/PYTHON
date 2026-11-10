import random

# ==========================================
# SUPER TRUNFO COMPLETO
# ==========================================

# GABARITO DOS ATRIBUTOS
atributos = [
    "Nome",
    "Velocidade",
    "Tanque",
    "Ano"
]

# BARALHO
baralho = [
    ["Ferrari F40", 324, 120, 1987],
    ["Bugatti Chiron", 420, 100, 2016],
    ["Porsche 911", 310, 64, 1964],
    ["McLaren P1", 350, 72, 2013],
    ["Lamborghini Aventador", 350, 90, 2011],
    ["Nissan GT-R", 315, 74, 2007],
    ["Ford Mustang", 250, 61, 1964],
    ["Chevrolet Camaro", 290, 72, 1966]
]

# EMBARALHAR
random.shuffle(baralho)

# DISTRIBUIR CARTAS
jogador1 = []
jogador2 = []

for i in range(len(baralho)):

    if i % 2 == 0:
        jogador1.append(baralho[i])

    else:
        jogador2.append(baralho[i])

# ESCOLHER MODO
print("=================================")
print("SUPER TRUNFO")
print("=================================")

print("\n1 - Jogador vs Computador")
print("2 - Jogador vs Jogador")

modo = input("\nEscolha o modo: ")

# DEFINIR TURNO
turno = 1

# MONTE DE EMPATE
monte = []

# LOOP PRINCIPAL
while len(jogador1) > 0 and len(jogador2) > 0:

    print("\n=================================")

    print("\nCartas Jogador 1:", len(jogador1))
    print("Cartas Jogador 2:", len(jogador2))

    carta1 = jogador1[0]
    carta2 = jogador2[0]

    if modo =="1":
        
        # MOSTRAR CARTA JOGADOR 1
        print("\nCarta do Jogador 1:")
        print("Nome:", carta1[0])
        print("1 - Velocidade:", carta1[1])
        print("2 - Tanque:", carta1[2])
        print("3 - Ano:", carta1[3])
        # ESCOLHA DO ATRIBUTO
        escolha = int(input("\nJogador 1 escolha um atributo: "))

    else:

        if modo == "1":

            escolha = random.randint(1, 3)

            print("\nComputador escolheu:", escolha)

        else:
            
            escolha = int(input("\nJogador 2 escolha um atributo: "))

    # PEGAR VALORES
    valor1 = carta1[escolha]
    valor2 = carta2[escolha]

    # MOSTRAR CARTA ADVERSÁRIO
    print("\nCarta do Jogador 2:")
    print("Nome:", carta2[0])

    if escolha == 1:
        print("Velocidade:", valor2)

    elif escolha == 2:
        print("Tanque:", valor2)

    else:
        print("Ano:", valor2)

    # ADICIONAR AO MONTE
    monte.append(carta1)
    monte.append(carta2)

    # RESULTADO DA RODADA
    if valor1 > valor2:

        print("\nJogador 1 venceu a rodada!")

        jogador1.pop(0)
        jogador2.pop(0)

        for carta in monte:
            jogador1.append(carta)

        monte = []

        turno = 1

    elif valor2 > valor1:

        print("\nJogador 2 venceu a rodada!")

        jogador1.pop(0)
        jogador2.pop(0)

        for carta in monte:
            jogador2.append(carta)

        monte = []

        turno = 2

    else:

        print("\nEMPATE!")
        print("Cartas guardadas no monte.")

        jogador1.pop(0)
        jogador2.pop(0)

# RESULTADO FINAL
print("\n=================================")

if len(jogador1) > 0:

    vencedor = "Jogador 1"

else:

    vencedor = "Jogador 2"

print("\nVENCEDOR:", vencedor)

# SALVAR RANKING
arquivo = open("ranking.txt", "a", encoding="utf-8")

arquivo.write(vencedor + "\n")

arquivo.close()

print("\nResultado salvo no ranking.txt")