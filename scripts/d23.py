#Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos digitos separados
#exemplo: Digite um número: 1834 - unidade:4 dezena: 3 centena:8 e milhar:1
n = input("Digite um número: ")
print("Unidade:{0}".format(n[3]))
print("Dezena:{0}".format(n[2]))
print("Centena:{0}".format(n[1]))
print("Milhar:{0}".format(n[0]))