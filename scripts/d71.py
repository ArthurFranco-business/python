#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa tem cédulas de 50, 20, 10, 1.

cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0

valor = int(input("Digite o valor para sacar: "))

while True:
    if valor >= 50:
        while valor >= 50:
            valor = valor - 50
            cont_50 = cont_50 + 1
        print("Foram necessárias {} cédulas de R$50".format(cont_50))

    if valor >= 20:
        while valor >= 20:
            valor = valor - 20
            cont_20 = cont_20 + 1
        print("Foram necessárias {} cédulas de R$20".format(cont_20))

    if valor >= 10:
        while valor >= 10:
            valor = valor - 10
            cont_10 = cont_10 + 1
        print("Foram necessárias {} cédulas de R$10".format(cont_10))

    if valor >= 1:
        while valor >= 1:
            valor = valor - 1
            cont_1 = cont_1 + 1
        print("Foram necessárias {} cédulas de R$1".format(cont_1))

    if valor == 0:
        break

