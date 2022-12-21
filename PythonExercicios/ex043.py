p = float(input('Digite Aqui o Seu Peso:'))
a = float(input('Agora Digite a Sua Altura:'))
imc = (p / a ** 2)
if imc < 18.5:
    print('Seu IMC é [ {:.2f} ], Você Está Abaixo do Peso Ideal..'.format(imc))
elif imc <= 25:
    print('Seu IMC é [ {:.2f} ], Você Está no Peso Ideal!'.format(imc))
elif imc > 25:
    print('Seu IMC é [ {:.2f} ] ,Você Está Gordo(a)!'.format(imc))
elif imc > 30:
    print('Seu IMC é [ {:.2f} ], Você Está OBESO que Nojo!'.format(imc))
elif imc > 40:
    print('Seu IMC é [ {:.2f} ], Ataque Cardiaco Fulminante aos 26 Anos..'.format(imc))


