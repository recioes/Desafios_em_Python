# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER


# Passo 1 - descobrir a data de nascimento do usuário
import datetime as date
ano_de_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = date.datetime.now().year
idade = ano_atual - ano_de_nascimento

# Passo 2 - mostrar a categoria do atleta por idade
if idade <= 5:
    print("Categoria Mirim")
elif idade <= 14:
    print("Categoria Júnior")
elif idade <= 25:
     print("Categoria Sênior")
else:
    print("Categoria Master")