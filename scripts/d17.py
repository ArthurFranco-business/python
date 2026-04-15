#Triangulo/hipotenusa/cateto
from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
a = (co**2) + (ca**2)
a2 = sqrt(a)
print('A hipotenusa desse triângulo é igual à {:.2f}'.format(a2))

