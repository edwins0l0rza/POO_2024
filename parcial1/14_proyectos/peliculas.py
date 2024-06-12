"""

 List (Array)
 son colecciones o conjunto de datos/valores bajo
 un mismo nombre, pra acceder a los valores se
 hace con un indice numerico

 Nota: sus valores si son modificables

 La lista es una coleccion ordenada y modificable. Permite miembros duplicados.

 
"""

#Ejemplo 1. Crear una lista con valores numericos enteros e imprimir una lista

"""numeros=[23,34]
print(numeros)"""

#Recorre la lista con un for

"""for i in numeros:
    print(i)"""

#Recorre la lista con un for
"""i=0
while i < len(numeros):
    print(numeros[i])
    i+=1"""

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar una palabra para buscar una 
# coicidencia en la lista e indicar si aparece la palabra y en que posicion en caso contrario
# indicar solo una vez si no la encontro.

"""palabra=["hola","2024","10.23","True"]
print(palabra)
palabra_buscar = input("inserta palabra a buscar: ")"""

"""if palabra_buscar in palabra:
    for i, p in enumerate(palabra):
        if p == palabra_buscar:
            print(f"Encontré la palabra en la posición =>{i}<=")
else:
    print("No encontré la palabra en la lista")"""

# noencontro=True
# for i in palabra:
#     if palabra_buscar == i:
#      print(f"Encontre la palabra => {palabra_buscar} <=, en la posición < {palabra.index(i)} >")
#      noencontro=False

# if noencontro:
#     print(f"No se encontro la palabra dentro de la lista")

"""i=0
while i < len(palabra):
    if palabra_buscar==palabra[i]:
        print(f"Encontre la palabra => {palabra_buscar} <=, en la posición < {i} >")
        noencontro = False
    i+=1


if noencontro:
    print("No se encontro dentro de la lista")"""

#Ejemplo 3 Crear una lista multidimensional (matriz) para crear una agenda telefonica

"""agenda=[
    ["Carlos",6181234567],
    ["Fernando",6181002614],
    ["Jordan",6754855662],
    ["Juan Mecanico",6186225489],
]

print(agenda)

for i in agenda:
    print(f"{agenda.index(i)+1}.-{i}")"""


#Ejemplo 4 Crear u programa que permita gestionar (administrar) peliculas, colocar un menu de opciones 
#para agregar, remover, consultar peliculas
#Notas:
#1.- Utilizar funciones y mandar a llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombres de peliculas


"""def insertarPeliculas():
    peliculas=input("Ingrese la pelicula: ")
    peliculas.append(peliculas)
    espereTecla()


def eliminarPeliculas():
    peliculas=input("Ingrese la pelicula: ")
    peliculas.remove(peliculas)
    espereTecla()


peliculas=[]

print("..::: CLONOPOLIS :::.. \n 1.-AGREGAR \n 2.-ELIMINAR \n 3.-CONSULTAR \n 4.-SALIR")
opcion=input("\t Elige una opción: ").upper()

if opcion=="1" or opcion=="AGREGAR":
    insertarPeliculas=()
elif opcion=="2" or opcion=="ELIMINAR":
    eliminarPeliculas=()
elif opcion=="3" or opcion=="CONSULTAR":
    eliminarPeliculas=()
elif opcion=="4" or opcion=="SALIR":
    eliminarPeliculas=()"""

#EJERCICIO: GESTION DE PELICULAS.


from varias_funciones import espereTecla, insertarPelicula, eliminarPelicula, consultarPeliculas, actualizarPelicula, buscarPelicula, vaciarPeliculas

peliculas = []

opcion_peliculas = True
while opcion_peliculas:
    print("\n\t..::: CLONOPOLIS :::... \n 1.- Agregar \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- Salir ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion == '1':
        insertarPelicula(peliculas)
    elif opcion == '2':
        eliminarPelicula(peliculas)
    elif opcion == '3':
        actualizarPelicula(peliculas)
    elif opcion == '4':
        consultarPeliculas(peliculas)
    elif opcion == '5':
        buscarPelicula(peliculas)
    elif opcion == '6':
        vaciarPeliculas(peliculas)
    elif opcion == '7':
        opcion_peliculas = False
        print("Regresando al menú principal.")
    else:
        print("Opción no válida, intente de nuevo.")