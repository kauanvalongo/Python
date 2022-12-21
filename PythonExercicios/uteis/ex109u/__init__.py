def dobro(n=0, formato=False):
    num = n * 2
    return num if formato is False else moeda(num)


def metade(n=0, formato=False):
    num = n / 2
    return num if formato is False else moeda(num)


def aumentar(n=0, taxa=0, formato=False):
    num = n + (n * taxa/100)
    return num if formato is False else moeda(num)


def diminuir(n=0, taxa=0, formato=False):
    num = n - (n * taxa/100)
    return num if formato is False else moeda(num)


def moeda(n=0, moeda='R$'):
        return f'{moeda}{n:>.2f}'.replace('.', ',')
