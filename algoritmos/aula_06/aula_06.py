print('atv_01')

nota_01 = float(input('Insira a primeira nota do aluno: '))
nota_02 = float(input('Insira a segunda nota do aluno: '))
nota_03 = float(input('Insira a terceira nota do aluno: '))

soma_final = (nota_01 + nota_02 + nota_03) / 3

if soma_final >= 7:
    print(soma_final)
    print('Aluno aprovado!')
else:
    print(soma_final)
    print('Aluno reprovado!')


print('atv_02')

while True:

    idade = int(input('Qual a sua idade?'))

    if idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade')

print('atv_03')

numero = int(input('Insira o número que deseja saber se é par ou ímpar:'))

if numero % 2 == 0:
    print('Número é par')
else:
    print('O número é impar')
    
    
print('atv_04')

valor_produto = float(input('Qual o valor do produto: '))

if valor_produto <= 50:
    valor_produto = valor_produto - (valor_produto * 0.1)
    print(f'O valor do produto com um desconto de 10% é: R${valor_produto}')
else:
    valor_produto = valor_produto - (valor_produto * 0.15)
    print(f'O valor do produto com um desconto de 15% é: R${valor_produto}')
    
    
print('atv_05')

numero = float(input('Insira o número que deseja saber se é positivo ou negativo:'))

if numero > 0:
    print(f'O número {numero} é positivo!')
elif numero < 0:
    print(f'O número {numero} é negativo')
else:
    print(f'O número é {numero}')


print('atv_06')

idade = int(input('Qual a sua idade?'))

if idade >= 16:
    print('Você pode votar!')
else:
    print('Você não pode votar!')
    
print('atv_07')

print('atv_08')

renda = float(input('Insira seu salário: '))

if renda <= 1000:
    print('Você está isento de impostos!')
elif renda > 1000 and renda < 2000:
    imposto = renda * 0.1
    print(f'O seu imposto de renda é: {imposto}')
else:
    imposto = renda * 0.2
    print(f'O seu imposto de renda é: {imposto:.2f}')


print('atv_09')

while True:

    ano = int(input('Insira o ano que você deseja saber: '))

    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto!')


print('atv_10')

letra = str(input('Digite uma letra: '))

if letra == 'a' or'e' or 'i' or 'o' or 'u':
    print(f'A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} não é uma vogal!')
