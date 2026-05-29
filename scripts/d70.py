#Crie um programa que leia o nome e o preço de vário produtos. O programa deverá perguntar se o usuário deve continuar ou não. No final, mostre:
# a) Qual é total gasto na compra
# b) quantos produtos custam mais de "1000,00"
# c) qual é o nome e o preço do produto mais barato
# d) qual é o nome e o preço do produto mais caro


total_gasto = 0
produtos_acima_mil = 0
preco_produto_mais_barato = 0
nome_produto_mais_barato = " "
preco_produto_mais_caro = 0
nome_produto_mais_caro = " "
ciclo = 0



print("-"*22)
print("    LOJA DO ARTHUR   ")
print("-"*22)


while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Preço: R$"))
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    ciclo = ciclo + 1
    total_gasto += preco

    if  ciclo == 1:
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = produto
        preco_produto_mais_caro = preco
        nome_produto_mais_caro = produto

    if preco < preco_produto_mais_barato:
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = produto

    if preco > preco_produto_mais_caro:
        preco_produto_mais_caro = preco
        nome_produto_mais_caro = produto

    if preco > 1000:
        produtos_acima_mil += 1

    if opcao == "N":
        break

print("-"*22)
print("O total da compra foi de RS{}".format(total_gasto))
print("Comprou {} produtos que custam acima de RS1000,00".format(produtos_acima_mil))
print("O produto mais barato foi {} que custa R${}".format(nome_produto_mais_barato, preco_produto_mais_barato))
print("O produto mais caro foi {} que custa R${}".format(nome_produto_mais_caro, preco_produto_mais_caro))