#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme a média atingida:
#- Média abaixo de 5: REPROVADO
#- Média entre 5 e 6,9: RECUPERAÇÃO
#- Média 7,0 ou superior: APROVADO
nome = str(input("Nome do aluno: "))
n1 = float(input("Qual foi a \033[4mprimeira\033[m nota do aluno(a) '{}': ".format(nome)))
n2 = float(input("Qual foi a \033[4msegunda\033[m nota do aluno(a) '{}': ".format(nome)))
m = (n1 + n2) / 2
print("A \033[4mmédia\033[m do aluno é de {:.2f}".format(m))
if m < 5:
    print("O aluno(a) '{}' foi \033[1;31mREPROVADO.\033[m".format(nome))
elif m >= 5 and m < 7:
    print("O aluno(a) '{}' está em \033[1;33mRECUPERAÇÃO.\033[m".format(nome))
elif m >= 7:
    print("O aluno(a) '{}' foi \033[32mAPROVADO.\033[m".format(nome))
else:
    print("Algo deu errado, execute o programa novamente.")
