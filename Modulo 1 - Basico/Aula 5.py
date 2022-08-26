'''
Função len - qwuantidade de caracteres
'''

string1 = input('Digite algo:')
string2 = input('Digite algo:')

print(len(string2 + string1))
print(string2.__len__())

'''
Funções built ins uteis e Documentações
'''

num1 = input('Digite algum numero: ')
num2 = input('Digite outro numero: ')

# Vamos usar o isdigit para saber se o numero pode ou nãos ser convertido em int

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Digite um numero valido.')

'''
Pass e elipse(...)
Usados para completar um codigo inacabado sem que ele retorne erro.
'''

valor = False

if valor:
    ...  # Ou Pass, vai imprimir o else sem dar erro.
else:
    print('Tchau')
