print('='*20)
print('BANCO SUPREMO')
print('='*20)
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
valor = int(input('Digite o Valor Que Deseja Sacar: R$'))
print('='*20)
while True:
    if valor - 50 >= 50:
        valor -= 50
        nota50 += 1
    elif valor - 20 >= 20:
        valor -= 20
        nota20 += 1
    elif valor - 10 >= 10:
        valor -= 10
        nota10 += 1
    elif valor - 1 >= 0:
        valor -= 1
        nota1 += 1
    else:
        break
if nota50 != 0:
    print(f'Total de {nota50} de cédulas de R$50')
if nota20 != 0:
    print(f'Total de {nota20} de cédulas de R$20')
if nota10 != 0:
    print(f'Total de {nota10} de cédulas de R$10')
if nota1 != 0:
    print(f'Total de {nota1} de cédulas de R$1')