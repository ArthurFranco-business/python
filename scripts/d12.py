#Preço com Desconto
preço = int(input('Digite o valor do produto: '))
desc = preço - (preço*0.05)
print('O Produto com desconto de 5%, tem o novo preço de R${:.2f}'.format(desc))