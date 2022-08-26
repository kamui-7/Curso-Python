def saudacao(msg, nome):
    print(msg, nome)

saudacao('Ola', 'Gabriel')
saudacao('Hello', "Guilherme")

print()

#######################################

def soma(n1,n2,n3):
    print(n1 + n2 + n3)

soma(1,2,3)
soma(3,4,6)

print()

#########################################

def soma(n1,n2):
    return n1 + (n2 * n1 /100)

print(soma(100,10))
print(soma(50,10))

print()

#########################################

def parametro(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'fizzbuzz'
    elif n1 % 3 == 0:
        return 'fizz'
    elif n1 % 5 == 0:
        return 'buzz'
    else:
        return n1

print(parametro(15))
print(parametro(20))
print(parametro(6))
print(parametro(1))