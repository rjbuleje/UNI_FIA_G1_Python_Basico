def crear_lista(cantidad_cuerpos, cantidad_parametros, palabra1, palabra2):
    lista=[]
    for i in range(cantidad_cuerpos):
        print("Ingresa los " + palabra2 + " del " + palabra1 + " "+ str(i+1))
        lista1=[]
        for j in range(cantidad_parametros):
            a=float(input("Ingresa el " + palabra2 + " " + str(j+1) + " del " + palabra1 + " "+ str(i+1)+ " : "))
            lista1.append(a)
        lista.append(lista1)   
    return lista


def adimensionar(lista_parametros):
    for i in range(len(lista_parametros)):
        suma=0
        for j in range(len(lista_parametros[0])):
            suma=suma+lista_parametros[i][j]
        for j in range(len(lista_parametros[0])):
            lista_parametros[i][j]=lista_parametros[i][j]/suma
    return lista_parametros
  

def fun_grey_clustering(parametro, cuerpos):
    resultado_final=[]
    niveles_parametro=len(parametro[0])
    parametros_cuerpos=len(cuerpos[0])
    for i in range(len(cuerpos)):
        valores_cuerpos=[]
        for j in range(parametros_cuerpos):
            valores_grey=[]
            for k in range(niveles_parametro):
                valor=cuerpos[i][j]
                if k==0 and valor <= parametro[j][k]:
                    valores_grey.append(1)
                elif k==0 and valor >= parametro[j][k+1]:
                    valores_grey.append(0)
                elif k==(niveles_parametro-1) and valor >= parametro[j][niveles_parametro-1]:
                    valores_grey.append(1)
                elif k==(niveles_parametro-1) and valor <= parametro[j][k-1]:
                    valores_grey.append(0)
                elif k!=0 and k!=(niveles_parametro-1) and ( valor <= parametro[j][k-1] or valor >= parametro[j][k+1] ):
                    valores_grey.append(0)
                elif valor <= parametro[j][k]:
                    valores_grey.append((valor - parametro[j][k-1])/(parametro[j][k] - parametro[j][k-1]))
                elif valor >= parametro[j][k]:
                    valores_grey.append((valor - parametro[j][k+1])/(parametro[j][k] - parametro[j][k+1]))    
            valores_cuerpos.append(valores_grey)
        resultado_final.append(valores_cuerpos)
    return resultado_final
  

def run():
    print(
"""Bienvenidos
Para procesar los datos con la metodología Grey Clustering,
por favor siga las instrucciones""")
    numero_parametros = int(input("Por favor ingresar el número de parámetros: "))
    numero_niveles_parametros = int(input("Por favor ingresar el número de niveles de cada parámetro: "))
    numero_cuerpos = int(input("Por favor ingresar el número de cuerpos de agua a evaluar: "))
    parametros=crear_lista(numero_parametros, numero_niveles_parametros, "parámetro", "nivel")
    cuerpos=crear_lista(numero_cuerpos, numero_parametros, "cuerpo", "parámetro")
    #parametros_adimensionados=adimensionar(parametros)
    evaluacion=fun_grey_clustering(parametros, cuerpos)
    print(evaluacion)
  


if __name__ == "__main__":
    run()