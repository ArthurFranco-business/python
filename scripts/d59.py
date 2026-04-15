#Crie um programa que leia 2 valores e mostre um menu como ao lado da tela. Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

p1 = int(input("Digite o primeiro valor: "))
p2 = int(input("Digite o segundo valor: "))
opcao = 0

while opcao != 5:
    sleep(1)
    print(" ")
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] fechar o programa")
    opcao = int(input("Opção selecionada: "))


    if opcao == 1:
        soma = p1 + p2
        print("A soma entre {} e {} = {}".format(p1, p2, soma))

    elif opcao == 2:
        multiplicar = p1 * p2
        print("A multiplicação entre {} e {} = {}".format(p1, p2, multiplicar))

    elif opcao == 3:
        maior = max(p1, p2)
        print("Entre {} e {}, o maior número = {}".format(p1, p2, maior))

    elif opcao == 4:
        p1 = float(input("Digite o primeiro novo valor: "))
        p2 = float(input("Digite o segundo novo valor: "))
print("Finalizando...")
sleep(1)
print("Programa encerrado, obrigado por participar!")

