import mysql.connector
from conexionBD import obtener_conexion

class clientes:
    def __init__(self, nif, nombre, direccion, ciudad, telefono):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono

    def agregar_cliente(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO clientes (nif, nombre, direccion, ciudad, telefono) 
                VALUES (%s, %s, %s, %s, %s)
            """, (self.nif, self.nombre, self.direccion, self.ciudad, self.telefono))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def consultar_cliente(nif):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT * FROM clientes WHERE nif = %s
            """, (nif,))
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def obtener_clientes():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
            conexion.close()

    def actualizar_cliente(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                UPDATE clientes 
                SET nombre = %s, direccion = %s, ciudad = %s, telefono = %s
                WHERE nif = %s
            """, (self.nombre, self.direccion, self.ciudad, self.telefono, self.nif))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar_cliente(nif):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM clientes WHERE nif = %s", (nif,))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()
