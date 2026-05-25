#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


cont = 0
print("==" * 21)
print("Bem vindo a Tabuada Online. Digite um valor para sua tabuada aparecer.")
print("Caso queira encerrar o programa, digite um valor negativo.")
print("==" * 21)
print("")
while True:

    valor = int(input("Qual valor você quer imprimir a tabuada: "))
    print("==" * 21)
    cont = 0
    if valor < 0:
        break

    for i in range(1, 12):
        print(valor, "x", cont, " = ", valor* cont)
        cont += 1
    print("=="*21)
print("Tabuada encerrada devido ao número negativo digitado. Obrigado por participar.")
