frase = str(input('Digite Uma Frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A Frase {junto} Ao Contrário Fica: {inverso} \n É um Palíndromo!')
else:print(f'A frase {junto} Ao Contrário Fica: {inverso} \n Não é um Palíndromo!')

