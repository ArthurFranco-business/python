import time

# Introdução
def introducao():
    print("\n=== TERROR NO ANIVERSÁRIO – ATO 1: A CHEGADA ===")
    time.sleep(2)
    print("Você e seus amigos foram convidados para uma festa de aniversário.")
    time.sleep(2)
    print("A casa fica afastada da cidade, cercada por uma floresta escura.")
    time.sleep(2)
    print("Tudo parece normal... até que o carro começa a falhar no meio do caminho.\n")
    input("Pressione ENTER para continuar...")
    estrada()

# Escolha inicial: continuar ou voltar
def estrada():
    print("\nO carro começa a fazer um barulho estranho.")
    time.sleep(1.5)
    print("Lucas, que está dirigindo, pergunta:")
    print("“Continuamos até a casa ou voltamos pra cidade?”")
    escolha = input("\n1 - Continuar\n2 - Voltar\nEscolha: ")

    if escolha == "1":
        print("\nVocê decide continuar. A curiosidade vence o medo.")
        time.sleep(1.5)
        print("Logo vocês avistam a casa iluminada à distância.")
        chegada()
    elif escolha == "2":
        print("\nVocês decidem voltar... mas o carro não liga mais.")
        time.sleep(1.5)
        print("De repente, algo se move entre as árvores.")
        print("O grupo entra em pânico e corre a pé até a casa.\n")
        chegada()
    else:
        print("\nOpção inválida!")
        estrada()

# Chegada na casa
def chegada():
    print("\nVocês chegam à casa. Há balões, música... mas ninguém parece estar lá.")
    time.sleep(2)
    print("A porta da frente está entreaberta.")
    time.sleep(1)
    print("Vocês entram e chamam o nome do aniversariante, mas ninguém responde.\n")
    input("Pressione ENTER para continuar...")
    salao()

# Explorar o salão principal
def salao():
    print("\nO salão está cheio de mesas e decorações.")
    time.sleep(1.5)
    print("Sobre a mesa principal há um bolo intocado e copos vazios.")
    time.sleep(1.5)
    print("De repente, vocês ouvem passos vindos do andar de cima.")
    time.sleep(1.5)

    escolha = input("\n1 - Subir para investigar\n2 - Ficar e procurar pistas no salão\nEscolha: ")

    if escolha == "1":
        print("\nVocê sobe as escadas com o coração acelerado...")
        andar_superior()
    elif escolha == "2":
        print("\nVocê decide procurar por algo útil no salão.")
        time.sleep(1.5)
        inventario = []
        inventario = pegar_itens(inventario)
        print("\nEnquanto você revira gavetas, uma sombra passa atrás de você.")
        print("Você se assusta e decide subir as escadas com o grupo.")
        andar_superior(inventario)
    else:
        print("Opção inválida!")
        salao()

# Coletar itens
def pegar_itens(inventario):
    itens_disponiveis = ["chave", "lanterna", "faca", "comida"]
    print("\nVocê encontra alguns objetos espalhados:")
    for item in itens_disponiveis:
        escolha = input(f"Deseja pegar {item}? (s/n): ").lower()
        if escolha == "s":
            inventario.append(item)
            print(f"{item.capitalize()} adicionada ao inventário.")
    return inventario

# Parte do andar superior
def andar_superior(inventario=None):
    if inventario is None:
        inventario = []

    print("\nAs escadas rangem sob seus pés.")
    time.sleep(2)
    print("No corredor, há três portas.")
    time.sleep(1)
    print("Uma delas está trancada. Outra parece ter sido forçada.")
    escolha = input("\n1 - Abrir a porta trancada\n2 - Entrar na porta forçada\n3 - Voltar\nEscolha: ")

    if escolha == "1":
        if "chave" in inventario:
            print("\nVocê usa a chave e destranca a porta.")
            quarto_trancado()
        else:
            print("\nA porta está trancada. Você não tem a chave.")
            andar_superior(inventario)
    elif escolha == "2":
        print("\nVocê empurra a porta forçada e entra.")
        quarto_forcado(inventario)
    elif escolha == "3":
        print("\nVocê decide descer novamente...")
        salao()
    else:
        print("Opção inválida!")
        andar_superior(inventario)

# Quarto trancado
def quarto_trancado():
    print("\nVocê entra em um quarto pequeno e escuro.")
    time.sleep(1.5)
    print("Há fotos espalhadas pelo chão... e todas mostram VOCÊ e seus amigos.")
    time.sleep(1.5)
    print("No verso de uma delas, uma mensagem escrita com sangue:")
    print("“VOCÊS NÃO DEVERIAM TER VINDO.”")
    time.sleep(2)
    print("\nDe repente, a porta se fecha sozinha!")
    print("Você ouve passos se aproximando do lado de fora...")
    time.sleep(2)
    esconder()

# Quarto forçado
def quarto_forcado(inventario):
    print("\nVocê entra e vê uma janela aberta, o vento balança as cortinas.")
    time.sleep(1.5)
    print("No canto, há uma mochila rasgada e um celular tocando.")
    escolha = input("\n1 - Atender o celular\n2 - Ignorar\nEscolha: ")

    if escolha == "1":
        print("\nVocê atende. Uma voz sussurra: 'Vocês não estão sozinhos...'")
        time.sleep(2)
        print("A ligação cai, e o celular se desliga sozinho.")
    elif escolha == "2":
        print("\nVocê ignora o celular, mas ele para de tocar subitamente.")
    else:
        print("Opção inválida!")
        quarto_forcado(inventario)

    print("\nVocês decidem sair do quarto.")
    time.sleep(1.5)
    andar_superior(inventario)

# Função de esconder
def esconder():
    print("\nVocê procura desesperadamente um lugar para se esconder!")
    lugares = ["embaixo da cama", "no armário", "atrás da cortina"]
    print(f"Opções: {lugares}")
    escolha = input("Escolha um lugar: ").lower()

    if "armário" in escolha:
        print("\nVocê segura a respiração...")
        time.sleep(2)
        print("Os passos param na frente da porta... e depois somem.")
        print("Você sobrevive... por enquanto.")
        final_ato1()
    else:
        print("\nVocê escolheu mal. Algo abre a porta e te encontra.")
        print("Um grito ecoa pela casa.")
        final_ruim()

# Final feliz (fim do Ato 1)
def final_ato1():
    print("\n=== FIM DO ATO 1 ===")
    print("Você sobreviveu à primeira noite na casa.")
    print("Mas o pesadelo está apenas começando...")

# Final ruim
def final_ruim():
    print("\n=== FINAL RUIM ===")
    print("Você foi uma das primeiras vítimas daquela noite sombria...")

# Execução principal
if __name__ == "__main__":
    introducao()
