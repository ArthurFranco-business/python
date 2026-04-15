#ARTHUR FRANCO MAGRI
#CAIO TEXEIRA FAUSTINO

# A CASA ABANDONADA - PARTE 1
# Jogo de RPG de Terror e Escolhas
# Agora com sistema de vida e inventário!

print("=" * 50)
print("     A CASA ABANDONADA")
print("=" * 50)
print()

# Variáveis do jogo
vida = 100
inventario = []  # lista vazia pro inventário

# Introdução
print("Você e seus amigos Carlos e Júlia estão entediados")
print("numa sexta-feira à noite.")
print()
print("Carlos: 'Cara, tô cansado de ficar em casa!'")
print("Júlia: 'Vamos fazer algo diferente hoje!'")
print()
print("Você se lembra da velha casa abandonada no fim da rua.")
print("Dizem que ninguém mora lá há 20 anos...")
print()

nome = input("Qual é o seu nome? ")
print()
print(f"Olá, {nome}! Vamos começar a aventura...")
print()

# Decisão 1
print("=" * 50)
print("DECISÃO 1: Ir para a casa?")
print("=" * 50)
print()
print(f"{nome}: 'Pessoal, e se a gente fosse na casa abandonada?'")
print("Carlos: 'Sério?! Aquela casa é assustadora...'")
print("Júlia: 'Mas vai ser emocionante! Vamos pixar as paredes!'")
print()
print("1 - Convencer eles a ir")
print("2 - Desistir da ideia")

escolha1 = input("Escolha (1 ou 2): ")
print()

if escolha1 == "2":
    print("Você desiste da ideia e volta pra casa.")
    print("FIM DE JOGO - Você perdeu a aventura!")
    exit()

# Continuação da história
print("Vocês decidem ir! Às 22h, vocês se encontram")
print("em frente ao portão enferrujado da casa.")
print()
print("A lua está cheia. O vento faz barulhos estranhos.")
print("A casa está completamente escura...")
print()
print("Antes de entrar, você encontra algo no chão!")
print("É uma LANTERNA velha mas que ainda funciona!")
print()
inventario.append("Lanterna")  # adiciona lanterna no inventário
print("✓ LANTERNA adicionada ao inventário!")
print()
print("*CRREEEEAAAAK* - O portão range ao abrir")
print()

# Decisão 2
print("=" * 50)
print("DECISÃO 2: Como entrar?")
print("=" * 50)
print()
print("Carlos: 'Cara, olha aquela janela quebrada ali!'")
print("Júlia: 'A porta da frente tá entreaberta também...'")
print()
print("1 - Entrar pela janela quebrada")
print("2 - Entrar pela porta da frente")

escolha2 = input("Escolha (1 ou 2): ")
print()

if escolha2 == "1":
    print("Vocês entram pela janela.")
    print("CRASH! Você corta o braço num vidro!")
    print()
    vida = vida - 15  # perde vida
    print(f"💔 VIDA: {vida}/100")
else:
    print("Vocês entram pela porta da frente.")
    print("*CRREEEEAAAAK* - A porta range muito alto!")
    print(f"❤️ VIDA: {vida}/100")

print()

# Dentro da casa
print("=" * 50)
print("DENTRO DA CASA")
print("=" * 50)
print()
print("Vocês acendem a lanterna.")
print("A casa está cheia de móveis cobertos por lençóis brancos.")
print("Há teias de aranha por toda parte...")
print()
print("Você vê uma MESA com uma gaveta entreaberta!")
print()
print("1 - Investigar a gaveta")
print("2 - Ignorar e continuar")

escolha_gaveta = input("Escolha (1 ou 2): ")
print()

if escolha_gaveta == "1":
    print("Você abre a gaveta e encontra uma CHAVE ENFERRUJADA!")
    inventario.append("Chave")  # adiciona chave
    print("✓ CHAVE adicionada ao inventário!")
    print()
else:
    print("Vocês ignoram a gaveta...")
    print()

print("Júlia: 'Cara, que frio aqui dentro!'")
print("Carlos: 'Vamos logo pixar e ir embora...'")
print()
print("De repente... *THUMMMMP*")
print("Um barulho forte vem do andar de cima!")
print()

# Decisão 3
print("=" * 50)
print("DECISÃO 3: Investigar o barulho?")
print("=" * 50)
print()
print("1 - Subir as escadas pra ver o que foi")
print("2 - Ignorar e começar a pixar a sala")
print("3 - Sair correndo da casa")

escolha3 = input("Escolha (1, 2 ou 3): ")
print()

if escolha3 == "3":
    print("Vocês saem correndo!")
    print("Carlos tropeça e cai. Você e Júlia o ajudam.")
    print()
    print("=" * 50)
    print("INVENTÁRIO FINAL:")
    print(inventario)  # mostra o inventário
    print("=" * 50)
    print()
    print("FIM DE JOGO - Vocês fugiram com medo!")
    exit()
elif escolha3 == "2":
    print("Vocês ignoram o barulho e começam a pixar.")
    print("Carlos faz um desenho na parede.")
    print()
    print("Mas o barulho continua... *THUMP* *THUMP* *THUMP*")
    print()
    print("ALGO CAI NA SUA CABEÇA!")
    vida = vida - 10  # perde vida
    print(f"💔 VIDA: {vida}/100")
    print()
    print("Júlia: 'Gente, acho que tem alguém aqui!'")
else:
    print("Vocês decidem subir as escadas...")
    print("Cada degrau range muito alto.")
    print("*creek* *creek* *creek*")

print()

