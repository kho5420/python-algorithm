from typing import List


# 461
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        print(bin(x))
        print(bin(y))
        return bin(x ^ y).count('1')


x = 1
y = 4
Solution().hammingDistance(x, y)