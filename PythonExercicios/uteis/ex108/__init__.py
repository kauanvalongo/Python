def dobro(n=0):
    num = n * 2
    return num


def metade(n=0):
    num = n / 2
    return num


def aumentar(n=0, taxa=0):
    num = n + (n * taxa/100)
    return num


def diminuir(n=0, taxa=0):
    num = n - (n * taxa/100)
    return num


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')