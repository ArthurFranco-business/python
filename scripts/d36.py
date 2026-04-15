#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode passar de 30% do salário ou então o empréstimo será negado.
casa = float(input("Qual o valor da casa que deseja comprar: R$"))
sal = float(input("Qual é seu salário: R$"))
anos = float(input("Em quantos anos você quer pagar: "))
pm = anos*12
parcelas = casa/pm
print("Para pagar uma casa de \033[34mR${}\033[m em \033[34m{:.1f} anos\033[m a prestação será de \033[34mR${:.2f}\033[m".format(casa,anos,parcelas))
if parcelas <= sal*0.3:
    print("\033[1;32mParabéns, o empréstimo de sua casa deu certo.\033[m")
else:
    print("\033[1;31mEmpréstimo Negado, infelizmente você não tem dinheiro suficiente para pagar.\033[m")
print("Obrigado!")