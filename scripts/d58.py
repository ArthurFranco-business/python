#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

print("O computador pensou em um número entre 0 e 10. Tente Adivinha-lo.")
n = random.randint(0,10)
p = int(input("Seu palpite: "))
t = 1

while p != n:
    p = int(input("Errou! Tente novamente: "))
    t = t + 1

print("Parabéns, você venceu! Foram necessários {} tentativas para acertar o número {}".format(t,n))