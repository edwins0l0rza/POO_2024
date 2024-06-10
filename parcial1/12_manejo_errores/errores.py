#Manejo de errores es la forma en la que tienen los lenguajes de programación 
#para evitar que sucedan en tiempo de ejecución.

#Ejemplo 1: Error cuando una variable no se genera

"""try:
    nombre=input("Dame el nombre: ")

    if len(nombre)>1:
        nombre_usuario="El nombre es: "+nombre

    print(nombre_usuario)
except:
    print("Es necesario inroducir un nombre de usuario: ")"""

#Ejemplo 2: Cuando se solicita un numero y se introduce una letra
""" ValueError: invalid literal for int() whit base 10: '13.999' """
"""try:
    numero=int(input("Dame un numero: "))

    if numero >0:
        print("Soy un numero entero positivo")
    else:
        print("Soy un numero entero negativo")
except:
    print("No se puede convertir un caracter no numerico a numero...")
else:
    print("Todo se ejecutó CORRECTAMENTE")"""

#Ejemplo 3: Cuando se generan multiples excepciones

try:
    numero=int(input("Dame un nuemro: "))

    print("El cuadrado es: " +str(numero*numero))
except ValueError:
    print("Debes introducir un nuemro. No se puede introducir un caracter que no sea nuemrico")
except TypeError:
    print("No es posible convertir el nuemro a entero")
else:
    print("Finalizo correctamente")
finally:
    print("como dijo tu ex: TERMINAMOS")