def matriz_vacia( filas, columnas):
    matriz_vacia = []
    for i in range(filas):
        matriz_vacia.append([0]*columnas)   
    print(matriz_vacia)


def suma_matrices( matriz1, matriz2):
    num_filas_1 = len(matriz1)
    num_columnas_1 = len(matriz1[0])
    num_filas_2 = len(matriz2)
    num_columnas_2 = len(matriz2[0])
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if num_filas_1 == num_filas_2 and num_columnas_1 == num_columnas_2:
        for i in range(num_filas_2):
            for j in range(num_columnas_1):
                matriz[i][j] = matriz1[i][j] + matriz2[i][j]
        return matriz
    else:
        print("Revisa tus matrices")


def multiplicacion_matrices(matriz_1, matriz_2):
    filas = len(matriz_1)
    columnas = len(matriz_2[0])
    recorrido = len(matriz_2)
    matriz_vacia = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #automatizar la creación de esta matriz vacia
    if  len(matriz_1[0]) == len(matriz_2):
        for i in range(filas):
            for j in range(columnas):
                for k in range(recorrido):
                    matriz_vacia[i][j] = matriz_vacia[i][j] + matriz_1[i][k] * matriz_2[k][j]
        return matriz_vacia
    else:
        print("Revisa tus matrices")
    

def determinante_3x3(matriz):
    numero_filas = len(matriz)
    numero_columnas = len(matriz)
    detp = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[1][0]*matriz[2][1]*matriz[0][2] 
    detn = matriz[2][0]*matriz[1][1]*matriz[0][2] + matriz[2][1]*matriz[1][0]*matriz[0][0] + matriz[1][0]*matriz[0][1]*matriz[2][2]
    return (detp - detn)


def matriz_transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_respuesta = matriz_vacia( filas, columanas)
    for i in range(filas):
        for j in range(columnas):
            matriz_respuesta[i][j] = matriz[j][i]
    return matriz_respuesta

def matriz_x_escalar(matriz, escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_respuesta = matriz_vacia( filas, columanas)
    for i in range(filas):
        for j in range(columnas):
            matriz_respuesta[i][j] = matriz[i][j] * escalar
    return matriz_respuesta

def matriz_adjunta_3x3(matriz):
    pass

def resolver_sistema_ecuaciones_3x3(matriz_cuadrada, matriz_columna):
    pass

def run():
    matriz_indentidad_3x3 = [[1 , 0, 0], [0, 1, 0], [0, 0, 1]]
    """ for i in range(len(matriz_indentidad_3x3)):
        for j in range(len(matriz_indentidad_3x3[0])):
            print(matriz_indentidad_3x3[i][j]) """


    matriz_3x3 = [[1, 1, 1], [0, 5, 1], [0, 0, 4]]  

    suma = suma_matrices(matriz_indentidad_3x3, matriz_3x3)
        
    multiplicacion = determinante_3x3(matriz_3x3)
    print(multiplicacion)


if __name__ == "__main__":
    run()