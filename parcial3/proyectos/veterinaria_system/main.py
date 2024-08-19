from animales import Animal
from funciones import limpiar_pantalla, esperar_tecla

def registrar_animal():
    limpiar_pantalla()
    nombre = input("Nombre del animal: ")
    especie = input("Especie: ")
    edad = input("Edad: ")
    animal = Animal(nombre, especie, edad)
    animal.registrar()
    esperar_tecla()

def ver_animales():
    limpiar_pantalla()
    animales = Animal.mostrar()
    if animales:
        for fila in animales:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Especie: {fila[2]}, Edad: {fila[3]}")
    else:
        print("No se encontraron animales registrados.")
    esperar_tecla()

def actualizar_animal():
    limpiar_pantalla()
    id = input("ID del animal a actualizar: ")
    nombre = input("Nuevo nombre: ")
    especie = input("Nueva especie: ")
    edad = input("Nueva edad: ")
    Animal.actualizar(id, nombre, especie, edad)
    esperar_tecla()

def eliminar_animal():
    limpiar_pantalla()
    id = input("ID del animal a eliminar: ")
    Animal.eliminar(id)
    esperar_tecla()

def menu():
    while True:
        limpiar_pantalla()
        print("\n--- ..:: Menú de Opciones ::.. ---")
        print("1. Registrar animal")
        print("2. Ver animales")
        print("3. Actualizar animal")
        print("4. Eliminar animal")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            registrar_animal()
        elif opcion == '2':
            ver_animales()
        elif opcion == '3':
            actualizar_animal()
        elif opcion == '4':
            eliminar_animal()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            esperar_tecla()

if __name__ == "__main__":
    menu()
