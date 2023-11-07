from typing import List

# 215
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_list = list(set(nums))
        nums_list.sort()
        print(nums_list)
        return nums_list[-k]



solution = Solution()
solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)