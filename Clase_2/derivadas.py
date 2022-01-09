def funcion(a):
    fx = a ** 2 + 3 * a + 1
    return fx


def run():
    a = int(input("Ingresa punto de inicio: "))
    h = float(input("Ingresa la precisión de la derivada: "))
    fx = funcion(a)
    fxh = funcion(a + h)
    derivada = round(((fxh - fx) / h), 2)
    print("El valor de la derivada es: " + str(derivada))



if __name__ == "__main__":
    run()