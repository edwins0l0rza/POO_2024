"""

Existe una estructura de condicion llamada "if"
la cual evalua la condicion para encontrar el valor "True" y si se cumple 
la condicion se ejecuta la linea o lineas de codigo

Tienes 4 variantes del if

1.- if simple
2.- if compuesto
3.- if anidado
4.- if y elif
"""

# #Ejemplo 1 if simple

# color=input("Ingresa un color")

# if color =="rojo":
#     print("Soy el color rojo")

# #Ejemplo 2 if compuesto

# color=input("Ingresa un color")

# if color =="rojo":
#     print("Soy el color rojo")
# else:
#     print("No soy el color rojo, soy otro")


# #Ejemplo 3 if anidado

# color=input("Ingresa un color")

# if color =="rojo":
#     print("Soy el color rojo")
#     if color!="rojo":
#         print("No soy el color")
# else:
#     print("No soy el color rojo, soy otro")




# #Ejemplo 4 if y elif

# color=input("Ingresa un color")

# if color =="rojo":
#     print("Soy el color rojo")
# elif color=="amarillo":
#     print ("Soy el color amarillo")
# elif color=="azul":
#     print("Soy el color azul")
# elif color=="morado":
#     print("Soy el color morado")
# else:
#     print("No soy ninguno de los anteriores")


#Ejemplo 4 Crear un programa que solicite el numero de la semana
# e imprima en pantalla el dia que le corresponde

dia=input("Ingresa un numero (del 1 al 7):")

if dia=="1":
    print("Domingo")
elif dia=="2":
    print("Lunes")
elif dia=="3":
    print("Martes")
elif dia=="4":
    print("Miercoles")
elif dia=="5":
    print("Jueves")
elif dia=="6":
    print("Viernes")
elif dia=="7":
    print("Sabado")
else:
    print("No es correcto")