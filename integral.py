def funcion(x):
    x = 2 * (x ** 2) + 4 * (x ** 3) + x ** (1/2)
    return x


def integral( a, b, n):
    algo = 0
    suma = 0
    while algo < n:
        d = (b - a) / n 
        area = d * funcion(a + d * algo)
        suma = suma + area
        algo = algo + 1
    return suma


def run():
    n = int(input("Ingresa el número de particiones: "))
    a = float(input("Ingresa el punto de inicio: "))
    b = float(input("Ingresa el punto final: "))
    integral_problema = integral(a, b, n)
    print(integral_problema)



if __name__ == "__main__":
    run()