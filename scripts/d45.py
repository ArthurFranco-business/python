#Crie um programa que jogue "pedra, papel, tesoura" com você.
import random
from time import sleep

print("\033[7m=====Pedra, Papel, Tesoura=====\033[m")
print(
"""[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")
eu = int(input('Sua escolha: '))
pedra = "Pedra"
papel = "Papel"
tesoura = "Tesoura"
conjuntos = [pedra, papel, tesoura]
ec = random.choice(conjuntos)
print("PEDRA,")
sleep(0.5)
print("PAPEL,")
sleep(0.5)
print("TESOURA,")
sleep(0.5)
print("o computador escolheu {}".format(ec))
if ec == pedra and eu == 2:
    print("\033[32mVocê ganhou!\033[m")
elif ec == papel and eu == 1:
    print("\033[31mVocê perdeu!\033[m")
elif ec == tesoura and eu == 1:
    print("\033[32mVocê ganhou!\033[m")
elif ec == pedra and eu == 3:
    print("\033[31mVocê perdeu!\033[m")
elif ec == papel and eu == 3:
    print("\033[32mVocê ganhou!\033[m")
elif ec == tesoura and eu == 2:
    print("\033[31mVocê perdeu!\033[m")
else:
    print("\033[33mEmpatou, execute o programa novamente.")


