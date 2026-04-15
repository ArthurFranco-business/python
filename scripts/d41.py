#A confederação Nacional de natação precisa de im programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade.
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER
from datetime import date

nome = str(input('Digite seu nome: '))
ano = int(input("Seu ano de nascimento: "))
anoatu = date.today().year
idade = anoatu - ano
print("O senhor tem {} anos.".format(idade))
if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 20:
    print("Categoria: SENIOR")
else:
    print("Categoria: MASTER")
print("Boa prova!")