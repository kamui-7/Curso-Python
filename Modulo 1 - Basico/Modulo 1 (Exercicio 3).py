nome1 = input('Qual o seu nome? ')
letras = len(nome1)

if letras <= 4:
    print("Seu nome é curto!")
elif letras == 5 or letras == 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é grande!")
