from datos_clientes.clientes import clientes
from datos_auto.autos import Autos
from datos_revisiones.revisiones import revisiones
from usuario import Usuarios
from funciones import borrarPantalla, esperarTecla
import getpass

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      :||||||:.  Menú Principal .:||||||: 
          1.- Registrar
          2.- Iniciar Sesión
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "REGISTRAR":
            borrarPantalla()
            print("\n \t => [Registro en el Sistema] <=")
            nombre = input("\t Ingresa tu numbre: -> ")
            apellidos = input("\t Ingresa tus apellidos: -> ")
            email = input("\t Ingresa tu correo electronico: -> ")
            password = getpass.getpass("\t Password: -> ")
            obj_usuario = Usuarios(nombre, apellidos, email, password)
            resultado = obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, Correo registrado con exito => [{email}]")
            else:
                print(f"\n\t X No fue posible registrarte :( ...Intenta de nuevo  X ...")  
            esperarTecla()      
        elif opcion == '2' or opcion == "INICIAR SESION":
            borrarPantalla()
            print("\n \t ||||[Inicio de Sesión]||||")     
            email = input("\t Ingresa tu correo: -> ")
            password = getpass.getpass("\t Ingresa tu password: ->")
            registro = Usuarios.iniciar_sesion(email, password)
            if registro:
                print(f"\n\t Hola de nuevo!!, {registro[1]} {registro[2]} ({registro[0]})")
                menu_secundario()  
            else:
                print(f"\n\t X-Correo y/o contraseña incorrectos. Vuelva a intentarlo.-X")
            esperarTecla()    
        elif opcion == '3' or opcion == "SALIR":
            print("\n\t.. ¡Gracias! ¡Hasta la proximaaaaaaa! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_secundario():
    while True:
        borrarPantalla()
        print("""
      ===///Agencia AUTOFAST\\\=== 
          1.- Autos
          2.- Clientes
          3.- Mantenimiento y Revisiones
          4.- Salir 
          """)
        opcion = input("\t Selecciona una opción: ")

        if opcion == "1":
            menu_autos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_revisiones()
        elif opcion == "4":
            print("\n\t.. ¡Bye, Bye! ...")
            break
        else:
            print("\n\t Opción no válida.")
            esperarTecla()

def menu_clientes():
    while True:
        borrarPantalla()
        print("""
           ///Servicio a Clientes\\\ 
          1.- Agregar cliente
          2.- Consultar cliente
          3.- Mostrar registro de clientes
          4.- Actualizar cliente
          5.- Eliminar cliente
          6.- Volver al menú secundario
          """)
        opcion = input("\t Selecciona una opción: ")

        if opcion == "1":
            nif = input("\t NIF: ")
            nombre = input("\t Nombre: ")
            direccion = input("\t Dirección: ")
            ciudad = input("\t Ciudad: ")
            tel = input("\t Teléfono: ")
            nuevo_cliente = clientes(nif, nombre, direccion, ciudad, tel)
            nuevo_cliente.agregar_cliente()  
            print("\n\t Cliente agregado con éxito.")
            esperarTecla()
        
        elif opcion == "3":
            nif = input("\t Ingresa el NIF del cliente a consultar: ")
            cliente_info = clientes.consultar_cliente(nif)  
            if cliente_info:
                print(f"\n\t NIF: {cliente_info[0]}, Nombre: {cliente_info[1]}, Dirección: {cliente_info[2]}, Ciudad: {cliente_info[3]}, Teléfono: {cliente_info[4]}")
            else:
                print("\n\t Cliente no encontrado.")
            esperarTecla()
        
        elif opcion == "2":
            lista_clientes = clientes.obtener_clientes()  
            for c in lista_clientes:
                print(f"\n\t NIF: {c[0]}, Nombre: {c[1]}, Dirección: {c[2]}, Ciudad: {c[3]}, Teléfono: {c[4]}")
            esperarTecla()
        
        elif opcion == "4":
            nif = input("\t Ingresa el NIF del cliente a actualizar: ")
            cliente_info = clientes.consultar_cliente(nif)  
            if cliente_info:
                nombre = input(f"\t Nuevo nombre ({cliente_info[1]}): ") or cliente_info[1]
                direccion = input(f"\t Nueva dirección ({cliente_info[2]}): ") or cliente_info[2]
                ciudad = input(f"\t Nueva ciudad ({cliente_info[3]}): ") or cliente_info[3]
                tel = input(f"\t Nuevo teléfono ({cliente_info[4]}): ") or cliente_info[4]
                cliente_actualizado = clientes(nif, nombre, direccion, ciudad, tel)
                cliente_actualizado.actualizar_cliente()  
                print("\n\t Cliente actualizado con éxito.")
            else:
                print("\n\t Cliente no encontrado.")
            esperarTecla()
        
        elif opcion == "5":
            nif = input("\t Ingresa el NIF del cliente a eliminar: ")
            clientes.eliminar_cliente(nif)  
            print("\n\t Cliente eliminado con éxito.")
            esperarTecla()
        
        elif opcion == "6":
            break
        else:
            print("\n\t Opción no válida.")
            esperarTecla()

def menu_autos():
    while True:
        borrarPantalla()
        print("""
          ///Servico de Autos\\\ 
          1.- Agregar auto
          2.- Consultar auto
          3.- Mostrar todos los autos
          4.- Actualizar auto
          5.- Eliminar auto
          6.- Volver al menú secundario
          """)
        opcion = input("\t Selecciona una opción: ")

        if opcion == "1":
            matricula = input("\t Matrícula: ")
            marca = input("\t Marca: ")
            modelo = input("\t Modelo: ")
            color = input("\t Color: ")
            nif = input("\t NIF del cliente: ")
            nuevo_auto = Autos(matricula, marca, modelo, color, nif)
            nuevo_auto.agregar_auto()  
            print("\n\t Auto agregado con éxito.")
            esperarTecla()
        
        elif opcion == "3":
            matricula = input("\t Ingresa la matrícula del auto a consultar: ")
            auto_info = Autos.consultar_auto(matricula)  
            if auto_info:
                print(f"\n\t Matrícula: {auto_info[0]}, Marca: {auto_info[1]}, Modelo: {auto_info[2]}, Color: {auto_info[3]}, NIF del cliente: {auto_info[4]}")
            else:
                print("\n\t Auto no encontrado.")
            esperarTecla()
        
        elif opcion == "2":
            lista_autos = Autos.obtener_autos()  
            for a in lista_autos:
                print(f"\n\t Matrícula: {a[0]}, Marca: {a[1]}, Modelo: {a[2]}, Color: {a[3]}, NIF del cliente: {a[4]}")
            esperarTecla()
        
        elif opcion == "4":
            matricula = input("\t Ingresa la matrícula del auto a actualizar: ")
            auto_info = Autos.consultar_auto(matricula)  
            if auto_info:
                marca = input(f"\t Nueva marca ({auto_info[1]}): ") or auto_info[1]
                modelo = input(f"\t Nuevo modelo ({auto_info[2]}): ") or auto_info[2]
                color = input(f"\t Nuevo color ({auto_info[3]}): ") or auto_info[3]
                nif = input(f"\t Nuevo NIF del propietario ({auto_info[4]}): ") or auto_info[4]
                auto_actualizado = Autos(matricula, marca, modelo, color, nif)
                auto_actualizado.actualizar_auto()  
                print("\n\t Auto actualizado con éxito.")
            else:
                print("\n\t Auto no encontrado.")
            esperarTecla()
        
        elif opcion == "5":
            matricula = input("\t Ingresa la matrícula del auto a eliminar: ")
            Autos.eliminar_auto(matricula)  
            print("\n\t Auto eliminado con éxito.")
            esperarTecla()
        
        elif opcion == "6":
            break
        else:
            print("\n\t Opción no válida.")
            esperarTecla()

def menu_revisiones():
    while True:
        borrarPantalla()
        print("""
           //Mantenimiento y Revisiones\\
          1.- Agregar revisión
          2.- Consultar revisión
          3.- Mostrar todas las revisiones
          4.- Actualizar revisión
          5.- Eliminar revisión
          6.- Volver al menú secundario
          """)
        opcion = input("\t Selecciona una opción: ")

        if opcion == "1":
            no_revision = input("\t Número de revisión: ")
            cambioFiltro = input("\t Cambio de filtro: ")
            cambioAceite = input("\t Cambio de aceite: ")
            cambioFrenos = input("\t Cambio de frenos: ")
            otros = input("\t Otros detalles: ")
            matricula_auto = input("\t Matrícula del auto: ")
            nueva_revision = revisiones(no_revision, cambioFiltro, cambioAceite, cambioFrenos, otros, matricula_auto)
            nueva_revision.agregar_revision()  
            print("\n\t Revisión agregada con éxito.")
            esperarTecla()
        
        elif opcion == "3":
            no_revision = input("\t Ingresa el número de revisión a consultar: ")
            revision_info = revisiones.consultar_revision(no_revision)  
            if revision_info:
                print(f"\n\t Número de revisión: {revision_info[0]}, Cambio de filtro: {revision_info[1]}, Cambio de aceite: {revision_info[2]}, Cambio de frenos: {revision_info[3]}, Otros detalles: {revision_info[4]}, Matrícula del auto: {revision_info[5]}")
            else:
                print("\n\t Revisión no encontrada.")
            esperarTecla()
        
        elif opcion == "2":
            lista_revisiones = revisiones.obtener_revisiones()  
            for r in lista_revisiones:
                print(f"\n\t Número de revisión: {r[0]}, Cambio de filtro: {r[1]}, Cambio de aceite: {r[2]}, Cambio de frenos: {r[3]}, Otros detalles: {r[4]}, Matrícula del auto: {r[5]}")
            esperarTecla()
        
        elif opcion == "4":
            no_revision = input("\t Ingresa el número de revisión a actualizar: ")
            revision_info = revisiones.consultar_revision(no_revision)  
            if revision_info:
                cambioFiltro = input(f"\t Nuevo cambio de filtro ({revision_info[1]}): ") or revision_info[1]
                cambioAceite = input(f"\t Nuevo cambio de aceite ({revision_info[2]}): ") or revision_info[2]
                cambioFrenos = input(f"\t Nuevo cambio de frenos ({revision_info[3]}): ") or revision_info[3]
                otros = input(f"\t Nuevos detalles ({revision_info[4]}): ") or revision_info[4]
                revision_actualizada = revisiones(no_revision, cambioFiltro, cambioAceite, cambioFrenos, otros, revision_info[5])
                revision_actualizada.actualizar_revision()  
                print("\n\t Revisión actualizada con éxito.")
            else:
                print("\n\t Revisión no encontrada.")
            esperarTecla()
        
        elif opcion == "5":
            no_revision = input("\t Ingresa el número de revisión a eliminar: ")
            revisiones.eliminar_revision(no_revision)  
            print("\n\t Revisión eliminada con éxito.")
            esperarTecla()
        
        elif opcion == "6":
            break
        else:
            print("\n\t Opción no válida.")
            esperarTecla()


if __name__ == "__main__":
    menu_principal()
