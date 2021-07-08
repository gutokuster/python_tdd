from calculadora import soma

'''
try:
    print(soma('4', 5))
except TypeError as e:
    print('Conta Inválida:', e)

'''

try:
    print(soma('4', '4'))
except AssertionError as e:
    print(f'Conta inválida:', e)
