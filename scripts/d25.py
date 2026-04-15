#Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome ou não
nome = input("Digite seu nome: ")
letras = nome.split()
print ("Silva" in letras)