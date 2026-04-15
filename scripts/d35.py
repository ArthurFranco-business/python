#Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar o triângulo
print("BEM VINDO. Nesse programa você consegue conferir se as retas formam um triangulo ou não!")
r1 = float(input("Digite o valor da reta 1: "))
r2 = float(input("Digite o valor da reta 2: "))
r3 = float(input("Digite o valor da reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível formar um triangulo!")
else:
    print("Não é possível formar um triangulo!")
print("Fim do programa!")