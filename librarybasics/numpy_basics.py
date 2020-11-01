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

np_a = np.array([1, 2, 3])
np_b = np.array([1, 2, 3])

np_a * np_b
