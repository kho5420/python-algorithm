from typing import List


# 455
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = {}
        for cookie in s:
            result[cookie] = 0
            for greed in g:
                if cookie >= greed:
                    result[cookie] += 1
                    break

        print(result)
        return max(result.values()) if result else 0

# g = [1,2,3]
g = [1,2]
# s = [1,1]
s = [1,2,3]
Solution().findContentChildren(g=g, s=s)