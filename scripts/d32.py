#Faça um programa que leia um ano qualquer e mostre se ele é bissexto ou não.
ano = int(input("Digite um ano qualquer: "))
if ano % 4 == 0:
    print("{0} é um ano bissexto!".format(ano))
else:
    print("{0} não é um ano bissexto!")
print("Fim")