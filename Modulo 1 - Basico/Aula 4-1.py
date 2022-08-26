'''
AULA 4 -Cont. IF, ELIF e ELSE + Operadores Relacionais
                                   == Igualdade
                                    > Maior que
                                    >= Maior ou igual a
                                    < Menor
                                    <= Menor ou igual
                                    != Diferente
                                   Operadores Booleanos (TRUE/FALSE)
'''

num_1 = 2  # int
num_2 = '2'  # str

expressao = (num_1 == num_2)

print(expressao)  # Vai dar False, pois é str e int e ele são diferentes

num_1 = 2  # int
num_2 = 2  # str

expressao = (num_1 == num_2)

print(expressao)  # Vai dar True

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar emprestimo

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não pode pegar o emprestimo.')

idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não pode pegar o emprestimo.')