#Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A".
# 2. Em que posição ela aparece a primeira vez.
# 3. Em qual posição ela aparece pela última vez.

frase = input("Digite uma frase: ")
fmi = frase.lower()
lA = fmi.count('a')
print("A letra (A) apareceu na frase: {} vezes".format(lA))

pv = fmi.find('a')
print("A letra (A) apareceu pela primeira vez na posição {0}".format(pv))
uv = fmi.rfind('a')
print("A letra (A) apareceu pela última vez na posição {0}".format(uv))
