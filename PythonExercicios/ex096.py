def total(a, b):
    s = a * b
    print(f'O Tamanho Total do Terreno é de {s}m2 ')


def frase(fr):
    print('='*30)
    print(fr)
    print('='*30)


frase('Controle de Terrenos')

total(float(input('LARGURA: ')), float(input('COMPRIMENTO: ')))

