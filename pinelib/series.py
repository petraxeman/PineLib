import numpy as np
from pinelib import utils
#np.seterr(divide='ignore')



class Serie:
    def __init__(self, data: np.ndarray | tuple | list):
        self.data = np.array(data)
        self.__reversed_data = np.flip(self.data)

    def get(self, index: int) -> int | float:
        return self.__reversed_data[index]

    def __getitem__(self, key: int):
        return self.__reversed_data[key]
        #return Serie(np.pad(self.data[key:], (0, key)))
    
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

