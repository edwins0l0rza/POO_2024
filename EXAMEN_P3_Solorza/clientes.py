from conexionBD import crear_conexion

class Clientes:
    def __init__(self, nif, nombre, direccion, ciudad):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad


    def insertar(self):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s)",
                    (self.nif, self.nombre, self.direccion, self.ciudad)
                )
                conexion.commit()
                print("Cliente insertado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al insertar el cliente: {e}")
                return False
                # cerrar_conexion(conexion)

    @staticmethod
    def consultar():
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM clientes")
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Error al consultar los clientes: {e}")
                return []
        
                # cerrar_conexion(conexion)

    @staticmethod
    def actualizar(nif, nombre, direccion, ciudad):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s",
                    (nombre, direccion, ciudad, nif)
                )
                conexion.commit()
                print("Cliente actualizado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al actualizar el cliente: {e}")
                return False
                # cerrar_conexion(conexion)

    @staticmethod
    def eliminar(nif):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "DELETE FROM clientes WHERE nif = %s",
                    (nif,)
                )
                conexion.commit()
                print("Cliente eliminado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al eliminar el cliente: {e}")
                return False
                # cerrar_conexion(conexion)
