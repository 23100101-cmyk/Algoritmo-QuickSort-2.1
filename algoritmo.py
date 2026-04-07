def quicksort(arr):
    # Caso base
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote (elemento del medio)
    pivote = arr[len(arr) // 2]
    
    # Crear subarrays
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # Llamadas recursivas
    return quicksort(menores) + iguales + quicksort(mayores)


# Ejemplo para usar
array = [10, 7, 8, 9, 1, 5]
ordenado = quicksort(array)

print("Array original:", array)
print("Array ordenado:", ordenado)

# Segundo ejemplo
#array = ["pera", "manzana", "uva", "banana", "kiwi"]
#ordenado = quicksort(array)

#print("Array original:", array)
#print("Array ordenado:", ordenado)






