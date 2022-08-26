def func():
    return('Ola')

def func2(arg):
    return arg()

executando = func2(func)
print(executando)

print()

##################################################

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def funcao1(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(funcao1, 'Gabriel')
executando2 = mestre(saudacao, 'Gabriel', saudacao='Bom Dia!')
print(executando)
print(executando2)