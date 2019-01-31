class Persona:
    """
    """   
    def __init__(self, n, ape, e):#Contructor de la clase estudiante que recibe 3 atributos
        """
        """
        self.nombre = n
        self.apellido = ape
        self.edad = int(e)

    #Metodos de agregar y obtener para cada atributo
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_apellido(self, n):
        """
        """
        self.apellido = ape

    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_edad(self, n):
        """
        """
        self.edad = int(e)

    def obtener_edad(self):
        """
        """
        return self.edad

    #Metodo str para presentar datos de la clase 
    def __str__(self):
        return "%s %s %d"%(self.nombre, self.apellido, self.edad)