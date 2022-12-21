quant = soma = 0
while True:
    num = int(input('Digite um Valor: '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'Foram Digitados {quant} números e a soma entre eles é: {soma}')
