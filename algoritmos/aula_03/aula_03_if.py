valor_prato = float(input('Informe o valor do prato: R$'))
valor_desconto = float(input('Informe o valor do desconto: R$'))
horario_visita = float(input('Qual o horario da sua visita? (hora.minutos)'))

valor_prato_desconto = valor_prato - valor_desconto

if horario_visita > 13.40:
    print(f'O valor do seu prato agora é: R${valor_prato}')
elif horario_visita < 12.00:
    print(f'O valor do seu prato agora é: R${valor_prato}')
else:
    print(f'voê não ganhou o desconto :( o valor do seu prato é: R$ {valor_prato_desconto}')