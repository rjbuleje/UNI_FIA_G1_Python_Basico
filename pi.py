def run():
    suma = 0
    numero_terminos = 50000000
    for i in range(numero_terminos):
        i = i+1
        a = (i ** 2)
        suma = suma + a
    suma = 6 * suma
    suma = suma ** ( 1 / 2 )
    print(suma)



if __name__ == "__main__":
    run()