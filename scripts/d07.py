#Notas e Médias do Aluno
aln = input('\033[32mNome do Aluno\033[m: ')
n1 = int(input('\033[32mDigite a primeira nota do aluno\033[m: '))
n2 = int(input('\033[32mDigite a Segunda nota do aluno\033[m: '))
media = (n1 + n2) / 2
print('O aluno {}, teve a primeira nota de \033[33m{}\033[m, a segunda \033[34m{}\033[m e sua media final \033[32m{}'.format(aln,n1,n2,media))