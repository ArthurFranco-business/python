#Ler um número real e mostrar a porção inteira
from math import trunc
n = float(input('Digite um número: '))
pi = trunc(n)
print ('O número {} tem a parte inteira {}'.format(n,pi))