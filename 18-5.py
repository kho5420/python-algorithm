from typing import List
from scipy.spatial import distance


# 240
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m1 in matrix:
            if target in m1:
                return True
        return False

matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 5
Solution().searchMatrix(matrix, target)