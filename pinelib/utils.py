import numpy as np



def fix_inf(array: np.ndarray) -> np.ndarray:
    array[array == np.inf] = 0
    array[array == -np.inf] = 0
    return array

def fit_arrays(array1: np.ndarray, array2: np.ndarray) -> tuple[np.ndarray]:
    if len(array1) > len(array2):
        array2 = np.pad(array2, (0, len(array1)-len(array2)))
    elif len(array1) < len(array2):
        array1 = np.pad(array1, (0, len(array2)-len(array1)))
    
    return array1, array2