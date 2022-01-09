import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(input("Ingresa un número: "))
    n = 1

    while numero_aleatorio != numero_usuario:
        if numero_aleatorio < numero_usuario:
            print("Es menor")
        if numero_aleatorio > numero_usuario:
            print("Es mayor")
        numero_usuario = int(input("Escoge un nuevo número: "))
        n = n + 1 
    

    print("Ganaste con " + str(n) + " intentos")
    


if __name__ == "__main__":
    run()