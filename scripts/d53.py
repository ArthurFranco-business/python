#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = (str(input("Digite uma frase: ")).upper().strip())
separador = frase.split()
junto = "".join(separador)
inverso = junto[::-1]
print(frase + " ->", inverso)
if inverso == frase:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo!")

