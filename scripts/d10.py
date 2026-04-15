#Real para Dólar
reais = int(input('Quanto você tem em reais para converter para dólares: '))
dol = reais / 5.72
print('Seus R${:.2f} reais equivalem à US${:.2f} dólares!'.format(reais,dol))