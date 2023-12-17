from pinelib.series import Serie
import numpy as np
import math as py_math

__math_abs = abs
__math_sum = sum

e = 2.7182818284590452
pi = 3.1415926535897932
phi = 1.6180339887498948
rphi = 0.6180339887498948


def abs(value: Serie | list | tuple | int | float) -> Serie | int | float:
    "Calculate the absolute value of Serie, list or integer"
    if isinstance(value, Serie):
        return Serie(np.abs(value.data))
    elif isinstance(value, (list, tuple)):
        array = (value)
        return np.abs(array)
    elif isinstance(value, (int, float)):
        return __math_abs(value)


def acos(value: Serie | list | tuple | int | float) -> Serie | float:
    if isinstance(value, Serie):
        value = value.get_array_for_calc()
        return Serie(np.arccos(value))
    elif isinstance(value, (list, tuple)):
        array = (value)
        return np.arccos(array)
    elif isinstance(value, (int, float)):
        return py_math.acos(value)


def asin(value: Serie | list | tuple | int | float) -> Serie | float:
    if isinstance(value, Serie):
        value = value.get_array_for_calc()
        return Serie(np.arcsin(value))
    elif isinstance(value, (list, tuple)):
        array = (value)
        return np.arcsin(array)
    elif isinstance(value, (int, float)):
        return py_math.asin(value)


def atan(value: Serie | list | tuple | int | float) -> Serie | float:
    if isinstance(value, Serie):
        value = value.get_array_for_calc()
        return Serie(np.arctan(value))
    elif isinstance(value, (list, tuple)):
        array = (value)
        return np.arctan(array)
    elif isinstance(value, (int, float)):
        return py_math.atan(value)


def avg(*value: list | tuple | Serie) -> Serie | float:
    if isinstance(value[0], Serie):
        value = value[0].data
        return Serie([__math_sum(value[i:]) / len(value[i:]) for i in range(len(value))])
    elif isinstance(value, tuple):
        return __math_sum(value) / len(value)


def ceil(value: Serie) -> Serie:
    if isinstance(value, Serie):
        return np.ceil(value)


def sqrt(value: Serie | int | float) -> Serie | float:
    if isinstance(value, Serie):
        return Serie(np.sqrt(value.data))
    elif isinstance(value, (int, float)):
        return py_math.sqrt(value)


def sum(value: Serie | list | tuple) -> Serie:
    if isinstance(value, Serie):
        return np.sum(value.data)
    elif isinstance(value, (list, tuple)):
        return __math_sum(value)


def pow(value: Serie | int | float, degree: int) -> Serie | int | float:
    if isinstance(value, (Serie, int, float)):
        return value ** degree


def min(value: Serie | list | tuple) -> Serie:
    if isinstance(value, Serie):
        return np.min(value.data)
    elif isinstance(value, (list, tuple)):
        return min(value)


def max(value: Serie | list | tuple):
    if isinstance(value, Serie):
        return np.max(value.data)
    elif isinstance(value, (list, tuple)):
        return max(value)


def exp(value: Serie | list | tuple):
    if isinstance(value, Serie):
        return Serie(np.exp(value.data))
    elif isinstance(value, (list, tuple)):
        array = (value)
        return np.exp(array)


def cos(value: Serie | list | tuple):
    if isinstance(value, Serie):
        return Serie(np.cos(value.data))
    elif isinstance(value, (list, tuple)):
        array = (value)
        return np.cos(array)