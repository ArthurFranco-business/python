#Faça um programa que leia os preços de 5 produtos. No final, mostre o produto mais caro, o produto mais barato, a diferença entre eles e o preço médio dos produtos.
maior = 0
menor = 99999
media = 0
for p in range(1,5):
    preco = float(input("Digite o preço do {}º produto: ".format(p)))
    media = media + preco
    if preco > maior:
        maior = preco
    if preco < menor:
        menor = preco
print("O produto mais caro custa R${:.2f}".format(maior))
print("O produto mais barato custa R${:.2f}".format(menor))
print("A diferença do preço mais caro para o mais barato é de R${:.2f}".format(maior-menor))
print("A média dos preços dos produtos apresentados é de R${:.2f}".format(media/5))

