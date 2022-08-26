nome = 'Gabriel Marins'
idade = 29
altura = 1.77
peso = 107.1
ano_atual = 2022
ano_nascimento = ano_atual - idade - 1
imc = peso / altura ** 2

print(nome, "tem", idade, 'anos,', altura, 'de altura e pesa', peso, 'kg.')
print(f'O IMC do {nome} é de {imc:.2f}.')
print('{} nasceu em {}.' .format(nome, ano_nascimento))
