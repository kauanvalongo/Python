import random
print('MÁQUINA DE PALPITES DA MEGA SENA')
print('-='*30)
quant = int(input('Quantos Jogos você quer palpitar? :'))
print('-='*30)
lista = []
for c in range(0, quant):
    while len(lista) < 6:
        n = random.randint(1, 60)
        if n not in lista:
            lista.append(n)
        lista.sort()
    print(f'O {c+1}o. palpite é {lista}')
    lista.clear()
print('-='*30)
