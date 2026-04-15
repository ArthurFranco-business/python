#Faça um programa que leia as notas de 4 alunos. No final, mostre a maior nota, a menor nota e quantos alunos tiraram nota acima de 7.
maior = 0
menor = 99999999999999
acimamedia = 0
for n in range(1,5):
    nota = float(input("Digite a nota do {}° aluno: ".format(n)))
    if nota >=7:
        acimamedia += 1
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

print("A maior nota foi de {:.1f}".format(maior))
print("A menor nota foi de {:.1f}".format(menor))
print("Quantidade de alunos que tiraram acima de 7.0:  {}".format(acimamedia))
