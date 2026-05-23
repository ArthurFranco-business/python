#Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência de Fibonacci.
print("=="*15)
print("    Sequência de Fibonacci    ")
print("=="*15)
print("")
n = int(input("Quantos elementos você quer mostrar: "))

pt = 0
st = 1
cont = 2

print("0 -> 1 -> ", end="")

while cont < n:
    nt = pt + st
    print(nt,  "-> ", end="")
    cont += 1
    pt = st
    st = nt



print("Fim", end="")