# Encontra poção
print("No meio da escada, você encontra uma POÇÃO MISTERIOSA!")
print("Tem uma etiqueta: 'Beba em emergência'")
print()
print("1 - Pegar a poção")
print("2 - Deixar ela lá")

escolha_pocao = input("Escolha (1 ou 2): ")
print()

if escolha_pocao == "1":
    inventario.append("Poção")  # adiciona poção
    print("✓ POÇÃO adicionada ao inventário!")
    print()
else:
    print("Você deixa a poção na escada...")
    print()

# O corredor
print("=" * 50)
print("O CORREDOR ASSOMBRADO")
print("=" * 50)
print()
print("Vocês chegam no corredor do segundo andar.")
print("Há várias portas fechadas.")
print("Uma luz fraca vem de baixo de uma das portas...")
print()
print("Carlos sussurra: 'Cara, isso não tá certo...'")
print()
print("SÚBITO! Uma porta se abre sozinha com força!")
print("*BAAAMMMM!*")
print()
print("Uma figura branca aparece no fim do corredor!")
print("Vocês ouvem uma voz rouca: 'Saiam... daqui...'")
print()
print("A figura avança! Você sente uma dor forte no peito!")
vida = vida - 20  # perde mais vida
print(f"💔 VIDA: {vida}/100")
print()

# Verifica se tem a poção
if "Poção" in inventario:
    print("Você se lembra da POÇÃO!")
    print()
    print("1 - Beber a poção agora")
    print("2 - Guardar pra depois")

    usar_pocao = input("Escolha (1 ou 2): ")
    print()

    if usar_pocao == "1":
        vida = vida + 30  # recupera vida
        inventario.remove("Poção")  # remove do inventário
        print("Você bebe a poção e se sente melhor!")
        print(f"❤️ VIDA: {vida}/100")
        print()

# Decisão final
print("=" * 50)
print("DECISÃO FINAL!")
print("=" * 50)
print()
print("Você vê uma porta TRANCADA com um símbolo estranho!")
print()
print("1 - Correr de volta pras escadas")
print("2 - Entrar no quarto com luz")
print("3 - Tentar abrir a porta trancada")

escolha_final = input("Escolha (1, 2 ou 3): ")
print()

if escolha_final == "1":
    print("VOCÊS CORREM!")
    print("A figura branca começa a flutuar em direção a vocês!")
    print("Carlos cai nas escadas! Júlia grita!")
    print()
    print(f"{nome}, você puxa seus amigos e conseguem sair da casa!")
    print("Vocês olham pra trás e veem uma sombra na janela...")
    print()
    print("=" * 50)
    print(f"STATUS FINAL - {nome}")
    print("=" * 50)
    print(f"❤️ VIDA: {vida}/100")
    print(f"🎒 INVENTÁRIO: {inventario}")
    print("=" * 50)
    print()
    print("FIM DA PARTE 1")
    print("Vocês sobreviveram... por enquanto.")

elif escolha_final == "2":
    print("Vocês entram no quarto iluminado.")
    print("É um quarto de criança... cheio de brinquedos antigos.")
    print("Uma caixa de música está tocando sozinha...")
    print()
    print("Você pisa num brinquedo quebrado!")
    vida = vida - 10
    print(f"💔 VIDA: {vida}/100")
    print()
    print("A porta se fecha atrás de vocês! *SLAM!*")
    print()
    print("=" * 50)
    print(f"STATUS FINAL - {nome}")
    print("=" * 50)
    print(f"❤️ VIDA: {vida}/100")
    print(f"🎒 INVENTÁRIO: {inventario}")
    print("=" * 50)
    print()
    print("FIM DA PARTE 1")
    print("Vocês estão trancados... O que será que vai acontecer?")

else:
    # Verifica se tem a CHAVE
    if "Chave" in inventario:
        print("Você usa a CHAVE ENFERRUJADA na porta!")
        print("*click* A porta abre!")
        print()
        print("Dentro há um baú antigo...")
        print("Vocês abrem e encontram... FOTOS antigas da casa!")
        print("Nas fotos, vocês veem a história do fantasma...")
        print()
        print("De repente, a figura branca desaparece!")
        print("Uma voz sussurra: 'Obrigado... por me lembrarem...'")
        print()
        print("A casa fica em paz. Vocês conseguem sair tranquilos.")
        print()
        print("=" * 50)
        print(f"STATUS FINAL - {nome}")
        print("=" * 50)
        print(f"❤️ VIDA: {vida}/100")
        print(f"🎒 INVENTÁRIO: {inventario}")
        print("=" * 50)
        print()
        print("FIM DA PARTE 1 - FINAL SECRETO!")
        print("Você descobriu a verdade sobre o fantasma!")
    else:
        print("A porta está trancada! Você não tem a chave!")
        print()
        print("A figura branca se aproxima ainda mais!")
        print("Você sente um frio congelante!")
        vida = vida - 30  # perde muita vida
        print(f"💔 VIDA: {vida}/100")
        print()
        print("Vocês saem correndo escada abaixo!")
        print()
        print("=" * 50)
        print(f"STATUS FINAL - {nome}")
        print("=" * 50)
        print(f"❤️ VIDA: {vida}/100")
        print(f"🎒 INVENTÁRIO: {inventario}")
        print("=" * 50)
        print()
        print("FIM DA PARTE 1")
        print("Você tentou abrir mas não tinha a chave...")

print()
print("=" * 50)
print("OBRIGADO POR JOGAR!")
print("Aguarde a PARTE 2...")
print("=" * 50)