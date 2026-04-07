def quicksort(arr):
    # Caso base: listas con 0 o 1 elemento ya están ordenadas
    if len(arr) <= 1:
        return arr
    else:
        # Selección del pivote (en este caso, el último)
        pivot = arr[-1]
        
        # Partición: elementos menores, iguales y mayores que el pivote
        menores = [x for x in arr[:-1] if x <= pivot]
        mayores = [x for x in arr[:-1] if x > pivot]
        
        # Recursión y concatenación
        return quicksort(menores) + [pivot] + quicksort(mayores)

# Ejemplo de uso:
mi_lista = [10, 7, 8, 9, 1, 5]
lista_ordenada = quicksort(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista ordenada: {lista_ordenada}")
