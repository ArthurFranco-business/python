#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo: Ana Maria de Souza. Primeiro=Ana último=Souza
nome = input("Digite seu nome: ")
letras = nome.split()
pnome = letras[0]
print("Primeiro: {0}".format(pnome))
ultimo = letras[-1]
print("Ultimo: {0}".format(ultimo))