#Faça um programa que leia o ano de nascimento de um jovem e informe, de acorde com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar
#Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
nome = str(input("Qual é o seu nome? "))
ano = int(input("Em que ano estamos: "))
anonas = int(input("Em que ano você nasceu? "))
niver = str(input("Já fez aniversário? 1- Sim // 2- Não: "))
hm = (ano - anonas) -  18
if ano - anonas == 18 and niver == "1":
    print("Caro {}, é hora de se alistar.".format(nome))
elif ano - anonas == 18 and niver == "2":
    print("Caro {}, ainda esse ano você deverá se alistar.".format(nome))
elif ano - anonas > 18:
    print("Caro {0}, já passou {1} anos do prazo de se alistar.".format(nome,hm))
elif ano - anonas < 18:
    print("Caro {}, o senhor ainda vai se alistar no ano de {}.".format(nome, (anonas +18)))
else:
    print("Algo deu errado, execute o programa novamente.")
print("SELVA!")

