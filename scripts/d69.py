#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deve perguntar se ela quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18
# b) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos

mais_de_18 = 0
homem = 0
mulheres_menos_20 = 0
print("=-"*14)
print("    CADASTRE UMA PESSOA!    ")
print("=-"*14)
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [F/M]: ")).strip().upper()[0]
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    print("")
    if idade > 18:
        mais_de_18 += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1
    if continuar == "N":
        break

print("Total de mais de 18 anos: {}".format(mais_de_18))
print("Total de Homens: {}".format(homem))
print("Total de mulheres menos de 20 anos: {}".format(mulheres_menos_20))