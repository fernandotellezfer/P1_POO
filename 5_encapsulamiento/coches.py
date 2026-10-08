"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
       self.__marca=marca
       self.__color=color
       self.__modelo=modelo
       self.__velocidad=velocidad
       self.__potencia=potencia
       self.__asientos=asientos


    def acelerar(self):
        self.__velocidad+=1

    def frenar(self):
        self.__velocidad-=1

    def getVelocidad(self):
        return self.__velocidad

    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getMarca(self):
        return self.__marca

    def setMarca(self,marca):
        self.__marca=marca

    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo

    def setModelo(self,modelo):
        self.__modelo=modelo

    def getPotencia(self):
        return self.__potencia

    def setPotencia(self,potencia):
        self.__potencia=potencia

    def getAsientos(self):
        return self.__asientos

    def setAsientos(self,asientos):
        self.__asientos=asientos




coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)



#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
        #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
        #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion


# def getVelocidad(self):
#     return self.__velocidad



