times = '0', 'b1', 'c2', 'd3', 'e4', 'f5', '6', '7', '8', '9', 'chapecoense', 'a11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
a = ''
b = ''
e = ''
d = ''
print(f'primeiros 5 colocados :')
for c in times[0:5]:
    print(f'{c}',end='-')
print(f'\nÚltimos 4 colocados :')
for y in times[17: 21]:
    print(f'{y}',end='-')
e = (sorted(times))
d = (times.index( 'chapecoense' ))
print(f'\nOrdem Alfabética : {e}')
print(f'Chapecoense está na posição: {d}')