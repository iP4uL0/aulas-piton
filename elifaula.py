nota1 = int(input("digite sua nota: "))
nota2 = int(input("digite sua nota: "))

media = (nota1 + nota2)/2

if media >= 7:
    print("passou")
elif media <3:
    print("Reprovado")
else:
    print("recuperação")