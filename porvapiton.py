# salario = int(input("digite o salario: "))
# tempo = int(input("digite seu tempo na empresa: "))
# salariobonus = 0
# tempobonus = 0
# valortotal = 0
# if salario <= 2000:
#     salariobonus = salario * 0.20
# elif salario > 2001 and salario < 5000:
#     salariobonus = salario * 0.12
# if tempo > 10:
#     tempobonus = 1500
# elif tempo >5 and tempo<= 10:
#    tempobonus = 800
# valortotal = salario + salariobonus + tempobonus

# print(salariobonus)
# print(tempobonus)
# print(valortotal)

# exer002
# quantidade = int(input("sãos quantos alunos?: ")) 
# nomemaior = ""
# treinomaior = 0
# totalacumulado = 0
# contamaior = 0
# for i in range(quantidade):
#     nome = input("nome aluno: ")
#     treino = int(input("minutos: "))
#     if treino > treinomaior:
#         nomemaior = nome
#         treinomaior = treino
#     totalacumulado = totalacumulado + treino
#     if treino > 60:
#         contamaior = contamaior +1
# mediaminuto = totalacumulado/quantidade

# print(totalacumulado)
# print(nomemaior, "=", treinomaior)
# print(contamaior)
# print(mediaminuto)


# exer003
pergunta = "sim"
totalgasolina = 0
totaletanol = 0
totaldiesel = 0
gasmaior = ""
combustivelmaior = 0
pergunta = ""
while  pergunta != "nao":  
    litros = int(input("quantos litro"))
    tipo = int(input("Tipo do combustivel 1-gasolina, 2-etanol, 3-diesel: "))
    if tipo == 1:
        totalgasolina = totalgasolina + litros 
    elif tipo == 2:
        totaletanol = totaletanol + litros 
    elif tipo == 3:
        totaldiesel = totaldiesel + litros 
    pergunta = input("Quer continuar?")
   
if totalgasolina > combustivelmaior:
      gasmaior = "gasolina"
elif totaletanol > combustivelmaior:
        gasmaior = "etanol"
elif totaldiesel > combustivelmaior:
        gasmaior = "diesel"
print(gasmaior)
print(totalgasolina)
print(totaletanol)
print(totaldiesel)