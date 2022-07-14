from typing import Union, List
import numpy as np
import math
import random

import array

class array:
    def __init__(self : array, data : List[Union[int, float]]) -> None:
        self._data = data
        self._shape  = len(data) # one dimensional array

    def shape(self : array)-> int: return self._shape
    def numpy(self : array) -> np.ndarray: return np.array(self._data)

    def __len__(self : array) -> int: return len(self._data)

    def __iter__(self : array): return self._data.__iter__()

    def __getitem__(self : array, idx: Union[slice, int]) -> Union[float, int]:
        if isinstance(idx, int):
            idx = idx if idx >= 0 else idx + self._shape
            return self._data[idx]
        if isinstance(idx, slice):
            return array([self._data[i] for i in range(*idx.indices(len(self._data)))])
        else:
            raise NotImplementedError("This type of indexing has not been implemented")

    def __setitem__(self : array, idx : Union[slice, int], value : Union[float,int]) -> None:
        if isinstance(idx, int):
            idx = idx if idx >= 0 else idx + self._shape
            self._data[idx] = value
        if isinstance(idx, slice):
            for i in range(*idx.indices(len(self._data))):
                self._data[i] = value
        else:
            raise NotImplementedError("This type of indexing has not been implemented")

    def __repr__(self: array, /) -> str: return "array(" + self._data.__str__() + ")"

    def __str__(self: array, /) -> str: return "array(" + self._data.__str__() + ")"

    def __add__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i].__add__(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i].__add__(other[i]) for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i].__add__(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")

    def __iadd__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i].__add__(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i].__add__(other[i]) for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i].__add__(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")
    
    def __sub__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i].__sub__(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i].__sub__(other[i])for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i].__sub__(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")
    
    def __isub__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i].__sub__(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i].__sub__(other[i])for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i].__sub__(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")
    
    def __mul__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i].__mul__(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i].__mul__(other[i]) for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i].__mul__(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")

    def __imul__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i].__mul__(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i].__mul__(other[i]) for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i].__mul__(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")

    def __truediv__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i] / other for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i]  / other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i]  / other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")

    def __itruediv__(self : array, other : Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, int) or isinstance(other, float):
            res = [self._data[i] / (other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert other.shape() == self._shape, f"[ERROR] incompatible shapes {other.shape()} != {self._shape}" 
            return array([self._data[i] / other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(other) == self._shape, f"[ERROR] incompatible shapes {len(other)} != {self._shape}" 
            return array([self._data[i] / other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(f"Type {type(other)} is not implemented!")

    def __pow__(self : array, other : Union[int, float]) -> array:
        res = [self._data[i].__pow__(other) for i in range(len(self._data))]
        return array(res)

    def sum(self : array) -> Union[float, int]: return sum(self._data)
    def mean(self : array) -> Union[float, int]: return sum(self._data)/self._shape
    def sqrt(self : array) -> array: return array([math.sqrt(a) for a in self._data])
    def dot(self: array, other) -> Union[float, int]: return sum(self*other)
    def max(self: array) -> Union[float, int]: return max(self._data)
    def min(self: array) -> Union[float, int]: return min(self._data)

    @classmethod
    def ones(cls : array, N: int) -> array: return cls([1 for _ in range(N)])
    @classmethod
    def zeros(cls : array, N : int) -> array: return cls([0 for _ in range(N)])
    @classmethod
    def uniform(cls : array, N :int, a :float=0.0, b : float = 1.0) -> array: return cls([random.uniform(a,b) for _ in range(N)])
