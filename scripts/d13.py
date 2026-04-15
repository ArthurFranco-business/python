#Salário do Funcionário com 15% de aumento
sa = int(input('Digite seu salário atual: '))
ns = sa + (sa*0.15)
print('Parabens! Você ganhou um aumento de 15%, seu novo salário é R${:.2f}'.format(ns))