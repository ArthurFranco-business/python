n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
m = (n1 + n2) / 2
print("A media do aluno foi {:.2f}".format(m))
if m >=7:
    print("Aprovado")
else:
    print("Reprovado")
