#Calculo do dobro, triplo e raiz quadrada de um número
n = int(input('Digite um número: '))
db = n*2
tr = n*3
rq = n**0.5
print('O dobro de {} é \033[32m{}\033[m, o triplo \033[35m{}\033[m e a raiz quadrada \033[31m{}'.format(n,db,tr,rq))
