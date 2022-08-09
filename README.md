# tinyarray

<div align="center">

![tests](https://github.com/harrisonlabollita/tinyarray/actions/workflows/test.yml/badge.svg)
![issues](https://img.shields.io/github/issues/harrisonlabollita/tinyarray)
![forks](https://img.shields.io/github/forks/harrisonlabollita/tinyarray)
![stars](https://img.shields.io/github/stars/harrisonlabollita/tinyarray)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![license](https://img.shields.io/github/license/harrisonlabollita/tinyarray)
	
</div>

If Python had arrays, I imagine they would be like this. 

Kind of like numpy arrays but a bit more lightweight (and not as much capability). No C backend.


## Example
```python
from tinyarray.array import array

x = array.uniform(10) # uniformly distributed array of size 10
x.mean()              # compute the mean of x
x.sum()               # sum the array x
x + 2                 # add 2 to the array x
x * 2                 # multiple 2 to the array x
# and more!
```

## Example in NumPy
```python
import numpy as np

x = np.random.uniform(10) # uniformly distributed array of size 10
np.mean(x)                # compute the mean of x
np.sum(x)                 # sum the array x
x + 2                     # add 2 to the array x
x * 2                     # multiple 2 to the array x
```

## Installation
```shell
git clone https://github.com/harrisonlabollita/tinyarray.git
cd tinyarray
pip install .
```

## Running tests

```shell
python -m unittest
```

Current limitation, only works on 1D arrays. Plan to add ND arrays.
