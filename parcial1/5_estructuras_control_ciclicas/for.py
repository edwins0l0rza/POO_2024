# Ciclo For Estructura iterativa que se ejecuta X veces

# Sintaxis
#     for variable in elemento_iterable(lista, rango, etc)
#         bloque de instrucciones

# Ejemplo 1 Crear un program que imprima en pantalla 5 veces el @

# contador=1

# for contador in range(1,6):
#     print("@")

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma

# contador=1
# suma=0
# for contador in range(1,6):
#     print(contador)
#     suma+=contador

# print(f"La suma es: {suma}")


#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuaria desee

tabla=int(input("Ingresa un numero para calcular su tabla de multiplicar: "))

i=1
multi=0

for i in range (1,11):
    multi=i*tabla
    print(f"{tabla} X {i} = {multi}")
