from typing import List


# 75
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


p_nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(p_nums)
