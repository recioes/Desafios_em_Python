# Elaborar um programa que calcule o valor a ser pago, considerando e preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

store_name = "ESTHER'S STORE"
print(f"{store_name:=^40}")
preco_produto = float(input("Preço das compras: "))
condicoes = ["1. À vista no dinheiro/cheque", 
             "2. à vista no cartão", 
             "3.em até 2x no cartão", 
             "4. 3x ou mais no cartão"]

# Condicões de pagamento
print("FORMAS DE PAGAMENTO:")
for opcao in condicoes:
    print(opcao)

# Mensagem de erro para caso o input não seja uma das opções em número
while True:
    try:
        escolha_condicao = int(input("Escolha uma forma de pagamento (digite um número de 1 a 4): "))
        if escolha_condicao < 1 or escolha_condicao > 4:
            print("Escolha uma opção válida")
        else:
            break  
    except ValueError:
        print("Escolha uma opção válida")

# Preço final
if escolha_condicao == 1:
   preco_final = preco_produto - (preco_produto * 0.1)
elif escolha_condicao == 2:
    preco_final = preco_produto - (preco_produto * 0.05)
elif escolha_condicao == 3:
    preco_final = preco_produto 
else:
   preco_final = preco_produto + (preco_produto * 0.2)
   
print(f"O valor final de sua compra ficou em {preco_final:.2f}")


