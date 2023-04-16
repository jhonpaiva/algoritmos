print ('questão 01')

num = float(input('Insira o número que deseja consultar: '))

if num > 0:
    print (f'O número {num} é positivo!')
elif num < 0:
    print (f'O número {num} é negativo!')
else:
    print (f'O número é {num} igual a zero')



print('questão 02')

letra = str(input('Insira a letra que desseja consultar: '))

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} é uma consoante!')



