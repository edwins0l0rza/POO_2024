import mysql.connector
from conexionBD import obtener_conexion

class Usuarios:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (nombre, apellidos, email, password) 
                VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.apellidos, self.email, self.password))
            conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def iniciar_sesion(email, password):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT email, nombre, apellidos 
                FROM usuarios 
                WHERE email = %s AND password = %s
            """, (email, password))
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            conexion.close()
