class Personas:
    def _init_(self,nombre,edad,tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel

    def info_persona(self):
        print(f"Informacion de la persona: {self.getNombre(), self.getEdad(), self.getTel()}")

    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad   
    def getTel(self):
        return self.tel
    def setNombre(self,nombre):
        self.nombre=nombre
    def setEdad(self,edad):
        self.edad=edad  
    def setTel(self,tel):
        self.tel=tel

class Estudiantes(Personas):
   def _init_(self,nombre,edad,tel,carrera,matricula):
      super()._init_(nombre,edad,tel)
      self.__carrera=carrera
      self.__matricula=matricula

   def info_persona(self):
        print(f"Informacion de la persona Estudiante: {self.getNombre(), self.getEdad(), self.getTel(), self.getCarrera(), self.getMatricula()}")

   def getCarrera(self):
        return self.__carrera
   def getMatricula(self):
        return self.__matricula   
    
   def setCarrera(self,carrera):
        self.__carrera=carrera
   def setMatricula(self,matricula):
        self.__matricula=matricula  

class Docentes(Personas):
   def _init_(self,nombre,edad,tel,modalidad,num_empleado):
      super()._init_(nombre,edad,tel)
      self._modalidad=modalidad
      self._num_empleado=num_empleado

   def info_persona(self):
        print(f"Informacion de la persona Docente: {self.getNombre(), self.getEdad(), self.getTel(), self.getModalidad(), self.getNum_empleado()}")

   def getModalidad(self):
        return self._modalidad
   def getNum_empleado(self):
        return self._num_empleado  
    
   def setModalidad(self,modalidad):
        self._modalidad=modalidad
   def setNum_empleado(self,num_empleado):
        self._num_empleado=num_empleado  









class Lectores:
    def _init_(self,nombre,direccion,tel):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel

    def reservar(self):
        print(f"Esta reservado el libro por: {self.getNombre()} y su telefono es: {self.getTel()}")

    def entregar(self):
        print(f"Esta entregado el libro por: {self.getNombre()} y su telefono es: {self.getTel()}")     

    def getNombre(self):
      return self.nombre
    def getDireccion(self):
      return self.direccion
    def getTel(self):
      return self.tel
    def setNombre(self,nombre):
      self.nombre=nombre
    def setDireccion(self,direccion):
      self.direccion=direccion
    def setTel(self,tel):
      self.tel=tel

class Estudiantes(Lectores):
   def _init_(self,nombre,direccion,tel,carrera,matricula):
     super()._init_(nombre,direccion,tel)
     self._carrera=carrera
     self._matricula=matricula

   def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def getCarrera(self):
      return self._carrera
   def getMatricula(self):
      return self._matricula
   
   def setCarrera(self,carrera):
      self._carrera=carrera
   def setMatricula(self,matricula):
      self._matricula=matricula     

class Docentes(Lectores):
   def _init_(self,nombre,direccion,tel,modalidad,num_empleado):
     super()._init_(nombre,direccion,tel)
     self.__modalidad=modalidad
     self.__num_empleado=num_empleado

   def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def getModalidad(self):
      return self.__modalidad
   def getNum_empleado(self):
      return self.__num_empleado
   
   def setModalidad(self,modalidad):
      self.__modalidad=modalidad
   def setMatricula(self,num_empleado):
      self.__num_empleado=num_empleado