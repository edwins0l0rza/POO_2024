def solicitarNumeros():
    # global n1,n2
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    return n1,n2

def calculadora(n1,n2,opcion):
     if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}/{n2}={n1/n2}"
     elif opcion=="5" or opcion=="r" or opcion=="RAIZ":
        raiz_cuadrada=pow(n1,0.5)
        return f"√{n1}={raiz_cuadrada}"
     elif opcion=="6" or opcion=="**" or opcion=="POTENCIA":
        
        return f"{n1}^{n2}={n1**n2}"
     

def espereTecla():
   print("Oprima cualquier tecla para continuar...")
   input()


#FUNCIONES DE PELICULAS:
def insertarPelicula(peliculas):
    pelicula = input("Ingrese la película: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPelicula(peliculas):
    pelicula = input("Ingrese la película: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print("Película eliminada con éxito.")
    else:
        print("La película no está en la lista.")
    espereTecla()

def consultarPeliculas(peliculas):
    print("Películas en la lista:")
    for pelicula in peliculas:
        print("-", pelicula)
    espereTecla()

def actualizarPelicula(peliculas):
    pelicula_vieja = input("Ingrese la película que desea actualizar: ")
    if pelicula_vieja in peliculas:
        pelicula_nueva = input("Ingrese el nuevo nombre de la película: ")
        index = peliculas.index(pelicula_vieja)
        peliculas[index] = pelicula_nueva
        print("Película actualizada con éxito.")
    else:
        print("La película no está en la lista.")
    espereTecla()

def buscarPelicula(peliculas):
    pelicula = input("Ingrese la película que desea buscar: ")
    if pelicula in peliculas:
        print("La película está en la lista.")
    else:
        print("La película no está en la lista.")
    espereTecla()

def vaciarPeliculas(peliculas):
    peliculas.clear()
    print("Todas las películas han sido eliminadas.")
    espereTecla()

def espereTecla():
    input("Presione Enter para continuar...")