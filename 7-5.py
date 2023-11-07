####
# 7-1 배열
####
import time
from math import prod

nums = [1, 2, 3, 4]

def find_index(nums):
    result = []

    for i in range(0, len(nums)):
        temp = nums.copy()
        del temp[i]

        result.append(prod(temp))

    print(result)

stime = time.time()
find_index(nums)
print(f"{time.time() - stime:.10f} sec")