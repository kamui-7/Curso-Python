a: int; b: int; c: int; menor: int;

a = int(input("Primeiro Valor: "));
b = int(input("Segundo Valor: "));
c = int(input("Terceiro Valor: "));

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print(f"MENOR = {menor}");