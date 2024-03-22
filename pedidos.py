from te import Te

# Pregunto por el tipo de te y guardo la respuesta
sabor = int(input(f"""Que sabor de te desea? (Ingrese numero de la opcion)
1. Te negro
2. Te verde
3. Te de hierbas
> """))

# Pregunto por el formato del te y guardo la respuesta
formato = int(input(f"""¿Que formato desea? (300 y 500 gramos)
> """))

# Guardo en variables los resultados de los metodos estaticos
tiempo, recomendacion = Te.definir_recomendacion(sabor)
precio = Te.formato_precio(formato)

# Evaluo el numero de sabor ingresado y guardo en una variable aparte el texto de sabores
if sabor == 1:
    tipo_sabor = "Te negro"
elif sabor == 2:
    tipo_sabor = "Te verde"
elif sabor  == 3:
    tipo_sabor = "Agua de Hierbas"

# Imprimo en pantalla toda la informacion
print(f"""
Tipo de te: {tipo_sabor}.
En formato es de: {formato} gramos.
Su valor es de: ${precio}. 
Tiempo de preparacion: {tiempo} minutos.
Uso recomendado: {recomendacion}.""")