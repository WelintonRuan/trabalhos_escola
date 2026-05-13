#### criar tabuada de um número inteiro

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
        
numero = int(input("Digite um número inteiro para ver a tabuada: "))
tabuada(numero)
        