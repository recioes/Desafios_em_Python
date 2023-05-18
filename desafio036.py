

print("Simulação de empréstimo bancário")
valor_da_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é seu salário? "))
anos = int(input("Em quantos anos pretende pagar a casa? "))
prestacao_mensal = valor_da_casa / (anos * 12)

if prestacao_mensal >= 0.3 * salario:
    print("Infelizmente, o empréstimo não poderá ser concedido")
else:
    print(f"Empréstimo concedido! O valor de sua prestação será de {prestacao_mensal:.2f}")