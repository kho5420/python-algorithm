from typing import List
from scipy.spatial import distance


# 973
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closet = {}
        for i, point in enumerate(points):
            closet[i] = distance.euclidean([0, 0], point)

        print(closet)
        closet_index = [index for index, v in sorted(closet.items(), key=lambda item: item[1], reverse=False)]

        result = []
        for index in closet_index[:k]:
            result.append(points[index])

        return result


p_points = [[3, 3], [5, -1], [-2, 4]]
p_k = 2
Solution().kClosest(p_points, p_k)
