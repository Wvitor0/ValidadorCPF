novocpf1 = ''
calculos = []
digits = []

while True:
    cpfuser = input('Digite seu CPF: ')
    novocpf1 += cpfuser
    novocpf1 = novocpf1[:9]
    if not cpfuser.isnumeric():
        print('Digite apenas números!')
        novocpf1 = ''
        continue
    if len(cpfuser) > 11:
        print('Digite apenas 11 números.')
        novocpf1 = ''
        continue
    elif len(cpfuser) < 11:
        print('Digite pelo menos 11 números.')
        novocpf1 = ''
        continue

    contador = 10

    for r in novocpf1:
        r = int(r)
        x = r * contador

        contador -= 1
        calculos.append(x)

    contador1 = 0
    for number in calculos:
        contador1 += number

    formula = 11 - (contador1 % 11)

    if formula <= 9:
        novocpf1 += str(formula)
    else:
        novocpf1 += str(0)

    contador2 = 11
    for y in novocpf1:
        y = int(y)
        z = y * contador2

        contador2 -= 1
        digits.append(z)

    contador3 = 0
    for value in digits:
        contador3 += value

    formula2 = 11 - (contador3 % 11)

    if formula2 <= 9:
        novocpf1 += str(formula2)
    else:
        novocpf1 += str(0)

    if novocpf1 == cpfuser:
        print(f'O CPF {novocpf1} é válido!')
        break
    else:
        print(f'O CPF {novocpf1} é inválido!, tente novamente.')
        novocpf1 = ''
        calculos.clear()
        digits.clear()
        continue
