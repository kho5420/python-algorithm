####
# 7-1 배열
####
import time

nums = [-1, 0, 1, 2, -1, -4]

def find_index(nums):
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if i == j or j == k or i == k:
                    continue
                else:
                    if i < j < k and nums[i] + nums[j] + nums[k] == 0:
                        print(nums[i], nums[j], nums[k])
                        print(i, j, k)
                        print("-------------------------")

stime = time.time()
find_index(nums)
print(f"{time.time() - stime:.10f} sec")

"""
투 포인터 기법
- 시작점과 끝점 또는 왼쪽 포인터와 오른쪽 포인터를 기준으로 하는 문제 풀이 전략.
- 정렬된 배열을 기준으로 하며, 두 포인터가 자유롭게 움직이며 문제를 풀이한다.
"""