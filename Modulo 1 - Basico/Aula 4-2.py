'''
AULA 4 - Operadores logicos + IF/ELSEIF/ELSE
           and, or, not
           in e not in
'''
comparacao1 = 1
comparacao2 = 1


#  (Verdadeiro E Verdadeiro) = True
comparacao1 and comparacao2

#  (Verdadeiro OU Verdadeiro) = True
comparacao1 or comparacao2

a = 2
b = 3

# not usado em negação, se b não for maior do que a
if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

# in usado pra sabe se esta contido na vriavel

nome = 'Luiz'

if 'u' in nome:
    print('Existe a letra U no seu nome.')
else:
    print('Não tem.')

# Not in so inverte a situação

nome = 'Luiz'

if 'u' not in nome:
    print('Existe a letra U no seu nome.')
else:
    print('Não tem.')

usuario = input('Nome de usuário: ')
senha = input('Senha do usuario: ')

user = 'kamui7'
password = '123456'

if user == usuario and password == senha:
    print('Você está logado.')
else:
    print('Usuário ou senha invalidos.')