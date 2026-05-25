#Faça um programa que jogue par ou ímpar com o computador, o jogo só será interrompido quando o jogador perder, mostrando o tanto de vitórias consecutivas que o jogador teve.
import random
contador_de_sequencia = 0

while True:
    numero_jogador = int(input("Digite um valor: "))
    numero_computador = random.randint(0, 10)
    par_impar = str(input("Par ou Ímpar? [P/I] ")).upper()[0]

    resultado = numero_jogador+numero_computador

    if par_impar == "P" and resultado % 2 == 0:
        contador_de_sequencia += 1
        print("\033[1;32mVocê venceu.\033[m O computador jogou {} e você {}, logo o resultado final foi \033[1;32mPAR\033[m".format(numero_computador, numero_jogador))
        print("O computador ficou \033[1;31mFurioso\033[m e te desafia para a próxima rodada...")

    if par_impar == "I" and resultado % 2 == 1:
        contador_de_sequencia += 1
        print("\033[1;32mVocê venceu.\033[m O computador jogou {} e você {}, logo o resultado final foi \033[1;32mÍMPAR\033[m".format(numero_computador,numero_jogador))
        print("O computador ficou \033[1;31mFurioso\033[m e te desafia para a próxima rodada...")

    if par_impar == "I" and resultado % 2 == 0:
        print("\033[1;31mVocê perdeu.\033[m O computador jogou {} e você {}, logo o resultado final foi \033[1;31mPAR\033[m".format(numero_computador, numero_jogador))
        print("\033[1;31mGame Over!\033[m Você conseguiu vencer o computador {} vezes!".format(contador_de_sequencia))
        break

    if par_impar == "P" and resultado % 2 == 1:
        print("\033[1;31mVocê perdeu.\033[m O computador jogou {} e você {}, logo o resultado final foi \033[1;31mÍMPAR\033[m".format(numero_computador, numero_jogador))
        print("\033[1;31mGame Over! Você conseguiu vencer o computador {} vezes!\033[m".format(contador_de_sequencia))
        break

