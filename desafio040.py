# criar um programa que leia duas notas e calcule a média
# tem que mostrar uma mensagem no final de acordo com a média atingida: 
# abaixo de 5 reprovado, entre 5 e 6.9 recuperação e 7 ou superior aprovado

print("Calculadora de nota")
# função para validar a nota
def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("Insira uma nota válida de 0 a 10: ")
        nota = float(input())
    return nota

# input das notas
lista_atividade = []
for i in range (1,3):
    print("informe uma nota de 0 a 10: ")
    nota = float(input(f"Qual a nota da atividade {i}? "))
    lista_atividade.append(nota)
    validar_nota(nota)

# Cálculo de nota
nota_final = sum(lista_atividade) / 2
if nota_final < 5:
    print("Reprovado")
elif nota_final <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")


