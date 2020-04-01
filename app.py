class Persona:
    #constructor de la clase
    #atributos
    name = []
    lastname = []

    #metodos
    def addPerson(self, name, lastname):
        self.name.append(name)
        self.lastname.append(lastname)
    
    def showPeople(self):
        for i in range(0,len(self.name)):
            print("name:" + str(self.name[i]) + " lastname: " + str(self.lastname[i]))

persona = Persona()
persona.addPerson("juan","zabala")
persona.addPerson("Jorge", "Lopez")
persona.showPeople()
