from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
def x_busqueda_binaria__mutmut_orig(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_1(arr: list[int], objetivo: int) -> int:

    bajo, alto = None
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_2(arr: list[int], objetivo: int) -> int:

    bajo, alto = 1, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_3(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) + 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_4(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 2
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_5(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo < alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_6(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = None
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_7(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) / 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_8(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo - alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_9(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 3
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_10(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] != objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_11(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] <= objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_12(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = None
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_13(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio - 1
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_14(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 2
        else:
            alto = medio - 1
    
    return -1
def x_busqueda_binaria__mutmut_15(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = None
    
    return -1
def x_busqueda_binaria__mutmut_16(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio + 1
    
    return -1
def x_busqueda_binaria__mutmut_17(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 2
    
    return -1
def x_busqueda_binaria__mutmut_18(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return +1
def x_busqueda_binaria__mutmut_19(arr: list[int], objetivo: int) -> int:

    bajo, alto = 0, len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -2

x_busqueda_binaria__mutmut_mutants : ClassVar[MutantDict] = {
'x_busqueda_binaria__mutmut_1': x_busqueda_binaria__mutmut_1, 
    'x_busqueda_binaria__mutmut_2': x_busqueda_binaria__mutmut_2, 
    'x_busqueda_binaria__mutmut_3': x_busqueda_binaria__mutmut_3, 
    'x_busqueda_binaria__mutmut_4': x_busqueda_binaria__mutmut_4, 
    'x_busqueda_binaria__mutmut_5': x_busqueda_binaria__mutmut_5, 
    'x_busqueda_binaria__mutmut_6': x_busqueda_binaria__mutmut_6, 
    'x_busqueda_binaria__mutmut_7': x_busqueda_binaria__mutmut_7, 
    'x_busqueda_binaria__mutmut_8': x_busqueda_binaria__mutmut_8, 
    'x_busqueda_binaria__mutmut_9': x_busqueda_binaria__mutmut_9, 
    'x_busqueda_binaria__mutmut_10': x_busqueda_binaria__mutmut_10, 
    'x_busqueda_binaria__mutmut_11': x_busqueda_binaria__mutmut_11, 
    'x_busqueda_binaria__mutmut_12': x_busqueda_binaria__mutmut_12, 
    'x_busqueda_binaria__mutmut_13': x_busqueda_binaria__mutmut_13, 
    'x_busqueda_binaria__mutmut_14': x_busqueda_binaria__mutmut_14, 
    'x_busqueda_binaria__mutmut_15': x_busqueda_binaria__mutmut_15, 
    'x_busqueda_binaria__mutmut_16': x_busqueda_binaria__mutmut_16, 
    'x_busqueda_binaria__mutmut_17': x_busqueda_binaria__mutmut_17, 
    'x_busqueda_binaria__mutmut_18': x_busqueda_binaria__mutmut_18, 
    'x_busqueda_binaria__mutmut_19': x_busqueda_binaria__mutmut_19
}

def busqueda_binaria(*args, **kwargs):
    result = _mutmut_trampoline(x_busqueda_binaria__mutmut_orig, x_busqueda_binaria__mutmut_mutants, args, kwargs)
    return result 

busqueda_binaria.__signature__ = _mutmut_signature(x_busqueda_binaria__mutmut_orig)
x_busqueda_binaria__mutmut_orig.__name__ = 'x_busqueda_binaria'

def x_busqueda_binaria_recursiva__mutmut_orig(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_1(arr: list[int], objetivo: int, bajo: int = 1, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_2(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is not None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_3(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = None
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_4(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) + 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_5(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 2
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_6(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo >= alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_7(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return +1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_8(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -2
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_9(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = None
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_10(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) / 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_11(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo - alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_12(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 3
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_13(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] != objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_14(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] <= objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_15(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(None, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_16(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, None, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_17(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, None, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_18(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, None)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_19(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_20(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_21(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_22(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, )
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_23(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio - 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_24(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 2, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_25(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(None, objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_26(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, None, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_27(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, None, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_28(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, None)

def x_busqueda_binaria_recursiva__mutmut_29(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(objetivo, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_30(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, bajo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_31(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, medio - 1)

def x_busqueda_binaria_recursiva__mutmut_32(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, )

def x_busqueda_binaria_recursiva__mutmut_33(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio + 1)

def x_busqueda_binaria_recursiva__mutmut_34(arr: list[int], objetivo: int, bajo: int = 0, alto: int = None) -> int:
    
    if alto is None:
        alto = len(arr) - 1
    
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 2)

x_busqueda_binaria_recursiva__mutmut_mutants : ClassVar[MutantDict] = {
'x_busqueda_binaria_recursiva__mutmut_1': x_busqueda_binaria_recursiva__mutmut_1, 
    'x_busqueda_binaria_recursiva__mutmut_2': x_busqueda_binaria_recursiva__mutmut_2, 
    'x_busqueda_binaria_recursiva__mutmut_3': x_busqueda_binaria_recursiva__mutmut_3, 
    'x_busqueda_binaria_recursiva__mutmut_4': x_busqueda_binaria_recursiva__mutmut_4, 
    'x_busqueda_binaria_recursiva__mutmut_5': x_busqueda_binaria_recursiva__mutmut_5, 
    'x_busqueda_binaria_recursiva__mutmut_6': x_busqueda_binaria_recursiva__mutmut_6, 
    'x_busqueda_binaria_recursiva__mutmut_7': x_busqueda_binaria_recursiva__mutmut_7, 
    'x_busqueda_binaria_recursiva__mutmut_8': x_busqueda_binaria_recursiva__mutmut_8, 
    'x_busqueda_binaria_recursiva__mutmut_9': x_busqueda_binaria_recursiva__mutmut_9, 
    'x_busqueda_binaria_recursiva__mutmut_10': x_busqueda_binaria_recursiva__mutmut_10, 
    'x_busqueda_binaria_recursiva__mutmut_11': x_busqueda_binaria_recursiva__mutmut_11, 
    'x_busqueda_binaria_recursiva__mutmut_12': x_busqueda_binaria_recursiva__mutmut_12, 
    'x_busqueda_binaria_recursiva__mutmut_13': x_busqueda_binaria_recursiva__mutmut_13, 
    'x_busqueda_binaria_recursiva__mutmut_14': x_busqueda_binaria_recursiva__mutmut_14, 
    'x_busqueda_binaria_recursiva__mutmut_15': x_busqueda_binaria_recursiva__mutmut_15, 
    'x_busqueda_binaria_recursiva__mutmut_16': x_busqueda_binaria_recursiva__mutmut_16, 
    'x_busqueda_binaria_recursiva__mutmut_17': x_busqueda_binaria_recursiva__mutmut_17, 
    'x_busqueda_binaria_recursiva__mutmut_18': x_busqueda_binaria_recursiva__mutmut_18, 
    'x_busqueda_binaria_recursiva__mutmut_19': x_busqueda_binaria_recursiva__mutmut_19, 
    'x_busqueda_binaria_recursiva__mutmut_20': x_busqueda_binaria_recursiva__mutmut_20, 
    'x_busqueda_binaria_recursiva__mutmut_21': x_busqueda_binaria_recursiva__mutmut_21, 
    'x_busqueda_binaria_recursiva__mutmut_22': x_busqueda_binaria_recursiva__mutmut_22, 
    'x_busqueda_binaria_recursiva__mutmut_23': x_busqueda_binaria_recursiva__mutmut_23, 
    'x_busqueda_binaria_recursiva__mutmut_24': x_busqueda_binaria_recursiva__mutmut_24, 
    'x_busqueda_binaria_recursiva__mutmut_25': x_busqueda_binaria_recursiva__mutmut_25, 
    'x_busqueda_binaria_recursiva__mutmut_26': x_busqueda_binaria_recursiva__mutmut_26, 
    'x_busqueda_binaria_recursiva__mutmut_27': x_busqueda_binaria_recursiva__mutmut_27, 
    'x_busqueda_binaria_recursiva__mutmut_28': x_busqueda_binaria_recursiva__mutmut_28, 
    'x_busqueda_binaria_recursiva__mutmut_29': x_busqueda_binaria_recursiva__mutmut_29, 
    'x_busqueda_binaria_recursiva__mutmut_30': x_busqueda_binaria_recursiva__mutmut_30, 
    'x_busqueda_binaria_recursiva__mutmut_31': x_busqueda_binaria_recursiva__mutmut_31, 
    'x_busqueda_binaria_recursiva__mutmut_32': x_busqueda_binaria_recursiva__mutmut_32, 
    'x_busqueda_binaria_recursiva__mutmut_33': x_busqueda_binaria_recursiva__mutmut_33, 
    'x_busqueda_binaria_recursiva__mutmut_34': x_busqueda_binaria_recursiva__mutmut_34
}

def busqueda_binaria_recursiva(*args, **kwargs):
    result = _mutmut_trampoline(x_busqueda_binaria_recursiva__mutmut_orig, x_busqueda_binaria_recursiva__mutmut_mutants, args, kwargs)
    return result 

busqueda_binaria_recursiva.__signature__ = _mutmut_signature(x_busqueda_binaria_recursiva__mutmut_orig)
x_busqueda_binaria_recursiva__mutmut_orig.__name__ = 'x_busqueda_binaria_recursiva'