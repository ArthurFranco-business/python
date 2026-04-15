#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
cont_maioridade = 0
cont_jovem = 0
for i in range(1,8):
    ano = (int(input("Digite o ano de nascimento da {}º pessoa: ".format(i))))
    if ano > 2008:
        cont_jovem = cont_jovem + 1
    elif ano < 2008:
        cont_maioridade = cont_maioridade + 1
print("Ao todo tivemos {} pessoas menores de idade!".format(cont_jovem))
print("E tivemos {} pessoas maiores de idade!".format(cont_maioridade))

