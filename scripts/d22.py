#crie um programa que leia o nome completo de uma pessoa e mostre:
# 1-) O nome com todas as letras maiúsculas.
# 2-) O nome com todas as letras minúsculas .
# 3-) Quantas letras ao todo (sem considerar os espaços).
# 4-) Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

lmai = nome.upper()
print("Seu nome com letras maiúsculas: {0}".format(lmai))


lmini = nome.lower()
print("Seu nome com letras minúsculas: {0}".format(lmini))

letras = nome.split()
junto = ''.join(letras)
print("Seu nome  tem {0} letras!".format(len(junto)))


pnome = letras[0]
print("Seu primeiro nome tem {0} letras!".format(len(pnome)))



