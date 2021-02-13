# Algoritmo Quicksort (Ordenamiento Rápido)
def quicksort(lista):
    tamaño = len(lista)
    if tamaño <= 1:
        return lista
    else:
        pivote = lista.pop()

    superiores = []
    inferiores = []

    for numero in lista:
        if numero > pivote:
            superiores.append(numero)
        else:
            inferiores.append(numero)

    return quicksort(inferiores) + [pivote] + quicksort(superiores)
