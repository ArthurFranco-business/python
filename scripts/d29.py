#Escreva um programa que leia a velocidade de um carro.
#Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar 7,00 para cada km acima do limite
v = int(input('Velocidade do seu carro: '))
if v<=80:
    print("Você está de parabéns! Está dentro do limite!")
else:
    print("Você está acima do limite!")
    multa = (v-80) * 7
    print("O valor da multa é igual a R${}.00".format(multa))