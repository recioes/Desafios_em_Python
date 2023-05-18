# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

# calcular o IMC
altura_entrada = float(input("Qual é sua altura em metros? "))
peso = float(input("Quanto você pesa em KG? "))
# condição para aceitar a altura em metros e em cm
if altura_entrada >= 100:
    altura = float(altura_entrada) / 100
else:
    altura = float(altura_entrada)

# Cálculo final
IMC = peso / (altura * altura)
print(f"Seu IMC é {IMC:.2f}")
if IMC < 18:
    print("Você está abaixo do peso")
elif IMC < 25:
    print("Você está com o peso ideal")
elif IMC < 30:
    print("Você está com sobrepeso")
elif IMC < 40:
     print("Você está com obesidade")
else:
     print("Você está com obesidade mórbida")