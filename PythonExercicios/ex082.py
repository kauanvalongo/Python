lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um número aqui: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    cont = str(input('Quer continuar? [S/N]'))
    if cont in 'Nn':
        break
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {listapar}')
print(f'Os números ímpares digitados foram: {listaimpar}')
