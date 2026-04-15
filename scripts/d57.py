#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valo correto.

sx = input("Digite o sexo [M/F]: ").upper()

while sx != "F" and sx != "M":
    sx = input("Digite novamente, só aceitamos valores como [M/F]: ").upper()

if sx == "M":
    print("Muito obrigado! Sexo registrado = Masculino")
elif sx == "F":
    print("Muito obrigado! Sexo registrado = Feminino")