print('Calculo de IMC')

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