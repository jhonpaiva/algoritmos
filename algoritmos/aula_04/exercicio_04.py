while True: 
    numero = int(input('Valor: '))

    cem = int(numero / 100)
    numero = numero -(cem*100) 

    cinquenta = int(numero/50)
    numero = numero % 50

    dez = int(numero/10)
    numero = numero % 10

    cinco = int(numero/5)
    numero = numero % 5

    um = numero

    print('Notas R$100,00 = ',cem)
    print('Notas R$ 50,00 = ',cinquenta)
    print('Notas R$ 10,00 = ',dez)
    print('Notas R$  5,00 = ',cinco)
    print('Notas R$  1,00 = ',um)

    continuar = input('Deseja continuar? S/N ').upper().strip()
    if continuar == 'N':
        break