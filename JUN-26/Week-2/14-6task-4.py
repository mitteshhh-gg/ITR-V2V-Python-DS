#w/o vectorization
nums = [1,2,3,4]
res = []

for i in nums:
    res.append(i + 5)
print(res)

#with vectorization 

import numpy as np

nums = np.array([1,2,3,4])
print(nums + 5)