import mysql.connector
from conexionBD import obtener_conexion

class Autos:
    def __init__(self, matricula, marca, modelo, color, nif_cliente):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif_cliente = nif_cliente

    def agregar_auto(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO autos (matricula, marca, modelo, color, nif_cliente) 
                VALUES (%s, %s, %s, %s, %s)
            """, (self.matricula, self.marca, self.modelo, self.color, self.nif_cliente))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def consultar_auto(matricula):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT * FROM autos WHERE matricula = %s
            """, (matricula,))
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def obtener_autos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM autos")
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
            conexion.close()

    def actualizar_auto(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                UPDATE autos 
                SET marca = %s, modelo = %s, color = %s, nif_cliente = %s
                WHERE matricula = %s
            """, (self.marca, self.modelo, self.color, self.nif_cliente, self.matricula))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar_auto(matricula):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM autos WHERE matricula = %s", (matricula,))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conexion.close()
