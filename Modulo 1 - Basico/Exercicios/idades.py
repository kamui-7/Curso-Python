nome1: str; nome2: str;
idade1: int; idade2: int;
media: float;

print(f"Dados da 1ª Pessoa: ");
nome1 = input("Nome da Primeira Pessoa: ");
idade1 = int(input("Idade da Primeira Pessoa: "));

print(f"Dados da 2ª Pessoa: ");
nome2 = input("Nome da Segunda Pessoa: ");
idade2 = int(input("Idade da Segunda Pessoa: "));

media = (idade1 + idade2) / 2;
print(f"A idade media de {nome1} e de {nome2} e de {media:.1f} anos.")