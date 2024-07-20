import math
import numpy as np

mySet = np.arange(1,21)
result = math.lcm(*mySet)
print(result)