from typing import List
from scipy.spatial import distance


# 33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            sorted_list = nums.sort()
            return nums


nums_list = [4,5,6,7,0,1,2]
Solution().search(nums_list, 0)