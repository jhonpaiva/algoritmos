import random

numero_correto = random.randint(1, 100)
tentativas_restantes = 10

print('Tente advinhar o número escolhido pelo programa(entre 1 e 100):')


while tentativas_restantes > 0:
    try:
        palpite = int(input('Digite o seu palpite!'))
    except ValueError:
        print('Digite apenas números!')
        continue
    if palpite == numero_correto:
        print('Parabéns, você acertou!')
        break
    elif palpite < numero_correto:
        print('Seu palpite é menor do que o número correto.')
    else:
        print('Seu palpite é maior do que o número correto.')
    tentativas_restantes -= 1
    
if tentativas_restantes == 0:
    print(f'Suas tentaivas acabaram. O número correto era {numero_correto}.')

