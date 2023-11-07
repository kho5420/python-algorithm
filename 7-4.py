####
# 7-1 배열
####
import time

# nums = [1, 4, 3, 2, 5, 6]
nums = [1, 4, 3, 2]

def find_index(nums):
    result = 0

    for i in range(0, len(nums) - 1):
        temp_list = nums.copy()
        temp_list.remove(nums[i])
        temp_list.remove(nums[i+1])

        for j in range(0, len(temp_list) - 1):
            if result < min(nums[i], nums[i+1]) + min(temp_list[j], temp_list[j+1]):
                result = min(nums[i], nums[i+1]) + min(temp_list[j], temp_list[j+1])

    print(result)

stime = time.time()
find_index(nums)
print(f"{time.time() - stime:.10f} sec")