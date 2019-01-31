import codecs
import sys

class MiArchivo:#Creamos la clase para abrir archivo 
    """
    """
    def __init__(self):#Constructor de la clase
        """
        """
        self.archivo = codecs.open("data/ejemplo.txt", "r")

    def obtener_informacion(self):#Obtiene la informacion de cada linea del archivo 
        return self.archivo.readlines()

    def cerrar_archivo(self):#Cierra el archivo 
        self.archivo.close()