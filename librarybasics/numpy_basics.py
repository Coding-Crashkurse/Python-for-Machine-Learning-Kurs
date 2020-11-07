# Beweise für Aussagen

import time
import numpy as np
import sys


start = time.time()
long_array = np.arange(100000000)
end = time.time()
print(end - start)


start = time.time()
long_list = list(range(100000000))
end = time.time()
print(end - start)

len(long_array) == len(long_list)

sys.getsizeof(long_array)
sys.getsizeof(long_list)

["a", 1, 2, 3]
np.array(["a", 1, 2, 3])

a = [1, 2, 3]
b = [1, 2, 3]

a * b

np_a = np.array([3, 4, 1])
np_b = np.array([2, 3, 1])

np_a * np_b

## Numpy Grundlagen
np.arange(4)
np.zeros(4)
np.ones(4)

# Indexing
arr = np.arange(11)
arr > 2
arr[arr > 2]

arr[0:3]

arr2 = arr
arr[2] = 10
arr2

arr2 = arr.copy()

# Operationen


np.random.rand(10)

np.random.seed(999)
np.random.rand(10)

np.random.seed(999)
np.random.rand(10)

np.sort(np_a)


a = np.array([[1,2],[1,2]])
b = np.array([[3,4]])
b

result = np.concatenate((a, b), axis = 0)
result.shape

result.reshape(2,3)


result * 3
result.sum()
result.min()
result.max()

result.sum(axis=1)
result.sum(axis=0)

np.unique(result)

result.transpose()

np.flip(result)

result.flatten()



