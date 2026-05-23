#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
from time import sleep
print("=="*15)
print("     10 TERMOS DE UMA PA     ")
print("=="*15)


pm = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão dessa PA: "))
cont = 1
termo = pm

while cont <=10:
    print(" {} -> ".format(termo), end="")
    termo = termo + r
    cont += 1

print("FIM", end="")
sleep(1)
print("")
