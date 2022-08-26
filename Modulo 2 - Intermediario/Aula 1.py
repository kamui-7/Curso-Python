'''
Fuções - def em Python (Parte 1)
'''

def funcao():
    print('Ola Mundo!')  # Evita a repetiçao de 4 prints, exemplificando para uma funação

funcao()
funcao()
funcao()
funcao()

print()

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Ola', 'Gabriel')
saudacao('Hi', 'Gabriel')
saudacao('Hola', 'Gabriel')
saudacao('Alola', 'Gabriel')

print()

def saudacao(msg='Ola', nome='usuario'):
    print(msg, nome)

saudacao()
saudacao(nome='Menino', msg='Hi')  # sempre vai seguir a ordem, para ficar fora de ordem so seguir esse exemplo.
saudacao('Ola', 'Gabriel')
saudacao('Hi', 'Gabriel')
saudacao('Hola', 'Gabriel')
saudacao('Alola', 'Gabriel')

