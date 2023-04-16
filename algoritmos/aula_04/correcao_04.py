valor = int(input('Digite um valor: '))

cem = valor//100
# print(cem)
resto = valor % 100
print(resto)

cinquenta = resto//50
# print(cinquenta)
resto = valor % 50
print(resto)

vinte = resto//20
# print(vinte)
resto = valor % 20
print(resto)

dez = resto//10
# print(dez)
resto = valor % 10
print(resto)

cinco = resto//5
# print(cinco)
resto = valor % 5
print(resto)

dois = resto//2
# print(dois)
resto = valor % 2
print(resto)

um = valor

print('notas de 100', cem)
print('notas de 50', cinquenta)
print('notas de 20', vinte)
print('notas de 10', dez)
print('notas de 5', cinco)
print('notas de 2', dois)
print('moedas de 1', um)