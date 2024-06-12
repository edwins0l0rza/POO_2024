# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for


# Crear una lista vacía
numeros = []

# Añadir valores a la lista mientras su longitud sea menor a 120
while len(numeros) < 120:
    # Añadir un número aleatorio o un valor incremental
    numeros.append(len(numeros) + 1)

# Mostrar la lista
print("Lista de números (longitud: {}):".format(len(numeros)))
for numero in numeros:
    print(numero)