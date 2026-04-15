import math
from time import sleep
print ('Para palavras usamos as aspas. Já para números não.')
print (1, 2 , 3, 4)
print (7+4)

variavel = input("Qual o seu nome: ")
print ("Tenha um ótimo dia, " + variavel + "!")

numero = int(input("Digite um número: "))

n1 = 2
n2 = 3
soma = n1 + n2
print(" A soma entre {} e {} é {}".format(n1, n2, soma))

n = input("Digite algo: ")
if n.isnumeric():
    print("O valor digitado é numérico!")
else:
    print("Por favor, digite um valor numérico.")

print("="*20)

d = 10/3
print("Para limitar as casas, fica assim {:.3f}".format(d))

num = int(input("Digite um número qualquer: "))
raiz = math.sqrt(num)

frase = "Curso em Vídeo Python"
print(frase)
len(frase)
print("A frase tem {} caracteres".format(len(frase)))
print(frase.upper())
print(frase.lower())

print("Vamos contar até 10!")
for i in range(1,11):
    print(i)
    sleep(1)




