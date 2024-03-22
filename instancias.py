from te import Te

# Creo dos instancias de te
primer_te = Te()
segundo_te = Te()

# Guardo en variables el tipo de los tés
tipo1 = type(primer_te)
tipo2 = type(segundo_te)

# Imprimo los tipos
print(tipo1)
print(tipo2)

# Comparo si son iguales
if tipo1 == tipo2 :
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos son de distinto tipo")