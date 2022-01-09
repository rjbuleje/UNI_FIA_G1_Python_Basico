a = int(input("Agregue el valor 1,1: "))
b = int(input("Agregue el valor 1,2: "))
c = int(input("Agregue el valor 1,3: "))
d = int(input("Agregue el valor 2,1: "))
e = int(input("Agregue el valor 2,2: "))
f = int(input("Agregue el valor 2,3: "))
g = int(input("Agregue el valor 3,1: "))
h = int(input("Agregue el valor 3,2: "))
i = int(input("Agregue el valor 3,3: "))
matriz = [[a,b,c], [d,e,f],[g,h,i]]
numero_filas = len(matriz)
numero_columnas = len(matriz)
detp = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[1][0]*matriz[2][1]*matriz[0][2] 
detn = matriz[2][0]*matriz[1][1]*matriz[0][2] + matriz[2][1]*matriz[1][0]*matriz[0][0] + matriz[1][0]*matriz[0][1]*matriz[2][2]
det = detp - detn
print ("")
print("Tenemos la matriz ") 
for i in range(numero_columnas): 
    print(matriz[i])
print("Con su determinante ")  
print(det)