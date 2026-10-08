"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado

def area_rectangulo(base,altura):
    return base * altura

base=float(input("Ingrese la base:  "))
altura=float(input("Ingrese la altura:  "))

area=area_rectangulo(base,altura)
print(f"El area del rectangulo es: {area}")


#Implementar el paradigma Orientado a Objetos (OO)

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area_rectangulo(self):
        return self.base * self.altura

rectangulo=Rectangulo(5,3)
print(f"El area es :  {rectangulo.area_rectangulo()}")


