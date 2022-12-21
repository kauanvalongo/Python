def dobro(n=0, formato=True):
    num = n * 2
    return num if formato is False else moeda(num)


def metade(n=0, formato=True):
    num = n / 2
    return num if formato is False else moeda(num)


def aumentar(n=0, taxa=0, formato=True):
    num = n + (n * taxa/100)
    return num if formato is False else moeda(num)


def diminuir(n=0, taxa=0, formato=True):
    num = n - (n * taxa/100)
    return num if formato is False else moeda(num)


def moeda(n=0, moeda='R$'):
        return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n, a, d):
    print('-'*30)
    print(f'{"       RESUMO DO VALOR"}')
    print('-' * 30)
    print(f'Preço Analisado:    {moeda(n)}')
    print(f'Dobro do Preço:     {dobro(n)}')
    print(f'Metade Do Preço:    {metade(n)}')
    print(f'{a}% De Aumento:     {aumentar(n,a)}')
    print(f'{d}% De Redução:     {diminuir(n,d)}')
    print('-' * 30)
