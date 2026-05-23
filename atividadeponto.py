# exercicio 1
# temp = 0
# frio = 0
# legal = 0
# quente = 0
# for i  in range (0,4):
#     temp = float(input(("digite a temperatura:")))
#     if temp < 18 :
#      frio = temp
#     else:
#         if temp < 30:
#             legal = temp 
#         else:
#             quente = temp
        
# 

# exercio 2
# idade = 0
# while idade != -1:
#     idade = int(input("digite os numeros:"))
#     if (idade != -1):
#         if(idade < 12 ):
#            print("crianca")
#         else:
#             if(idade <= 17):
#                 print("adole")
#             else:
#                 print("adulto")

# exercio 3

senha = int(input("digite a senha: "))

while senha != "UNIFAFIBE":
        if(senha == "UNIFAFIBE"):
                print("entro")
        else:
         print("tenta dinovo")
        senha = int(input("digite a senha"))