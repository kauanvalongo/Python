primeiro = int(input('Termo:'))
razao = int(input('Razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end='-')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos a mais você quer mostrar?'))
print('Programa Finalizado!')


