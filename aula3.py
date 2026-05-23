# exer 1
notas = 4

notas1 = int(input("digite suas notas: "))
notas2 = int(input("digite suas notas: "))
notas3 = int(input("digite suas notas: "))
notas4 = int(input("digite suas notas: "))

soma = notas1 + notas2 + notas3 + notas4

media = soma /notas 

if(media >= 7):
    print("aprovado")
else:
    if(5<= media < 7):
        print("recuperação")
    if(media <5):
        print("reprovado")