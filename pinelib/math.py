from pinelib.series import Serie
import numpy as np
import math as __math

__math_abs = abs
__math_sum = sum

e = 2.7182818284590452
pi = 3.1415926535897932
phi = 1.6180339887498948
rphi = 0.6180339887498948


def abs(value: Serie | list | tuple | int | float) -> Serie | int | float:
    """ Function convert all numbers to absolute numbers and return Serie, int or float """
    if isinstance(value, Serie):
        return Serie(np.abs(value.data))      # Return Series with absolute values
    elif isinstance(value, (list, tuple)):
        return Serie(np.abs(np.array(value))) # Also return a Series with absolute values
    elif isinstance(value, (int, float)):
        return __math_abs(value)              # Return only one absolute integer or float


def acos(value: Serie | list | tuple | int | float) -> Serie | float:
    """ Function return calculated arc cos values from given array or number. Return Serie or float """
    if isinstance(value, Serie):
        return Serie(np.arccos(value.data))      # Return Series with arc cos values
    elif isinstance(value, (list, tuple)):
        return Serie(np.arccos(np.array(value))) # Return Series with arc cos values
    elif isinstance(value, (int, float)):
        return __math.acos(value)                # Return only one arc cos float


def asin(value: Serie | list | tuple | int | float) -> Serie | float:
    """ Function return calculated arc sin values from given array or number. Return Serie or float """
    if isinstance(value, Serie):
        return Serie(np.arcsin(value.data))      # Return Series with arc sin values
    elif isinstance(value, (list, tuple)):
        return Serie(np.arcsin(np.array(value))) # Return Series with arc sin values
    elif isinstance(value, (int, float)):
        return __math.asin(value)                # Return only one arc sin float


def atan(value: Serie | list | tuple | int | float) -> Serie | float:
    """ Function return calculated arc tan values from given array or number. Return Serie or float """
    if isinstance(value, Serie):
        return Serie(np.arctan(value.data))      # Return Series with arc tanh values
    elif isinstance(value, (list, tuple)):
        return Serie(np.arctan(np.array(value))) # Return Series with arc tanh values
    elif isinstance(value, (int, float)):
        return __math.atan(value)                # Return only one arc tanh float


def avg(*value: list | tuple | Serie) -> Serie | float:
    """ Function finds average value of given array or squence of numbers and return Serie or float """
    if isinstance(value[0], (list, tuple)):
        value[0] = np.array(value[0])
    if isinstance(value[0], Serie):
        value = list(np.flip(value[0].data))
        value = np.array([__math_sum(value[i:]) / len(value[i:]) for i in range(len(value))])
        return Serie(value)                      # Return Series with calculated average numbers
    elif isinstance(value, tuple):
        return __math_sum(value) / len(value)    # Return average float number


def ceil(value: Serie) -> Serie:
    if isinstance(value, Serie):
        return np.ceil(value.data)


def sqrt(value: Serie | int | float) -> Serie | float:
    if isinstance(value, Serie):
        return Serie(np.sqrt(value.data))
    elif isinstance(value, (int, float)):
        return __math.sqrt(value)


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