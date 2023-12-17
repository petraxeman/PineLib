import numpy as np
from pinelib import utils
#np.seterr(divide='ignore')



class Serie:
    def __init__(self, data: np.ndarray | tuple | list, flip: bool = False):
        if flip:
            data = np.flip(data)
        
        self.__data = np.array(data)
        self.__reversed = np.flip(self.data)

    def get(self, index: int) -> int | float:
        return self.__reversed[index]

    def get_array_for_calc(self) -> np.ndarray:
        return self.reversed

    @property
    def reversed(self):
        return self.__reversed

    @property
    def data(self):
        return self.__data

    def __getitem__(self, key: int):
        return self.__reversed[key]
    
    def __add__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(data + value)
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(self.data + value)
    
    def __sub__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(data - value)
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(self.data - value)
    
    def __mul__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(data * value)
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(self.data * value)
    
    def __floordiv__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(utils.fix_inf(data // value))
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(utils.fix_inf(self.data // value))
    
    def __truediv__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(utils.fix_inf(data / value))
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(utils.fix_inf(self.data / value))
    
    def __mod__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(utils.fix_inf(data % value))
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(utils.fix_inf(self.data % value))
    
    def __pow__(self, value: 'Serie') -> 'Serie':
        if isinstance(value, Serie):
            data, value = utils.fit_arrays(self.data, value.data)
            return Serie(data ** value)
        elif isinstance(value, int) or isinstance(value, float):
            return Serie(self.data ** value)

    def __repr__(self):
        return f'<Serie len:{len(self.data)} {self.data}>'

