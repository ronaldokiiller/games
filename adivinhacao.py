import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?", numero_secreto)
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# os parentesese são redundantes, ou seja, desnecessários
for rodada in range(1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if (total_de_tentativas == rodada):
            print("O numero secretor era {} e você fez {} pontos".format(numero_secreto,pontos))



print("Fim do jogo")