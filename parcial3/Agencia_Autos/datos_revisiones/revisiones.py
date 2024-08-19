import mysql.connector
from conexionBD import obtener_conexion

class revisiones:
    def __init__(self, no_revision, cambioFiltro, cambioAceite, cambioFrenos, otros, matricula_auto):
        self.no_revision = no_revision
        self.cambioFiltro = cambioFiltro
        self.cambioAceite = cambioAceite
        self.cambioFrenos = cambioFrenos
        self.otros = otros
        self.matricula_auto = matricula_auto

    def agregar_revision(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
        INSERT INTO revisiones (no_revision, cambioFiltro, cambioAceite, cambioFrenos, otros, matricula_auto) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (self.no_revision, self.cambioFiltro, self.cambioAceite, self.cambioFrenos, self.otros, self.matricula_auto)
        try:
            cursor.execute(query, values)
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
           
    @staticmethod
    def consultar_revision(no_revision):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "SELECT * FROM revisiones WHERE no_revision = %s"
        cursor.execute(query, (no_revision,))
        result = cursor.fetchone()
        cursor.close()
        
        return result

    @staticmethod
    def obtener_revisiones():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "SELECT * FROM revisiones"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        
        return result

    def actualizar_revision(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
        UPDATE revisiones 
        SET cambioFiltro = %s, cambioAceite = %s, cambioFrenos = %s, otros = %s, matricula_auto = %s 
        WHERE no_revision = %s
        """
        values = (self.cambioFiltro, self.cambioAceite, self.cambioFrenos, self.otros, self.matricula_auto, self.no_revision)
        try:
            cursor.execute(query, values)
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
           

    @staticmethod
    def eliminar_revision(no_revision):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM revisiones WHERE no_revision = %s"
        try:
            cursor.execute(query, (no_revision,))
            conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
           