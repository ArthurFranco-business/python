#Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos.
maioridade = 0
media_idade = 0
nome_maioridade = 0
menosdevinte = 0

for i in range(1,5):
    print("------{}º PESSOA------".format(i))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    media_idade = media_idade + idade

    if sexo == "M" and idade > maioridade:
        maioridade = idade
        nome_maioridade = nome

    if sexo == "F" and idade < 20:
        menosdevinte = menosdevinte + 1


print("A média das idades é de {:.0f}".format(media_idade / 4))
print("O homem mais velho é {}, com {} anos".format(nome_maioridade, maioridade))
print("Existem {} mulheres com menos de 20 anos".format(menosdevinte))

