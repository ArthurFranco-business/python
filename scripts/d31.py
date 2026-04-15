#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando 0,50 centavos por km para viagens até 200km e 0,45 para viagens mais longas.
d = float(input("Qual é a distância da sua viagem? "))
if d>=200:
    print("Sua viagem é longa!")
    pl = d * 0.45
    print("O preço de sua passagem é R${:.2f}".format(pl))
else:
    print("Sua viagem é curta!")
    pc = d * 0.50
    print("O preço de sua passagem é R${:.2f}".format(pc))
print("Boa viagem!")
