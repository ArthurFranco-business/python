#Peça para o usuário digitar um texto. A seguir, mostre um menu com as seguintes opções:
#1) Imprimir todo o texto em letras maiúsculas.
#2) Imprimir todo o texto em letras minusculas. 
#3) Imprimir o texto de forma alternada:

text = input("Digite o texto: ")
tm = text.upper()
print (" ")
print ("Texto com letras maiúsculas: {0}".format(tm))
print (" ")
tmi = text.lower()
print ("Texto com letras minúsculas: {0}".format(tmi))