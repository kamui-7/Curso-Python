'''
Função while em Python - Aula 7
Utilizado para realizar ações enquanto uma condição
for verdadeira.

'''

x = 0
while x < 11:
    print(x)
    x = x + 1

print('Acabou')

#  Exemplo da função continue, ela faz com que a linha seguinte não seja mais executada.

x = 0
while x < 10:
    if x == 3:
        x = x + 1  # Temos que repetir  função que tinha abaixo pois apos o continue
        continue   # ela não sera mais executada, e vai pular o numero 3 da lista.

    print(x)
    x = x + 1

print('Acabou')

#  Similar ao continue temos a break, ele finaliza a execução e pula para o final.

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print('Acabou')

print()

x = 0 # coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1  # y = y + 1

    x += 1  # x = x + 1

print('Acabou!!')

print()

while True:
    print()
    num1 = input('Digite um numero: ')
    operador = input('Digite o operador: ')
    num2 = input('Digite outro numero: ')
    sair = input('Deseja sair? [s]im ou [n]ão? ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Impossivel de calcular.')

    if sair == 's':
        break
