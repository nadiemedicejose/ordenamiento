# Algoritmo de Ordenamiento por Inserción (Insertion Sort)
def insertion_sort(lista):
	# asumir que el primer elemento es una lista ordenada
	# de 1 item, por lo que omitimos este elemento
    elementos = range(1, len(lista))
    for i in elementos:
        numero = lista[i]

        while lista[i-1] > numero and i>0:
			# intercambiamos los valores
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i -= 1

    return lista