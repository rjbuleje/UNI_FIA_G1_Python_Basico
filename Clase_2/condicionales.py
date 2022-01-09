def tipo_cambio( cambio, monto):
    resultado_final = cambio * monto
    resultado_final = round(resultado_final, 3)
    print("Al día de hoy recibes: " + str(resultado_final))



print("""
Bienvenido a esta cada de cambios
Dueño: Daniel

Aquí aceptamos dólares y devolvemos soles o pesos colombianos

Por favor ingrese el monto a cambiar y el tipo de moneda que desee obtener:

Seleccione la moneda de ingreso:
1. soles
2. pesos colombianas
3. dolares

Seleccione la moneda de salida:
1. soles
2. pesos colombianas
3. dolares

""")

monto_inicial = float(input("Ingresa el monto a cambiar: "))
moneda_inicial = int(input("Ingrese 1 o 2 o 3 según la moneda inicial: "))
moneda_final = int(input("Ingrese 1 o 2 o 3 según la moneda final: "))
dolar_pesos = 3589.0
dolar_soles = 3.85
soles_pesos = 932.0
pesos_dolar = 1/dolar_pesos
soles_dolar = 1/dolar_soles
pesos_soles = 1/soles_pesos

if moneda_inicial == moneda_final:
    print("Vuelva a comenzar")
elif moneda_inicial == 1 and moneda_final == 2:
    tipo_cambio(soles_pesos, monto_inicial)
elif moneda_inicial == 1 and moneda_final == 3:
    tipo_cambio(soles_dolar, monto_inicial)
elif moneda_inicial == 2 and moneda_final == 1:
    pass
elif moneda_inicial == 2 and moneda_final == 3:
    pass
elif moneda_inicial == 3 and moneda_final == 2:
    pass
elif moneda_inicial == 3 and moneda_final == 1:
    pass
else:
    print("Esto fue un error, vuelva a comenzar")




