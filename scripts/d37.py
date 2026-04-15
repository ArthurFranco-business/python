#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
#1 para binário
#2 para octal
#3 para hexadecimal
n = int(input("Digite um número: "))
bc = int(input("""Qual será a base de conversão? 
     [ 1 ] Para binário
     [ 2 ] Para octal
     [ 3 ]Para hexadecimal
     OPÇÃO SELECIONADA: """))
if bc == 1:
    print("Base de conversão selecionada: BINÁRIO")
    print("{} convertido para binário = {}".format(n, bin(n)[2:]))
elif bc == 2:
    print("Base de conversão selecionada: OCTAL")
    print("{} convertido para octal = {}".format(n, oct(n)[2:]))
elif bc == 3:
    print("Base de conversão selecionada: HEXADECIMAL")
    print("{} convertido para hexadecimal = {}".format(n, hex(n)[2:]))
else:
    print("Algo deu errado, execute o programa novamente.")
