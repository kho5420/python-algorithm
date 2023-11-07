####
# 7-1 배열
####
import time

nums = [2, 7, 11, 15]
target = 9

def find_index(nums, target):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue
            else:
                if nums[i] + nums[j] == target:
                    print(i, j)
                    return

stime = time.time()
find_index(nums, target)
print(f"{time.time() - stime:.10f} sec")

"""
브루트 포스
- 배열을 이중으로 반복하면서 무차별 대입으로 모든 경우의 수를 일일이 확인하는 방법.
"""