#Faça um programa que leia as idades de 6 pessoas. No final, mostre qual foi a maior idade lida, a menor idade lida e a média das idades.
maior = 0
menor = 9999999
media = 0
for i in range(1,7):
    idade = int(input('Digite a {}º idade: '.format(i)))
    media += idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
print("A maior idade encontrada foi de {} anos".format(maior))
print("A menor idade encontrada foi de {} anos".format(menor))
print("A média das idades foi de {:.0F} anos".format(media/6))
