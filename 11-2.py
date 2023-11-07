class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        index = 0

        for stone in stones:
            if stone in jewels:
                index = index + 1

        return index

Solution.numJewelsInStones(None, "aA", "aAAbbbb")