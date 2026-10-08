#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches, Camiones, Camionetas

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)

# coche1.acelerar()
# coche1.acelerar()



for i in range(1,101):
    coche1.acelerar()

print(coche1.getVelocidad())

coche1.setVelocidad(400)
print(coche1.getVelocidad())


camion1=Camiones("Dina","Negro","2020",180,300,12,8,2500)
camion2=Camiones("Star","Azul","2019",150,400,14,6,2000)

camion1.cargar("Ladrillos")

camioneta1=Camionetas("Renault","Amarillo","2025",240,250,8,"Delantera",True)
camioneta2=Camionetas("Nissan","Blanca","2020",180,150,6,"Trasera",False)













