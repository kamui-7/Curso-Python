print(f"Digite dois numeros: ");
x = input()
y = input()

while x and y:
    if not x.isnumeric() or not y.isnumeric():
        print("Digite apenas numeros.")
        break
    elif x > y:
        print(f"DECRESCRENTE.");
    elif y > x:
        print(f"CRESCENTE.");
    else:
        print('ELES SÃO IGUAIS.')

    print(f"Digite outros dois numeros: ");
    x = input();
    y = input();