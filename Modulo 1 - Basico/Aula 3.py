'''
Condições IF, ELIF e ELSE - AULA 3

IF (SE)
ELIF (SENÃO SE)
ELSE (SENÃO)

'''

if False:
    print("Verdadeiro")
else:
    print("Não é verdadeira.")

# Imprime a segunda, já que o if não é false.

if True:
    print("Verdadeiro")
else:
    print("Não é verdadeira.")

# Imprime a primeira, já que o if é true.

if False:
    print("Verdadeiro")
elif True:
    print("Agora é verdadeiro.")

# Imprime o que é true, usando o elif.

if False:
    print("Verdadeiro")
elif False:
    print("Agora é verdadeiro.")
elif True:
    print("Mais uma verdadeira.")
else:
    print("Não é verdadeiro.")

# Imprime a primeira que for true

if False:
    print("Verdadeiro")
elif False:
    print("Agora é verdadeiro.")
elif False:
    print("Mais uma verdadeira.")
else:
    print("Não é verdadeiro.")

# Imprime o else se for todas false