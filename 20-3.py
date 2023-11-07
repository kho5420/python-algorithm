from collections import Counter
from typing import List
from scipy.spatial import distance


# 424
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        first = Counter(s).most_common()[0][0]

        for word in s:
            if first == word:
                continue
            print(word)


s = "AABABBA"
k = 1
Solution().characterReplacement(s, k)