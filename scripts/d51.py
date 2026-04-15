#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
print("=="*15)
print("     10 TERMOS DE UMA PA     ")
print("=="*15)


pm = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão dessa PA: "))

a10 = pm + 9 * r + 1
for i in range(pm, a10, r):
    print( i , "-> " , end=" ")
print("Acabou!")
