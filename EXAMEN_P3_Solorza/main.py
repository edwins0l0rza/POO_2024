from clientes import Clientes
from funciones import *


# Registro de clientes
def insertar_cliente():
    limpiar_pantalla()
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    cliente = Clientes(nombre, direccion, ciudad)
    cliente.crear()
    esperar_tecla()

def consultar_cliente():
    limpiar_pantalla()
    clientes = Clientes.mostrar()  # Llamar al método de la clase Clientes
    if clientes:
        for fila in clientes:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Dirección: {fila[2]}, Ciudad: {fila[3]}")
    else:
        print("No se encontraron clientes.")
    esperar_tecla()

def actualizar_cliente():
    limpiar_pantalla()
    id = input("ID del cliente a actualizar: ")
    nombre = input("Nuevo nombre: ")
    direccion = input("Nueva dirección: ")
    ciudad = input("Nueva ciudad: ")
    Clientes.actualizar(id, nombre, direccion, ciudad)
    esperar_tecla()

def eliminar_cliente():
    limpiar_pantalla()
    id = input("ID del cliente a eliminar: ")
    Clientes.eliminar(id)
    esperar_tecla()

def menu():
    while True:
        limpiar_pantalla()
        print("\n--- ..:: Menú de Opciones ::.. ---")
        print("1. Crear cliente")
        print("2. Consultar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            insertar_cliente()
        elif opcion == '2':
            consultar_cliente()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            esperar_tecla()

if __name__ == "__main__":
    menu()
