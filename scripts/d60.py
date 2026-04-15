#Faça um programa que leia um número qualquer e mostre seu fatorial.
n = int(input("Digite um número: "))
f = 1
print("{}! = ".format(n), end="")
while n > 0:
    print("{}".format(n), end="")
    print(" x " if n >1 else " = ", end="")
    f *= n
    n -= 1
print("{}".format(f), end="")