print ('atv_01')

resistencia = float(input('Informe a resistência elétrica do circuito: '))
tensao = float(input('Agora informe qual a tensão elétrica do circuito: '))

corrente_eletrica = resistencia / tensao

print(f'A sua corrente elétrica é:{corrente_eletrica}v')


print ('atv_02')


idade = int(input('Qual a sua idade?'))

if idade >= 18:
    print('Você pode dirigir!')
else:
    print('Você não pode dirigir!')


print ('atv_03')


numero = float(input('Insira um número: '))

if (numero % 2) == 0:
    print('O número é par!')
else:
    print('O número é impar!')
    

print ('atv_04')

altura_inicial = float(input('Defina a altura inicial do objeto: '))
aceleracao_gravidade = 9.81
velocidade_lancamento = float(input('Informe a velocidade de lançamento: '))
t = float(input('Insira o tempo: '))

altura_maxima = (velocidade_lancamento**2)*t - (aceleracao_gravidade**2)*t

print(f'a altura máxima é de: {altura_maxima}m')

# Vy = V0y T - gt
# vy = gt

altura_final = aceleracao_gravidade

print (f'a altura final é de: {altura_final}m')


print ('atv_05')

velocidade_inicial = float(input('Defina a velocidade inicial do objeto: '))
aceleracao = float(input('Defina a aceleração do objeto: '))
tempo_deslocamento = float(input('Defina o tempo de deslocamento do objeto: '))

velocidade_final = velocidade_inicial + (aceleracao*tempo_deslocamento)

print(f'A velocidade final do objeto é de: {velocidade_final} m/s')

distancia_percorrida = (velocidade_inicial*tempo_deslocamento) + ((aceleracao*((tempo_deslocamento**2))/2))

print(f'A distância percorrida pelo objeto é de: {distancia_percorrida} m/s')


print ('atv_06')

lado_a = float(input('insira a medida do primeiro lado do triângulo: '))
lado_b = float(input('insira a medida do segundo lado do triângulo: '))
lado_c = float(input('insira a medida do terceiro lado do triângulo: '))

if lado_a == lado_b and lado_b == lado_c:
    print ('O triângulo é um Equilatero!')
elif lado_a == lado_b and lado_a != lado_c:
    print ('O triângulo é um Isóceles!')
elif lado_a == lado_c and lado_a != lado_b:
    print ('O triângulo é um Isóceles!')
elif (lado_b == lado_c != lado_a):
    print ('O triângulo é um Isóceles!')
else:
    print ('O triângulo é um escaleno')


print ('atv_07')

nome = input('Qual seu nome?')
peso = float(input('Insira seu peso:'))
altura = float(input('Insira sua altura em metros:'))

imc = peso / (altura**2)

if imc < 18.5 and imc > 0:
    print(f'{nome}, Você está abaixo do peso normal!')
elif imc > 18.5 and imc <= 24.9:
    print(f'{nome}, o seu peso é normal!')
elif imc > 24.9 and imc <= 34.9:
    print(f'{nome}, Você está em um grau de obesidade I!')
elif imc > 35 and imc <= 39.9:
    print(f'{nome}, Você está em um grau de obesidade II!')
elif imc >= 40:
    print(f'{nome}, Você está em um grau de obesidade III!')
else:
    print(f'{nome}, não consegui receber bem os dados, confira os valores e vamos começar do 0!')


print ('atv_08')


print('Conversor de °C em °F')

temp_celsius = float(input('Qual a temperatura em Celsius?'))

conversao = temp_celsius * 1.8 + 32

print('A temperatura de',temp_celsius, '°C convertida é:',conversao, '°F')


print ('atv_09')

diametro = float(input('informe o diâmetro da esfera que deseja calcular o volume: '))

pi = 3.14

raio = diametro / 2

volume = (4*pi*raio**3)/3

print (volume)


print ('atv_09')

lista = []

n = int(input("Qual a quantidade de itens que você deseja adicionar a lista?"))

for i in range(n):
    item = int(input('Digite o valor do item {}: '.format(i+1)))
    lista.append(item)
    
soma_itens = sum(lista)
quantidade_itens = len(lista)

media_aritmetica = soma_itens / quantidade_itens

print(f'A média aritmética da sua lista é: {media_aritmetica}')










