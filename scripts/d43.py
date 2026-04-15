#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre sua condição conforme a tabela abaixo.
#Abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso ideal
#25 até 30: sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
kg = float(input("Digite seu peso em kg: "))
h = float(input("Digite sua altura: "))
imc = kg / (h*h)
print("O seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
    print("IMC: Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("IMC: Peso ideal.")
elif imc >= 25 and imc < 30:
    print("IMC: Sobrepeso.")
elif imc >= 30 and imc < 40:
    print("IMC: Obesidade.")
elif imc >= 40:
    print("IMC: Obesidade Mórbida.")
else:
    print("Algo deu errado, preencha as medidas corretamente.")

