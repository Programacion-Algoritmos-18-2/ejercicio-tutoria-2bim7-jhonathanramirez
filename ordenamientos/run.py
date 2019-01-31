from archivo.MiArchivo import *
from modelado.modelo import *
from ordenamiento.combinacion import *

obj = MiArchivo()#Creamos un objeto de tipo mi archivo para leer el text 
listado = obj.obtener_informacion()#Guarda la informacion en una lista 
listado = [l.split(";") for l in listado]#Separamos los datos de la lista con ";"

listado2 = []
listado3 = []

for f in listado:
    p = Persona(f[0],f[1],f[2])#Creamos un objeto tipo persona para enviar datos  
    listado2.append(p)

for i in listado2:
	listado3.append(i.obtener_edad())
print(merge_sort(listado3))						