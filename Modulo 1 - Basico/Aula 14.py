'''
Operador ternario em Python
'''

logged_user = True

if logged_user:  # Essa frase é igual a if logged_user == True:.
    msg = "Logado!"
else:
    msg = "Precisa logar!"

print(msg)

# Da pra simplificar e encurtar o codigo

logged_user = False
msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'

print(msg)

# Se tiver mais que uma condição deve se usar o ()
# Ex: msg = 'Usuario logado' if (logged_user) else 'Usuario precia logar'

idade = 18

if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode')

idade = input("QUal a sua idade?")

if not idade.isnumeric():
    print("VOce precisa digitar um numero.")
else:
    idade = int(idade)
    idmaior = (idade >= 18)
    msg = 'Pode acessar' if idmaior else 'Não pode'

    print(msg)

print()

#####################################
'''
Expressão condiconal com operador OR
'''

nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Voce não digitou nada =(')

#  Voce pode resumir com a condição OR

nome = input('Qual o seu nome? ')
print(nome or 'Você não digitou nada!')

#  Voce pode usar mais de um or e ele vai parar na primiera afirmação verdadeira

nome = input('Qual o seu nome? ')
print(nome or None or False or 0 or 'Você não digitou nada!')

print()

#####################################

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Gabriel'

variavel = a or b or c or d or e or f or g

print(variavel)
