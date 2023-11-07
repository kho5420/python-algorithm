from typing import List
from collections import Counter


# 136
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [key for key, value in Counter(nums).items() if value == 1][0]


nums = [4,1,2,1,2]
Solution().singleNumber(nums)
