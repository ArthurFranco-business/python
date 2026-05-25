#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = "S"
cont = 0
soma = 0
maior_num = 0
menor_num = 0


while resp == "S":
    num = int(input("Digite um número: "))
    resp = input("Você deseja continuar? [S/N] ")
    resp = resp.upper()

    cont = cont + 1
    soma = soma + num

    if cont == 1:
        maior_num = num
        menor_num = num

    if num > maior_num:
        maior_num = num

    if num < menor_num:
        menor_num = num



media = soma / cont
print("Você digitou {} números e a média foi de {}".format(cont, media))
print("O maior valor digitado foi {} e o menor foi {}".format(maior_num, menor_num))




