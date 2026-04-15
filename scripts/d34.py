#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a 1250,00. Calcule um aumento de 10%.
#Para os inferiores ou iguais o aumento é de 15%.
salario = float(input("Digite seu salário: "))
if salario > 1250:
    nvsal = (salario * 0.10) + salario
    print("Seu novo salário é de R${}".format(nvsal))
else:
    onsal = (salario * 0.15) + salario
    print("Seu novo salário é de R${}".format(onsal))
print("Parabéns pelo aumento!")