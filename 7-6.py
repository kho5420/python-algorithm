####
# 7-1 배열
####
import time

nums = [7, 1, 5, 3, 6, 4]

def find_index(nums):
    result = min(nums) - max(nums)

    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if i == j:
                continue
            else:
                if result < nums[j] - nums[i]:
                    result = nums[j] - nums[i]

    print(result)

stime = time.time()
find_index(nums)
print(f"{time.time() - stime:.10f} sec")

"""
파이썬의 최댓값 최솟값
- 시스템에서 지정할 수 있는 가장 높은 값, 낮은 값을 설정할 수 있다.
- mx : -sys.maxsize
- mn : sys.maxsize
"""