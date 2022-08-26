hora = input("Que horas são? ")

if hora.isdigit():
    hora = int(hora)

# EU usei o and, mas o programa me smplificou para essa forma.
# Ex: if hora >= 0 and hora <= 11

    if 0 <= hora <= 11:
        print("Bom Dia!")
    elif 12 <= hora <= 17:
        print('Boa Tarde!')
    elif 18 <= hora <= 23:
        print('Boa Noite!')
    else:
        print('Insira um horario valido entre as 00h e as 23h.')