from conexionBD import crear_conexion

class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def registrar(self):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO animales (nombre, especie, edad) VALUES (%s, %s, %s)",
                    (self.nombre, self.especie, self.edad)
                )
                conexion.commit()
                print("Animal registrado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al registrar el animal: {e}")
                return False
            finally:
                conexion.close()

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM animales")
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Error al leer los registros de animales: {e}")
                return []
            finally:
                conexion.close()

    @staticmethod
    def actualizar(id, nombre, especie, edad):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE animales SET nombre = %s, especie = %s, edad = %s WHERE id = %s",
                    (nombre, especie, edad, id)
                )
                conexion.commit()
                print("Animal actualizado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al actualizar el registro del animal: {e}")
                return False
            finally:
                conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "DELETE FROM animales WHERE id = %s",
                    (id,)
                )
                conexion.commit()
                print("Animal eliminado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al eliminar el registro del animal: {e}")
                return False
            finally:
                conexion.close()
