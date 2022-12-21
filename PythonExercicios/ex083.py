exp = str(input('Digite uma Expressão: '))
lista = []
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A Expressão é válida!')
else:
    print('A expressão não é válida!')
