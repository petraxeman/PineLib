import pinelib.series as pls
import numpy as np
import math

math_abs = abs

e = 2.7182818284590452
pi = 3.1415926535897932
phi = 1.6180339887498948
rphi = 0.6180339887498948


def abs(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.abs(value.data))
    elif isinstance(value, (list, tuple)):
        array = np.array(value)
        return np.abs(array)
    elif isinstance(value, (int, float)):
        return math_abs(value)


def acos(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.arccos(value.data))
    elif isinstance(value, (list, tuple)):
        array = np.array(value)
        return np.arccos(array)
    elif isinstance(value, (int, float)):
        return math.acos(value)


def asin(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.arcsin(value.data))
    elif isinstance(value, (list, tuple)):
        array = np.array(value)
        return np.arcsin(array)
    elif isinstance(value, (int, float)):
        return math.asin(value)


def atan(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.arctan(value.data))
    elif isinstance(value, (list, tuple)):
        array = np.array(value)
        return np.arctan(array)
    elif isinstance(value, (int, float)):
        return math.atan(value)


def avg(*value):
    if isinstance(value, pls.Serie):
        return np.average(value.data)
    elif isinstance(value, (list, tuple)):
        return sum(value) / len(value)


def ceil(value):
    if isinstance(value, pls.Serie):
        return np.ceil(value)


def sqrt(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.sqrt(value.data))
    elif isinstance(value, (int, float)):
        return math.sqrt(value)


def sum(value):
    if isinstance(value, pls.Serie):
        return np.sum(value.data)
    elif isinstance(value, (list, tuple)):
        return sum(value)


def pow(value, degree: int):
    if isinstance(value, (pls.Serie, int, float)):
        return value ** degree


def min(value):
    if isinstance(value, pls.Serie):
        return np.min(value.data)
    elif isinstance(value, (list, tuple)):
        return min(value)


def max(value):
    if isinstance(value, pls.Serie):
        return np.max(value.data)
    elif isinstance(value, (list, tuple)):
        return max(value)


def exp(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.exp(value.data))
    elif isinstance(value, (list, tuple)):
        array = np.array(value)
        return np.exp(array)


def cos(value):
    if isinstance(value, pls.Serie):
        return pls.Serie(np.cos(value.data))
    elif isinstance(value, (list, tuple)):
        array = np.array(value)
        return np.cos(array)