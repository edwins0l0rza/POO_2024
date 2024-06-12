# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado



# Crear una lista de 8 números enteros
numeros = [5, 3, 8, 6, 2, 9, 1, 4]

# a.- Recorrer la lista y mostrarla
def mostrar_lista(lista):
    for numero in lista:
        print(numero)

# b.- Función que recorra la lista de números y devuelva un string
def lista_como_string(lista):
    return ', '.join(str(numero) for numero in lista)

# c.- Ordenar la lista y mostrarla
def ordenar_lista(lista):
    return sorted(lista)

# d.- Mostrar la longitud de la lista
def longitud_lista(lista):
    return len(lista)

# e.- Buscar un elemento que el usuario pida por teclado
def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El número {elemento} se encuentra en la lista."
    else:
        return f"El número {elemento} no se encuentra en la lista."

# Mostrar la lista
print("a.- Lista original:")
mostrar_lista(numeros)

# Devolver la lista como un string
print("\nb.- Lista como string:")
print(lista_como_string(numeros))

# Ordenar y mostrar la lista
print("\nc.- Lista ordenada:")
numeros_ordenados = ordenar_lista(numeros)
mostrar_lista(numeros_ordenados)

# Mostrar la longitud de la lista
print("\nd.- Longitud de la lista:")
print(longitud_lista(numeros))

# Buscar un elemento que el usuario pida por teclado
elemento_a_buscar = int(input("\ne.- Ingrese un número para buscar en la lista: "))
print(buscar_elemento(numeros, elemento_a_buscar))