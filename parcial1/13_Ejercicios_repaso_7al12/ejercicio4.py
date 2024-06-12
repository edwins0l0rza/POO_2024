# 4.- 

#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

# Definir las variables
una_lista = [27, 6, 19, 20]
una_cadena = "Edwin Solorza"
un_entero = 42
un_logico = True

# Función para determinar y mostrar el tipo de dato
def mostrar_tipo(variable):
    tipo = type(variable)
    print(f"La variable '{variable}' es de tipo {tipo}.")

# Mostrar el tipo de cada variable
mostrar_tipo(una_lista)
mostrar_tipo(una_cadena)
mostrar_tipo(un_entero)
mostrar_tipo(un_logico)