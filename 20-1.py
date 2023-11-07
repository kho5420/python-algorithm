from typing import List
from scipy.spatial import distance


# 191
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

n = "00000000000000000000000000001011"
Solution().hammingWeight(n)