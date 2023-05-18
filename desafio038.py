print("Comparação numérica")
a = int(input("Escolha um número inteiro: "))
b = int(input("Escolha mais um número inteiro: "))

if a > b:
    print(f"{a} é maior que {b}")
elif b > a:
    print(f"{b} é maior que {a}")
else:
    print("Os dois são iguais, não existe valor maior")

