num = input('Digite um numero inteiro: ')

if not num.isdigit():
    print('Desculpe o numero não é inteiro.')
else:
    num = int(num)

    if num == 0:
        print('ZERO é NEUTRO')
    elif num % 2 == 0:
        print('Este numero é PAR')
    else:
        print("Este numero é IMPAR")