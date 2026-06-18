P, R = map(int, input().split())

# Seu código vai aqui
if P == 1 and R == 0:
    print ("B")
if P == 0 and R == 0:   
    print("C")
elif P == 1 and R ==1:
    print("A")
else:
    print("C")