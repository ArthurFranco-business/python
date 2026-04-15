#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento.
#À vista dinheiro ou cheque: desconto 10%
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
valor = float(input("Digite um valor do produto: R$"))
print("""\033[4;34mOrientações:\033[m
- À vista dinheiro ou cheque: \033[32mdesconto 10%\033[m
- À vista no cartão: \033[32m5% de desconto\033[m
- Em até 2x no cartão: \033[33mpreço normal\033[m
- 3x ou mais no cartão: \033[31m20% de juros\033[m """)
print("""
\033[7m[ 1 ]\033[m dinheiro ou cheque
\033[7m[ 2 ]\033[m a vista no cartão
\033[7m[ 3 ]\033[m até 2x no cartão
\033[7m[ 4 ]\033[m 3x ou mais no cartão""")
fp = int(input("Opção escolhida: "))
if fp == 1:
    print("\033[34mDINHEIRO ou CHEQUE\033[m")
    d = (valor * 0.10)
    d1 = valor - d
    print("""DESCONTO: R${} 
    VALOR FINAL: R${} """.format(d, d1))
elif fp == 2:
    print("\033[34mA VISTA NO CARTÃO\033[m")
    d = (valor * 0.05)
    d1 = valor - d
    print("""DESCONTO: R${}
        VALOR FINAL: R${} """.format(d, d1))
elif fp == 3:
    print("\033[34mATÉ 2 VEZES NO CARTÃO\033[m")
    print("VALOR FINAL: R${} """.format(valor))
elif fp == 4:
    print("\033[34m3X OU MAIS NO CARTÃO\033[m")
    j = (valor * 0.20)
    vf = j + valor
    print("""JUROS: R${}
    VALOR FINAL: R${} """.format(j, vf))
else:
    print("Algo deu errado, execute o programa novamente.")
print("Obrigado pela confiança!")


