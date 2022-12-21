d = int(input('Qual a distância em KM que você percorrerá nesta viajem?'))
p = 0.50 * d
p2 = 0.45 * d
if d <= 200:
        print('Sua passagem custará R${}.'.format(p))
else:
    print('Sua passagem custará R${}.'.format(p2))
