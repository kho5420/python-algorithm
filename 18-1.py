from typing import List
from scipy.spatial import distance


# 704
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            mid_index = int(len(nums)/2)


nums_list = [-1,0,3,5,9,12]
Solution().search(nums_list, 9)