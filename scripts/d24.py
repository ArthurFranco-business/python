#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo
ncidade = input("Digite o nome da cidade: ")
letras = ncidade.split()
pnome = letras[0]
print ("Santo" in pnome)

