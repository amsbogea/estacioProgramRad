de_novo = 's'

while (de_novo == 's'):

    peso = input('Digite seu peso: ')
    altura = input('Digite sua altura: ')
    imc = float(peso) / (float(altura) * float(altura))

    if imc <= 17:
        print('Muito abaixo do peso')
    elif imc > 17 and imc <=18.5:
        print('Abaixo do peso')
    elif imc > 18.5 and imc <= 25:
        print('Peso normal')
    elif imc > 25 and imc <= 30:
        print('Acima do peso')
    elif imc > 30 and imc <= 35:
        print('Obesidade I')
    elif imc > 35 and imc <= 40:
        print('Obesidade II(Severa)')
    elif imc > 40:
        print('Obesidade III(Mórbida')
    else:
        print('Inválido')

    de_novo = input('Deseja continuar (s/n)? ')