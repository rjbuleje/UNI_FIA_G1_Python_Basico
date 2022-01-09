def run():
    CONSTANTE = 1000

    print("""
    Escribe un programa que me imprima todas las potencias de 2 menor a 1000""")
    for contador in range (1000):
        a = 2 ** contador
        #print(a)
        if a > 1000:
            break
        print(a)

        
    print("""
    Escribe todos los números pare entre 0 y 1000, utilizando la siguiente estructura incial for i in range(1001)""")
    
    for i in range(1001):
        if i % 2 != 0:
            continue
        print(i)



if __name__ == "__main__":
    run()