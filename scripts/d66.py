#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

print("Digite um número [999 para parada] ")
num = 0
soma = 0
cont = -1

while num != 999:
    num = int(input("Seu número: "))
    if num == 999:
        break
    soma += num
    cont += 1





print("Você digitou {} números, e a soma deles foi de {}.".format(cont, soma))
