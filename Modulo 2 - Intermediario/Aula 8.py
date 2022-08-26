
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'resposta': {'a': '1', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'd',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2x6?',
        'resposta': {'a': '3', 'b': '12', 'c': '13', 'd': '2'},
        'resposta_certa': 'b',
    }
}
print()

respostas_certas = 0
for chave_p, chave_r in perguntas.items():
    print(f'{chave_p}: {chave_r["pergunta"]}')

    print('Respostas: ')
    for resposta_p, resposta_r in chave_r['resposta'].items():
        print(f'[{resposta_p}]: {resposta_r}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == chave_r['resposta_certa']:
        print('Resposta correta.')
        respostas_certas += 1
    else:
        print('Resposta incorreta.')

    print()

qtd_perg = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perg * 100

print(f'Voce acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')