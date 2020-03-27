class Persona:

    #Constructor de la clase
    #Atributos
    nombre = []
    apellido = []

    #Metodos
    def addPerson(self,nombre,apellido):
        self.nombre.append(nombre)
        self.apellido.append(apellido)

    def showPerson(self):
        for i in range(0,len(self.nombre)):
            print("nombre" + str(self.nombre[i] + "apellido" + str(self.apellido[i]))

Persona = Persona()
Persona.addPerson("Juan","Cano")
Persona.addPerson("Jorge","Lopez")
Persona.showPerson()

