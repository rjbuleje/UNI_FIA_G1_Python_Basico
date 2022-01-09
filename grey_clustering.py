def fun_grey_clustering(parametro, valor):
    resultado=[]
    for i in range(len(parametro)):
        if i==0 and valor <= parametro[i]:
            resultado.append(1.00)
        elif i==0 and valor >= parametro[i+1]:
            resultado.append(0)
        elif i==(len(parametro)-1) and valor>=parametro[len(parametro)-1]:
            resultado.append(1)
        elif i==(len(parametro)-1) and valor<=parametro[i-1]:
            resultado.append(0)
        elif i!=0 and i!=(len(parametro)-1) and ( valor < parametro[i-1] or valor> parametro[i+1]):
            resultado.append(0)    
        elif valor < parametro[i]:
            a = (valor - parametro[i-1])/(parametro[i]-parametro[i-1])
            resultado.append(a)
        elif valor > parametro[i]:
            resultado.append((valor - parametro[i+1])/(parametro[i]-parametro[i+1]))
    return resultado


def suma_valores_lista(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma


def dividir_lista(lista, divisor):
    for i in range(len(lista)):
        lista[i]=lista[i]/divisor
    return lista
       

def run():
    valores_parametro_1 = [1, 2, 4, 10, 65, 160]
    valores_a_evaluar_parametro_1= [2.01, 1.68, 50, 10]
    #preparación de los datos
    promedio_valores_parametro_1=suma_valores_lista(valores_parametro_1)
    wnd_valores_parametro_1=dividir_lista(valores_parametro_1, promedio_valores_parametro_1)
    wnd_valores_a_evaluar_parametro_1=dividir_lista(valores_a_evaluar_parametro_1, promedio_valores_parametro_1)
    #evaluando los datos
    cuerpo_1=fun_grey_clustering(wnd_valores_parametro_1, wnd_valores_a_evaluar_parametro_1[0])
    print(cuerpo_1)



if __name__ == "__main__":
    run()