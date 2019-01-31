# Función merge_sort
def merge_sort(listado):
    """ 
        if para retornar el listado ordenado si es menor a 2 
    """
    if len(listado) < 2:
        return listado
    # dividimos en dos el listado
    else:
        middle = len(listado) // 2
        right = merge_sort(listado[:middle])
        left = merge_sort(listado[middle:])
        return merge(right, left)

# Función merge
def merge(listado1, listado2):
    """
        merge realiza la funcion de intercalar los elementos de las dos diviciones.
    """
    i, j = 0, 0 # contadores
    resultado = [] # Lista de resultado inicializada vacia

    # Intercalar ordenadamente
    while(i < len(listado1) and j < len(listado2)):
        if (listado1[i] < listado2[j]):
            resultado.append(listado1[i])
            i += 1
        else:
            resultado.append(listado2[j])
            j += 1
    # Agregamos los resultados a la lista
    resultado += listado1[i:]
    resultado += listado2[j:]

    # Retornamos el resultado
    return resultado