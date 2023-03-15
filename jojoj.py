from abc import ABC, abstractmethod
class Persona():
  @abstractmethod
  def Datos():
        pass

class Xiomara(Persona):
    def __init__(self, nombre, edad, altura, color_ojos):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.color_ojos = color_ojos

    def Datos(self):
        return 'Su nombre es : {}, una edad de: {} años una altura de: {} metros y su color de ojos es: {} '.format(self.nombre, self.edad, self.altura, self.color_ojos)
    

class Mascota(Persona):
    def __init__(self,nombre_Persona, nombreMascota, genero, edad):
        self.nombre_Persona = nombre_Persona
        self.nombreMascota = nombreMascota
        self.genero = genero
        self.edad = edad

    def Datos(self):
        return '{} tiene un perro de mascota su nombre es: {} su genero es: {} y tiene una edad de {} meses'.format(self.nombre_Persona, self.nombreMascota, self.genero, self.edad)
    


class hijito(Persona):
    def __init__(self, nombreMadre, NombreHijo):
        self.nombreMadre = nombreMadre
        self.nombreHijo = NombreHijo

    def Datos(self):
        return '{} Es la madre del niño {}'.format(self.nombreMadre, self.nombreHijo)
    
Erika = Xiomara("Xiomara", 19, 1.60, "cafe oscuro")
perrito = Mascota("xiomara", "Xiumin", "masculino", 11)
Familia = hijito("Ermelinda", "Erika")
print(Erika.Datos())
print(perrito.Datos())
print(Familia.Datos())