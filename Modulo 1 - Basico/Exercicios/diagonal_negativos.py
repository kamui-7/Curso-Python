N = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
 for j in range(0, N):
     mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")

for i in range(N):
	print(f"{mat[i][i]} ", end="")

count = 0
for i in range(N):
	for j in range(N):
		if mat[i][j] < 0:
			count = count + 1

print(f"\nQUANTIDADE DE NEGATIVOS = {count}")


