def busqueda_binaria(arr: list[int], objetivo: int) -> int:
    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:  # pragma: no mutate
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1


def busqueda_binaria_recursiva(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:  # pragma: no mutate
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)