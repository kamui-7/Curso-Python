"""
Entrada de Dados
"""

nome = input("Escreva seu nome aqui: ")
idade = input("Escreva a sua idade aqui: ")
print(f'O usuario digitou {nome} e o tipo da variavel é ' f'{type(nome)}')
print(f'O usuario digitou {idade} e o tipo da variavel é ' f'{type(idade)}')

# Vemos que a idade é str e não int, então temos que fazer unm casting pois não é possivel fazer operações entre str e int

nome = input("Escreva seu nome aqui: ")
idade = int(input("Escreva a sua idade aqui: "))
print(f'O usuario digitou {nome} e o tipo da variavel é ' f'{type(nome)}')
print(f'O usuario digitou {idade} e o tipo da variavel é ' f'{type(idade)}')

# Agora a idade é int, outro exemplo de se fazer casting é:

numero_1 = int(input("Digite um numero: "))
numero_2 = input("Digite outro numero: ")
numero_2 = int(numero_2)

print(numero_1 ** numero_2)