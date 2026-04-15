#Altura, Largura e área de uma parede para ver quantos litros de tinta serão necessários
lar = int(input('Digite a Largura de sua parede: '))
h = int(input('Digite a Altura de sua parede: '))
area = lar*h
tinta = area/2
print('A área de sua parede é {}m². Serão necessários {} litros de tinta.'.format(area,tinta))