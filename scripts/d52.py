#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
num = int(input("Digite um número: "))
for i in range(1, (num+1)):
    print("\033[33m {}" , end=" ")
    if num % i == 0:
        print("\033[33m", end=" ")
        cont = cont + 1


print("\033[37m O número {} foi divisível {} vezes.".format(num, cont))
if cont <= 2:
    print("Por isso ele é um número primo!")
elif cont > 2:
    print("Por isso ele não é primo!")



