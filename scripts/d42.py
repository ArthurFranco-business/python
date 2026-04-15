#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais.
#Escaleno: todos os lados diferentes
print("""BEM VINDO. Nesse programa você consegue conferir se as retas "
      formam um triangulo ou não! Além de identificar o seu tipo. """)
r1 = float(input("Digite o valor da reta 1: "))
r2 = float(input("Digite o valor da reta 2: "))
r3 = float(input("Digite o valor da reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[32mÉ possível formar um triangulo!\033[m")
    if r1 == r2 and r2 == r3 and r3 == r1:
        print("Esse triângulo é \033[31mEquilátero!\033[m Pois possui todos os lados iguais")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Esse triângulo é  \033[31mIsósceles!\033[m Pois possui dois lados iguais")
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print("Esse triângulo é \033[31mEscaleno!\0331m Pois não possui nenhum dos lados iguais")
else:
    print("Não é possível formar um triangulo!")
print("Fim do programa!")
