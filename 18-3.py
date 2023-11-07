from typing import List
from scipy.spatial import distance


# 349
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


l_nums1 = [1,2,2,1]
l_nums2 = [2,2]
Solution().intersection(l_nums1, l_nums2)