import math

base: float;
altura: float;
diagonal: float;
area: float;
perimetro: float;

base = float(input("Base do retangulo: "));
altura = float(input("Altura do retangulo: "));

area = base * altura;
perimetro = 2 * (altura + base);
diagonal = math.sqrt(base * base + altura * altura);

print(f"AREA = {area:.4f}");
print(f"PERIMETRO = {perimetro:.4f}");
print(f"DIGAONAL = {diagonal:.4f}");
