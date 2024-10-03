# Andrea Mondragon Saa

# Algoritmo de ordenación por selección

import random  # Importamos el módulo random para generar números aleatorios

# Se define la función para el algoritmo de ordenación por selección
def seleccion_ordenacion(lista):
    # Iteramos sobre cada elemento de la lista
    for i in range(len(lista)):
        # Asumimos que el primer elemento no ordenado es el mínimo
        minimo_indice = i
        # Iteramos sobre los elementos restantes para encontrar el mínimo
        for j in range(i + 1, len(lista)):
            # Si encontramos un elemento menor, actualizamos el índice del mínimo
            if lista[j] < lista[minimo_indice]:
                minimo_indice = j
        # Intercambiamos el mínimo encontrado con el primer elemento no ordenado
        lista[i], lista[minimo_indice] = lista[minimo_indice], lista[i]

# Generamos una lista desordenada de los números del 1 al 10
numeros = random.sample(range(1, 11), 10)  # Lista de los números del 1 al 10 en desorden

# Imprimimos la lista original
print("Lista original:", numeros)

# Llamamos a la función para ordenar la lista
seleccion_ordenacion(numeros)

# Imprimimos la lista ordenada
print("Lista ordenada:", numeros)