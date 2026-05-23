#Exercicio 1
# cont = 0
# for i in range(1,11):
#     valor = int(input("Digite o valor:"))
#     if(valor % 2 == 0):
#         print("par")
#         cont += 1
#     else:
#         print("impar")
# print("Existe",cont,"numeros pares")

# Exercicio 2
# nota = 0
# soma = 0 
# qtd = 0
# while nota != -1:
#     nota = int(input("digite uma nota: "))
#     if 0<= nota <= 10:
#         qtd = qtd + 1
#         soma = soma + nota 
# media = soma / qtd
# print(media)

# exercicio 3
# numero = int(input("digite os numeros: "))
# menor = numero
# maior = numero
# while numero != 0:
#     numero = int(input("digite os numeros: "))
#     if (numero != 0):
#         if(numero > maior):
#             maior = numero
#         if(numero < menor):
#           menor = numero
        
# print(maior, "e", menor)

# Exercicio 4
resposta = None
numero = int(input("digite o numero: ")) 
while resposta != "nao":
    for i in range (1,11):
     tabuada = int(numero * i)
     print(numero,"x", i, "=", tabuada )
    resposta = input("quer outro numero?:")
    if(resposta == "sim"):
        numero = int(input("digite o numero: ")) 
   

# Exercicio 5




     
     