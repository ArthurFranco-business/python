#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
cont = 0
soma = 0
for i in range(1,7):
    num = int(input("Digite valor {}: ".format(i)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print("Você informou {} números pares, e a soma é igual à {}" .format(cont, soma))

