# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas



# Crear una lista vacía
palabras = []

# Verificar si la lista está vacía y llenarla 
if not palabras:
    print("La lista está vacía. Por favor, añade palabras o frases.")
    while True:
        entrada = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        palabras.append(entrada)

# Imprimir el contenido de la lista en mayúsculas
print("\nContenido de la lista en mayúsculas:")
for palabra in palabras:
    print(palabra.upper())