def matriz_vacia( x, y):
    a = []
    for i in range(x):
        a.append([])
        for j in range(y):
            a[i].append(0)
    return a
   
def multiplicacion_matrices( a, b):
    filas = len(a)
    columas = len(b[0])
    recorrido = len(a[0])
    c = matriz_vacia( filas, columas)
    for i in range(filas):
        for j in range(columas):
            for k in range(recorrido):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c



def run():
    matriz_a = [[1, 2], [3, 4], [5, 6]]
    matriz_b = [[1, 2, 3], [4, 5, 6]]
    matriz_c = multiplicacion_matrices(matriz_a, matriz_b)
    #matriz_c = matriz_vacia( 2, 4) 
    print(matriz_c)



if __name__ == "__main__":
    run()