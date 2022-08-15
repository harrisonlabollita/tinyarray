from typing import Union, List
import numpy as np
import math
import random

import array


class array:
    def __init__(self: array, data: List[Union[int, float, complex]]) -> None:
        self._data = data
        self._shape = len(data)  # one dimensional array

    def __len__(self: array) -> int: return len(self._data)

    def __iter__(self: array): return self._data.__iter__()

    def __getitem__(self: array, idx: Union[slice, int, bool]) -> Union[float, int, complex]:
        if isinstance(idx, int):
            idx = idx if idx >= 0 else idx + self._shape
            return self._data[idx]
        elif isinstance(idx, slice):
            return array([self._data[i] for i in range(*idx.indices(len(self._data)))])
        elif hasattr(idx, "__iter__"):  # <- should this be better?
            if isinstance(idx[0], bool):
                return array([self._data[i] for i, ind in enumerate(idx) if ind])
            elif isinstance(idx[0], int):
                return array([self._data[i] for i in idx])
        else:
            raise NotImplementedError(
                "This type of indexing has not been implemented")


    def __setitem__(self: array, idx: Union[slice, int, bool], value: Union[float, int, complex]) -> None:
        if isinstance(idx, int):
            idx = idx if idx >= 0 else idx + self._shape
            self._data[idx] = value
        elif isinstance(idx, slice):
            for i in range(*idx.indices(len(self._data))):
                self._data[i] = value
        elif hasattr(idx, "__iter__"):  # <- should this be better?
            if isinstance(idx[0], bool):
                for i, ind in enumerate(idx):
                    if ind:
                        self._data[i] = value
            elif isinstance(idx[0], int):
                for i in idx:
                    self._data[i] = value
        else:
            raise NotImplementedError(
                "This type of indexing has not been implemented")

    def __repr__(self: array, /) -> str: return "array(" + \
        self._data.__str__() + ")"

    def __str__(self: array, /) -> str: return self._data.__str__()

    def __add__(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] + other
                   for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] + other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] + other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")


    def __iadd__(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] + other
                   for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"

            return array([self._data[i] + other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] + other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")

    __radd__ = __add__

    def __sub__(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] - other
                   for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] - other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] - other[i]  for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")
    __rsub__ = __sub__

    def __isub__(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] - other
                   for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] - other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] - other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")


    def __mul__(self: array, other: Union[int, float, complex,List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] * other
                   for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")
    
    __rmul__ = __mul__

    def __imul__(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] * other
                   for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * other[i] for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * other[i] for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")


    def __truediv__(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] * 1/(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * 1/(other[i]) for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * 1/(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")

    __rtruediv__ = __truediv__

    def __itruediv__(self: array, other: Union[int, float, List[Union[int, float]]], /) -> array:
        if isinstance(other, (int, float, complex)):
            res = [self._data[i] * 1/(other) for i in range(len(self._data))]
            return array(res)
        elif isinstance(other, array):
            assert len(other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * 1/(other[i]) for i in range(len(self._data))])
        elif isinstance(other, List):
            assert len(
                other) == self._shape, f"incompatible shapes {len(other)} != {self._shape}"
            return array([self._data[i] * 1/(other[i]) for i in range(len(self._data))])
        else:
            raise NotImplementedError(
                f"Type {type(other)} is not implemented!")

    def __pow__(self: array, other: Union[int, float, complex]) -> array:
        res = [self._data[i].__pow__(other) for i in range(len(self._data))]
        return array(res)

    def __lt__(self: array, other: Union[int, float, complex]) -> array:
        if not isinstance(other, complex) and self.dtype != complex:
            res = [a < other for a in self._data]
        else:
            res = [a.real < other.real for a in self._data]
        return array(res)

    def __gt__(self: array, other: Union[int, float, complex]) -> array:
        if not isinstance(other, complex) and self.dtype != complex:
            res = [a > other for a in self._data]
        else:
            res = [a.real > other.real for a in self._data]
        return array(res)

    def __le__(self: array, other: Union[int, float, complex]) -> array:
        if not isinstance(other, complex) and sel.dtype !=complex:
            res = [a <= other for a in self._data]
        else:
            res = [a.real <= other.real for a in self._data]
        return array(res)

    def __ge__(self: array, other: Union[int, float, complex]) -> array:
        if not isinstance(other, complex) and self.dtype != complex:
            res = [a >= other for a in self._data]
        else:
            res = [a.real >= other.real for a in self._data]
        return array(res)

    def __eq__(self: array, other: Union[int, float, complex]) -> array:
        return array([a == other for a in self._data])

    def append(self: array, other: Union[int, float, complex, List[Union[int, float, complex]]]) -> None:
        if isinstance(other, (int, float, complex)):
            self._data.append(other)
        elif hasattr(other, "__iter__"):
            for o in other:
                self._data.append(o)
        else:
            raise Exception(f"{other} can not be appended to an array object")

    # Removing shape allows for tinyarray's arrays to be "plottable" by matplotlib
    #@property
    #def shape(self: array) -> tuple: return tuple([self._shape])

    @property
    def dtype(self: array) -> Union[float, int, complex]: return type(self._data[0])

    @property
    def data(self: array) -> List[Union[float, int, complex]]: return self._data
    
    @property
    def real(self: array) -> List[Union[float, int]]: return array([a.real for a in self._data])

    @property
    def imag(self: array) -> List[Union[float, int]]: return array([a.imag for a in self._data])

    def numpy(self: array) -> np.ndarray: return np.array(self._data)

    def pad(self: array, N: int) -> None:
        if self.dtype == float:
            self._data.extend([0.0 for _ in range(N)])
            self._shape = len(self._data)
        elif self.dtype == int:
            self._data.extend([0 for _ in range(N)])
            self._shape = len(self._data)
        elif self.dtype == complex:
            self._data.extend([0.0+0.0j for _ in range(N)])
            self._shape = len(self._data)

    def argsort(self: array) -> array: 
        return array(sorted(range(len(self._data)), key=self._data.__getitem__))

    def sort(self: array) -> array: return array(sorted(self._data, key=lambda x: x.real))

    def find(self: array, val, func=lambda x, val: x ==
             val) -> array: return array([a for a in self._data if func(a, val)])

    def sum(self: array) -> Union[float, int]: return sum(self._data)

    def mean(self: array) -> Union[float, complex,
                                   int]: return sum(self._data)/self._shape
    
    def arg(self: array) -> array:
        return array([math.atan(a.imag/a.real) for a in self._data])

    def modulus(self: array) -> array:
        return array([math.sqrt(a.real**2 + a.imag**2) for a in self._data])

    def sqrt(self: array) -> array: 
        if self.dtype in (int, float):
            return array([math.sqrt(a) for a in self._data])
        elif self.dtype == complex:
            def cpx_sqrt(z):
                norm_z = math.sqrt(z.real**2 + z.imag**2)
                r = math.sqrt((norm_z + z.real)/2)
                i = (z.imag/abs(z.imag))*math.sqrt((norm_z - z.real)/2)
                return r + i*1j
            return array(list(map(cpx_sqrt, self._data)))
    
    def exp(self: array) -> array: 
        if self.dtype in (int, float):
            return array([math.exp(a) for a in self._data])
        else:
            return array( [math.exp(a.real)*(math.cos(a.imag) + 1j*math.sin(a.imag)) for a in self._data])

    def log(self: array) -> array:
        if self.dtype in (int, float):
            return array([math.log(a) for a in self._data])
        else:
            m = self.modulus()
            argz = self.arg()
            return array([math.log(m[i]) + 1j*argz[i] for i in range(len(m))])

    def dot(self: array, other) -> Union[float, int, complex]: return sum(self*other)
    def max(self: array) -> Union[float, int, complex]: return max(self._data)
    def min(self: array) -> Union[float, int, complex]: return min(self._data)
    def reverse(self: array) -> array: return array(self._data[::-1])
    def conjugate(self: array) -> array: return array([a.conjugate() for a in self._data])

    def prod(self: array) -> Union[float, int, complex]:
        res = self._data[0]
        for i in range(1, len(self)):
            res *= self._data[i]
        return res
    
    @classmethod
    def ones(cls: array, N: int) -> array: return cls([1 for _ in range(N)])
    @classmethod
    def zeros(cls: array, N: int) -> array: return cls([0 for _ in range(N)])

    @classmethod
    def uniform(cls: array, N: int, a: Union[int,float] = 0.0,
                b: Union[int,float] = 1.0) -> array: return cls([random.uniform(a, b) for _ in range(N)])
