def funcion(a):
    fx = a ** a - 100 + a ** 2
    return fx


def derivada(a):
    h = 0.0000001
    fx = funcion(a)
    fxh = funcion(a + h)
    derivada = (fxh - fx) / h
    return derivada


def newton_raphson(a, error):
    aproximacion = a
    while abs(funcion(aproximacion)) - 0 > error:
        aproximacion = aproximacion - funcion(aproximacion) / derivada(aproximacion)
    return aproximacion


def run():
    a = int(input("Ingresa punto de inicio: "))
    error = 0.000000000001
    respuesta = newton_raphson(a, error)
    print(round(respuesta, 9))
    


if __name__ == "__main__":
    run()