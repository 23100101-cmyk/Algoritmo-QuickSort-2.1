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
