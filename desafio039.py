import datetime 

ano_de_nascimento = int(input("Em que ano nocê nasceu? "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_de_nascimento

#Calcular quanto tempo falta para o usuário completar 18 anos
anos_depois = datetime.timedelta(days=365*18)
anos_para_18 = anos_depois + ano_de_nascimento 
diferenca_tempo = anos_para_18 - ano_atual

#Calcular quanto tempo passou desde que o usuário completou 18 anos
falta_tempo = ano_atual - anos_para_18

if idade == 18:
    print("Já está na hora de se alistar ao exército")
elif idade < 18:
    print("Ainda não precisa se alistar", f"Mas faltam {diferenca_tempo} ano(s) para você se alistar")
else:
    print("Já passou o tempo de se alistar", f"você deveria ter se alistado há {falta_tempo} anos")