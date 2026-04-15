#Aluguel de Carros
d = int(input('Digite por quantos dias você alugou o carro: '))
km = int(input('Digite quantos km você rodou com ele: '))
preço = (km*0.15) + (60*d) 
print('O total a pagar é de R${}'.format(preço))