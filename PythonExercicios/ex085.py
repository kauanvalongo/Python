lista = [[], []]
n = 0
for c in range(0,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*30)
print(f'Os números digitados foram: {lista}')
lista[0].sort()
print(f'Os números pares foram: {lista[0]}')
lista[1].sort()
print(f'Os números ímpares foram: {lista[1]}')