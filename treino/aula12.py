nome = str(input('Digite seu nome: '))
if nome == 'Arthur':
    print("Belo nome rapaz")
elif nome == 'Paulo' or nome == 'Pedro' or nome == 'Maria':
    print("Seu nome é bem popular no Brasil")
elif nome in 'Ana Claúdia Jéssica Juliana':
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia, {}!".format(nome))