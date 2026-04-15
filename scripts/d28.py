import random
#Escreva um programa que faça o computador pensar em um número entre 0 e 5 e peça para o usuário tentar escolher qual o número escolhido pelo computador
#O programa deverá mostrar se o usuário venceu ou perdeu esse jogo.
print("O computador pensou em um número entre 0 e 5. Tente Adivinha-lo.")
n = random.randint(0,5)
nu = int(input("Seu palpite: "))
if n == nu:
    print("Parabéns, você venceu!")
else:
    print("Você perdeu! Eu ganhei hahaha!")
print("Obrigado por usar o programa! O número era {}".format(n))

